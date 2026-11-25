# Nháp Nhiệm vụ C · phần của Hiếu (Người gắn nhãn 2)

> **Đọc trước, cho cả Hiếu và AI agent của Hiếu.** Đây là file nháp, không phải file nộp.
> Khoa đã tổng hợp `report/team/bang_loi.md` trên nhánh `khoa`: đủ hai bộ nhãn, đồng thuận 18/20 = 90%, nhãn thống nhất (ca 6 = Do người dùng, ca 8 = Hệ thống, theo nhãn tham khảo), và đã bốc thăm 5 ca cho bảng khắc phục: 9, 15, 10, 11, 17.
>
> **Phạm vi việc của Hiếu, chỉ gồm:**
> 1. Viết **một câu quy tắc phân biệt cho ca 8** (bước 7).
> 2. Điền **hai dòng bảng khắc phục cho ca 11 và ca 17** (bước 9).
>
> **Không làm:**
> - **Không sửa `report/team/bang_loi.md`** hay bất kỳ file nào khác. Chỉ ghi vào file này. Khoa sẽ gộp vào `bang_loi.md` để tránh conflict.
> - Không đổi hai cột nhãn độc lập, nhãn thống nhất, tỉ lệ đồng thuận, hay 5 ca đã chọn.
> - Không làm phần của Khoa (ca 6, ca 9, 15, 10), không làm nhiệm vụ D, E.
>
> **Cách làm:** `git fetch origin` → `git switch khoa` → `git pull` → điền các chỗ `...` dưới đây → `git add nhap_C_hieu.md` → `git commit -m "Nhiem vu C: phan cua Hieu (ca 8, 11, 17)"` → `git push` → báo Khoa.

## Bước 7 · Quy tắc phân biệt cho ca 8

Ca 8: *Trợ lý dẫn "Điều 7.2 chính sách hoàn phí" làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng.*
Nhãn người 1: Ngầm · Nhãn người 2: Hệ thống · **Nhãn thống nhất: Hệ thống**

Một câu, gồm: nhãn chọn và nhãn loại · dấu hiệu quyết định trong mô tả ca · vì sao điều gây lẫn không đổi nhãn. Viết bằng lời của mình (hội đồng có thể hỏi).

- Ca 8: Chọn **Hệ thống** và loại **Ngầm** vì trợ lý bịa trích dẫn "Điều 7.2" không có trong chính sách và lỗi đã lộ ra trực tiếp trong câu trả lời cho người đọc thấy; việc số tiền hoàn vẫn đúng không đổi nhãn thành Ngầm vì lỗi không hề ẩn tới lúc kiểm tra mẫu.

## Bước 9 · Bảng khắc phục, ca 11 và ca 17

- Ca 11 (Giới hạn hệ thống): *Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời "vui lòng nhập bằng chữ".*
- Ca 17 (Ngầm): *Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại.*

Yêu cầu rubric C3: "Phát hiện bằng gì" phải **đo được** (tên event, ngưỡng, tần suất); "Ai phụ trách" là **một vai trò** có quyền quyết định (ví dụ PM trợ lý hoàn phí, Kỹ sư trưởng agent, Trưởng nhóm CSKH, Kế toán trưởng), không ghi "cả đội"; không dùng từ "production".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 11 | Giới hạn hệ thống | Event `unsupported_input_type` (audio) / `handoff_to_staff`; cảnh báo hàng tuần khi vượt 3% tổng yêu cầu | Hiển thị hướng dẫn rõ ràng kèm nút chuyển sang nhập chữ hoặc chuyển nhân viên; cân nhắc tích hợp speech-to-text nếu tỉ lệ vượt ngưỡng | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu ngẫu nhiên 100 đơn/tuần đối chiếu với bảng giá hiện hành; cảnh báo khi vượt 1% đơn lệch giá | Xoá bộ nhớ đệm ngay khi cập nhật bảng giá mới và ghi phiên bản bảng giá vào `trace_id` của mỗi lần chạy để đối soát | Kế toán trưởng |

