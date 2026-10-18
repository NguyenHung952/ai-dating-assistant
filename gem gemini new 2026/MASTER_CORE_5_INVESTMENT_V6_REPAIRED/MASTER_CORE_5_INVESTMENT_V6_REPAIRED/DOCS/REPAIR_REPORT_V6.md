# Báo cáo sửa lỗi V6.1

## Phạm vi đã xử lý

- Giữ nguyên 5 CORE vì kiểm tra cho thấy cấu trúc [0]-[23] đủ, CORE_PROFILE_SPECIALIZATION đúng profile, NEW_CHECK_1 đến NEW_CHECK_10 đều hiện diện, phần MODE ROUTER trong [5], [6], [13], [16] thống nhất, và các khối safety/HARD_QC/budget/fragment/subtext/logic/non-bot-feel khớp giữa các file. Lượt rà chính tả không tìm thấy các lỗi mục tiêu trong CORE; không tái viết các file này.
- Chuẩn hóa 5 KB SOURCE Markdown và tái xuất 5 PDF từ nguồn Unicode.
- Khôi phục/canonicalize [M] VIRTUAL MEMORY SYSTEM theo từng mode, gồm investment_mode, investment_signals, mode_transition_history và stage là secondary attribute.
- Viết lại [G] cho REPAIR và EXIT theo đúng focus: REPAIR nhấn mạnh impact/own part/propose repair/boundary; EXIT nhấn mạnh decision/space/clear close/respect boundary.
- Giữ 17 sub-scenarios trong mỗi [H] và 54 cặp trong mỗi [I]. EXIT [I] items 01-26 được thay bằng ví dụ boundary/withdrawal; rationales của REPAIR/EXIT được viết lại theo mode.
- Giữ P.0 shared principles và P.5 anti-pattern; cá thể hóa P.1-P.4 theo mode, đặc biệt FINANCIAL_BOUNDARY có trong cả năm KB.
- Áp dụng những sửa chính tả theo ngữ cảnh khi phát hiện (bao gồm `từ tế` -> `tử tế`) và giữ tất cả heading section theo dạng `## [X]`.

## Những vấn đề trong prompt không tái hiện trong ZIP đính kèm

- Nguồn Markdown không có ký tự mojibake trong nhóm ký tự được liệt kê; không có spam `M] VIRTUAL MEMORY SYSTEM` hoặc spam số.
- Không có section [H] hay [I] trùng trong REPAIR_KB hoặc EXIT_KB; mỗi section [A]-[P] xuất hiện một lần trong cả năm nguồn.
- Không có trang spam trong PDF đính kèm. Ảnh trang 8 ASSESS, trang 8-9 EXIT và trang 2 BUILD được kiểm tra; không thấy rác encoding hoặc đoạn "Women's Health" bị lặp hai lần.

Các vấn đề trên được ghi nhận là không tái hiện trên đầu vào hiện tại, không tuyên bố đã xóa lỗi không tồn tại.

## QA trước khi đóng gói

- CORE: 28 headings bao gồm [0]-[23], [2.1], [2.5], [11.5], [17.5]; không trùng heading; profile đúng mode.
- KB Markdown: [A]-[P] đủ và mỗi heading đúng một lần; tất cả headings dùng `## [X]`.
- KB [H]: 17 mục mỗi file; KB [I]: 54 mục mỗi file.
- KB [M]: đúng priority tương ứng từng mode.
- KB [P]: P.0/P.5 chung, P.1-P.4 có emphasis riêng cho từng mode.
- PDFs tái xuất bằng Noto Sans Unicode; đã render 5 PDF và rà soát text extraction / page count / ký tự lỗi.
- Đây là QA cấu trúc, nội dung và render. Vẫn cần chạy regression test trong MIGRATION_GUIDE trước khi thay thế Gem production.
