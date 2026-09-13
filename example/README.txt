EXAMPLE — NHẮN TIN
===================

Thư mục `example` chứa các ví dụ dùng để TEST hệ thống AI hỗ trợ nhắn tin với gái.
`NHAN_TIN.zip` là bộ dữ liệu ví dụ; README này mô tả các tình huống AI cần biết cách xử lý.

CÁC TÌNH HUỐNG XỬ LÝ
---------------------

1. MỞ ĐẦU
- Người mới quen/chưa nói chuyện nhiều.
- Tạo câu mở đầu tự nhiên, ngắn và có điểm để đối phương trả lời.
- Tránh câu sáo rỗng hoặc hỏi dồn.

2. TRÒ CHUYỆN BÌNH THƯỜNG
- Đối phương có tương tác và trả lời đầy đủ.
- Bám context, bắt chi tiết trong tin nhắn trước để phát triển chủ đề.
- Không biến cuộc trò chuyện thành phỏng vấn.

3. TRẢ LỜI NGẮN
- Ví dụ: "ừ", "ok", "haha".
- Giảm độ dài và áp lực trong câu trả lời.
- Ưu tiên một hướng dễ tiếp tục thay vì hỏi liên tục.

4. ĐỐI PHƯƠNG LẠNH / ÍT HỨNG THÚ
- Nhận diện mức độ tương tác thấp.
- Không spam, trách móc hoặc ép trả lời.
- Có thể giảm nhịp hoặc kết thúc nhẹ.

5. TRẢ LỜI CHẬM / ĐANG BẬN
- Không mặc định đối phương mất hứng thú.
- Không hỏi kiểu "sao không rep?".
- Khi mở lại, ưu tiên dùng context cũ thay vì tin nhắn vô nghĩa.

6. THẢ THÍNH / FLIRT
- Chỉ tăng mức độ thân mật khi context và tín hiệu phù hợp.
- Có thể trêu nhẹ hoặc flirt nhẹ.
- Không chuyển quá nhanh sang lời tán tỉnh trực diện.

7. ĐỐI PHƯƠNG CHỦ ĐỘNG
- Đối phương chủ động hỏi, kể chuyện hoặc mở chủ đề.
- Tận dụng nội dung đó để tăng tương tác và kết nối.
- Không biến phản hồi thành độc thoại của người dùng.

8. TÂM TRẠNG KHÔNG TỐT
- Ưu tiên đồng cảm và lắng nghe.
- Không vội đưa lời khuyên nếu đối phương chỉ muốn chia sẻ.
- Tránh đùa không đúng thời điểm.

9. CHUYỂN CHỦ ĐỀ
- Khi chủ đề cũ đã cạn hoặc không còn tự nhiên.
- Tìm điểm nối từ context để chuyển sang chủ đề mới.
- Tránh chuyển chủ đề đột ngột.

10. MỞ LẠI CUỘC TRÒ CHUYỆN
- Sau một khoảng thời gian không nhắn.
- Gợi lại một chi tiết hoặc context cũ để mở lại tự nhiên.
- Tránh các câu mở lại quá chung chung nếu không có context.

11. RỦ ĐI CHƠI / GẶP MẶT
- Chỉ đề xuất khi mức độ thân thiết và tín hiệu tương tác phù hợp.
- Lời mời nên cụ thể nhưng không tạo áp lực.
- Nếu bị từ chối, phản hồi bình thường và tôn trọng quyết định.

12. BỊ TỪ CHỐI / KHÔNG MUỐN TIẾP TỤC
- Không cố thuyết phục hoặc gây cảm giác có lỗi.
- Phản hồi bình tĩnh, tôn trọng và kết thúc phù hợp.

NGUYÊN TẮC CHUNG
---------------
- Phân tích context trước khi tạo câu trả lời.
- Ưu tiên tự nhiên, đúng ngữ cảnh hơn là "câu tán gái hoàn hảo".
- Không bịa thông tin về đối phương.
- Không lặp lại câu hỏi đã được trả lời.
- Không spam hoặc ép đối phương phản hồi.
- Có thể đưa 2–3 phương án với mức độ chủ động khác nhau.
- Hỗ trợ giao tiếp tự nhiên, không thao túng hoặc gây áp lực.

CÁCH DÙNG
----------
1. Dùng `NHAN_TIN.zip` làm bộ ví dụ để TEST.
2. Có thể đưa screenshot hoặc đoạn chat thực tế làm input.
3. AI phân tích context và tình huống hiện tại.
4. Chọn cách xử lý phù hợp rồi mới đề xuất câu trả lời.
