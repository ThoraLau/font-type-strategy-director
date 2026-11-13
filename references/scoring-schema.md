# Scoring schema

Scoring supports comparison after research; it does not generate truth.

## Brief JSON

```json
{
  "weights": {
    "audience_culture": 20,
    "category_position": 15,
    "emotion_voice": 15,
    "era_context": 15,
    "formal_semiotics": 15,
    "functional_fit": 10,
    "distinctiveness": 5,
    "license_delivery": 5
  },
  "hard_requirements": {
    "script": "Latin",
    "roles": ["display", "body"],
    "commercial_allowed": true
  }
}
```

Weights must total 100. Adjust them when the brief makes a dimension unusually important.

## Candidates JSON

```json
[
  {
    "name": "Candidate A",
    "eligible": true,
    "scores": {
      "audience_culture": 4,
      "category_position": 5,
      "emotion_voice": 4,
      "era_context": 3,
      "formal_semiotics": 5,
      "functional_fit": 4,
      "distinctiveness": 3,
      "license_delivery": 4
    },
    "confidence": "medium",
    "hard_failures": [],
    "notes": "Evidence-aware summary"
  }
]
```

Use integer scores from 0 to 5:

- `0`: contradicts the requirement;
- `1`: weak;
- `2`: partial with major risk;
- `3`: credible;
- `4`: strong;
- `5`: unusually strong and evidenced.

Any unverified hard requirement makes `eligible` false or creates a visible `hard_failures` entry. Unknown is not a neutral 3.

