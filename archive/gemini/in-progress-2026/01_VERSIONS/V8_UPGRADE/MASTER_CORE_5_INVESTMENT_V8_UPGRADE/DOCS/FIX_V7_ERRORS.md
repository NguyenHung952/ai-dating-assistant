# FIX_V7_ERRORS — V7 source audit before V8

## Audit scope
Reviewed the actual supplied V7 package: the master instructions, all five mode CORE files, all five KB Markdown sources, and text extracted from all five V7 PDFs.

## Findings
- The specifically listed mojibake strings/control characters (including `¡¢£¤¥`, C1 control characters and common UTF-8 corruption patterns) were **not reproduced** in the supplied Markdown sources or PDF text extraction.
- Repeated-number spam patterns such as `1.1.1.1.1...`, `2.1.1.1.1...`, `3.1.1.1.1...` were **not reproduced** in the supplied Markdown, COREs or extracted PDFs.
- Section headings `[A]` through `[V]` appeared once per KB source; no duplicated section headers were found in the actual sources.
- The mentioned typos were checked contextually. No unambiguous targeted corruption requiring a global substitution was found in this supplied package. Words like `mở/mờ`, `dùng/dừng`, `bắt/bất`, `phân/phần`, and `cãi` were not globally replaced because they can be correct Vietnamese depending on context.
- **A real version-label inconsistency was found:** all five mode-specific CORE files were named V7 but began with `MASTER CORE V6 — MODE` and `V9 INVARIANTS PRESERVED`. V8 copies now use `MASTER CORE V8 — MODE` and `V8 INVARIANTS PRESERVED`.
- [Q]–[V] section-level numbering is normalized to two digits where applicable. New sections [W]–[Y] use the same `## [X]` header convention.

## What was changed
1. Applied only safe, unambiguous text cleanup patterns; none of the listed corruption variants were present to replace.
2. Corrected version labels in five CORE files.
3. Added the V8 personality, poetic and natural-flow rules, five HARD_QC checks, memory fields and runtime commands.
4. Added personality metadata to Q/R/S/T/V entries where permitted. EXIT deliberately omits personality tags and remains neutral, per the mode lock.
5. Added W/X/Y sections to all five KBs. X is disabled in ASSESS/EXIT; Y is disabled in REPAIR/EXIT to honor the stricter mode lock. REPAIR's poetic bank is conditional and must not be used during active hurt.

No source facts were invented to “repair” errors that could not be reproduced.
