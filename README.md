# 💬 AI Dating Assistant

> Kho lưu trữ prompt và tài liệu cho hệ thống **Conversational AI / Prompt Engineering** hỗ trợ phân tích và soạn phản hồi hội thoại tiếng Việt theo ngữ cảnh.

## 🎯 Mục tiêu

Project tập trung vào việc phát triển một **Conversation Copilot** cho các model AI, với trọng tâm:

- Phân tích screenshot hoặc đoạn chat.
- Xác định speaker và context.
- Khóa relationship stage và cách xưng hô.
- Phân tích evidence, signal, contradiction và uncertainty.
- Xác định conversation state và intent.
- Chọn response strategy phù hợp.
- Tạo nhiều candidate response tự nhiên, ngắn gọn.
- Giảm overinterpretation và cảm giác “mùi AI”.

Nguyên tắc cốt lõi:

```text
FACT ≠ SIGNAL ≠ INTERPRETATION ≠ INFERENCE ≠ DECISION
```

## 🧠 Hệ thống hiện tại

Phiên bản Gemini hiện tại sử dụng **MASTER_CORE v2.6_GENZ_EQ**, kế thừa reasoning/decision architecture của v2.5 và bổ sung lớp response surface cho natural Gen-Z Vietnamese, teencode calibration và high-EQ emotional calibration.

```text
INPUT
  ↓
INPUT DETECTION
  ↓
RELATIONSHIP STAGE
  ↓
EVIDENCE ANALYSIS
  ↓
REASONING / DECISION
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
```

Project ưu tiên evidence từ conversation hiện tại, kiểm tra giả thuyết thay thế và giữ mức độ không chắc chắn khi dữ liệu chưa đủ.

## ✍️ Response Style

Bản v2.6 tập trung làm cho câu trả lời nghe giống **tin nhắn tiếng Việt thật của người trẻ**, thay vì cố nhồi slang hoặc teencode.

Ưu tiên:

```text
BELIEVABILITY > EMOTIONAL CALIBRATION > USER VOICE > NATURAL VIETNAMESE > GEN-Z RHYTHM > TEENCODE / SLANG > EMOJI > CLEVERNESS
```

### Natural Gen-Z

Gen-Z được thể hiện trước hết qua nhịp chat: câu ngắn, reaction tự nhiên, fragment khi phù hợp, lowercase/punctuation theo USER và từ ngữ đời thường. Không ép mọi candidate phải có slang, emoji, `haha` hoặc `=))`.

### Teencode calibration

Teencode là **optional surface layer**, được calibration theo USER voice, context, emotional state và relationship stage. Không vì OTHER hoặc dataset dùng nhiều teencode mà tự động bắt chước.

### High-EQ

EQ cao được thể hiện qua phản ứng đúng mức với emotional need: acknowledge cụ thể, không over-read, không biến reply thành therapy/coaching, và khi người kia vulnerable thì ưu tiên comfort và space hơn escalation.

## 📚 Knowledge Base

Thư mục `gemini/gem/` hiện có 10 PDF knowledge base:

| # | Tài liệu |
|---|---|
| 01 | Relationship Stages |
| 02 | Conversation States |
| 03 | Gen Z Real Conversations |
| 04 | Cases Success / Failure |
| 05 | Flirting Cases |
| 06 | Emotional Connection |
| 07 | Topic Transition |
| 08 | Low Energy / Pause |
| 09 | Reopening Conversations |
| 10 | Meeting Transition |

Các tài liệu này dùng để **routing và tham chiếu pattern**, không phải để sao chép nguyên câu trả lời.

## ✍️ Response Strategy

Các hướng xử lý chính gồm:

- `PLAY` — tạo nhịp vui.
- `CONNECT` — tăng kết nối.
- `CONTINUE` — duy trì hội thoại.
- `CLARIFY` — làm rõ.
- `REPAIR` — xử lý interaction bị lệch.
- `TEASE` — trêu nhẹ.
- `FLIRT` — flirt phù hợp context.
- `ESCALATE / DE-ESCALATE` — điều chỉnh mức độ tương tác.
- `SUPPORT` — phản hồi hỗ trợ.
- `CLOSE` — kết thúc tự nhiên.

