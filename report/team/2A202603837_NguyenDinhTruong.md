# Báo cáo cá nhân — NguyenDinhTruong-2A202603837

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đình Trường
- MSSV: 2A202603837
- Email: 26ai.truongnd@vinuni.edu.vn
- Vai trong nhóm: Người viết code (Vai trò 1)

## 2. Phần việc phụ trách

- Phát triển và chạy `src/lab13.py` cho các nhiệm vụ tính chi phí A, phân tích độ nhạy B, tính cỡ mẫu pilot D1 và các chỉ số E1 từ hai bộ dữ liệu giả lập của lab.
- Đảm bảo các phép tính có xét giới hạn số lần chạy, chi phí xem lại/làm lại và gắn nhãn `simulated` cho các kết quả dùng dữ liệu giả lập.

## 3. Đóng góp cụ thể

- Cài đặt các công thức A1 và ba phép thử đáp án biết trước; cả ba phép thử đạt lần lượt `1,20`, `1,25` và `1,25`.
- Xây dựng mô hình chi phí từ trace, tách chi phí token, tool, xem lại và làm lại; tính chi phí mỗi việc thành công là `4.472 đ` (`simulated`) trên `978` việc thành công.
- Tính kết quả theo loại yêu cầu, chi phí cố định và các kịch bản độ nhạy B1–B4. Kết quả nổi bật: `quoc_te` có chi phí `22.515 đ/việc` (`1,88×` mức nhân viên); giới hạn hai lần chạy cho tổng chi phí hệ thống thấp nhất trong ba kịch bản (`6.901.220 đ`, `simulated`).
- Cài đặt phép tính cỡ mẫu và power cho D1; kết quả gồm `859` yêu cầu hiệu dụng mỗi nhóm ở MDE `+6` điểm, `299` yêu cầu/nhân viên và power khoảng `0,64` nếu hiệu ứng thực chỉ `+5` điểm.
- Tính các chỉ số E1 trên dữ liệu mẫu: chỉ số chính `82,83%` (`994/1.200`), tỉ lệ sửa/bỏ gợi ý `27,12%` (`48/177`) và tỉ lệ mở lại trong 7 ngày `4,25%` (`51/1.200`).

## 4. Bằng chứng

- `src/lab13.py`: các hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, `mo_hinh`, `in_a3`, `in_a4`, `in_b`, `co_mau_hai_ti_le`, `in_d1` và `in_e1`.
- `report/team/bang_chi_phi.md`: kết quả A1–A4 và B1–B4.
- `report/team/pilot_plan.yaml`: phương án pilot và các con số cỡ mẫu/đánh đổi D1.
- `report/team/chi_so.md`: đặc tả chỉ số, event và rủi ro kinh tế E1–E2.
- Đã chạy `python lab13.py` trong thư mục `src/`; ba phép thử A1 in `ĐẠT`, các kết quả đầu ra đối chiếu được với bảng chi phí và các file hồ sơ nêu trên.
- Mã commit: 83bff90c8c8c1a8d25c97d3866eba2393aa71242, 7e154fe326b76b8fef9c472e414e0e102b8c9179, 0f73a4b55ddb688758576519f8fa4cf39ddc1cea

## 5. Công cụ AI đã dùng

- Trong phiên hoàn thiện báo cáo này, dùng trợ lý AI Copilot SDK trong VS Code để tổng hợp nội dung.
- Tự kiểm tra bằng cách chạy `python lab13.py`, đối chiếu ba phép thử A1 và các số liệu A2, B, D1, E1 với `bang_chi_phi.md`, `pilot_plan.yaml` và `chi_so.md`; các số được tính từ dữ liệu giả lập được ghi nhãn `simulated`.

## 6. Tự đánh giá

- Hoàn thành phần lập trình và tính toán thuộc vai trò người viết code, bao gồm mô hình chi phí, phân tích độ nhạy, cỡ mẫu pilot và chỉ số kết quả/dùng/an toàn. Đã chạy lại chương trình và đối chiếu đầu ra với hồ sơ nhóm; email và mã commit cần bổ sung nếu nhóm yêu cầu ghi đầy đủ.
