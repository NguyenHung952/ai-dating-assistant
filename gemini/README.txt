GEMINI - README
================

Mục đích
--------
Thư mục này chứa tài liệu dùng để cấu hình Gemini Conversation Copilot.

QUY TẮC SỬ DỤNG
---------------
1. Dùng gemini/instructions/MASTER_CORE_v2.7_GENZ_EQ_SHORT.txt làm canonical instruction.
2. Các PDF trong gemini/gem/ là Knowledge Base theo routing function.
3. Chỉ retrieve 1-3 PDF liên quan đến state/intent/context hiện tại.
4. Current conversation evidence luôn được ưu tiên hơn KB pattern.
5. KB dùng để tham khảo pattern/case, không sao chép nguyên câu trả lời.
6. Các prompt cũ trong versions/ là lịch sử/phục vụ regression, không override canonical v2.7.

CẤU TRÚC
--------
gemini/
├── gem/
│   ├── 01_CORE_STATE_ENGINE.pdf
│   ├── 02_GENZ_EQ_RESPONSE_ENGINE.pdf
│   ├── 03_CONVERSATION_FLOW_PATTERNS.pdf
│   ├── 04_PLAY_FLIRT_BOUNDARIES.pdf
│   └── 05_CASES_AND_REGRESSION.pdf
├── instructions/
│   ├── MASTER_CORE v2.4.txt
│   ├── MASTER_CORE v2.5.txt
│   ├── MASTER_CORE v2.6_GENZ_EQ.txt
│   ├── MASTER_CORE_v2.7_GENZ_EQ_SHORT.txt
│   └── README_v2.7.txt
└── README.txt

Phiên bản hiện tại
------------------
MASTER_CORE v2.7_GENZ_EQ_SHORT
5-PDF Consolidated Knowledge Base
Gemini Conversation Copilot