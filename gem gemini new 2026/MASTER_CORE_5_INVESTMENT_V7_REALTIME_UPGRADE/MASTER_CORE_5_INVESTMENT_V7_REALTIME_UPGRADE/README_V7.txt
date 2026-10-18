MASTER CORE + 5 INVESTMENT MODES — V7 FLIRT + REALTIME

Bản V7 giữ kiến trúc Investment Mode (ASSESS / BUILD / MAINTAIN / REPAIR / EXIT) và mở rộng T1–T12.

FILES
- MASTER_CORE_V7_CUSTOM_GEM_INSTRUCTIONS.txt: master instructions.
- CORE/*_CORE_V7.txt: mode overlays; mỗi mode giữ cấu trúc [0]–[23].
- KB_SOURCE/*_KB_V7_SOURCE.md: nguồn Markdown có thể chỉnh sửa, giữ [A]–[T] và thêm [U]–[V].
- KB_PDF/*_KB_V7.pdf: bản PDF xuất từ nguồn Markdown V7.
- DOCS/CHANGELOG_V7.md, MIGRATION_NOTES_V7.md, TEST_CASES_V7.md, QA_REPORT_V7.md: lịch sử, cách triển khai, test và kiểm tra.

IMPORTANT
- @realtime mặc định OFF. Chỉ bật khi cần context công khai hiện hành và có thể xác minh. Không có nguồn thì hỏi user hoặc bỏ chi tiết.
- HARD_QC vẫn giữ 13 checks nền và thêm checks 14–18.
- Safety, consent, autonomy, boundary, factual accuracy và mode lock luôn ghi đè technique.
- [Q] có 30 mục mỗi KB. Yêu cầu tối thiểu 5 ví dụ cho từng T1–T12 không thể thỏa trong từng bank 30 mục (cần 60); coverage được kiểm tra trên toàn bộ corpus 5 KB. REFERENCE_ONLY entries không được xuất ở mode bị khóa.
- PDFs ban đầu trong ZIP đầu vào đã không còn các chuỗi mojibake/spam được liệt kê; REPAIR [I] đã có mục 43–54. V7 regenerate PDFs từ source mới để tránh lỗi layout cũ quay lại.
