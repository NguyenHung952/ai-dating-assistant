# 07 - CHANGE LOG V3

## 1. Baseline audited

V2 source inspected from the uploaded `MASTER_CORE_5_STAGE_V2_FINAL(1).zip`.

The package contains:
- 5 stage-locked runtime cores
- 10 sanitized Knowledge PDFs with 100 structured synthetic case records each
- prior audit/installation files

The V2 cores already correctly enforced Core Identity stage locking, disabled stage elicitation, treated Knowledge as reference-only, separated FACT/SIGNAL/INFERENCE/DECISION, and allowed WAIT/CLOSE_NATURALLY.

The main quality defect was confirmed in all five cores:
`Each option MUST be EXACTLY 2 SENTENCES.`
This made the second sentence a formatting obligation instead of a conversational function.

## 2. V2 -> V3 changes

| V2 | V3 | Why |
|---|---|---|
| EXACTLY 2 SENTENCES | SENTENCE BUDGET 1-3 | Conversation turns vary in length and sequence role; rigid two-sentence output can create filler. Research: turn-taking, adjacency pairs, responsiveness. |
| Sentence 2 = generic EXPANSION | HOOK ENGINE with 8 hook types | Forces a concrete continuation function rather than padding. |
| No explicit question policy | QUESTION BUDGET | Questions create response obligations; not every turn needs a question. |
| No length calibration | REPLY LENGTH MATCH | Makes the reply recipient-sensitive rather than fixed-width. |
| Reciprocity = general principle | REAL RECIPROCITY LEDGER | Uses observable interactional behavior without creating attraction scores. |
| “No AI smell” as slogan | Explicit ANTI-AI-SMELL CHECK | Converts style goal into hard failure criteria. |
| Recent context read was implicit | TURN READING RULE, 3-5 turns | Protects topic continuity and prevents reset/random jumps. |
| Uncertainty only as general caution | PRESSURE DOWNGRADE | Provides an explicit safe fallback when evidence is sparse. |
| Flirt ranges existed | FLIRT GATE tied to >=2 reciprocity indicators and <=1-level change | Prevents escalation from isolated signals. |
| Output labels mostly fixed | Optional hook tags, TAGS ON/OFF | Allows debugging/legibility without exposing chain-of-thought. |

## 3. Stage-specific changes

STRANGER: prioritizes comfort, common ground, observation, low-pressure hooks.

ADDED_ONLY: adds familiarity, profile/shared-interest bridges, light reciprocal self-share.

EARLY_TALKING: adds callbacks, reciprocal disclosure, playful continuity, but requires repeated reciprocity for higher flirt.

MET_IN_PERSON: favors shared-memory callbacks, scene-specific observations, contextual flirt, optional next experiences.

DATING: emphasizes responsiveness, care, affection, emotional calibration, repair and shared activities; flirt is not mandatory.

## 4. Research mapping

- Responsiveness/listening: APA + PubMed reviews -> direct response, acknowledgment, validation, and context-sensitive questions.
- Gottman bids/turning toward: -> recognize bids without forcing escalation.
- Conversation analysis: Sacks/Schegloff/Jefferson + adjacency-pair literature -> answer the immediate action first, preserve sequential relevance, do not stack obligations.
- Backchannels: -> acknowledgment can be a valid conversational move; not every turn needs a question.
- Dialogue-system research: -> explicit topic manager/next-act selection is preferable to keyword-only routing.
- Pew: -> safety/pressure constraints; U.S. prevalence kept out of Vietnam assumptions.
- Tinder APAC + Tuổi Trẻ/B&Company Vietnam: -> cultural calibration, openness of dating-app motives, direct Vietnam context, and caution around safety/trust.
- Attachment review: -> no attachment-style diagnosis from sparse chat.
- OpenAI/Google official prompt guidance: -> clear separation of instructions, context, output format, and iterative preview/testing.

## 5. Evidence status

The following are ENGINE DESIGN POLICIES requested by the project, not claims of empirical constants:
- statement:question >= 2:1 over recent assistant turns
- 1-3 sentence budget
- 1-2 / 2-3 / 2-4 reply length targets
- >=2 positive reciprocity indicators before increasing flirt
- <=1 flirt-level increase per turn
- 8 hook categories

They are explicit product constraints designed to operationalize the research principles, not validated psychological laws.

## 6. Quality target

V3 should optimize for:
REAL_CONVERSATION_FIT > CLEVERNESS
RESPONSIVENESS > PERFORMANCE
CONTINUITY > NOVELTY
RECIPROCITY > ESCALATION
COMFORT > PRESSURE
NATURAL_VIETNAMESE > FORCED_GEN-ZNESS

V3 must never optimize for control, manipulation, response-rate gaming, or “winning” the interaction.

## 7. Static build validation

Files created: 7 required deliverables.
Static Core checks: PASS.
SHA-256 ZIP: `64fefc4e770eb0e35a854b43e326bff65a5af0556d4559b5d71a72f2058d2c3f`