## 📂 Cấu trúc Repository

```text
ai-dating-assistant/
├── README.md
├── claude/
│   └── SKILL.md
├── example/
│   ├── NHAN_TIN.zip
│   └── README.txt
├── gemini/
│   ├── gem/
│   │   └── 10 PDF Knowledge Base
│   └── instructions/
│       ├── MASTER_CORE v2.4.txt
│       ├── MASTER_CORE v2.5.txt
│       └── README_v2.5.txt
└── versions/
    ├── ver1.0/
    ├── ver2.0/
    ├── ver3.0/
    ├── ver4.0/
    ├── ver5.0/
    └── ver6.0/
```

### Vai trò thư mục

- **`gemini/`** — hệ thống Gemini hiện tại, gồm Master Core và Knowledge Base.
- **`versions/`** — lịch sử phát triển prompt từ `ver1.0` đến `ver6.0`.
- **`claude/`** — skill/instruction dành cho Claude.
- **`example/`** — ví dụ và tài liệu phục vụ thử nghiệm.

## 🚀 Cách sử dụng

### Gemini

Có thể bắt đầu từ:

```text
gemini/instructions/
```

Sau đó cung cấp theo intake của prompt:

1. Relationship Stage.
2. Cách xưng hô.
3. Screenshot hoặc đoạn chat.
4. Context cần thiết.
5. Để hệ thống phân tích evidence và conversation state.
6. Chọn candidate response phù hợp.

Các prompt và case cũ trong `versions/` nên được xem là **lịch sử phát triển/tham chiếu**, không phải script bắt buộc.

## 🧪 Định hướng phát triển

- Cải thiện speaker attribution.
- Tăng độ ổn định khi context không đầy đủ.
- Cải thiện continuity và memory.
- Tối ưu Knowledge Base retrieval.
- Giảm hallucination và overinterpretation.
- Tiếp tục phát triển pipeline đa model Gemini / Claude.

## ⚠️ Lưu ý

Đây là framework prompt / conversational assistant, không phải công cụ có thể xác định chắc chắn cảm xúc, attraction hay ý định thật của người khác. Khi evidence yếu, hệ thống nên giữ uncertainty và ưu tiên hành động tự nhiên, ít áp lực.

**Lưu ý bảo mật:** trước khi public repository, kiểm tra screenshot, conversation, tài khoản, dữ liệu cá nhân hoặc dữ liệu bên thứ ba có trong project.

## 👨‍💻 Author

**Nguyễn Ngọc Hùng**  
Sinh viên Điện tử Viễn thông – IUH

## 📌 Project Status

- **Current system:** Gemini Conversation Copilot
- **Reasoning / decision core:** `MASTER_CORE v2.6_GENZ_EQ`
- **Base architecture:** `MASTER_CORE v2.5`
- **Knowledge Base:** 10 PDF
- **Prompt history:** `ver1.0` → `ver7.0`
- **Primary language:** Vietnamese


## 📦 Consolidated Knowledge Base v2.7

The current release can be organized into 5 routed PDFs instead of the original 10-PDF set:

| File | Covers |
|---|---|
| 01_CORE_STATE_ENGINE.pdf | Relationship stages, conversation states, evidence, temporal context, memory, decision lock |
| 02_GENZ_EQ_RESPONSE_ENGINE.pdf | Gen-Z rhythm, short responses, high-EQ calibration, anti-AI, user voice |
| 03_CONVERSATION_FLOW_PATTERNS.pdf | Stories, topic transitions, low-energy/pause, reopening, reciprocity, offline transition |
| 04_PLAY_FLIRT_BOUNDARIES.pdf | Play/flirt, emotional connection, boundaries, dignity, non-manipulative interaction |
| 05_CASES_AND_REGRESSION.pdf | Cases, regression tests, LIVE/DEBUG output, hard QC |

The new prompt is gemini/instructions/MASTER_CORE_v2.7_GENZ_EQ_SHORT.txt.

Routing rule: retrieve only 1-3 relevant PDFs for the current state/intent. Current conversation evidence remains the primary source of truth; KB examples are pattern references, not scripts.
