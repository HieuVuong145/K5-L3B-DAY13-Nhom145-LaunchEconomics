# Báo cáo cá nhân — NguyenLeDangKhoa-2A202603847

## 1. Thông tin thành viên

- Họ tên: Nguyễn Lê Đăng Khoa
- MSSV: 2A202603847
- Email: nguyenledangkhoa1510@gmail.com
- Vai trong nhóm: Người gắn nhãn 1 (Vai trò 3), kiêm theo dõi điều kiện "Xong khi"

## 2. Phần việc phụ trách

- **CP3 (Nhiệm vụ C):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR (không trao đổi với Người gắn nhãn 2, commit bộ nhãn trước khi xem nhãn của bạn); so nhãn, tính tỉ lệ đồng thuận, chốt nhãn thống nhất cho các ca lệch; viết quy tắc phân biệt cho ca 6; điền bảng khắc phục ca 9, 15, 10; tổng hợp toàn bộ `report/team/bang_loi.md` (gộp cả phần ca 8, 11, 17 của Người gắn nhãn 2).
- **CP4 (Nhiệm vụ D):** Soạn 5 câu D2, 3 luật dừng 4 vế (an toàn, chi phí, sử dụng), các trường `owner`, `scope`, `assignment`, `rollout`, `primary_metric`, `identifiability`, `interim_looks`, `rollback`, `decision_date`, `simulated_inputs` trong `report/team/pilot_plan.yaml`; rà điều kiện "Xong khi" của CP4 (bước 4C).
- **CP5 (Nhiệm vụ E + duyệt chéo):** Kiểm tra chéo bảng E1 với danh sách event trong `report/team/chi_so.md`; soạn checklist chấm chéo Gate 2a cho nhóm dùng khi làm hội đồng và tự rà hồ sơ; rà toàn bộ `report/team/` trước khi nộp và sửa các lỗi chung.

## 3. Đóng góp cụ thể

- **Nhiệm vụ C:** hai bộ nhãn độc lập đồng thuận **18/20 = 90%** (lệch ca 6 và ca 8); nhãn thống nhất cho hai ca này theo nguyên nhân gốc (ca 6 Do người dùng, ca 8 Hệ thống). Chọn 5 ca cho bảng khắc phục bằng `random.seed(13)`, mỗi loại một ca (9, 15, 10, 11, 17); mỗi dòng có event, ngưỡng, tần suất và một vai trò phụ trách.
- **Nhiệm vụ D:** `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn dấu `?` ngoài chú thích, 3 luật dừng đủ 4 vế. Luật an toàn đặt ngưỡng tuyệt đối 6% so với mức nền 3,97% trong phạm vi, và chỉ áp luật "chênh ≥ 2 điểm so với đối chứng" từ bước 10 người, vì mô phỏng cho thấy ở bước 4 người khả năng báo động giả khoảng 14%. Luật chi phí dùng ngưỡng 8.000 đ phần biến đổi (đợt chạy thử 3.414 đ trong phạm vi, simulated), không cộng 40 triệu cố định.
- **Hai lỗi phát hiện và sửa trong kế hoạch pilot:**
  - Bước 20 người cần **khoảng 10 ngày**, không phải 8 ngày: pilot chỉ nhận noi_dia + hang_nang (81,8% số yêu cầu) nên mỗi nhân viên chỉ có ≈ 30,7 đơn/ngày để đủ 299 đơn.
  - `decision_date` đổi từ 2027-01-05 sang **2027-01-12**: chỉ số chính cần 7 ngày theo dõi mở lại, đơn cuối của bước 20 người (04/01/2027) chỉ đủ dữ liệu từ 11/01/2027.
- **Nhiệm vụ E:** kiểm tra chéo 5 chỉ số E1 với danh sách event; bổ sung 4 event còn thiếu (`staff_rework_completed`, `handoff_to_staff`, `input_validation_failed`, `unsupported_input_type`) để luật dừng chi phí và bảng khắc phục đều tính được từ event, nâng danh sách lên 12 event có `trace_id`.
- **Rà soát trước khi nộp:** bỏ từ bị cấm theo quy tắc 5 trong `phieu_cham.md` (lệnh tự kiểm tra trong `CHECKPOINTS.md` bắt được dòng đó); sửa cách ghi "cố định 45k/tháng" thành "cố định 40 triệu đ/tháng ở 45.000 yêu cầu/tháng" và đổi người phụ trách Mục 1, Mục 5 sang vai trò có quyền quyết định trong `ho_so_launch_v0.md`.

## 4. Bằng chứng

- `fa188c6` (15:43): điền thông tin trong `TEAM.md` và bộ nhãn độc lập 20 ca (`phieu_gan_nhan_C_nguoi1.md`), commit trước khi xem nhãn của Người gắn nhãn 2.
- `2f27609`: điền hai bộ nhãn, tỉ lệ đồng thuận 18/20, nhãn thống nhất và 5 ca được chọn trong `report/team/bang_loi.md`.
- `0283228`: file giao việc cho Người gắn nhãn 2 (ca 8, 11, 17) để hai người không sửa chung một file.
- `e906381`: gộp quy tắc ca 6, ca 8 và bảng khắc phục 5 ca vào `report/team/bang_loi.md`.
- `b80dd4c`: điền D2, các trường và 3 luật dừng trong `report/team/pilot_plan.yaml`; sửa "8 ngày" thành "khoảng 10 ngày".
- `6211a64`: đổi `decision_date` sang 2027-01-12; thêm `checklist_cham_cheo.md`.
- `ed8a1b5`: sửa lỗi chung trong `phieu_cham.md`, `ho_so_launch_v0.md`, `chi_so.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (ứng dụng Claude trên máy tính).
- **Dùng vào việc gì:**
  - Đọc đề và tóm tắt yêu cầu từng checkpoint; giải thích 5 loại lỗi Google PAIR bằng ví dụ ở lĩnh vực khác (không đụng tới 20 ca) và tạo phiếu gắn nhãn trống.
  - Sau khi hai người đã gắn nhãn độc lập: so hai bộ nhãn, tính tỉ lệ đồng thuận, chọn ngẫu nhiên 5 ca có seed.
  - Đưa các phương án để tôi chọn cho bảng khắc phục và cho các trường, luật dừng của `pilot_plan.yaml`, kèm nhận xét điểm mạnh, yếu của từng phương án.
  - Chạy `src/lab13.py`, `yaml.safe_load`, lệnh lọc dấu `?` và từ bị cấm; tính số nền (tỉ lệ mở lại 3,97%, bỏ qua gợi ý 21,1%, power 0,64), mô phỏng báo động giả ở bước 4 người, tính lịch pilot.
  - Soạn nháp báo cáo cá nhân này và đưa lệnh git.
