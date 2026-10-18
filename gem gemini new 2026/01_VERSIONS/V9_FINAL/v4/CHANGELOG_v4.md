# CHANGELOG_v4 — MASTER_CORE_5_STAGE_V9_FINAL_v4

## Phạm vi

Đã xử lý bộ `MASTER_CORE_5_STAGE_V9_FINAL_v3.zip`, gồm 5 CORE `.txt` và 5 KB `.pdf`. Bản xuất giữ nguyên tên 10 file nguồn; thay đổi tập trung vào yêu cầu A.1–A.4 và B.1–B.8.

## Danh sách file đã sửa

**CORE (5/5):**
- `STRANGER_CORE_V9.txt`
- `ADDED_ONLY_CORE_V9.txt`
- `EARLY_TALKING_CORE_V9.txt`
- `MET_IN_PERSON_CORE_V9.txt`
- `DATING_CORE_V9.txt`

**KB (5/5):**
- `STRANGER_KB_V9.pdf`
- `ADDED_ONLY_KB_V9.pdf`
- `EARLY_TALKING_KB_V9.pdf`
- `MET_IN_PERSON_KB_V9.pdf`
- `DATING_KB_V9.pdf`

## PHẦN A — Tone profile và ví dụ mới

- **A.1 — Cả 5 CORE:** thêm `WITTY_CONFIDENT` trong `[11.5] TONE_ENGINE` sau `PLAYFUL_CHARM`; thêm phân biệt với `CONFIDENT_BOLD` và `PLAYFUL_CHARM`; quy định trả lời thẳng trước rồi mới thêm wit, không đảo vai ép OTHER tự thú và không hỏi ngược để né câu hỏi quan trọng. Cập nhật “nine labels” thành “ten labels”. Guardrail anti-manipulation được mở rộng để bao gồm `WITTY_CONFIDENT`; `NEW_CHECK_7: NO_MANIPULATION` và `[15] ANTI-ELICITATION KILL SWITCH` được giữ nguyên.
- **A.2 — Cả 5 KB:** thêm `WITTY_CONFIDENT` vào `[E] TONE ENGINE NOTES` và `[K] STYLE PROFILES`; cập nhật header thành `10 PROFILES`. Với `ADDED_ONLY_KB_V9.pdf`, các profile cũ bị thiếu trong phần `[K]` đã được tích hợp để đủ 10 profile theo schema chung; `DEFAULT TONE` riêng của stage được giữ nguyên. Hai guardrail hiện có được tích hợp trong `[L]` và guardrail tone được mở rộng để bao gồm `WITTY_CONFIDENT`.
- **A.3 — Cả 5 KB:** thêm cặp 33–38 vào cuối `[I] GOLDEN EXAMPLES`, cùng format `BAD / GOOD / Rationale`; cập nhật header thành `38 BAD/GOOD PAIRS` và mục lục `[A]` thành `38 BAD vs GOOD`.
- **Điều chỉnh nhất quán an toàn:** wording GOOD ở cặp 33–35 được chỉnh nhẹ so với ví dụ đầu vào để trả lời câu hỏi trực tiếp trước khi thêm câu duyên, đúng nguyên tắc A.1. Cặp 36–38 giữ nội dung theo yêu cầu. Không bổ sung tone hay protocol ngoài phạm vi yêu cầu.
- **A.4:** không tạo `V3 SECTION ADDITIONS`; nội dung cũ được nhập vào các mục chính `[J]`, `[K]`, `[L]`.

## PHẦN B — Lỗi tồn đọng

- **B.1 — `STRANGER_KB_V9.pdf`:** tái tạo PDF từ phần văn bản còn đọc được, gồm title, Focus, Runtime emphasis, `[A] COVER + MỤC LỤC`, `[B] RESEARCH NOTES + EVIDENCE LEVEL`, `[C] GEN Z CALIBRATION NOTES` và `[D] PLATFORM CALIBRATION NOTES`. Mục lục được cập nhật các số 38/12/10. Không có file v2 trong ZIP đầu vào, nên không thể đối chiếu từng chữ với bản v2 gốc.
- **B.2 — `STRANGER_KB_V9.pdf`:** chuẩn hóa `[I]` thành danh sách duy nhất 01–38; đầu ra có đúng một cặp 27. Lớp text trích xuất từ PDF đầu vào chỉ cho thấy một cặp 27, nên không xác định được bản trùng cụ thể nào đã tồn tại ở lớp hiển thị.
- **B.3 — `MET_IN_PERSON_KB_V9.pdf`:** header recovery được chuẩn hóa thành `[J] RECOVERY PLAYBOOK — 12 PROTOCOLS`.
- **B.4 — `EARLY_TALKING_KB_V9.pdf`:** tái tạo trang từ nội dung đọc được, giữ `[E] TONE ENGINE NOTES` và các mục kế tiếp; dãy Latin mở rộng nêu trong mô tả không xuất hiện trong phần render/text extraction kiểm tra của file v3 được cung cấp.
- **B.5 — Cả 5 KB:** xóa khối `V2 SECTION ADDITIONS`; nhập protocols 11–12 vào `[J]`, các profile `CONFIDENT_BOLD`/`PLAYFUL_CHARM` cùng `WITTY_CONFIDENT` vào `[K]`, và các guardrail vào `[L]`.
- **B.6 — Cả 5 KB:** sắp xếp `[I] GOLDEN EXAMPLES` thành một khối liên tục 01–38, hoàn tất trước khi `[J]`, `[K]`, `[L]` bắt đầu.
- **B.7 — Cả 5 KB:** định dạng `[K] STYLE PROFILES` sao cho mỗi profile là một dòng/đoạn riêng; đủ 10 profile ở từng KB.
- **B.8 — Cả 10 file:** áp dụng các thay thế typo được cung cấp. Kiểm tra cuối xác nhận các chuỗi typo đã liệt kê không còn trong CORE/PDF text đầu ra; cụm `thể hiện` không bị thay thế.

## Kiểm tra đầu ra

- Có đủ 5 CORE và 5 KB; tên file được giữ nguyên.
- Cả 5 KB có đúng 38 cặp `01`–`38`, mỗi số xuất hiện một lần trong `[I]`.
- Cả 5 KB có 12 protocol, 10 profile, tone `WITTY_CONFIDENT`, và không có chuỗi `V2 SECTION ADDITIONS`.
- Thứ tự section được xác nhận: `[I]` → `[J]` → `[K]` → `[L]` → `[M]` → `[N]` → `[O]`.
- PDF được dựng lại ở khổ A4 và render kiểm tra; chữ tiếng Việt đọc được, các section không bị chồng lấn/cắt mất.

## Giới hạn cần biết

ZIP đầu vào không chứa bản v2 để làm nguồn so sánh. Ngoài ra, hai chuỗi lỗi trang được báo ở B.1 và B.4 không xuất hiện trong phần render/text extraction quan sát được của các PDF v3 được cung cấp; vì vậy bản v4 được làm sạch bằng cách tái tạo từ phần nội dung có thể đọc được, thay vì tuyên bố khôi phục nguyên văn từ v2. Do việc gom lại thứ tự section và loại phần lặp, bố cục PDF được reflow; số trang đầu ra là 5 trang/KB thay vì giữ nguyên từng ngắt trang vật lý của v3, nhưng cấu trúc mục lục và thứ tự section được giữ.
