# MASTER_CORE 5 STAGE V4

Version: 4.0
Date: 2026-09-24
Target: Vietnamese dating conversation copilot for dating coaches, matchmakers, and power users.

## Package contents

This package contains the 15 explicitly named V4 deliverables (00-14), a README, the 10 verified V2 Knowledge PDFs used as the Knowledge continuity layer, four commercial appendices, and the uploaded V3 files under `PROVENANCE_V3/`.

Note on source package integrity:
The uploaded `MASTER_CORE_5_STAGE_V3_FINAL(1).zip` actually contained 8 files (`00`-`07`) and did not contain `README.txt` or the 10 Knowledge PDFs described in the request. To avoid data loss, V4 preserves the uploaded V3 files exactly under `PROVENANCE_V3/` and reuses the 10 verified Knowledge PDFs from the prior V2 build workspace under `KNOWLEDGE_BASE/`. No V3 source file was overwritten.

## Runtime principle

The stage is fixed by the selected Core. Runtime must never ask the user to identify, confirm, or select a relationship stage.

`CORE_IDENTITY > HARD_STAGE_LOCK > CURRENT_CONVERSATION > CORE_WORKFLOW > KNOWLEDGE_BASE > HISTORICAL_CASES`

Knowledge is reference-only and cannot activate a stage gate.

## V4 product layers

1. Runtime framework and 5 stage cores.
2. Sub-scenario patterns.
3. Golden examples.
4. Memory schema.
5. Failure recovery.
6. Style profiles.
7. Safety layer.
8. Commercial packaging.
9. Research and change log.

## Important product caveat

V4 is a prompt/product architecture. Pricing and commercial packaging are positioning assumptions informed by public benchmarks; they are not proof of customer willingness to pay or a guarantee of commercial success.

## Gemini installation

Each stage Core is intended to be the Gem's Instructions for that stage.

Upload the 10 Knowledge PDFs as Knowledge files.

Do not upload historical V2/V3 runtime prompts as additional instruction sources.

The product-level onboarding can ask stage once before provisioning/selecting the stage-specific Gem. The runtime Core itself must not ask for stage selection.

Use Gemini Preview before saving the Gem. For production, use the regression suite and capture outputs before each release.

## API concept

`POST /v4/generate`

Input:
- memory_schema
- current_message
- stage
- style_profile
- optional recent_turns
- optional mode

Output:
- candidates
- selected_action
- scorecard (internal/debug capable)
- memory_update
- safety_flags

The API should keep approval with the human. It must not auto-send messages.
