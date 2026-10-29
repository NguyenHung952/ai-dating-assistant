# CHANGELOG V7 — FLIRT + REALTIME CONTEXT

## Master/Core
- Mở rộng FLIRT_CRAFT từ T1–T7 lên T1–T12 (T8 Contextual Play, T9 Self-Aware Humor, T10 Parallel Shift, T11 Callback-to-Future, T12 Micro-Story).
- Nâng EMOTIONAL_IMPACT_QC từ 6 lên 10 tiêu chí; pass >=6/10, 4–5 rewrite, dưới 4 loại.
- Thêm [14] REALTIME_CONTEXT và [15] AI_SMELL_REMOVAL vào Master.
- Giữ 13 HARD_QC checks nền và thêm 14 REALTIME_VERIFIED, 15 AI_SMELL_SCAN, 16 TECHNIQUE_DIVERSITY, 17 ANCHOR_LINE_PRESENT, 18 NO_CONTEXT_DUMP.
- Thêm @realtime on/off (OFF mặc định), @flirt 1/2/3, @tech T#, @explain và @compare; command không override mode/safety.
- Giữ consent, autonomy, boundary-first, no manipulation và no-labeling.

## KB
- Giữ [A]–[T], 54 BAD/GOOD pairs và đủ mục 43–54 trong REPAIR.
- [Q] chuẩn hóa thành 30 mẫu có Technique, Layer, Context requirement và mode gate.
- [R] có 30 tình huống, gồm 10 tình huống realtime có source gate và `Realtime?`.
- [S] có 40 before/after pairs; mọi AFTER <=40 ký tự và có Technique + Layer.
- [T] giữ 20 tình huống khó, bổ sung Layer tags.
- Thêm [U] với 20 realtime hooks (Context source bắt buộc) và [V] với 15 anti-template pairs.
- Numbering chuẩn hóa 01., 02. … trong các phần Q–V.

## Tệp và PDF
- Xuất nguồn, CORE và PDF theo tên V7 để tránh nhầm với bản V6.
- PDF xuất lại từ Markdown V7; kiểm tra lại các trang có vấn đề nêu trong prompt và các trang mới của U/V.

## Mâu thuẫn yêu cầu đã giải quyết
- “30 câu mỗi Q bank” và “5 ví dụ cho mỗi T1–T12 trong mỗi Q bank” mâu thuẫn toán học (30 vs 60). V7 giữ 30 câu/KB theo yêu cầu định lượng trực tiếp, đảm bảo mỗi technique có ít nhất 5 ví dụ trên toàn bộ 5 KB.
- Mode restrictions mâu thuẫn với yêu cầu thêm T8–T12 vào mọi bank. Các mẫu không được phép trong ASSESS/REPAIR/EXIT được gắn `REFERENCE_ONLY`; không được phát ra thành candidate ở mode đó.
