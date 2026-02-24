%%writefile docs/preprocess_policy.md
Cleaning:

- remove extra whitespace
- remove control characters

Normalization:

- unify apostrophes and quotes
- normalize dashes

Masking:

- URLs -> <URL>
- Emails -> <EMAIL>
- Phones -> <PHONE>

Do NOT change:

- numbers, identifiers, financial values

Sentence splitting:
Rule-based regex with protection for UA abbreviations:
м., вул., р., т.д.

Pipeline is deterministic and reproducible.
