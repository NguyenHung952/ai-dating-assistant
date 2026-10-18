# CHANGELOG V6 — MASTER CORE / KB ĐỔI TRỤC SANG INVESTMENT MODE

## 1. Thay đổi chính
- Đổi trục runtime từ chronological stage sang investment mode: ASSESS, BUILD, MAINTAIN, REPAIR, EXIT.
- Thay [2] STAGE LOCK bằng [2] INVESTMENT_MODE_LOCK và [2.1] STAGE_ATTRIBUTE. Stage STRANGER → ADDED_ONLY → EARLY_TALKING → MET_IN_PERSON → DATING vẫn tồn tại nhưng là thuộc tính phụ.
- Bổ sung INVESTMENT_SIGNAL_DETECTION cho reciprocity, one-sided patterns, red flags, repair cues và exit cues. Delay, emoji, độ dài tin nhắn chỉ là contextual signals, không phải FACT độc lập.
- Bổ sung INVESTMENT_MODE_TRANSITION_RULES: ASSESS→BUILD khi có ít nhất 2 tín hiệu reciprocity liên tiếp; BUILD→MAINTAIN khi có ritual/shared memory ổn định; mismatch/hurt → REPAIR; red flag nghiêm trọng hoặc lời nói muốn dừng → EXIT.
- Điều chỉnh RESPONSE FUNCTION, CANDIDATE ENGINE variants, tone defaults, recovery và knowledge routing theo mode.
- Thêm investment_mode, investment_signals, mode_confidence và mode_transition_history vào virtual memory.
- KB có đủ [A]–[P], gồm H 17 sub-scenarios, I 54 BAD/GOOD examples, J 12 protocols cộng routing theo mode, K tone map theo mode, N Investment Playbook và P Modern Dating Context.
- Thêm INVESTMENT_ETHICS: không ép tăng investment, không guilt, không xem reciprocity là nghĩa vụ, không biến care thành control, không dùng exit để trừng phạt.

## 2. Những gì được giữ
- Giữ các section CORE chính [0]–[23]; thêm [2.1] làm thuộc tính stage phụ, gộp candidate variants vào [6].
- Giữ nguyên [2.5] ROLE_LOCK_CHECK, [18] HARD_QC và NEW_CHECK_1 đến NEW_CHECK_10, gồm NO_LABELING.
- Giữ nguyên các nguyên tắc [7] FRAGMENT MODE, [8] CHARACTER BUDGET, [9] SHORT MODE, [20] SUBTEXT_READING, [21] LOGIC_ENGINE, [22] NON_BOT_FEEL.
- Giữ 11 tone profiles; chỉ đổi default tone theo investment mode.
- Giữ safety, consent, autonomy, privacy, anti-elicitation, no-labeling và recovery chống silent treatment, jealousy bait, scarcity giả, guilt-trip.
- Giữ nội dung nguồn [A]–[O] của KB làm nền tham chiếu và bổ sung/điều chỉnh những phần cần thiết để nhất quán với investment mode. Ví dụ legacy mang tính fake scarcity đã được sửa để không xung đột với safety và no-manipulation checks.

## 3. Mapping stage cũ → mode mới (khởi tạo, không phải ánh xạ cứng)
| Stage cũ | Mode khởi tạo thường gặp | Ghi chú |
|---|---|---|
| STRANGER | ASSESS | BUILD chỉ sau ít nhất 2 tín hiệu reciprocity liên tiếp. |
| ADDED_ONLY | ASSESS hoặc BUILD | Việc đã thêm bạn không chứng minh reciprocity. |
| EARLY_TALKING | ASSESS hoặc BUILD | MAINTAIN cần ritual/shared memory ổn định. |
| MET_IN_PERSON | ASSESS / BUILD / MAINTAIN | Đã gặp không tự động cấp intimacy hoặc commitment. |
| DATING | BUILD / MAINTAIN, nhưng có thể ASSESS / REPAIR / EXIT | Thời gian quen nhau không chứng minh đáng đầu tư. |

REPAIR và EXIT có thể xuất hiện ở bất kỳ stage nào. OTHER đang tổn thương: ưu tiên REPAIR nếu chưa yêu cầu dừng; lời yêu cầu dừng/boundary cứng phải được tôn trọng ngay và xử lý theo EXIT/CLOSE.

