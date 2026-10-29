# V6 — Virtual Memory Conversation Engine

V6 giữ kiến trúc 5 stage của V5 và bổ sung một protocol rõ ràng cho virtual memory.

## Thành phần
- core/: 5 runtime cores có memory protocol.
- knowledge/: 5 stage-specific PDF knowledge bases.
- README này là documentation duy nhất ở cấp version.

## Điểm chính
- CURRENT_CONVERSATION > VIRTUAL_MEMORY > KNOWLEDGE_BASE.
- Virtual memory có schema cho stage, topic, useful detail, boundary, reciprocity, recent candidates và outcome history.
- Có cơ chế xử lý conflict/stale data: evidence mới và user-correction được ưu tiên.
- Giữ question budget, length matching, pressure downgrade và anti-AI-smell.
- Có regression checks để bảo vệ stage lock, hook, question limit và anti-manipulation.

## Đánh giá
V6 là bước chuyển quan trọng từ prompt stateless sang workflow có continuity giữa session, nhưng vẫn yêu cầu dữ liệu memory phải được kiểm chứng và không được biến suy đoán thành fact.
