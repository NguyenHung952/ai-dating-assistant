# MIGRATION_NOTES_V8

## Suggested rollout
1. Replace the previous master with `MASTER_CORE_V8_CUSTOM_GEM_INSTRUCTIONS.txt`.
2. Replace mode COREs only where the current setup uses them; use the V8 file matching the mode.
3. Replace each old KB with exactly one corresponding `KB_SOURCE/*_KB_V8_SOURCE.md` or its PDF from `KB_PDF/`.
4. Keep only one version per mode in the Gem's retrieval corpus to avoid V7/V8 duplicate hits.
5. Begin with `@persona off` (auto-select), `@poetic off` unless the chosen personality/context supports it, and `@realtime off` unchanged from V7.
6. Use `@persona [name]` to force a style for a session, `@poetic on/off` to set poetic preference and `@flow on/off` to set NF preference. These commands never override mode locks.
7. `@random on` affects the next session only when the runtime supports session state. Without memory/RNG, the prompt can choose heuristically but cannot guarantee truly random, cross-session non-repeating selection.

## Mode locks
- ASSESS: no active poetic bank and no expectation of flirt escalation.
- BUILD: personality/poetic/NF can activate only when the evidence and context gates pass.
- MAINTAIN: warmth, shared memory and low-pressure poetic callbacks may activate when reciprocal.
- REPAIR: WARM/DEEP/neutral only; no NF. Do not use poetic craft while OTHER is hurt, asking for space, or receiving an apology/accountability response. The [X] examples are conditional/reference-only until acute repair is resolved and the style is welcome.
- EXIT: neutral close only; no active personality tags, no flirt, no poetic craft, no NF.

## Known constraint
V7 error patterns named in the source prompt were not found in the package provided here. Avoid global replacements for context-dependent Vietnamese word pairs. Audit any future fresh PDFs against the source Markdown and render images before distribution.
