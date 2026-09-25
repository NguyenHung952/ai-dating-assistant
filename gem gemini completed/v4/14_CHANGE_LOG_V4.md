# 14 - CHANGE LOG V4

## 1. Baseline

V3 source package uploaded in this turn was audited. The actual ZIP contained 8 files:
00_RESEARCH_NOTES_V3.md
01_MASTER_FRAMEWORK_V3.txt
02_STRANGER_CORE_V3.txt
03_ADDED_ONLY_CORE_V3.txt
04_EARLY_TALKING_CORE_V3.txt
05_MET_IN_PERSON_CORE_V3.txt
06_DATING_CORE_V3.txt
07_CHANGE_LOG_V3.md

The uploaded ZIP did not contain the README or 10 PDFs listed in the user request. V4 preserves the V3 source files under `PROVENANCE_V3/` and reuses the 10 verified Knowledge PDFs from the prior V2 build workspace.

## 2. V3 -> V4 changes

| V3 | V4 | Reason | Source mapping |
|---|---|---|---|
| Hook Engine only | 8-hook operational engine + examples | Reduce filler and random topic jumps | Gottman bids; CA turn relevance |
| Question Budget | Question Budget + recent-turn ratio | Reduce interview feel | Adjacency pairs; recipient design |
| Reply Length Match | Stage-independent recipient-length envelope | Match other person's local turn shape | Sacks/Schegloff/Jefferson |
| Reciprocity Ledger | Ledger + memory persistence | Make reciprocity traceable across turns | APA responsiveness; PPR research |
| Anti-AI-Smell checklist | Explicit hard-fail patterns + positive human test | Turn slogan into QC | OpenAI prompt guidance + product heuristic |
| Pressure Downgrade | Explicit high-uncertainty path | Preserve autonomy | Gottman + safety design |
| Flirt Gate | Stage + >=2 positive reciprocity + <=1 level/turn | Prevent isolated-signal escalation | Research-informed product policy |
| No persistent memory schema | Full JSON schema + update protocol | Make multi-turn product behavior stateful | Prior MASTER_CORE memory model |
| No sub-scenarios | 60 stage-local scenarios | Improve local decision specificity | Conversation-analysis inspired product design |
| No Golden Examples | 24 BAD/GOOD pairs | Provide few-shot contrastive guidance | OpenAI recommends examples/clear output |
| No recovery layer | 7 recovery protocols | Handle failure without pressure | Gottman repair concepts + product design |
| No scorecard | 6-dimension candidate scorecard | Make quality measurable | OpenAI iterative evaluation guidance |
| No refinement loop | Post-send real-outcome loop | Separate drafted vs actually sent evidence | OpenAI iterative refinement |
| Basic safety | Advanced red flags + mental-health guardrails | Reduce harm | Attachment/relationship research + safety design |
| Product tiers basic | Coach/Enterprise implementation packaging | Support commercial deployment | Consumer pricing + B2B SaaS benchmark |

## 3. Golden Example design

Each hook has 3 BAD vs GOOD examples.

Bad lines are intentionally synthetic anti-patterns.
Good lines are natural Vietnamese demonstrations.

These examples do not establish causal effectiveness.

## 4. Sub-scenario design

Each of the five stages covers 12 sub-scenarios:
REPLIED_ONE_WORD
REPLIED_WITH_QUESTION
SHARED_PERSONAL_DETAIL
LEFT_ON_SEEN
USED_EMOJI_ONLY
CANCELLED_PLAN
MENTIONED_EX
ASKED_ABOUT_YOU
SENT_VOICE_NOTE
REPLIED_AFTER_LONG_GAP
BROUGHT_UP_ANOTHER_GUY
COMPLIMENTED_YOU

Each scenario includes PATTERN, RESPONSE_FUNCTION, RECOMMENDED_HOOKS, ANTI_PATTERN, PRESSURE_LEVEL and a stage-specific note.

## 5. Memory

V4 adds a JSON Schema with:
- person_id
- locked stage
- facts with source_turn
- topics
- inside jokes
- boundaries
- preferences
- last state
- ledger snapshot
- last 5 turns
- outcome history

The schema forbids treating generated AI drafts as facts.

## 6. Safety

V4 explicitly blocks:
- manipulation requests
- jealousy tactics
- guilt pressure
- coercion
- sexual escalation without mutual context
- mental-health diagnosis
- AI dependency framing
- minor sexual/dating assistance

## 7. Commercial packaging

The product now separates:
PRODUCT ONBOARDING
from
RUNTIME CORE.

Onboarding may ask stage once to provision/select the correct Gem.
Runtime Core may never ask stage again.

## 8. Research limitations

The exact V4 numeric rules remain product policies:
- >=2 reciprocity indicators
- question ratio >=2:1
- 1-3 sentence budget
- >=20/30 quality threshold
- flirt scale
- 3-5 turn window

They are not presented as scientifically validated constants.

## 9. Final acceptance criteria

- 15 named V4 deliverables: PASS
- README: PASS
- 10 Knowledge PDFs: PASS
- 5 stage cores: PASS
- stage selector runtime: NONE
- stage elicitation: DISABLED
- core-specific routing: PASS
- hook engine: PASS
- question budget: PASS
- reply length match: PASS
- reciprocity ledger: PASS
- memory schema: PASS
- sub-scenarios: 60 / 60
- golden examples: 24 / 24
- recovery protocols: 7 / 7
- safety layer: PASS
- commercial packaging: PASS
- appendices: 4 / 4
- static regression: PASS

