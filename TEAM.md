# Team

## Thông tin nhóm

- Tên nhóm: Nhom145
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Nhom145-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/HieuVuong145/K5-L3B-DAY13-Nhom145-LaunchEconomics` · nhánh `main`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |        |      |       |        |         |
|   2 | Nguyễn Tuấn Dũng | 2A202603859 | 26ai.dungnt16@vinuni.edu.vn | | Người kiểm số |
|   3 | Nguyễn Lê Đăng Khoa | 2A202603847 | 26ai.khoanld@vinuni.edu.vn | S0ra1n0 | Người gắn nhãn 1 |
|   4 | Vương Toàn Minh Hiếu | 2A202603853 | 26ai.hieuvtm@vinuni.edu.vn | HieuVuong145 | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## NguyenLeDangKhoa-2A202603847

### Phần việc phụ trách

- Người gắn nhãn 1 (Vai trò 3): Nhiệm vụ C (gắn nhãn độc lập 20 ca, so nhãn, bảng khắc phục, tổng hợp `report/team/bang_loi.md`).
- Nhiệm vụ D: 5 câu D2, 3 luật dừng và các trường trong `report/team/pilot_plan.yaml`; rà điều kiện "Xong khi" của CP4.
- Nhiệm vụ E: kiểm tra chéo bảng E1 với danh sách event trong `report/team/chi_so.md`; checklist chấm chéo Gate 2a; rà hồ sơ trước khi nộp.

### Đóng góp cụ thể

- Bộ nhãn độc lập 20 ca; đồng thuận 18/20 = 90%; bảng khắc phục 5 ca đủ 5 loại (gộp phần của Người gắn nhãn 2).
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn `?`, 3 luật dừng đủ 4 vế; sửa bước 20 người từ 8 ngày thành khoảng 10 ngày và `decision_date` sang 2027-01-12 (đủ 7 ngày theo dõi mở lại).
- Thêm 4 event để mọi chỉ số và luật dừng tính được từ event (12 event có `trace_id`); bỏ từ bị cấm trong `phieu_cham.md`; sửa cách ghi chi phí cố định và người phụ trách trong `ho_so_launch_v0.md`.

### Bằng chứng

- Commit `fa188c6`, `2f27609`, `0283228`, `e906381`, `b80dd4c`, `6211a64`, `ed8a1b5`.
- Báo cáo cá nhân: `report/team/2A202603847_NguyenLeDangKhoa.md`.

## VuongToanMinhHieu-2A202603853

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ (Vai trò 4): lập kế hoạch tiến trình nhóm; gắn nhãn độc lập 20 ca ở CP3, viết quy tắc ca 8 và bảng khắc phục ca 11, ca 17 (`nhap_C_hieu.md` gộp vào `report/team/bang_loi.md`).
- Giữ hồ sơ từ đầu buổi và hoàn thiện `report/team/ho_so_launch_v0.md` (7 mục + đề xuất `Go có điều kiện`).
- Duyệt chéo Gate 2a: chấm hồ sơ của `Nhom1234` vào `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- Lập `plan_ABC.md`, `plan_ABC_checkpoint.md`, `plan_DE_checkpoint.md` cho cả nhóm phối hợp theo checkpoint.
- Hoàn thành bộ nhãn độc lập 20 ca (đồng thuận 18/20 = 90%), quy tắc phân biệt ca 8 và bảng khắc phục ca 11, ca 17.
- Hoàn thiện đủ 7 mục (gắn nhãn `Giả lập` / `simulated` đúng quy định) và đề xuất `Go có điều kiện` kèm 3 điều kiện có người phụ trách và ngày kiểm tra trong `report/team/ho_so_launch_v0.md`.
- Chấm chéo `Nhom1234` theo 3 tiêu chí trong `report/team/phieu_cham.md` (30/30, `Go có điều kiện`) và duyệt/merge các PR của nhóm về `main`.

### Bằng chứng

- Commit `e529cf6`, `43560b4`, `cd7c491`, `5ff30f4`, `e67d42b`, `2050f62`, `9444450`, `ea57e66`, `e61dc83`, `b38b6fc`, `c72e65f`.
- Báo cáo cá nhân: `report/team/2A202603853_VuongToanMinhHieu.md`.
