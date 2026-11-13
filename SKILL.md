---
name: type-strategy-director
description: Select and explain 3-5 Latin typeface directions from audience, category, emotion, era, cultural context, medium, and licensing constraints using typographic semiotics and documented type-strategy methods. Use for brand typography direction, font shortlists, type-system roles, or original specimen/poster concepts; not for merely identifying a font from an image.
---

# Type Strategy Director

Turn a brand or audience brief into an evidence-aware type strategy, then recommend 3-5 genuinely different typeface directions. Treat type as the visible form of language, a functional system, and a cultural signal—not a bag of mood tags.

## Core position

- Begin with the audience, message, category, cultural setting, and medium. Do not begin with a favorite font.
- Separate `documented fact`, `historical association`, `contextual inference`, and `creative hypothesis`.
- A typeface does not possess one universal personality. Meaning changes with language, setting, scale, layout, imagery, color, tracking, and prior use.
- Never infer that a demographic has a single taste. Translate audience information into testable expectations, tensions, references, and rejection risks.
- Distinguish typeface selection from typography. A suitable family can still fail through inappropriate weight, width, hierarchy, spacing, or composition.
- Prefer a few legible, ownable signals over novelty in every glyph. Character accumulates across words and systems.
- Do not imitate an ethnic or cultural identity using superficial pseudo-script forms. For non-Latin or multiscript work, require script expertise and local review.

## Intake

Extract what is known:

- audience: location, language/script, life stage, subculture, familiarity, aspiration, and accessibility needs;
- brand: category, price position, promise, personality, competitors, heritage, and desired difference;
- expression: 3-7 emotion words, forbidden impressions, era references, cultural references, and desired tension;
- use: display/body/UI/data, media, sizes, copy length, languages, weights, variable axes, and performance;
- constraints: budget, license type, deadline, existing identity, supplied fonts, and whether commercial fonts are allowed.

If a missing answer would change the candidate pool, ask one highest-impact question at a time. Otherwise state assumptions and proceed. Script/language coverage, commercial-font permission, and body-versus-display use normally outrank mood refinements.

## Required workflow

### 1. Write the type-strategy sentence

For unfamiliar or high-stakes brand work, read [references/roles-and-work-products.md](references/roles-and-work-products.md) and cover the relevant strategy, research, design-system, and production responsibilities rather than reducing the task to font shopping.

Use this shape:

> The typography should help **[audience]** experience **[brand/product]** as **[desired meaning]**, by combining **[formal signals]** while avoiding **[category cliché or rejection risk]**, across **[primary applications]**.

Add one productive tension, such as `authoritative but not institutional`, `technical but not sterile`, or `nostalgic without costume`.

### 2. Build the semiotic brief

Read [references/typographic-semiotics.md](references/typographic-semiotics.md). Translate words into observable variables, historical lineages, likely associations, counter-readings, and layout conditions. Never map an adjective directly to a font name.

### 3. Apply expert lenses

Read [references/expert-methods.md](references/expert-methods.md) for new strategy work or when explaining why a choice is credible. Select only the relevant lenses, but always include:

- one brand-voice/system lens;
- one historical/contextual lens;
- one use/reading lens;
- one cultural or multiscript check when applicable.

### 4. Form candidate territories before font names

Create 3-5 territories that solve the brief differently. Examples: `measured humanist`, `editorial contrast`, `vernacular utility`, `controlled grotesk`, `expressive variable display`. Each territory must state its benefit and risk.

### 5. Research and shortlist

Read [references/research-and-evidence.md](references/research-and-evidence.md). Prefer official foundry pages, designer essays/interviews, specimens, documented in-use cases, and license pages. Use aggregators only for discovery.

For each candidate verify:

- current family name and official source;
- designer/foundry where documented;
- relevant formal characteristics from an actual specimen;
- required styles, language support, and technical formats;
- current licensing path without guessing price;
- evidence for historical or contextual claims;
- whether the recommendation depends on typography rather than the font alone.

Do not copy recommendation labels or training datasets from other font-selection projects. They may inspire software architecture only.

### 6. Filter, then score

Hard-filter candidates that fail script coverage, use size, essential styles, technical delivery, licensing permission, or accessibility requirements.

For repeatable ranking, encode candidates and the brief according to [references/scoring-schema.md](references/scoring-schema.md), then run:

```powershell
python scripts/rank_candidates.py --brief brief.json --candidates candidates.json
```

If Python is unavailable, use the same rubric manually and disclose that the score is a decision aid, not research evidence.

Do not let a high aggregate score hide a hard failure. Do not use decimal precision to imply scientific certainty.

### 7. Return a deliberately varied shortlist

Return 3-5 options, usually covering:

- best strategic fit;
- safer/long-life system;
- more distinctive or culturally charged direction;
- expressive or experimental direction when appropriate;
- accessible/open-license alternative when useful.

Do not return five near-identical grotesks. If the brief genuinely calls for a narrow territory, vary construction, provenance, texture, or system behavior and explain why the range is intentionally narrow.

### 8. Design the representative specimen/poster

Read [references/specimen-and-poster.md](references/specimen-and-poster.md). The visual must test the proposed strategy in the user's real content hierarchy—not merely display an alphabet.

- With an open font: render an original poster using the verified font file and preserve its license notice.
- With a commercial font supplied by the user under an appropriate license: render from that file without redistributing it.
- Without a licensed commercial font file: provide an art-direction mockup/specification and link to the official specimen. Never substitute another font while labeling it as the commercial face.
- Do not copy a foundry specimen or a designer's composition.

## Output contract

Keep the response decision-oriented:

1. **Type strategy** — one sentence plus the core tension.
2. **Audience reading** — relevant expectations and risks, not stereotypes.
3. **Semiotic translation** — form, history, symbolism, counter-reading, and setting.
4. **3-5 candidates** — role, reason, formal evidence, historical/cultural association, best use, risk, license/source, and confidence.
5. **System recommendation** — primary/display/body/utility roles, weights, width/optical-size guidance, and pairing logic.
6. **Poster/specimen** — one representative visual or an honest art-direction specification.
7. **Validation plan** — what to test with target users and in production.

Use `high`, `medium`, or `exploratory` confidence. A precise-looking score may accompany the comparison but must not replace reasoning.

## Boundaries

- Do not claim that type alone causes conversion, trust, luxury, or demographic preference.
- Do not invent quotations, case studies, font features, language coverage, availability, or licensing terms.
- Do not recommend a font solely because a prestigious brand uses it.
- Do not present trend alignment as timeless strategy.
- Do not reproduce commercial fonts, copyrighted specimen artwork, or proprietary foundry data.
- Treat visual examples as evidence of use, not proof of audience response.

