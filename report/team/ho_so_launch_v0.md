# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 145 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ toàn mẫu (simulated); 4.599 đ phạm vi `noi_dia` + `hang_nang` gồm cố định 45k/tháng (simulated) | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%) (simulated) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | 0,38× (`noi_dia` + `hang_nang` + cố định 45k/tháng, simulated); 0,49× cả hệ thống toàn mẫu (5.865 đ/yc, simulated) | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đóng 24h không mở lại 7 ngày: 82,83%; bỏ qua gợi ý: 27,12%; mở lại 7 ngày: 4,25%; 8 event có `trace_id` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 18/20 (90%); đã lập bảng khắc phục 5 ca (`9, 15, 10, 11, 17`) đủ 5 loại có ngưỡng đo & vai trò phụ trách | Xong, có bằng chứng | Người gắn nhãn 2 |
| 6 · Pilot plan | 20+20 nhân viên (`noi_dia` + `hang_nang`); MDE +6đ (`n=859`, `m=299`, `DE=6,96`, ~10 ngày; power ~0,64 ở +5đ); 3 luật dừng | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2: +51,8% (6.787 đ); xem lại 100%: 11.743–12.415 đ (0,98–1,03×); giảm nửa khối lượng: cố định +2.370 đ (simulated) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện

- Hoàn thiện khoá chống trùng và đối soát sổ cái (ca 7, 20) trước khi bật pilot — **Kỹ sư trưởng agent** (kiểm tra `2026-12-04`).
- Phê duyệt phạm vi thu hẹp (`noi_dia` + `hang_nang`, loại `quoc_te` `1,88×` và `doi_tac` `0,85×`) cùng đánh đổi MDE `+6` điểm (`power ~0,64` nếu hiệu ứng thật chỉ `+5` điểm; bước 20 người chạy 10 ngày) — **Giám đốc vận hành LogiX-VN** (kiểm tra `2026-12-04`).
- Bật đủ 8 event có `trace_id`, thay phút `_simulated` bằng thời gian đo thật sau tuần 1 và đặt lộ trình giảm tỉ lệ xem lại theo bậc (tránh xem lại 100% làm chi phí lên `11.743–12.415 đ`, `simulated`) — **PM trợ lý hoàn phí** (kiểm tra `2026-12-14`).
