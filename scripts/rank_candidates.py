#!/usr/bin/env python3
"""Rank researched typeface candidates with a transparent weighted rubric."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


EXPECTED_DIMENSIONS = {
    "audience_culture",
    "category_position",
    "emotion_voice",
    "era_context",
    "formal_semiotics",
    "functional_fit",
    "distinctiveness",
    "license_delivery",
}


def load_json(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_weights(weights: dict[str, Any]) -> None:
    if set(weights) != EXPECTED_DIMENSIONS:
        missing = EXPECTED_DIMENSIONS - set(weights)
        extra = set(weights) - EXPECTED_DIMENSIONS
        raise ValueError(f"Invalid weight dimensions; missing={sorted(missing)}, extra={sorted(extra)}")
    if any(not isinstance(value, (int, float)) or value < 0 for value in weights.values()):
        raise ValueError("Weights must be non-negative numbers")
    if abs(sum(weights.values()) - 100) > 1e-9:
        raise ValueError("Weights must total 100")


def score_candidate(candidate: dict[str, Any], weights: dict[str, float]) -> dict[str, Any]:
    scores = candidate.get("scores", {})
    if set(scores) != EXPECTED_DIMENSIONS:
        raise ValueError(f"{candidate.get('name', '<unnamed>')}: score dimensions do not match rubric")
    if any(not isinstance(value, int) or value < 0 or value > 5 for value in scores.values()):
        raise ValueError(f"{candidate.get('name', '<unnamed>')}: scores must be integers from 0 to 5")

    failures = list(candidate.get("hard_failures", []))
    eligible = bool(candidate.get("eligible", True)) and not failures
    weighted = sum(scores[key] * weights[key] for key in EXPECTED_DIMENSIONS) / 5
    return {
        "name": candidate.get("name", "Unnamed candidate"),
        "eligible": eligible,
        "score_100": round(weighted, 1),
        "confidence": candidate.get("confidence", "exploratory"),
        "hard_failures": failures,
        "notes": candidate.get("notes", ""),
        "scores": scores,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--brief", required=True, help="Path to brief JSON")
    parser.add_argument("--candidates", required=True, help="Path to candidate array JSON")
    args = parser.parse_args()

    brief = load_json(args.brief)
    candidates = load_json(args.candidates)
    if not isinstance(candidates, list) or not candidates:
        raise ValueError("Candidates JSON must be a non-empty array")

    weights = brief.get("weights", {})
    validate_weights(weights)
    ranked = [score_candidate(candidate, weights) for candidate in candidates]
    ranked.sort(key=lambda item: (item["eligible"], item["score_100"]), reverse=True)
    print(json.dumps({"rubric": weights, "ranked": ranked}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

