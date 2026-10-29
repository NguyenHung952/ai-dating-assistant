# V7 FLIRT + REALTIME CONTEXT — QA REPORT

## Scope

This report covers static validation of the generated text sources, the five mode-specific CORE files, the 20 regression test definitions, and the five regenerated PDFs. No `SAMPLE_CONVERSATIONS_RAW.txt` was present in the input package, and the revised prompts were not run inside a deployed Custom Gem. Therefore, this is a source/package QA report, not a claim that live model responses have already passed the 20 behavioral tests.

## Structure and item counts

- Master includes `[11] FLIRT_CRAFT` with T1–T12, `[12] EMOTIONAL_IMPACT_QC` with ten criteria, `[13] RESPONSE_RHYTHM`, `[14] REALTIME_CONTEXT`, and `[15] AI_SMELL_REMOVAL`.
- The Master and every mode CORE have 18 named HARD_QC checks. Each of the five CORE files has exactly the numbered sections `[0]`–`[23]`.
- Each KB has exactly one copy of every section `[A]`–`[V]`.
- Per KB: `[G]` 20 profile-analyzer examples; `[I]` 54 numbered BAD/GOOD pairs (including 43–54 in REPAIR); `[Q]` 30 tagged entries; `[R]` 30 contextual situations; `[S]` 40 before/after pairs; `[T]` 20 difficult responses; `[U]` 20 realtime hooks; `[V]` 15 anti-template pairs.
- Every `[Q]` entry has `Technique`, `Layer`, `Context requirement`, and `Mode use` metadata. `[R]` entries have `Technique`, `Layer`, `Realtime?`, and `Context source`. `[S]`, `[T]`, and `[V]` include `Technique` and `Layer` tags. Mode-disallowed examples are marked `REFERENCE_ONLY` where applicable.
- Technique coverage across the five 30-entry `[Q]` banks is: T1=16, T2=6, T3=6, T4=16, T5=44, T6=6, T7=6, T8=10, T9=10, T10=10, T11=10, T12=10.

## Length, format, and encoding checks

- Extracted message candidates in `[Q]`, `[R]`, `[S]`, `[T]`, `[U]`, and `[V]` are all at most 80 characters.
- All 40 `[S] AFTER` messages in every KB are at most 40 characters.
- Section numbering and counts were validated by script. No duplicate section headings were found.
- The listed mojibake and repeated-number spam patterns from the input prompt were not found in V7 source files during the final scan. The previously highlighted `REPAIR [I]` entries 43–54 are present in the source.
- Conflicting `ACTIVE`/`REFERENCE_ONLY` labels were not found by the final static scan.

## PDF validation

All five PDFs were regenerated from their corresponding V7 Markdown source with XeLaTeX, then rendered to PNG pages for visual inspection. The first, middle, and final pages of each PDF were reviewed in a contact sheet; a representative dense page was inspected at full resolution. The sampled pages showed Vietnamese glyphs rendering normally and no obvious clipped text or overlaps.

| PDF | Pages |
|---|---:|
| `ASSESS_KB_V7.pdf` | 26 |
| `BUILD_KB_V7.pdf` | 24 |
| `MAINTAIN_KB_V7.pdf` | 24 |
| `REPAIR_KB_V7.pdf` | 25 |
| `EXIT_KB_V7.pdf` | 25 |

Extracted text from the final PDFs was also scanned for the specified mojibake and numbering-spam patterns.

## Known requirement conflict

The prompt simultaneously asks for 30 entries in each `[Q]` bank and at least five examples for each of T1–T12 within every bank. The latter requires at least 60 entries. V7 preserves the stated 30-entry bank size and provides at least five examples of every technique across the five-bank corpus. Examples disallowed by a mode are tagged `REFERENCE_ONLY` and must not be emitted as live candidates.

## Test execution status

`TEST_CASES_V7.md` contains 20 expected-behavior regression cases covering mode lock, realtime evidence, AI-smell checks, technique diversity, consent/boundary, and character limits. These cases are prepared for execution; they have not been executed against a deployed Custom Gem because no runtime/model endpoint or raw sample-conversation dataset was provided.
