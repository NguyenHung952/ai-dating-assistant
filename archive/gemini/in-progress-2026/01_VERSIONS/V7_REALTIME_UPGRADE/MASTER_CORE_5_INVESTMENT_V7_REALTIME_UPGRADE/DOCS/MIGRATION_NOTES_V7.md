# MIGRATION NOTES — V7

## Deployment order
1. Dùng `MASTER_CORE_V7_CUSTOM_GEM_INSTRUCTIONS.txt` làm master instruction.
2. Dùng đúng một CORE overlay theo mode hoặc tích hợp phần mode router, tránh ghép nhiều CORE chồng lấn.
3. Tải một KB tương ứng cho mỗi Investment Mode; PDF và Markdown có cùng nội dung, Markdown là nguồn sửa chính.
4. Chạy toàn bộ TEST_CASES_V7 trước khi thay cấu hình đang chạy.

## Realtime behavior
- Default `@realtime off`; không được tự lấy tin/trend/thời tiết bên ngoài.
- `@realtime on` cho phép tìm/kiểm chứng context công khai hiện hành nếu môi trường có browsing. Khi không có truy cập nguồn, hỏi user hoặc bỏ context.
- Lưu `Context source` cùng thời điểm/địa điểm nếu có liên quan. Khi `@explain`, nêu nguồn; không nhất thiết đưa URL vào candidate nhắn cho đối phương.
- Không dùng realtime trong lúc OTHER đang hurt, yêu cầu space hoặc có boundary cần xử lý.

## Technique gates
- ASSESS: active T1/T4/T8; các T khác chỉ làm ví dụ tham khảo/không xuất. T8 cần context evidence.
- BUILD: T1–T10/T12 khi phù hợp; T11 chỉ khi >=3 turns reciprocity và invitation có đường từ chối.
- MAINTAIN: T1–T12 khi có context; không mặc định escalation.
- REPAIR: active T5 + acknowledge. Các technique flirt còn lại reference-only đến khi repair ổn và có reciprocity.
- EXIT: T5 neutral close; không flirt, không hứa hẹn, không kéo dài sau no-contact.

## Character and output
- Candidate <=80 ký tự; sweet spot <=50; burst <=30 ký tự/tin.
- [S] AFTER <=40 ký tự. Các tag kỹ thuật là metadata, không tính vào message người dùng gửi đi.
- `@flirt 1/2/3`, `@tech T#`, tone và metadata không override consent, safety hoặc active mode.

## Source hygiene
- Không dùng `REFERENCE_ONLY` trong candidate gửi thật.
- Không tự suy ra địa điểm, schedule, attraction hoặc intention từ online status/delay.
- Không sửa các từ tiếng Việt hợp lệ một cách toàn cục chỉ vì chúng giống typo.
