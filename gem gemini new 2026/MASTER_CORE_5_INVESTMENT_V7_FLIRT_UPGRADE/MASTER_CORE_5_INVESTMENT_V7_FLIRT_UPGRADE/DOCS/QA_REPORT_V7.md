# V7 FLIRT UPGRADE — QA REPORT

## Structural checks

- Master retains its existing organization; added `[11] FLIRT_CRAFT`, `[12] EMOTIONAL_IMPACT_QC`, and `[13] RESPONSE_RHYTHM`.
- All five mode CORE files retain the numbered `[0]`–`[23]` sections and include `NEW_CHECK_11`–`NEW_CHECK_13` alongside the existing HARD_QC checks.
- Each KB source retains `[A]`–`[P]` and adds `[Q]`–`[T]`.
- Each KB contains 20 Profile Analyzer examples, 54 BAD/GOOD pairs with technique tags and rationale, 16 recovery protocols, 20 FLIRT BANK examples, 20 contextual responses, 30 before/after examples, and 20 difficult-situation responses.
- The three new recovery protocols 13–16 are present: `emotional_repair_pause`, `attraction_uncertainty`, `reply_after_silence`, and `overtext_recovery`.
- The ten core short-bank candidates and six priority candidates are retained in compact, paired rows; three of the ten original short-bank entries are shortened per mode where applicable.
- GOOD candidates in section `[I]` are at most 50 characters in the current source files (maximum range across modes: 49–50 characters).

## PDF checks

- All five PDFs were regenerated from the final Markdown sources.
- Each PDF renders to 17 pages and was visually checked in PDFium for Vietnamese glyph rendering, clipped text, and final-page pagination.
- The final difficult-situation entries remain separated rather than merging into one paragraph or leaving a single-item final page.

## Files

- `MASTER_CORE_V6_CUSTOM_GEM_INSTRUCTIONS.txt`
- `CORE/` — five mode-specific CORE files
- `KB_SOURCE/` — five editable Markdown sources
- `KB_PDF/` — five generated PDFs
- `DOCS/` — change log, migration guide, repair report, and this QA report
