# Research and evidence protocol

## Source priority

1. Official foundry/type designer page, specimen, essay, case study, and license.
2. Client or design studio case study documenting the use.
3. Recorded lecture or interview with the responsible designer.
4. Museum, archive, university, standards body, or serious design publication.
5. Aggregator, retailer, social post, or community discussion only for discovery and reception signals.

Open the actual page. Do not rely on a search snippet. Preserve the difference between what the designer intended, what a critic interpreted, and what an audience reported.

## Candidate evidence record

For every recommended family capture:

```json
{
  "family": "Example Family",
  "official_url": "https://...",
  "foundry_or_designer": "...",
  "verified_on": "YYYY-MM-DD",
  "formal_observations": ["..."],
  "documented_history": ["..."],
  "contextual_inferences": ["..."],
  "counter_readings": ["..."],
  "best_roles": ["display"],
  "weak_roles": ["dense UI"],
  "scripts_languages": ["verify on official page"],
  "formats_axes": ["verify on official page"],
  "license_status": "commercial|open|unknown",
  "license_url": "https://...",
  "evidence_urls": ["https://..."]
}
```

Do not store current price as durable knowledge. Pricing, license scope, language coverage, and product availability can change; verify them during the recommendation.

## Research questions

- What problem was the family designed to solve?
- What historical material or medium informed it?
- Which characteristics are visible in actual words and paragraphs?
- Which associations come from the form, and which from famous later uses?
- How does it behave at the user's sizes and copy lengths?
- What does it communicate when paired with the user's actual copy, imagery, and category?
- Where would it become cliché, misleading, inaccessible, or technically expensive?

## Reception research

When the task needs audience fit rather than expert interpretation alone:

- collect examples from the target market and period;
- sample competitor typography without treating prevalence as preference;
- conduct quick recognition/association tests using identical layouts;
- ask respondents what feels expected, distinctive, trustworthy, dated, or inappropriate;
- record disagreement and segment differences;
- test typography in context, not isolated font names.

Do not claim conversion impact without an experiment using comparable creative, traffic, offer, and measurement.

## Architecture inspiration boundary

Open-source font tools may inform implementation patterns such as BM25 retrieval, MCP interfaces, deterministic scoring, local-first previews, metadata schemas, and visual comparison. Do not import their mood tags, pairings, quality scores, or recommendation datasets unless the user later authorizes a separately audited data source.

