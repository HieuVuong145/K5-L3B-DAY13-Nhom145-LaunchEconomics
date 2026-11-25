# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Lê Đăng Khoa · Người gắn nhãn 2: Vương Toàn Minh Hiếu (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Giới hạn hệ thống | Do người dùng | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Hệ thống | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90% (không trùng: ca 6, ca 8)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 6: Do người dùng, không phải Giới hạn hệ thống hay Hệ thống, vì gốc lỗi là khách chọn sai mục "Hoàn phí giao trễ" cho một ca hàng vỡ; dễ nhầm là hệ thống xử lý sai hoặc thiếu thông tin, nhưng việc trợ lý không đối chiếu mục đã chọn với nội dung mô tả chỉ là chỗ cần sửa, không đổi nguyên nhân gốc.
- Ca 8: Hệ thống, không phải Ngầm, vì trợ lý bịa trích dẫn "Điều 7.2" không có trong chính sách và lỗi đã lộ ra trực tiếp trong câu trả lời cho người đọc thấy; việc số tiền hoàn vẫn đúng không đổi nhãn thành Ngầm vì lỗi không hề ẩn tới lúc kiểm tra mẫu.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

Năm ca được chọn ngẫu nhiên, mỗi loại một ca, bằng `random.seed(13)` rồi `random.choice` trên danh sách ca của từng loại theo nhãn thống nhất (không tính hai ca 6 và 8 vì là ca có tranh luận).

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` có `reason = ma_san_tmdt` (mã khớp mẫu mã sàn TMĐT), đếm theo ngày; cảnh báo khi vượt 2% số yêu cầu/ngày | Thêm hướng dẫn ngay ở ô nhập: "Nhập mã vận đơn LogiX, không phải mã đơn của sàn", kèm ảnh chỉ vị trí mã vận đơn | PM trợ lý hoàn phí |
| 15 | Hệ thống | Event `staff_review_decision` = `sua` có `ly_do = sai_ti_le_hoan`, cộng bộ kiểm tra tự động so số tiền đề xuất với bảng tỉ lệ theo giờ trễ trước khi gửi; theo dõi hằng ngày, ngưỡng 0 ca lọt qua kiểm tra, rà lại khi tỉ lệ sửa vì sai tỉ lệ vượt 1%/tuần | Tính tỉ lệ hoàn bằng tool tính cố định theo bảng chính sách (không để model tự tính), thêm ca thử ở các mốc biên 24 giờ và 48 giờ | Kỹ sư trưởng agent |
| 10 | Ngữ cảnh | Event `ticket_reopened` của các yêu cầu bị từ chối vì bất khả kháng, tổng hợp theo tuần; cảnh báo khi vượt 15% số ca bị từ chối vì bất khả kháng bị mở lại | Tin nhắn từ chối nêu rõ điều khoản bất khả kháng và giải thích vì sao "cam kết giao 24 giờ" không áp dụng khi có bão; đề xuất ứng dụng tạm ẩn dòng cam kết ở khu vực đang có cảnh báo thời tiết | PM trợ lý hoàn phí |
| 11 | Giới hạn hệ thống | Event `unsupported_input_type` (audio) và `handoff_to_staff`; cảnh báo hàng tuần khi vượt 3% tổng yêu cầu | Hiển thị hướng dẫn rõ ràng kèm nút chuyển sang nhập chữ hoặc chuyển nhân viên; cân nhắc tích hợp speech-to-text nếu tỉ lệ vượt ngưỡng | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu ngẫu nhiên 100 đơn/tuần đối chiếu với bảng giá hiện hành; cảnh báo khi vượt 1% đơn lệch giá | Xoá bộ nhớ đệm ngay khi cập nhật bảng giá mới và ghi phiên bản bảng giá vào trace của mỗi lần chạy (theo `trace_id`) để đối soát | Kế toán trưởng |
