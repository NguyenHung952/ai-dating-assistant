# 00 - RESEARCH NOTES V4

Ngày nghiên cứu: 2026-09-24
Phạm vi: conversational AI, close-relationship communication, conversation analysis, dating-app context, Vietnam localization, commercial benchmark.

## Evidence policy

- Nguồn học thuật/official được dùng để xây principle và guardrail.
- Nguồn thị trường được dùng để localize và benchmark product packaging, không dùng để chứng minh hiệu quả tình cảm.
- ENGINE DESIGN POLICY = quyết định thiết kế sản phẩm; không phải hằng số tâm lý.
- Không dùng nguồn PUA/red-pill/negging/manipulation.
- Không suy luận attraction từ một tín hiệu đơn lẻ.

## Principle register

| # | Principle | Nguồn | Confidence | Vietnam | Map to V4 |
|---|---|---|---|---|---|
| R01 | Responsiveness nên phản hồi nhu cầu/bối cảnh của đối phương và liên quan đến liking, intimacy, trust, commitment. | https://dictionary.apa.org/responsiveness | CAO | PARTIAL | Direct Response; Emotional Calibration; Scorecard |
| R02 | Self-disclosure và perceived partner responsiveness là các tiến trình liên quan đến intimacy/relationship quality; context matters. | https://pmc.ncbi.nlm.nih.gov/articles/PMC8022838/ | CAO | PARTIAL | Reciprocity Ledger; Deepening; Safety |
| R03 | Attachment insecurity là một hướng nghiên cứu quan trọng nhưng không phù hợp để chẩn đoán từ vài tin nhắn. | https://pmc.ncbi.nlm.nih.gov/articles/PMC4845754/ | CAO | PARTIAL | Safety Layer; no attachment labeling |
| R04 | Turning toward bids hỗ trợ việc nhận diện và đáp lại các nỗ lực kết nối nhỏ. | https://www.gottman.com/blog/the-sound-relationship-house-turn-towards-instead-of-away/ | CAO | PARTIAL | Bid recognition; Hook Engine; Response Function |
| R05 | Criticism, contempt, defensiveness, stonewalling là các pattern giao tiếp phá hoại; repair nên giảm attack/defensiveness. | https://www.gottman.com/blog/the-four-horsemen-recognizing-criticism-contempt-defensiveness-and-stonewalling/ | CAO | PARTIAL | Repair; Safety Layer; Recovery |
| R06 | Turn-taking là locally managed, interactionally controlled, và sensitive to recipient design. | https://www.cambridge.org/core/journals/language/article/simplest-systematics-for-the-organization-of-turntaking-for-conversation/3DB6C0378A96BD5E480A2C0A12FE229A | CAO | PARTIAL | Turn Reading; Reply Length Match |
| R07 | Adjacency pairs tạo cấu trúc first-pair-part / second-pair-part và câu trước có thể tạo kỳ vọng cho phản hồi sau. | https://academic.oup.com/edited-volume/61882/chapter/547683169 | CAO | PARTIAL | Question Budget; Direct Response |
| R08 | Emoji có thể tăng perceived responsiveness trong thí nghiệm digital messaging, nhưng tác động phụ thuộc context; nghiên cứu dùng mẫu 260 người và kịch bản bạn bè. | https://pmc.ncbi.nlm.nih.gov/articles/PMC12221085/ | CAO | PARTIAL | Style Profiles; Anti-AI-Small; emoji mirroring |
| R09 | Nghiên cứu 2025 với 100 người 15-30 tại Việt Nam ghi nhận slang/từ mới phổ biến và ảnh hưởng của TikTok/Facebook; đây là mẫu nhỏ, không phải toàn bộ Gen Z. | https://ijlangstudies.org/index.php/home/article/view/v2.n3.003 | TRUNG BÌNH | YES | Vietnamese style envelope |
| R10 | Tinder Modern Dating in APAC: khảo sát 7,000 người 18-25 tại Australia, India, Japan, Korea, Singapore, Thailand, Vietnam vào 7/2024. | https://datinginapac.com/ | CAO | YES | APAC/Vietnam localization |
| R11 | B&Company BEAN survey 2020 tại Việt Nam: 244 người 18-49; dating apps dùng cho nhiều mục tiêu, privacy/trust là concern; dữ liệu cũ. | https://b-company.jp/online-dating-apps-on-the-trend/ | TRUNG BÌNH | YES | Market context; privacy/Trust |
| R12 | Tuổi Trẻ 2025 tóm lược khảo sát B&Company: dating app có cả mục tiêu kết bạn và tìm quan hệ có ý nghĩa. | https://tuoitre.vn/dulichtphcm/hen-ho-hay-ket-ban-gen-z-viet-nam-tim-gi-tren-ung-dung-hen-ho-10798767.htm | TRUNG BÌNH | YES | Product messaging; intent plurality |
| R13 | Tuổi Trẻ 2026: một bộ phận người trẻ chuyển sang dating events/offline activities để tìm kết nối trực tiếp. | https://news.tuoitre.vn/in-vietnam-busy-young-people-turn-to-offline-dating-events-to-find-connection-103260321114003617.htm | TRUNG BÌNH | YES | Meeting/Shared Activity |
| R14 | OpenAI khuyến nghị instructions rõ, cụ thể, context tách biệt, output format rõ và iterative refinement. | https://help.openai.com/en/articles/6654000-comprehensive-next-generation-prompting | CAO | PARTIAL | Framework organization; refinement loop |
| R15 | OpenAI nhấn mạnh iterative refinement: thử, xem output, chỉnh prompt và context. | https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt | CAO | PARTIAL | Iterative Refinement; Benchmarking |
| R16 | Google Gems: clear/detailed instructions, Knowledge files, preview trước khi Save. | https://support.google.com/gemini/answer/15235603?hl=en | CAO | YES | Gemini installation; V4 layering |
| R17 | Rizz tại App Store Việt Nam đang dùng freemium/in-app purchases; một listing hiển thị các mức từ khoảng 99k-2.999m VND tùy gói/offer. | https://apps.apple.com/vn/app/rizz/id1663430725 | CAO | YES | Consumer price benchmark |
| R18 | Một listing Rizz AI khác ở Việt Nam hiển thị weekly 149k và weekly/trial 199k. | https://apps.apple.com/vn/app/rizz-ai-flirt-texting-wingman/id6758720466 | CAO | YES | Consumer price benchmark |
| R19 | WingAI official pricing: Pro weekly $7.99 sau offer, annual $69.99, Ultimate $129.99; features include reply generation and expert-oriented add-ons. | https://www.wingai.app/pricing | CAO | PARTIAL | Consumer/prosumer benchmark |
| R20 | Wingman official site: free 5 replies/day; Pro $7/week with unlimited analyses/checks/coach. | https://wingmantheapp.com/ | CAO | PARTIAL | Consumer/prosumer benchmark |
| R21 | Hinge Helper publishes $49 DIY Reset Kit and $149 done-for-you on its site; terms describe tiers up to $349 for Match Booster. This is a specialized service, not a direct AI prompt benchmark. | https://hingehelper.com/ | TRUNG BÌNH | NO | Service packaging benchmark |
| R22 | YourMove is described as a dating assistant with free/trial access; public pricing was not reliably verified in current search. | https://domore.ai/tools/yourmove.ai | THẤP | PARTIAL | Competitive note only |
| R23 | Intercom current B2B benchmark: Essential $29/seat/month annual, Advanced $85, Expert $132, Fin from $0.99/outcome. | https://www.intercom.com/pricing | CAO | PARTIAL | B2B packaging and usage pricing |
| R24 | RevenueCat 2026: AI subscription apps median Y1 realized LTV $30.16 vs $21.37 non-AI; AI retains less at 12 months across weekly/monthly/annual plans in its dataset. | https://www.revenuecat.com/state-of-subscription-apps | CAO | PARTIAL | Pricing architecture; retention caution |
| R25 | Lemon Squeezy examples show small prompt products around $5-$197; use only as low-rigor market signal, not valuation evidence. | https://promptquik.lemonsqueezy.com/ | THẤP | NO | Low-end prompt-product benchmark |

