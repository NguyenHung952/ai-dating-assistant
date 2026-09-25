# Gemini Completed Archive

Kho archive các bản stage-specific của Gemini Conversation Engine từ **v1 → v7.1**.

Mỗi version được tổ chức thống nhất:

```text
vX/
├── README.txt
├── core/       # Runtime cores / framework
├── knowledge/  # PDF Knowledge Base
└── docs/       # Research, changelog, schema, validation
```

## Version map

| Version | Nội dung chính |
|---|---|
| v1 | 5 stage cores + 10 PDF case/knowledge files |
| v2 | V2 stage cores + 10 PDF case/knowledge files |
| v3 | Research-driven framework, hooks, question budget, reciprocity |
| v4 | Memory, scenarios, style, safety, recovery, validation |
| v5 | Unified stage cores, routing, scorecard, human approval |
| v6 | Virtual memory protocol + regression checks |
| v7 | V7.1 short-response stage-specific engine |

Các file trong archive được giữ nguyên nội dung; việc sắp xếp lại chỉ tách **core / knowledge / docs** để dễ tìm và tránh trộn nhiều loại artifact trong cùng một thư mục.
