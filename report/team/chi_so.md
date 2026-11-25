# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng (đề xuất) | Tỉ lệ kích hoạt trợ lý | Yêu cầu thuộc nhóm can thiệp có `agent_suggestion_shown` / tổng yêu cầu đủ điều kiện được gán vào nhóm can thiệp | Chưa tính được từ mẫu hiện tại; cần ghi event trong pilot |
| An toàn (đề xuất) | Tỉ lệ hoàn sai tiền trong mẫu kiểm toán | Số mẫu có `so_tien_da_hoan != so_tien_dung` / tổng mẫu đã kiểm tra | Chưa tính được từ mẫu hiện tại; cần event kiểm toán |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi yêu cầu được gửi |
| `agent_run_completed` | Agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý được hiển thị |
| `staff_review_decision` | Nhân viên | `request_id`, `staff_id`, `quyet_dinh` (`giu/sua/bo`), `phut_xem_lai`, `trace_id` | Khi nhân viên quyết định |
| `refund_ledger_write` | Sổ cái hoàn tiền | `request_id`, `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi nhận hoàn tiền |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi đóng ticket |
| `ticket_reopened` | Hệ thống ticket | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi ticket được mở lại |
| `audit_sample_checked` | Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Khi kiểm tra mẫu định kỳ |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `refund_request_created` + `ticket_closed` để tính thời gian đóng; `ticket_reopened` để xác nhận không mở lại trong 7 ngày.
- Tỉ lệ bỏ qua gợi ý: `staff_review_decision`; tử số là quyết định `sua` hoặc `bo`, mẫu số là các yêu cầu có quyết định xem lại.
- Tỉ lệ mở lại: `ticket_reopened` trong 7 ngày / `refund_request_created`.
- Tỉ lệ kích hoạt trợ lý: `agent_suggestion_shown` / yêu cầu được gán `arm=can_thiep` trong `refund_request_created`.
- Tỉ lệ hoàn sai tiền: so sánh `so_tien_da_hoan` và `so_tien_dung` trong `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (chất lượng trả lời giảm hoặc trôi dữ liệu) | Chi phí mỗi việc thành công tăng **+51,8%**, từ **4.472 đ** lên **6.787 đ/việc** (`simulated`) | Tỉ lệ `lam_lai` vượt **8%** hoặc tỉ lệ mở lại trong 7 ngày (`mo_lai_trong_7_ngay`) vượt **6%** trong 48 giờ liên tiếp | Tạm dừng mở rộng bước pilot, khoá nhóm loại yêu cầu gây lỗi và kiểm tra lại prompt/quy tắc trích xuất chính sách | Kỹ sư trưởng agent |
| Phải duy trì xem lại 100% kéo dài (phạm vi `noi_dia` + `hang_nang`) | Chi phí mỗi việc thành công lên **11.743 đ** (`0,98×`, mức 9 phút làm lại) đến **12.415 đ** (`1,03×`, mức trung bình thực tế 15,3 phút `simulated`), gần như hết tiết kiệm hoặc đắt hơn nhân viên tự làm | Tỉ lệ `duoc_xem_lai` duy trì **> 80%** sau tuần thứ 2 hoặc thời gian xem lại trung bình vượt ngưỡng hoà vốn **4,8–5,1 phút/ca** (`simulated`) | Chuyển sang xem lại theo mẫu/ngưỡng rủi ro tiền lớn và cải tiến giao diện duyệt nhanh để kéo thời gian xem lại xuống **< 4,8 phút/ca**; nếu không đạt thì dừng pilot | PM trợ lý hoàn phí |
| Khối lượng xử lý thấp hơn dự kiến (phân bổ 40 triệu đ/tháng chi phí cố định) | Ở quy mô đầy đủ (`33.750` việc/tháng) cố định thêm **+1.185 đ/việc** (tổng **4.599 đ = 0,38×** `simulated`); giảm nửa khối lượng (`16.875` việc/tháng) cố định tăng gấp đôi lên **+2.370 đ/việc** (tổng **5.784 đ = 0,48×** `simulated`) | Số việc thành công quy đổi theo tháng `< 17.000` việc hoặc chi phí biến đổi bước pilot vượt **8.000 đ/việc** (`simulated`) | Ở bước 4–10 người chỉ đánh giá trên chi phí biến đổi (~3.414 đ/việc `simulated`), đồng thời đàm phán lại gói thuê cố định 40 triệu đ/tháng theo bậc khối lượng thay vì kết luận sớm trợ lý đắt | Giám đốc vận hành LogiX-VN |