## 4. File cũ có thể retire hoặc archive
- `STRANGER_CORE_V9.txt` → archive sau khi triển khai `ASSESS_CORE_V6.txt`.
- `ADDED_ONLY_CORE_V9.txt` → archive; logic familiarity chuyển vào STAGE_ATTRIBUTE và BUILD/ASSESS routing.
- `EARLY_TALKING_CORE_V9.txt` → archive; các callback/reciprocity examples được tái phân bổ vào BUILD.
- `MET_IN_PERSON_CORE_V9.txt` → archive; offline memory/contextual warmth trở thành stage attribute trong các mode.
- `DATING_CORE_V9.txt` → archive; maintenance/recovery/coordination được tái phân bổ vào MAINTAIN/REPAIR/EXIT.
- Năm PDF `*_KB_V9.pdf` → archive bản gốc để traceability; thay bằng `*_KB_V6.pdf` khi đã kiểm thử, và giữ `*_KB_V6_SOURCE.md` nếu cần biên tập.

## 5. Ghi chú triển khai
V6 là bản chuyển đổi kiến trúc và biên tập dựa trên file đã cung cấp; không tuyên bố đã được kiểm định thực nghiệm. Trước khi thay thế production, chạy test matrix trong MIGRATION_GUIDE và so sánh output với bản V9 trên các tình huống thực tế đã ẩn danh.

## V6.1 — Repair patch

- Giữ nguyên 5 CORE sau khi xác nhận section, mode router, safety, HARD_QC NEW_CHECK_1..NEW_CHECK_10, budget và các khối bất biến đã đồng bộ; rà lỗi chính tả mục tiêu không phát hiện lỗi trong CORE.
- Chuẩn hóa VIRTUAL MEMORY [M] theo từng mode: ASSESS giữ profile facts/topic/signals; BUILD giữ callbacks/reciprocal disclosures/shared context; MAINTAIN giữ shared memory/ritual/care/boundaries/coordination; REPAIR giữ hurt/own part/proposed repair/boundary/next step; EXIT giữ boundary/decision/space/logistics.
- Viết lại PROFILE ANALYZER [G] cho REPAIR và EXIT bằng ví dụ đúng mode.
- Giữ 17 sub-scenarios trong [H] và 54 BAD/GOOD pairs trong [I]. Ví dụ EXIT [I] 01–26 chuyển sang boundary/withdrawal; toàn bộ rationales của REPAIR/EXIT được đặc thù hóa theo mode.
- Cá thể hóa MODERN DATING CONTEXT [P] cho từng mode ở P.1–P.4; giữ nguyên P.0 shared principles và P.5 anti-pattern.
- Tái xuất toàn bộ KB PDF bằng Noto Sans Unicode; kiểm tra text extraction, section coverage và rendered pages.
- Các lỗi mojibake/spam và section [H]/[I] trùng được nêu trong yêu cầu không tái hiện trong ZIP đầu vào hiện tại; được xác minh và ghi trong REPAIR_REPORT_V6.md thay vì tuyên bố xóa lỗi không tồn tại.


## V7 — Flirt craft and emotional impact upgrade

- Added master sections [11] FLIRT_CRAFT, [12] EMOTIONAL_IMPACT_QC, [13] RESPONSE_RHYTHM, four emotional subtypes L2a-L2d, and flirt/tone user controls.
- Integrated the same controls into the five mode COREs without removing existing sections [0]-[23] or HARD_QC NEW_CHECK_1..10. Added NEW_CHECK_11..13 and recovery protocols 13-16.
- Updated all five KB Markdown files: 54 shorter, technique-tagged GOOD examples each; 10 added profile examples; 20 Q-bank responses; 20 contextual scenarios; 30 before/after examples; 20 hard scenarios; 16 recovery protocols.
- Mode calibration: ASSESS low-pressure; BUILD playful only with reciprocity; MAINTAIN callback/care/space; REPAIR neutral while hurt is active; EXIT no flirt.
- This upgrade is a candidate set; human judgement and regression testing remain necessary.
