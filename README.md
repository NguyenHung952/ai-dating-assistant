# 💬 AI Dating Assistant

> Kho lưu trữ prompt, Knowledge Base và tài liệu nghiên cứu cho hệ thống Conversational AI hỗ trợ phân tích ngữ cảnh và soạn phản hồi hội thoại tiếng Việt.

## 🎯 Mục tiêu

Project tập trung vào Conversation Copilot / Prompt Engineering, với các năng lực chính:

- Phân tích screenshot, tin nhắn và transcript.
- Xác định speaker, context và topic hiện tại.
- Tách OBSERVED / SIGNAL / INFERENCE / DECISION, giữ uncertainty khi evidence chưa đủ.
- Khóa relationship stage theo từng core thay vì tự suy diễn stage.
- Xác định conversation state và primary intent.
- Route Knowledge Base theo stage/state/intent.
- Sinh response ngắn, tự nhiên, có continuity và pressure phù hợp.
- Kiểm tra anti-AI-smell, question budget, reply-length và reciprocity.
- Hỗ trợ nhiều stage từ STRANGER đến DATING, với các bản archive từ v1 đến v7.1.

Nguyên tắc xuyên suốt:

```text
CURRENT CONVERSATION > VIRTUAL MEMORY > KNOWLEDGE BASE
FACT ≠ SIGNAL ≠ INFERENCE ≠ DECISION
REPEATED PATTERNS > ISOLATED SIGNALS
UNCERTAINTY > FALSE CERTAINTY
```

## 🧠 Trạng thái hiện tại

Bản release stage-specific mới nhất trong repository là **v7.1**, với prompt canonical:

```text
versions/ver7.1/prompts/MASTER_CORE_v2.7_GENZ_EQ_SHORT.txt
```

Bộ v7.1 stage cores nằm trong:

```text
gem gemini completed/v7/core/
gem gemini completed/v7/knowledge/
```

V7.1 chuyển sang mô hình output rất ngắn, mặc định 2 candidates, HARD MAX 80 ký tự cho candidate, fragment mode, platform calibration và virtual-memory schema. Current Conversation vẫn là nguồn chính; Knowledge Base chỉ hỗ trợ pattern/function/anti-pattern.

Song song, repository có **Consolidated KB v2.7 gồm 5 PDF** tại `gemini/gem/`. Các PDF này được build từ `gemini/gem/source/` bằng `scripts/build_kb_pdfs.py`.

## 📚 Knowledge Base hiện tại

| File | Vai trò |
|---|---|
| `01_CORE_STATE_ENGINE.pdf` | Relationship stage, conversation state, evidence, memory, decision lock |
| `02_GENZ_EQ_RESPONSE_ENGINE.pdf` | Natural Gen-Z rhythm, short response, high-EQ, anti-AI |
| `03_CONVERSATION_FLOW_PATTERNS.pdf` | Topic transition, low-energy, reopening, reciprocity, offline transition |
| `04_PLAY_FLIRT_BOUNDARIES.pdf` | Play/flirt, emotional connection, boundaries và non-manipulative interaction |
| `05_CASES_AND_REGRESSION.pdf` | Cases, regression, LIVE/DEBUG và QC |

Quy tắc routing: thường chỉ retrieve 1–3 PDF phù hợp; không copy historical cases thành câu trả lời; conversation hiện tại luôn được ưu tiên.

## ✍️ Response architecture

Pipeline tổng quát:

```text
INPUT
  ↓
INPUT DETECTION
  ↓
EVIDENCE / CONTEXT
  ↓
RELATIONSHIP STAGE
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
ANTI-AI-SMELL / QC
  ↓
SEND-READY OUTPUT
```

Các response function thường gặp:

```text
ACKNOWLEDGE · CONTINUE · CONTRIBUTE · ASK · CLARIFY · REPAIR · CLOSE
```

Các bản V3–V6 phát triển mạnh hook engine, question budget, reply-length matching, reciprocity ledger, pressure downgrade và virtual memory. V7.1 rút gọn output xuống candidate cực ngắn và tăng hard length control.

## 📂 Cấu trúc repository

