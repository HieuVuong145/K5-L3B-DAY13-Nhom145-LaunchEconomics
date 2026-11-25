# Báo cáo cá nhân — VuongToanMinhHieu-2A202603853

## 1. Thông tin thành viên

- Họ tên: Vương Toàn Minh Hiếu
- MSSV: 2A202603853
- Email: 26ai.hieuvtm@vinuni.edu.vn
- GitHub: `HieuVuong145`
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ (Vai trò 4)

## 2. Phần việc phụ trách

- **Điều phối tiến trình nhóm:** Lập kế hoạch phân công 4 vai trò và tiến trình theo các checkpoint cho A, B, C và D, E.
- **CP3 (Nhiệm vụ C):** Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR; so nhãn với Người gắn nhãn 1; viết quy tắc phân biệt cho ca 8 và điền bảng khắc phục ca 11, ca 17 (`nhap_C_hieu.md` để gộp vào `report/team/bang_loi.md`).
- **CP5 (Nhiệm vụ E — Giữ hồ sơ):** Cập nhật dần từ đầu buổi và hoàn thiện đủ 7 mục cùng đề xuất cuối (`Go có điều kiện`) trong `report/team/ho_so_launch_v0.md`.
- **Duyệt chéo Gate 2a:** Đọc hồ sơ của `Nhom1234` (`ho_so_launch_v0.md`, `pilot_plan.yaml`) và chấm theo 3 tiêu chí trong `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- **Lập kế hoạch & điều phối**
- **Nhiệm vụ C:** Hoàn thành bộ nhãn độc lập 20 ca của Người gắn nhãn 2 (đồng thuận **18/20 = 90%** với Người gắn nhãn 1, khớp 20/20 với nhãn tham khảo theo nguyên nhân gốc); viết quy tắc phân biệt ca 8 (**Hệ thống**, không phải **Ngầm**, vì trích dẫn sai "Điều 7.2" đã lộ ra trực tiếp trong câu trả lời) và điền bảng khắc phục ca 11 (Giới hạn hệ thống), ca 17 (Ngầm) có event/kiểm tra mẫu, ngưỡng, tần suất và 1 vai trò phụ trách.
- **Hồ sơ launch v0:** Tổng hợp đủ 7 mục trong `report/team/ho_so_launch_v0.md` (ghi rõ `Giả lập` / `simulated` cho các mục từ cột `_simulated`), chốt đề xuất **`Go có điều kiện`** với 3 điều kiện cụ thể, vai trò phụ trách và ngày kiểm tra (`2026-12-04`, `2026-12-14`), nêu rõ đánh đổi `power ~0,64` ở mức +5 điểm và rủi ro xem lại 100% (`11.743–12.415 đ` `simulated`).
- **Chấm chéo Gate 2a (`Nhom1234`):** Chấm 2 lượt theo tiến độ cập nhật của `Nhom1234` trong `report/team/phieu_cham.md`; ở bản cuối (`94dda92`), chấm **30 / 30** (`Go có điều kiện`) kèm câu hỏi phản biện về phần chi phí cố định 40 triệu đ/tháng (A4) còn bỏ ngỏ ở Mục 3.

## 4. Bằng chứng

- `e529cf6`, `43560b4`, `cd7c491`, `5ff30f4`: Các file kế hoạch `plan_ABC.md`, `plan_ABC_checkpoint.md`, `plan_DE_checkpoint.md`.
- `e67d42b`: Bộ nhãn độc lập 20 ca của Người gắn nhãn 2 trong `report/team/bang_loi.md`.
- `2050f62`: Phần quy tắc ca 8 và bảng khắc phục ca 11, ca 17 được gộp vào `report/team/bang_loi.md`.
- `9444450`, `ea57e66`, `e61dc83`, `b38b6fc`: Các lần cập nhật và hoàn thiện `report/team/ho_so_launch_v0.md` (PR #6, #8, #9).
- `c72e65f`: Chấm chéo `Nhom1234` trong `report/team/phieu_cham.md` (PR #10).

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI trong IDE).
- **Dùng vào việc gì:**
  - Duyệt hệ thống file markdown của đề bài và tạo kế hoạch chia việc cho 4 vai trò theo checkpoint (`plan_ABC.md`, `plan_ABC_checkpoint.md`, `plan_DE_checkpoint.md`).
  - Trích xuất 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, gợi ý phân loại theo nguyên nhân gốc và soạn thảo nội dung quy tắc ca 8, bảng khắc phục ca 11 & ca 17.
  - Tổng hợp các số liệu từ `src/lab13.py`, `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md` vào `report/team/ho_so_launch_v0.md`.
  - Đối chiếu hồ sơ của `Nhom1234` theo rubric C6–C8 để chấm vào `report/team/phieu_cham.md`.
- **Cách tự kiểm tra:**
  - Chạy `cd src && .venv/bin/python lab13.py` và `yaml.safe_load` để kiểm tra lại toàn bộ số liệu trước khi đưa vào `ho_so_launch_v0.md`.
  - Chạy lệnh kiểm tra từ bị cấm trong `report/team` theo đúng checklist của lab.
  - Tự đọc lại từng dòng bảng khắc phục (event, ngưỡng, tần suất, 1 vai trò phụ trách) và kiểm tra lại hồ sơ `Nhom1234` sau khi họ push bản mới để cập nhật điểm chấm từ 15/30 lên 30/30.

## 6. Tự đánh giá

- **Làm tốt:** Bám sát tiến độ giữ hồ sơ từ đầu buổi, hoàn thiện `ho_so_launch_v0.md` kịp mốc duyệt chéo, điều phối merge PR trên GitHub cho nhóm và chấm chéo `Nhom1234` công bằng theo đúng bản cập nhật mới nhất.
- **Chưa tốt:** Còn phụ thuộc nhiều vào AI khi rà soát/soạn thảo văn bản; cần chủ động hoàn thiện báo cáo cá nhân và thông tin thành viên sớm hơn trước giờ đóng gói.
- **Lần sau:** Tự gắn nhãn 20 ca hoàn toàn trước khi hỏi AI giải thích lại các ca phân vân, và chốt `TEAM.md` ngay từ đầu buổi.
