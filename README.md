# 💬 AI Dating Assistant

<p align="center">
  <img src="https://img.shields.io/badge/AI-Conversational%20Assistant-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Gemini-Conversation%20Copilot-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Vietnamese-Gen%20Z-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Prompt%20Engineering-v6.0-orange?style=for-the-badge">
</p>

> Hệ thống prompt hỗ trợ phân tích và soạn phản hồi hội thoại tiếng Việt theo ngữ cảnh, giai đoạn quan hệ, cách xưng hô và tín hiệu tương tác — ưu tiên tự nhiên, ngắn gọn và tránh cảm giác “mùi AI”.

---

## 📌 Dự án là gì?

**AI Dating Assistant** là một project tập trung vào **Prompt Engineering + Conversational AI**, không phải một chatbot độc lập hay một ứng dụng web hoàn chỉnh.

Project phát triển qua nhiều phiên bản prompt (`ver1.0` → `ver6.0`), trong đó phiên bản hiện tại tập trung vào **Conversation Copilot cho Gemini**.

Hệ thống được thiết kế để hỗ trợ:

- Phân tích screenshot hoặc đoạn chat.
- Xác định đúng người nói và ngữ cảnh.
- Xem xét giai đoạn của mối quan hệ.
- Phân tích trạng thái cuộc trò chuyện và mức độ tương tác.
- Đánh giá tín hiệu dựa trên bằng chứng thay vì suy diễn từ một dấu hiệu đơn lẻ.
- Đề xuất nhiều câu trả lời khác nhau nhưng vẫn giữ chung một hướng xử lý.
- Duy trì cách xưng hô do người dùng chỉ định.
- Tạo tin nhắn tiếng Việt theo phong cách tự nhiên, ngắn gọn và phù hợp ngữ cảnh.

---

## 🧠 Kiến trúc xử lý

Phiên bản **MASTER_CORE v2.5** bổ sung một tầng reasoning trước khi hệ thống quyết định cách phản hồi.

```text
INPUT
  ↓
INPUT DETECTION
  ↓
RELATIONSHIP STAGE GATE
  ↓
STAGE LOCK
  ↓
EVIDENCE ANALYSIS
  ↓
REASONING / DECISION ENGINE
  ↓
CONVERSATION STATE
  ↓
PRIMARY INTENT
  ↓
ACTION
  ↓
KNOWLEDGE ROUTING
  ↓
RESPONSE STRATEGY
  ↓
CANDIDATE ENGINE
  ↓
QUALITY CONTROL
  ↓
INTERACTIVE OUTPUT
```

Nguyên tắc cốt lõi:

```text
FACT ≠ SIGNAL ≠ INTERPRETATION ≠ INFERENCE ≠ DECISION
```

Hệ thống ưu tiên **bằng chứng từ cuộc trò chuyện hiện tại**, đồng thời kiểm tra các cách diễn giải thay thế, bằng chứng mâu thuẫn và mức độ không chắc chắn trước khi chọn hành động.

---

## 🎯 Các thành phần chính

### 1. Relationship Stage

Người dùng xác định giai đoạn quan hệ trước khi phân tích conversation:

- `STRANGER` — Người lạ
- `ADDED_ONLY` — Chỉ thêm bạn
- `EARLY_TALKING` — Trò chuyện vài lần
- `MET_IN_PERSON` — Đã gặp mặt trực tiếp
- `DATING` — Đang hẹn hò
- `CONFIRMED_RELATIONSHIP` — Đã xác nhận mối quan hệ
- `UNKNOWN` — Chưa chắc

Stage do người dùng chọn được **lock** và không bị AI tự ý thay đổi.

### 2. Speaker & Context Safety

Phiên bản Gemini hiện tại yêu cầu xác định **stage + cách xưng hô** trước khi xử lý screenshot hoặc đoạn chat mới.

Điều này giúp hạn chế:

- Nhầm người nói.
- Đổi đại từ ngoài ý muốn.
- Dùng context của cuộc trò chuyện khác.
- Tự suy đoán relationship stage.

### 3. Reasoning / Decision Engine

Thay vì đi thẳng từ message → response, hệ thống kiểm tra:

- Evidence mạnh và yếu.
- Alternative hypotheses.
- Contradiction.
- Reciprocity.
- Repeated patterns.
- Uncertainty.
- Action robustness.
- Mức độ pressure và escalation.

Một signal đơn lẻ như emoji, reply nhanh/chậm, seen hoặc một câu ngắn **không được tự động biến thành kết luận chắc chắn**.

### 4. Knowledge Base

Project có **10 PDF knowledge base** dùng làm tài liệu hỗ trợ reasoning và response strategy:

| # | Knowledge Base |
|---|---|
| 01 | Relationship Stages |
| 02 | Conversation States |
| 03 | Gen Z Real Conversations / Style Reference |
| 04 | Cases Success / Failure |
| 05 | Flirting Cases |
| 06 | Emotional Connection |
| 07 | Topic Transition |
| 08 | Low Energy / Pause |
| 09 | Reopening Conversations |
| 10 | Meeting Transition |

Knowledge Base được dùng để **routing và tham chiếu pattern**, không phải để copy nguyên câu trả lời lịch sử.

---

## ✍️ Response Engine

Hệ thống hướng tới các dạng phản hồi như:

