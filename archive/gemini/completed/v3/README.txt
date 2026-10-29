# V3 — Research-Driven Conversation Engine

V3 là bước chuyển từ output cố định sang conversation engine có quy tắc theo ngữ cảnh.

## Thành phần
- core/: MASTER_FRAMEWORK_V3 và 5 stage runtime cores.
- docs/00_RESEARCH_NOTES_V3.md: nghiên cứu và mapping từ evidence sang design policy.
- docs/07_CHANGE_LOG_V3.md: audit V2 và các thay đổi V2 → V3.
- knowledge/: không có PDF riêng trong V3.

## Điểm chính
- Bỏ quy tắc cứng EXACTLY 2 SENTENCES.
- Dùng sentence budget 1–3 câu tùy turn.
- Có hook engine, question budget và reply-length matching.
- Theo dõi reciprocity bằng observable behavior, không tạo attraction score.
- Có pressure downgrade và anti-AI-smell checks.
- Knowledge/historical cases chỉ là reference; current conversation được ưu tiên.

## Đánh giá
V3 là bản framework nghiên cứu + runtime core, phù hợp để đọc logic tiến hóa của engine trước V4–V7.
