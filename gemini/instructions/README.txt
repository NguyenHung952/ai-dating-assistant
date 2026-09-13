GEMINI — INSTRUCTIONS README
=============================

Mục đích
--------
Thư mục này chứa các INSTRUCTIONS dùng để paste vào Gemini.

QUY TẮC ƯU TIÊN
---------------
1. Nếu người dùng đang sử dụng GEM:
   - Ưu tiên sử dụng GEM làm nguồn tham khảo chính.
   - Tuân theo cấu hình, kiến thức và cách xử lý của GEM.
   - Không tự ý thay thế GEM bằng các prompt cũ nếu không cần thiết.

2. Nếu không sử dụng GEM:
   - Sử dụng INSTRUCTIONS trong thư mục này.
   - Phiên bản hiện tại: MASTER_CORE v2.5.

3. Thư mục gem/:
   - Chứa 10 PDF Knowledge Base.
   - Dùng để tham khảo pattern, case và kiến thức liên quan.
   - Không xem PDF là instruction.
   - Không sao chép máy móc câu trả lời từ PDF.

4. Thư mục instructions/:
   - Chứa các prompt/instruction để paste vào Gemini.
   - MASTER_CORE là instruction chính.
   - README chỉ giải thích cách sử dụng, không phải prompt chính.

CÁCH SỬ DỤNG
------------
A. Dùng GEM
   → Mở GEM.
   → Để GEM xử lý theo cấu hình của nó.
   → Khi cần tham khảo thêm, sử dụng Knowledge Base trong gem/.

B. Dùng Gemini thông thường
   → Mở file MASTER_CORE v2.5.txt.
   → Copy toàn bộ nội dung.
   → Paste vào Gemini.
   → Sau đó cung cấp screenshot, đoạn chat và context cần thiết.

THỨ TỰ THAM KHẢO
----------------
GEM
↓
MASTER_CORE v2.5
↓
10 PDF Knowledge Base
↓
Conversation hiện tại
↓
Phân tích và tạo response

NGUYÊN TẮC
----------
- Ưu tiên evidence từ conversation hiện tại.
- Không suy diễn quá mức khi thiếu dữ liệu.
- Phân biệt FACT, SIGNAL, INTERPRETATION, INFERENCE và DECISION.
- Knowledge Base dùng để tham khảo pattern, không phải để sao chép câu trả lời.
- Khi evidence yếu, giữ uncertainty.
- Ưu tiên response tự nhiên, phù hợp context và ít áp lực.

CẤU TRÚC
--------
gemini/
├── gem/
│   └── 10 PDF Knowledge Base
└── instructions/
    ├── MASTER_CORE v2.4.txt
    ├── MASTER_CORE v2.5.txt
    └── README.txt

Phiên bản hiện tại
------------------
MASTER_CORE v2.5
10 PDF Knowledge Base
Gemini Conversation Copilot
