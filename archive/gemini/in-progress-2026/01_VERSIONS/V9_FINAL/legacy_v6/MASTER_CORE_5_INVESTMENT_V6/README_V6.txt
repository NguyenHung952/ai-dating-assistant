MASTER CORE V6 — INVESTMENT-MODE ARCHITECTURE

FOLDER MAP
- CORE/: 5 runtime CORE instruction files (.txt).
- KB_PDF/: 5 final Knowledge Base PDFs, one for each investment mode.
- KB_SOURCE/: editable Markdown source for each PDF; use for future maintenance, not required as a separate KB upload if the PDF is already loaded.
- DOCS/CHANGELOG_V6.md: architecture changes, preserved invariants, stage mapping, archive list.
- DOCS/MIGRATION_GUIDE.md: mode selection, evidence detection, transition rules, mode examples, regression test matrix.

RUNTIME PRINCIPLES
- Investment mode is internal routing state, never a label shown to OTHER.
- Stage is a secondary attribute, not a proxy for relationship value or consent.
- If evidence is insufficient, active mode defaults to ASSESS.
- Hurt/mismatch routes to REPAIR when dialogue remains open; explicit stop/boundary or serious red flag routes to EXIT/CLOSE.
- Existing character budget, fragment-mode conditions, ROLE_LOCK_CHECK, HARD_QC NEW_CHECK_1..NEW_CHECK_10, SUBTEXT_READING, LOGIC_ENGINE and NON_BOT_FEEL were preserved from the supplied CORE baseline.

QA SUMMARY
- All 5 COREs contain required sections [0]–[23], plus [2.1] STAGE_ATTRIBUTE, with no duplicate section headings.
- Protected source blocks [2.5], [7], [8], [9], [18], [20], [21], [22], [23] match the supplied STRANGER CORE source exactly.
- All 5 KB PDFs contain sections [A]–[P] and 54 BAD/GOOD examples. Each PDF was rendered and visually checked after generation.
- V6 is a design/migration draft based on the supplied files; run the regression matrix in MIGRATION_GUIDE.md before replacing a production Gem.