- `PLAY` — tạo nhịp vui / playful.
- `CONNECT` — tăng kết nối.
- `CONTINUE` — duy trì conversation.
- `CLARIFY` — làm rõ hiểu lầm.
- `REPAIR` — xử lý interaction bị lệch.
- `TEASE` — trêu nhẹ.
- `FLIRT` — flirt phù hợp context.
- `ESCALATE` / `DE-ESCALATE` — tăng hoặc giảm mức độ tương tác.
- `SUPPORT` — phản hồi hỗ trợ.
- `CLOSE` — kết thúc tự nhiên.

Candidate Engine có thể tạo nhiều phương án, nhưng các phương án phải **khác nhau về cách triển khai**, không chỉ thay vài từ đồng nghĩa.

---

## 🚫 Anti-AI Principles

Project ưu tiên giảm các đặc điểm thường khiến câu trả lời có cảm giác máy móc:

- ❌ Câu quá hoàn hảo.
- ❌ Văn phong như caption.
- ❌ Over-explain.
- ❌ Khen chung chung.
- ❌ EQ giả.
- ❌ Therapist / self-help vibe không phù hợp.
- ❌ Escalation chỉ vì muốn câu trả lời “ấn tượng” hơn.
- ❌ Suy diễn romantic interest từ một signal đơn lẻ.

Thay vào đó:

- ✅ Ngắn gọn.
- ✅ Đúng ngữ cảnh.
- ✅ Giữ nhịp hội thoại.
- ✅ Phù hợp cách xưng hô.
- ✅ Có mức độ không chắc chắn khi evidence yếu.
- ✅ Ưu tiên hành động tự nhiên, ít áp lực và có tính đảo ngược.

---

## 📂 Cấu trúc Repository

```text
ai-dating-assistant/
│
├── README.md
│
├── claude/
│   └── SKILL.md
│
├── example/
│   ├── NHAN_TIN.zip
│   └── README.txt
│
├── gemini/
│   ├── gem/
│   │   └── 10 PDF Knowledge Base
│   │
│   └── instructions/
│       ├── MASTER_CORE v2.5.txt
│       └── README_v2.5.txt
│
├── ver1.0/
├── ver2.0/
├── ver3.0/
├── ver4.0/
├── ver5.0/
└── ver6.0/
    ├── GEMINI_CONVERSATION_PROMPT_1.txt
    ├── GEMINI_CONVERSATION_PROMPT_2.txt
    ├── GEMINI_CONVERSATION_PROMPT_3.txt
    ├── GEMINI_CONVERSATION_PROMPT_4.txt
    └── GEMINI_CONVERSATION_PROMPT_5.txt
```

### Vai trò các thư mục

- **`gemini/`** — hệ thống Gemini hiện tại, gồm Master Core và Knowledge Base.
- **`ver6.0/`** — các phiên bản Conversation Copilot prompt mới nhất.
- **`claude/`** — skill/instruction dành cho Claude.
- **`ver1.0` → `ver5.0`** — lịch sử phát triển và các phiên bản prompt trước.
- **`example/`** — tài liệu/example phục vụ thử nghiệm.

---

## 🚀 Cách sử dụng

Project chủ yếu được sử dụng bằng cách đưa prompt tương ứng vào model hỗ trợ, sau đó cung cấp conversation theo đúng intake mà prompt yêu cầu.

### Với Gemini

Khuyến nghị bắt đầu từ hệ thống trong:

```text
gemini/instructions/
ver6.0/
```

Quy trình cơ bản:

```text
1. Chọn prompt.
2. Cung cấp Relationship Stage.
3. Cung cấp cách xưng hô hiện tại.
4. Gửi screenshot hoặc đoạn chat.
5. Để hệ thống phân tích context và evidence.
6. Nhận các candidate response.
```

Không nên xem các câu trả lời trong Knowledge Base hoặc các case cũ là script bắt buộc. Chúng chỉ đóng vai trò tham chiếu pattern.

---

## 🔬 Định hướng phát triển

- Tăng độ chính xác của speaker attribution.
- Cải thiện reasoning dưới context không đầy đủ.
- Cải thiện memory và continuity giữa các conversation.
- Mở rộng Vietnamese Gen Z conversation dataset.
- Tối ưu Knowledge Base retrieval.
- Tiếp tục giảm hallucination và overinterpretation.
- Phát triển pipeline đa model cho Gemini / Claude và các model tương thích.

---

## ⚠️ Lưu ý

Đây là một **framework prompt / conversational assistant**, không phải hệ thống có khả năng xác định chính xác cảm xúc hoặc ý định thật của một người.

Các kết luận về interest, attraction, rejection hoặc intent luôn có thể không chắc chắn nếu conversation không cung cấp đủ evidence. Hệ thống vì vậy được thiết kế để ưu tiên **context thực tế, uncertainty và low-pressure actions** thay vì khẳng định quá mức.

---

## 👨‍💻 Author

**Nguyễn Ngọc Hùng**  
Sinh viên Điện tử Viễn thông – IUH

---

## 📌 Project Status

**Current focus:** `ver6.0` — Gemini Conversation Copilot  
**Reasoning core:** `MASTER_CORE v2.5`  
**Knowledge Base:** `10 PDF`  
**Primary language:** Vietnamese

---

<p align="center">
  Built with Prompt Engineering • Conversational AI • Reasoning • Vietnamese Gen Z Conversation
</p>
