#!/usr/bin/env python3
"""Validate candidate evidence records before they are used in recommendations."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


REQUIRED = {
    "family",
    "official_url",
    "foundry_or_designer",
    "verified_on",
    "formal_observations",
    "documented_history",
    "contextual_inferences",
    "counter_readings",
    "best_roles",
    "weak_roles",
    "scripts_languages",
    "formats_axes",
    "license_status",
    "license_url",
    "evidence_urls",
}
LICENSES = {"commercial", "open", "unknown"}


def valid_https(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", help="JSON file containing one record or an array")
    args = parser.parse_args()

    payload = json.loads(Path(args.records).read_text(encoding="utf-8"))
    records = payload if isinstance(payload, list) else [payload]
    problems: list[str] = []

    for index, record in enumerate(records):
        label = record.get("family", f"record[{index}]")
        missing = REQUIRED - set(record)
        if missing:
            problems.append(f"{label}: missing {sorted(missing)}")
            continue
        try:
            date.fromisoformat(record["verified_on"])
        except (TypeError, ValueError):
            problems.append(f"{label}: verified_on must be YYYY-MM-DD")
        if record["license_status"] not in LICENSES:
            problems.append(f"{label}: invalid license_status")
        for field in ("official_url", "license_url"):
            if record[field] and not valid_https(record[field]):
                problems.append(f"{label}: {field} must be an HTTPS URL or empty")
        if not isinstance(record["evidence_urls"], list) or not record["evidence_urls"]:
            problems.append(f"{label}: evidence_urls must be a non-empty list")
        elif any(not valid_https(url) for url in record["evidence_urls"]):
            problems.append(f"{label}: every evidence URL must use HTTPS")

    if problems:
        raise SystemExit("Evidence validation failed:\n- " + "\n- ".join(problems))
    print(f"Validated {len(records)} evidence record(s).")


if __name__ == "__main__":
    main()

