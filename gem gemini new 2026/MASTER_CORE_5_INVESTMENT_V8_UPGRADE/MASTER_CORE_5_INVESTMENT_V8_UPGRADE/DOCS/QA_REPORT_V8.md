# QA_REPORT_V8

Status reflects static source checks and render inspection, not a live deployed-Gem evaluation.

## V7 source audit
- No listed mojibake/control-character/number-spam patterns were reproduced in supplied Markdown source or extracted V7 PDF text.
- No duplicate `[A]`–`[V]` section headers were found in supplied KB Markdown.
- Corrected V7 CORE version-label inconsistency in V8 copies.

## V8 structural QA
- **ASSESS:** sections A–Y ordered/unique=True; W=40/40; X=0 (disabled in ASSESS/EXIT); Y=20 (disabled in REPAIR/EXIT); max candidate length across Q-Y=58; personality counts={'WITTY': 5, 'POETIC': 5, 'COOL': 5, 'WARM': 5, 'PLAYFUL': 5, 'DEEP': 5, 'NERDY': 5, 'MYSTERIOUS': 5}; result=PASS.
- **BUILD:** sections A–Y ordered/unique=True; W=40/40; X=20 (disabled in ASSESS/EXIT); Y=20 (disabled in REPAIR/EXIT); max candidate length across Q-Y=58; personality counts={'WITTY': 5, 'POETIC': 5, 'COOL': 5, 'WARM': 5, 'PLAYFUL': 5, 'DEEP': 5, 'NERDY': 5, 'MYSTERIOUS': 5}; result=PASS.
- **MAINTAIN:** sections A–Y ordered/unique=True; W=40/40; X=20 (disabled in ASSESS/EXIT); Y=20 (disabled in REPAIR/EXIT); max candidate length across Q-Y=61; personality counts={'WITTY': 5, 'POETIC': 5, 'COOL': 5, 'WARM': 5, 'PLAYFUL': 5, 'DEEP': 5, 'NERDY': 5, 'MYSTERIOUS': 5}; result=PASS.
- **REPAIR:** sections A–Y ordered/unique=True; W=40/40; X=20 (disabled in ASSESS/EXIT); Y=0 (disabled in REPAIR/EXIT); max candidate length across Q-Y=60; personality counts={'WITTY': 5, 'POETIC': 5, 'COOL': 5, 'WARM': 5, 'PLAYFUL': 5, 'DEEP': 5, 'NERDY': 5, 'MYSTERIOUS': 5}; result=PASS.
- **EXIT:** sections A–Y ordered/unique=True; W=40/40; X=0 (disabled in ASSESS/EXIT); Y=0 (disabled in REPAIR/EXIT); max candidate length across Q-Y=58; personality counts=neutral-only; result=PASS.

### Cross-corpus checks
- Q bank total per KB: 30 entries; coverage across the corpus (5 KBs): T1=16, T2=6, T3=6, T4=16, T5=44, T6=6, T7=6, T8=10, T9=10, T10=10, T11=10, T12=10.
- Master contains 23 explicit NEW_CHECK labels in its QC block (V7 checks plus V8 additions are preserved).
- EXIT [W] uses neutral closes without personality labels; EXIT [X]/[Y] are disabled. This is an explicit safety exception to generic bank-count expectations.
- REPAIR [Y] is disabled. REPAIR [X] contains conditional examples but must not activate during acute hurt, apology/accountability, or a space request.
- Q/R/S/T/V personality tags are added where allowed; EXIT deliberately omits them by instruction.

## Candidate length audit
- Scanned tagged direct message fields (`Text`, `GOOD`, `Response`, `Candidate`) across all five V8 KB source files: **696 fields**, **0 over 80 characters**; maximum observed length was **61 characters**. This is a static text-field scan, not proof that every runtime-generated output will comply.

## PDF checks
- All five V8 KB PDFs were generated from the V8 Markdown sources with Pandoc/XeLaTeX and DejaVu Sans for Vietnamese glyph coverage.
- Static text extraction and page rendering are checked after generation; no live Gem test is claimed.

## Overall
PASS