```text
ai-dating-assistant/
├── README.md
├── .github/
│   └── workflows/
│       └── build-kb-pdfs.yml
├── claude/
│   ├── README.txt
│   └── SKILL.md
├── example/
│   ├── README.txt
│   └── NHAN_TIN.zip
├── gemini/
│   ├── gem/
│   │   ├── *.pdf                  # Consolidated release KB
│   │   ├── CONSOLIDATED_KB_v2.7_MANIFEST.txt
│   │   ├── legacy/                # Legacy 10-PDF KB
│   │   └── source/                # Markdown source để build PDF
│   ├── instructions/              # Prompt/instruction history
│   └── README.txt
├── gem gemini completed/
│   ├── README.md
│   ├── v1/ ... v7/
│   │   ├── README.txt
│   │   ├── core/                  # Runtime cores
│   │   ├── knowledge/             # PDF knowledge bases
│   │   └── docs/                  # Research/change logs/schema
│   └── ...
├── versions/
│   ├── README.txt
│   └── ver1.0/ ... ver7.1/
│       ├── README.txt             # khi có
│       ├── prompts/               # Prompt history
│       └── docs/                  # Release notes
└── scripts/
    └── build_kb_pdfs.py
```

### Ý nghĩa từng khu vực

- **`gemini/`**: release pipeline hiện tại cho Gemini, gồm instruction, source và consolidated PDF KB.
- **`gem gemini completed/`**: archive stage-specific hoàn chỉnh từ v1 đến v7.1; mỗi version được tách rõ `core/`, `knowledge/`, `docs/`.
- **`versions/`**: lịch sử prompt cũ theo phiên bản; prompt được gom vào `prompts/`, release note vào `docs/`.
- **`claude/`**: skill/instruction dành cho Claude.
- **`example/`**: dữ liệu/example phục vụ thử nghiệm.
- **`scripts/` + `.github/workflows/`**: pipeline build PDF tự động.

## 📊 Thống kê repository

Tại thời điểm audit cấu trúc:

| Metric | Count |
|---|---:|
| Files | **208** |
| Markdown `.md` | 20 |
| Text `.txt` | 115 |
| PDF `.pdf` | 60 |
| JSON `.json` | 2 |
| Python `.py` | 1 |
| YAML `.yml` | 1 |
| ZIP `.zip` | 1 |
| Files không extension | 8 |

Tổng 208 file được giữ nguyên về số lượng; lần dọn này chủ yếu **di chuyển và phân loại**, không xoá lịch sử.

## 🧭 Lịch sử phát triển

- **v1–v2**: stage-locked cores + 10-PDF case/knowledge set.
- **v3**: research notes, hook engine, question budget, reply-length matching, reciprocity và anti-AI-smell được hệ thống hóa.
- **v4**: mở rộng memory/schema, sub-scenario, golden examples, failure recovery, style/safety và validation.
- **v5**: stage cores thống nhất, scorecard nội bộ, human approval và routing theo stage/state/intent.
- **v6**: bổ sung virtual memory protocol và regression checks.
- **v7.0**: tiếp tục hoàn thiện Human Conversation Copilot.
- **v7.1**: short-response engine, 2 candidates mặc định, fragment mode, platform calibration và hard 80-character budget.

## 🚀 Sử dụng

### Gemini

Nếu cần dùng bản consolidated KB, bắt đầu từ:

```text
gemini/instructions/
gemini/gem/
```

Nếu cần xem bản stage-specific mới nhất:

```text
versions/ver7.1/prompts/MASTER_CORE_v2.7_GENZ_EQ_SHORT.txt
gem gemini completed/v7/core/
gem gemini completed/v7/knowledge/
```

### Build lại PDF

Workflow hiện tại build PDF từ:

```text
gemini/gem/source/*.md
        ↓
scripts/build_kb_pdfs.py
        ↓
gemini/gem/*.pdf
```

GitHub Actions có workflow `.github/workflows/build-kb-pdfs.yml` để tự động build khi source hoặc script thay đổi.

## ⚠️ Lưu ý

Đây là framework prompt/conversational assistant, không phải công cụ có thể xác định chắc chắn cảm xúc, attraction hay ý định thật của người khác. Evidence từ một tin nhắn riêng lẻ không đủ để kết luận. Các heuristic như question ratio, sentence budget, reciprocity threshold hay character budget là **engine design policies**, không phải định luật tâm lý.

Trước khi public/share repository, nên kiểm tra screenshot, transcript, tài khoản, dữ liệu cá nhân và dữ liệu bên thứ ba.

## 👨‍💻 Author

**Nguyễn Ngọc Hùng**  
Sinh viên Điện tử Viễn thông – IUH
