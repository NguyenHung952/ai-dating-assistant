# 13 - COMMERCIAL PACKAGING V4

## Product thesis

Position MASTER_CORE V4 as a conversational operating system for human-approved dating communication, not as a “pickup line generator”.

Core differentiation:
- stage-locked runtime architecture
- local Vietnamese context
- turn-aware generation
- hook-based continuation
- explicit question budget
- recipient-length matching
- observable reciprocity ledger
- memory schema
- failure recovery
- safety and consent guardrails
- coach/matchmaker enterprise controls

## Onboarding flow

Important architecture distinction:

PRODUCT ONBOARDING may ask for stage before provisioning the correct Gem.

RUNTIME STAGE CORE must never ask for stage again.

Seven onboarding questions:
1. Bạn đang ở stage nào?
2. Style giao tiếp của bạn?
3. Style của người kia?
4. Mục tiêu: làm quen / hẹn hò / serious?
5. Khu vực: Bắc / Trung / Nam?
6. Tuổi của hai người?
7. Context cụ thể cần xử lý?

Age question is for adult eligibility and context calibration; do not use age to fabricate psychological assumptions.

## Product tiers

### FREE
- 3 candidates / turn
- 5 assisted turns / day
- no persistent memory
- no recovery playbook
- basic stage core
- safety layer active

### PRO - $29/month
- 4 candidates / turn
- higher/unlimited assisted-turn allowance subject to fair-use policy
- persistent Memory Schema
- Reciprocity Ledger
- Style Profiles
- full Recovery Playbook
- stage-specific knowledge routing
- debug export optional

### COACH - $299/month
- multi-client dashboard
- client-scoped memories
- export conversation reports
- custom brand voice
- reusable coaching policies
- quality regression reports
- priority updates
- role-based access

### ENTERPRISE - $30,000 one-time
Position as B2B implementation/license, not as a consumer prompt purchase.

Includes:
- white-label license
- custom training/knowledge onboarding using customer-supplied lawful data
- API integration
- stage-core deployment
- onboarding session
- implementation workshop
- custom safety/policy configuration
- 12 months support
- release/change-log discipline

Excludes unless separately contracted:
- third-party API usage fees
- cloud infrastructure
- legal counsel
- app-store fees
- unlimited custom development
- private data acquisition

## Pricing rationale

Public consumer dating-AI products are generally low-ticket. Current examples include Rizz in-app purchases in Vietnam, WingAI weekly/annual pricing, and Wingman at about $7/week. Hinge Helper publishes one-off specialized service packages from $49/$149 and higher tiers, while Intercom shows a B2B pattern with seat + usage pricing. citeturn213386search0turn213386search2turn832821search1turn832821search4turn832821search3turn850133search0

RevenueCat's 2026 benchmark reports median Y1 realized LTV of $30.16 for AI subscription apps in its dataset, alongside lower 12-month retention for AI than non-AI. This means a $30,000 one-time product price cannot sensibly be defended as consumer LTV alone. It needs an enterprise value stack: implementation, customization, integration, support, governance, and brand/operational leverage. citeturn347364search2

Therefore:
- $29/month = prosumer utility tier.
- $299/month = professional workflow tier.
- $30,000 one-time = custom B2B deployment/license tier.

These prices are product-positioning choices, not verified market-clearing prices.

## API spec

### POST /v4/generate

Request:
```json
{
  "memory_schema": {},
  "current_message": "string",
  "stage": "EARLY_TALKING",
  "style_profile": "STYLE_SOUTH_CASUAL",
  "recent_turns": [],
  "requested_mode": "MULTI",
  "debug_mode": false
}
```

Response:
```json
{
  "candidates": [
    {
      "text": "string",
      "hook_tags": ["callback"],
      "action": "CONNECT",
      "scorecard": null
    }
  ],
  "selected_action": "CONNECT",
  "memory_update": {},
  "safety_flags": [],
  "next_loop": "WAIT_FOR_REAL_REPLY"
}
```

Production rule:
- API must never auto-send.
- Human approval is required.
- Scorecard is hidden unless debug mode is authorized.
- Store minimum necessary data.
- Separate client tenants.

## Coach dashboard

Minimum screens:
1. Client list
2. Conversation timeline
3. Current stage Core
4. Memory snapshot
5. Reciprocity ledger
6. Recovery status
7. Safety flags
8. Draft history with sent/unsent provenance
9. Quality reports
10. Export

## Demo script

### Demo 1 - “Câu cứng”
Input:
“nay em mệt quá”

Show:
V3-style fixed output vs V4 selecting acknowledgement + low-pressure hook and respecting reply length.

### Demo 2 - “Không phải lúc nào cũng hỏi”
Input:
“hôm nay em vừa đi ăn với bạn”

Show:
one statement candidate, one callback candidate, one light question candidate. Explain that question is not mandatory.

### Demo 3 - “Mixed signal”
Input includes one warm turn followed by two short replies.

Show:
Reciprocity Ledger does not create an attraction score; pressure downgrades and WAIT becomes valid.

### Demo 4 - “Recovery”
Show a clearly mismatched message followed by a concise repair rather than a sequence of apologies.

### Demo 5 - “Coach workflow”
Paste 5 turns -> select client -> memory update -> ledger update -> 4 candidates -> approve/send manually -> paste real reply -> next-loop update.

## KPIs for product testing

Do not claim romantic success from response rate alone.

Recommended product metrics:
- candidate acceptance rate by user
- edit distance before send
- percentage of candidates passing hard QC on first generation
- question-stack rate
- topic-jump rate
- average reply-length mismatch
- memory provenance error rate
- safety false-positive/false-negative rate
- recovery usage and user-rated usefulness
- week-4 and month-3 paid retention
- coach client retention
- enterprise deployment success criteria

## Licensing model

Recommended commercial scope:
- licensee-specific configuration
- tenant separation
- no resale of raw training data
- customer owns supplied proprietary data
- provider owns generic framework and non-customer-specific improvements unless contract states otherwise
- custom work governed by statement of work

