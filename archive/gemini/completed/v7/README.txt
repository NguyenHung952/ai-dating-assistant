# V7.1 — Short-Response Stage Engine

V7 folder chứa bộ **V7.1 stage-specific conversation response engine**.

## Thành phần
- core/: 5 stage cores V7.1.
- knowledge/: 5 stage-specific KB PDFs V7.1.
- Không có docs riêng; README này mô tả release.

## Điểm chính
- Gemini-specific override: không giả vờ truy cập nguồn không có.
- Current Conversation > Virtual Memory > Knowledge Base.
- Evidence tách OBSERVED / INFERRED / POSSIBLE / UNCERTAIN.
- Mỗi candidate có một primary social function.
- Default 2 candidates, phải khác social function/move/pressure/tone.
- Fragment mode cho phép câu cụt/reaction khi tự nhiên.
- HARD MAX 80 ký tự cho candidate.
- Platform calibration và Gen-Z calibration dựa trên chính conversation, không dùng stereotype.
- Recovery ưu tiên repair, clarification, lower pressure và close tự nhiên.
- Anti-elicitation bảo vệ quyền từ chối và tránh ép tiết lộ thông tin.

## Đánh giá
V7.1 là bản stage-specific ngắn và chặt về output format nhất trong archive hiện tại. Nó phù hợp khi mục tiêu là tin nhắn gửi ngay, cực ngắn, có context và dễ reply.
