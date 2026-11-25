# Phiếu gắn nhãn độc lập · Nhiệm vụ C (bản trống)

> File làm việc cá nhân, **không phải file nộp**. Mỗi người gắn nhãn dùng một bản riêng.
> 20 ca chép nguyên văn từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục "Hai mươi ca lỗi". Phiếu này không có gợi ý nhãn.

- Người gắn nhãn: Nguyễn Lê Đăng Khoa (Vai trò: Người dán nhãn 1)
- Bắt đầu: 15:00 · Kết thúc: 15: (8 phút, không trao đổi, không hỏi AI)

## Năm loại lỗi (Google PAIR) và ký hiệu viết nhanh

| Ký hiệu | Loại | Nghĩa là | Câu hỏi để nhận ra |
| --- | --- | --- | --- |
| **ND** | Do người dùng | Người dùng nhập sai hoặc chọn sai | Đầu vào của khách có sai không? |
| **HT** | Hệ thống | Hệ thống trả lời sai hoặc làm sai so với thiết kế và chính sách | Có vi phạm thiết kế/chính sách, và có người thấy? |
| **NC** | Ngữ cảnh | Hệ thống làm đúng thiết kế nhưng người dùng thấy là sai, vì giả định của hệ thống không khớp hoàn cảnh của họ | Kết quả đúng, chỉ giả định không khớp hoàn cảnh? |
| **GH** | Giới hạn hệ thống | Hệ thống không thể trả lời, do thiếu dữ liệu, ngoài phạm vi, hoặc dạng đầu vào không xử lý được | Có làm được không, dù có cố gắng? |
| **NG** | Ngầm | Có sai nhưng cả người dùng lẫn hệ thống đều không nhận ra | Chỉ phát hiện qua kiểm tra mẫu? |

Quy tắc: **gắn theo nguyên nhân gốc, không theo chỗ cần sửa.** Mỗi ca đúng một nhãn.

## Hai mươi ca

| Ca | Mô tả | Nhãn | Lý do (một dòng) |
| --: | --- | :---: | --- |
| 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi. | ND | người dùng nhập sai |
| 2 | Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. | HT | Trợ lý tra sai bảng giá |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo "chưa được hoàn". | NC | Khách nghĩ là hệ thống hoàn tiền ngay lập tức trong khi thời gian hoàn tiền về ví theo quy ước của hệ thống là 5 phút|
| 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên. | GH | Không có dữ liệu cho trợ lý xử lý |
| 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích. | NG | Không ai nhận ra, hệ thống cũng không báo, chỉ phát hiện khi tổng kết|
| 6 | Khách chọn mục "Hoàn phí giao trễ" nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. | GH | Hệ thống nhận thông tin đầu vào bị vỡ, nên không xử lý chính xác được|
| 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách "đã hoàn tiền thành công". | HT | Hệ thống làm sai |
| 8 | Trợ lý dẫn "Điều 7.2 chính sách hoàn phí" làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng. | NG | Không tồn tại chính sách được trợ lý trích dẫn, nhưng kết quả ra đúng và không ai phát hiện|
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo "mã không hợp lệ" rồi dừng, không gợi ý gì. | ND | Khách nhập sai thông tin|
| 10 | Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện "cam kết giao 24 giờ". | NC | Hệ thống xử lý theo đúng điều khoản, khách thấy không đúng do mâu thuẩn với thông tin hiện trên ứng dụng|
| 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời "vui lòng nhập bằng chữ". | GH | Trợ lý không xử lý được âm thanh, nằm ngoài phạm vi, khả năng của hệ thống, hoặc input không rõ, chất lượng không được tốt|
| 12 | Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy. | NG | Không ai và cả hệ thống không phát hiện lỗi|
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được. | GH | Trợ lý không có thông tin về sản phẩm của công ty đối tác nên không đưa ra câu trả lời chính xác được |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận. Yêu cầu bị đóng. | ND | Khách input nhầm |
| 15 | Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi. | HT | Hệ thống tính sai|
| 16 | Theo thiết kế "gửi ngay khi xong", trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. | NC | Hệ thống làm theo quy tắc, khách thấy thông tin được gửi vào giờ ngủ nên bị làm phiền|
| 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại. | NG | Trợ lý dùng sai bản, không ai phát hiện ra lỗi |
| 18 | Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi "Đã hoàn 15.000 đ", không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu. | NC | Trợ lý tính đúng, khách không biết công thức tính nên cho là hệ thống tính sai |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt. | GH | Trợ lý không có quyền truy cập các đơn từ hơn 12 tháng trước |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng. | HT | Hoàn 2 lần |

## Đếm nhanh sau khi gắn (tự kiểm, chưa so với ai)

| ND | HT | NC | GH | NG | Tổng |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 3 | 4 | 4 | 5 | 4 | 20 |