- **Không dùng AI cho:** gắn nhãn 20 ca (tự gắn trong khoảng 8 phút, không hỏi AI; tự phát hiện và sửa ca 9 ghi nhầm ký hiệu trước khi so với bạn cùng nhóm).
- **Cách tự kiểm tra:**
  - Đọc từng phương án và lý do AI đưa ra rồi tự chọn; có chỗ tôi chọn khác và đổi lại sau khi xem lý do có số (người phụ trách, luật chi phí 12.000 đ so với 8.000 đ, cột phát hiện của ca 10).
  - Với ca 6 và ca 8, đối chiếu nhãn thống nhất với mục "Nhãn tham khảo" trong tài liệu hướng dẫn sau khi cả hai đã gắn xong, rồi chọn theo nguyên nhân gốc thay vì giữ nhãn ban đầu của mình.
  - Đối chiếu số trong `pilot_plan.yaml` với output của `src/lab13.py` và bảng D1 trong tài liệu hướng dẫn; chạy lại lệnh kiểm tra yaml sau mỗi lần sửa.

## 6. Tự đánh giá

- **Làm tốt:** gắn nhãn độc lập và có bằng chứng commit trước khi so; đồng thuận 18/20; tìm ra hai chỗ sai về thời gian trong kế hoạch pilot (8 ngày, ngày quyết định) và lỗi từ bị cấm trong phiếu chấm trước khi nộp.
- **Chưa tốt:** gắn sai hai ca 6 và 8 so với nhãn tham khảo (nhầm giữa nguyên nhân gốc và chỗ cần sửa, và giữa lỗi đã lộ ra với lỗi ngầm); một số phần của nhiệm vụ D chọn từ phương án AI soạn sẵn thay vì tự viết từ đầu do thiếu thời gian.
- **Lần sau:** đọc kỹ quy tắc "gắn theo nguyên nhân gốc" trước khi gắn nhãn; tự viết nháp luật dừng trước rồi mới so với gợi ý.