## What research supports for V4

### 1. Responsiveness over performance
Research supports responding to what the other person actually disclosed or asked, rather than optimizing solely for “cleverness”. This maps to direct response, acknowledgment, self-disclosure reciprocity, and the choice to pause.

### 2. Turn-by-turn sequential relevance
Conversation analysis supports treating the latest turn as a local action that normally deserves a locally relevant next move. V4 therefore answers the current action before opening another branch.

### 3. Hooks as continuation functions
The eight V4 hook categories are product abstractions derived from continuity, self-disclosure, recipient design, open conversational structure, and playful/social moves. The eight categories themselves are NOT an established scientific taxonomy.

### 4. Question budget as a product constraint
Adjacency-pair research suggests questions create a response-relevant next part. V4 uses a one-question cap and a recent statement/question balancing rule as an ENGINE DESIGN POLICY, not as a universal psychological law.

### 5. Reply length matching
The research supports recipient design and sequential fit. The exact sentence ranges in V4 are implementation heuristics, not published scientific cutoffs.

### 6. Reciprocity ledger
The five tracked dimensions are deliberately observable. They should not be converted into an attraction score. Repetition across turns is treated as stronger evidence than an isolated signal.

### 7. Safety and attachment
Attachment theory belongs in a cautionary layer, not a diagnostic classifier. Sparse chat evidence is insufficient to label someone anxious, avoidant, depressed, manipulative, or romantically invested.

