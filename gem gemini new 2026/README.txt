# GEM GEMINI NEW 2026

## Mục đích
Thư mục lưu các thế hệ phát triển của bộ hướng dẫn Gemini cho hệ thống chat hẹn hò (V6–V9), gói cập nhật KB V8 và tài liệu nguồn.

## Cấu trúc thư mục

- **00_ARCHIVES/** — Các file ZIP gốc để tải về, đóng gói hoặc lưu trữ.
- **01_VERSIONS/**
  - **V6_REPAIRED/** — Bản V6 đã sửa lỗi.
  - **V7_FLIRT_UPGRADE/** — Bản nâng cấp flirt.
  - **V7_REALTIME_UPGRADE/** — Bản nâng cấp xử lý hội thoại theo thời gian thực.
  - **V8_UPGRADE/** — Bộ V8.
  - **V9_FINAL/**
    - **v1/** đến **v5/** — Các bản V9 và những lần cập nhật được giữ lại để đối chiếu.
    - **legacy_v6/** — Gói legacy V6 được lưu cùng nhóm V9.
- **02_SOURCE/** — Tài liệu DOCX gốc và danh sách file nguồn.
- **03_V8_KB_DOCX_SAFE_UPDATE/** — Gói cập nhật KB V8 từ DOCX và các tài liệu liên quan.
- **README.txt** — Hướng dẫn nhanh cho thư mục này.

## Nên bắt đầu từ đâu?

1. **Dùng V8:** xem `01_VERSIONS/V8_UPGRADE/` và đối chiếu với `03_V8_KB_DOCX_SAFE_UPDATE/`.
2. **Dùng V9:** bắt đầu ở `01_VERSIONS/V9_FINAL/v1/`; đọc changelog/QA report trước khi chọn phiên bản.
3. **Xem tài liệu nguồn:** mở `02_SOURCE/Bao-Cao-Bo-Day-Con-Tan-Gai-Full.docx`.
4. **Tìm gói ZIP:** xem `00_ARCHIVES/`.

## Quy ước quản lý

- Các bản cũ và ZIP được giữ lại để truy vết; không tự động xóa các bản có vẻ trùng lặp.
- Tên gốc của từng gói được giữ bên trong thư mục phân loại để dễ đối chiếu nguồn.
- Trước khi sử dụng, hãy đọc README, changelog và QA report bên trong gói tương ứng.
- Không sửa `MASTER_CORE_V8_CUSTOM_GEM_INSTRUCTIONS` hoặc prompt runtime trong quá trình sắp xếp này. Thay đổi KB cần được kiểm tra riêng.
- Nội dung giao tiếp hẹn hò cần tôn trọng sự đồng thuận, ranh giới và quyền tự quyết; tránh ép buộc, gây ghen, tạo mặc cảm hoặc thao túng cảm xúc.

## Lưu ý

Đây là kho lưu trữ nhiều thế hệ phát triển, không phải một gói runtime duy nhất đã được xác nhận. Hãy kiểm tra tài liệu của từng phiên bản trước khi chọn gói phù hợp.
