# V5 — Unified Stage Core

V5 chuẩn hóa 5 stage runtime cores theo cùng một kiến trúc: STRANGER, ADDED_ONLY, EARLY_TALKING, MET_IN_PERSON và DATING.

## Thành phần
- core/: 5 runtime cores.
- knowledge/: 5 stage-specific PDF knowledge bases, tương ứng từng core.
- Không có research/changelog riêng trong folder V5.

## Điểm chính
- Hard stage lock và anti-elicitation.
- Current conversation > Knowledge Base.
- Evidence được tách khỏi inference.
- Hook engine, question budget, reply-length match và reciprocity ledger.
- Pressure downgrade khi uncertainty cao.
- Flirt gate dựa trên repeated reciprocity, không dùng một tín hiệu đơn lẻ.
- Candidate có internal scorecard; human approval trước khi gửi.

## Đánh giá
V5 là bản hợp nhất kiến trúc runtime và routing theo stage/state/intent. Nó là cầu nối rõ giữa V4 framework và V6 virtual-memory architecture.
