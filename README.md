# zoltra-sast-fixture

Controlled SAST fixture repository for the Zoltra Hermes Opengrep SAST
spec (`zoltra-hermes-opengrep-sast`). Not a product, not a demo, not
for reuse: it exists so a pinned commit of deliberately vulnerable and
clean files can be fetched by SHA and scanned deterministically.

- `vulnerable.py` / `vulnerable.js` — must produce matches under the
  owned `zoltra.sast.*` rule pack.
- `clean.py` / `clean.js` — must produce no matches.

The `AWS_SECRET_ACCESS_KEY` value in `vulnerable.py` is AWS's published
documentation example key (non-functional, ends in `EXAMPLEKEY`).
