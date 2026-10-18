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


REPAIR PATCH V6.1
- CORE files were retained because structural, protected-block, mode-router, and spelling checks passed.
- KB Markdown was cleaned/normalized, mode-specific [G]/[I]/[M]/[P] content was corrected, and PDFs were re-exported with embedded Noto Sans Unicode fonts.
- The uploaded archive did not contain the reported mojibake/spam pages or duplicated [H]/[I] headings; this was verified rather than treated as a defect.
- See DOCS/REPAIR_REPORT_V6.md for exact changes and validation results.


V7 FLIRT CRAFT UPGRADE
- Master instruction adds [11] FLIRT_CRAFT, [12] EMOTIONAL_IMPACT_QC, [13] RESPONSE_RHYTHM, L2a-L2d subtext, length sweet spot, and HARD_QC NEW_CHECK_11..13.
- The five mode COREs retain their original [0]-[23] structure and prior checks, with technique/rhythm overlays, mode-specific flirt levels, user controls, and recovery protocols 13-16.
- The five KB Markdown sources preserve [A]-[P], retain 54 numbered BAD/GOOD pairs with short GOOD candidates and technique tags, add 10 Profile Analyzer examples, expand Recovery to 16 protocols, and add [Q]-[T].
- EXIT explicitly uses flirt level 0; REPAIR stays non-flirt while harm is active. Safety, consent, boundary and evidence remain higher priority than style.
- V7 is a design draft. Run the regression matrix in DOCS/MIGRATION_GUIDE.md before production replacement.
