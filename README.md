# AI Dating Assistant 💬

Kho lưu trữ prompt, knowledge base và tài liệu nghiên cứu cho hệ thống conversational AI hỗ trợ phân tích ngữ cảnh và soạn phản hồi hội thoại tiếng Việt.

## Nguyên tắc
- Ưu tiên ngữ cảnh hội thoại hiện tại; không suy diễn ý định hoặc cảm xúc khi thiếu bằng chứng.
- Phân biệt dữ kiện, tín hiệu, suy luận và quyết định.
- Tôn trọng ranh giới, sự đồng thuận và quyền riêng tư.
- Giữ các bản cũ để truy vết lịch sử; không xóa nội dung chỉ vì đã có phiên bản mới.

## Cấu trúc repository
```text
.
├── .github/workflows/        # GitHub Actions
├── docs/reference/            # PDF tham khảo trước đây ở thư mục gốc
├── examples/                  # Ví dụ và tài liệu minh họa
├── gemini/                    # Pipeline Gemini hiện tại; giữ nguyên đường dẫn build
│   └── gem/
│       └── source/            # Nguồn dùng để tạo consolidated KB PDFs
├── archive/
│   ├── gemini/
│   │   ├── completed/         # Các bộ Gemini đã hoàn thành
│   │   └── in-progress-2026/  # Các bản đang phát triển năm 2026
│   └── versions/              # Lịch sử prompt theo phiên bản
├── prompts/providers/claude/  # Prompt và skill dành cho Claude
├── scripts/                   # Script build và bảo trì
└── README.md
```

## Khu vực chính
| Đường dẫn | Mục đích |
|---|---|
| `gemini/` | Pipeline Gemini hiện tại. Đường dẫn này được giữ ổn định để tương thích với GitHub Actions. |
| `archive/versions/` | Lịch sử prompt theo phiên bản; dùng để tra cứu và so sánh. |
| `archive/gemini/completed/` | Các bộ knowledge/prompt Gemini đã hoàn thành. |
| `archive/gemini/in-progress-2026/` | Tài liệu đang phát triển trong năm 2026. |
| `prompts/providers/claude/` | Tài liệu và skill dành cho Claude. |
| `docs/reference/` | PDF tham khảo cấp repository. |
| `examples/` | Ví dụ và dữ liệu minh họa. |
| `scripts/` | Script tự động hóa. |

## Build consolidated Knowledge Base PDFs
Workflow sử dụng các đường dẫn hiện tại:
```text
gemini/gem/source/*.md
        ↓
scripts/build_kb_pdfs.py
        ↓
gemini/gem/*.pdf
```

Chạy thủ công:
```bash
python -m pip install reportlab
python scripts/build_kb_pdfs.py
```

Workflow GitHub Actions nằm tại `.github/workflows/build-kb-pdfs.yml`.

## Cách chọn tài liệu
1. Bắt đầu từ `gemini/` nếu cần pipeline hiện tại.
2. Dùng `archive/versions/` để xem lịch sử prompt.
3. Dùng `archive/gemini/` để tra cứu bộ tài liệu Gemini đã hoàn thành hoặc đang phát triển.
4. Xem `docs/reference/` cho các PDF tham khảo cấp repository.

Các bản archive có thể chứa nội dung trùng lặp theo chủ đích để giữ nguyên lịch sử phát triển. Không xóa bản trùng chỉ dựa trên tên file; cần so sánh nội dung và các liên kết tham chiếu trước.

## Quyền riêng tư và giới hạn
Đây là framework hỗ trợ hội thoại, không thể xác định chắc chắn cảm xúc hay ý định thật của người khác. Trước khi công khai dữ liệu, hãy kiểm tra screenshot, transcript, thông tin tài khoản và dữ liệu cá nhân của bên thứ ba.
