# 01 - CORE STATE ENGINE

Gộp: Relationship Stages + Conversation States + Evidence + Temporal + Memory + Decision Lock

## 01. CORE STATE ENGINE

**Mục tiêu**

Giữ nguyên pipeline hiện tại: hiểu đúng input trước, khóa state/intent/action, sau đó mới sinh câu trả lời. Bản gộp này không thay decision architecture; nó làm knowledge base nhỏ hơn và routing rõ hơn.

INPUT → SPEAKER → EVIDENCE → TEMPORAL → CONTEXT → STAGE/STATE → INTENT → ACTION → ROUTING → GENERATION → HUMAN FILTER → QC → MEMORY

### Relationship Stage

| Stage | Dùng để khóa |
|---|---|
| STRANGER | Người lạ; chưa có lịch sử đủ rõ |
| ADDED_ONLY | Đã kết nối nhưng gần như chưa trò chuyện |
| EARLY_TALKING | Đang làm quen/trò chuyện vài lần |
| MET_IN_PERSON | Đã gặp trực tiếp |
| DATING | Đang có tương tác hẹn hò |
| CONFIRMED_RELATIONSHIP | Đã xác nhận mối quan hệ |
| UNKNOWN | Chưa đủ chắc; không tự suy ra |

USER_SELECTED_STAGE và STAGE_LOCK luôn có ưu tiên cao hơn stage do AI suy luận. STAGE không đồng nghĩa với attraction hay mức độ tình cảm.

### Evidence hierarchy

- Explicit statement > repeated observable pattern > isolated signal.
- Latest relevant event > old weak inference.
- Conversation hiện tại > knowledge-base pattern.
- AI draft/candidate không phải evidence về điều người kia thực sự nói hoặc cảm thấy.
- Fast reply, slow reply, seen, typing indicator, một emoji hoặc một câu ngắn không đủ để kết luận attraction.

### Uncertainty

Khi evidence yếu hoặc mâu thuẫn, giữ UNKNOWN/UNCERTAIN và chọn action ít áp lực, dễ đảo ngược. Không biến inference thành fact.

## 02. CONVERSATION STATE

State mô tả trạng thái hiện tại của cuộc trò chuyện, không phải tính cách cố định của người kia.

| State | Signal chính | Hướng response |
|---|---|---|
| FLOWING | Hai bên đều đóng góp, hỏi lại, phát triển topic | Continue / connect |
| PLAYFUL | Có humor/tease qua lại | Play nhẹ |
| DEEPENING | Self-disclosure, context sâu hơn | Connect / listen |
| LOW_ENERGY | Reply ngắn, năng lượng thấp | Short / soft / space |
| PAUSE | Endpoint tự nhiên hoặc cần nghỉ | WAIT |
| REOPENING | Có tín hiệu mở lại sau khoảng nghỉ | Respond to new episode |
| UNCERTAIN | Dữ liệu mâu thuẫn/thiếu | Neutral / low-pressure |

### Two critical distinctions

- LOW_ENERGY ≠ LOW_INTEREST. Người kia có thể mệt nhưng vẫn muốn nói chuyện lúc khác.
- TOPIC_FAILURE ≠ PERSON_DISENGAGEMENT. Một chủ đề không hợp không có nghĩa toàn bộ interaction thất bại.

## 03. MEMORY + TEMPORAL

Chỉ ghi nhớ điều người thật sự nói/cho thấy đủ rõ. Không ghi memory từ câu AI vừa tự viết. Khi dữ liệu mới mâu thuẫn dữ liệu cũ, đánh dấu CONFLICTED hoặc giảm confidence thay vì overwrite mù quáng.

REAL MESSAGE → MEMORY CANDIDATE → RELEVANCE CHECK → CONFLICT CHECK → WRITE / HOLD

Tách các episode theo thời gian. Một câu trả lời mới có thể reset state dù lịch sử trước đó từng rất nhiệt.

## 04. DECISION LOCK

Sau khi chọn ACTION, generation không được tự đổi mục tiêu. Ví dụ ACTION=WAIT thì candidate text phải rỗng; ACTION=REACT thì không tự thêm một chuỗi câu hỏi.

DECISION = LOCKED → GENERATE ONLY FOR THAT JOB → HARD QC