### 8. Vietnam localization
The best direct context source found is Tinder's APAC study covering Vietnam in a 7-country survey of 7,000 18-25 year olds. B&Company data is useful but older. Vietnamese youth-language evidence supports flexible style mirroring, not a fixed slang dictionary.

## Commercial benchmark synthesis

Current public consumer dating-AI pricing is mostly low-ticket subscription or lifetime access. Rizz listings in Vietnam show multiple in-app purchase points, WingAI publishes weekly and annual tiers, and Wingman advertises a free daily allowance plus a $7/week Pro plan. Hinge Helper demonstrates that a highly specific, human-assisted dating service can charge $49-$149+ for one-off service packages, but its service is not directly comparable to a conversational AI engine. citeturn213386search0turn213386search2turn832821search1turn832821search4turn832821search3

B2B software often monetizes through seats and/or usage rather than a single giant prompt-pack payment; Intercom currently publishes seat and per-outcome pricing, while RevenueCat's 2026 data shows AI subscriptions can achieve higher median Y1 LTV than non-AI apps but weaker retention. citeturn850133search0turn347364search2

Therefore the requested `$30,000 one-time ENTERPRISE` tier should be positioned as a B2B implementation/license package with customization, training, integration, onboarding and support—not as “a $30k prompt”. This is a product-positioning recommendation, not proof that $30,000 is an accepted market price.

## Research limitations

- No reliable public source verified current YourMove pricing.
- No high-quality Vietnam dating-coach price dataset was found that would support a numeric market average.
- Consumer dating-app benchmarks and B2B AI software benchmarks are not interchangeable.
- Public product claims about user counts or “results” are treated as marketing claims unless independently verified.
- Research cited above does not validate V4's exact numeric engine policies.

## Core design policies that are intentionally NOT empirical constants

- sentence budget 1-3
- question cap 1
- statement:question >= 2:1 over three recent assistant turns
- >=2 positive reciprocity indicators before increasing flirt
- max one flirt-level increase per turn
- score threshold >=20/30
- 3-5 turn reading window
- sub-scenario pressure labels
- 5-point flirt scale

These exist to make the product behavior predictable and testable.
