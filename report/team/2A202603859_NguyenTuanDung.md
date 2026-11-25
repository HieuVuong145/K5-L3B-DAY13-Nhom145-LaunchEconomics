# Báo cáo cá nhân — NguyenTuanDung-2A202603859

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tuấn Dũng
- MSSV: 2A202603859
- Email: 26ai.dungnt16@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số (Vai trò 2)

## 2. Phần việc phụ trách

- **Giai đoạn 0 & CP1 (Nhiệm vụ A):** Cài đặt môi trường Python (`.venv`, `requirements.txt`), nắm 6 công thức & bộ đơn giá giả định; tính tay kiểm tra 3 phép thử A1 (`1,20 · 1,25 · 1,25`), đối chiếu hàm `mo_hinh()` trong `src/lab13.py` và điền đầy đủ bảng A1, A2, A3, A4 vào `report/team/bang_chi_phi.md`.
- **CP2 (Nhiệm vụ B):** Kiểm tra chéo 9 kịch bản B1 (xác nhận tính nhất quán tuyến tính giảm nửa = nửa mức tăng gấp đôi), điền B2, B3, B4 (đủ cả 2 mức phút làm lại 9 phút & 15,3 phút và ngưỡng hoà vốn `4,8–5,1 phút/ca`) vào `report/team/bang_chi_phi.md`.
- **CP3 (Song song):** Chạy lại `src/lab13.py` trên máy thứ hai để xác nhận chạy sạch, rà nhãn `simulated`, giới hạn `≤ 3 dòng/câu` và đảm bảo chỉ dùng phạm vi kế hoạch pilot.
- **CP4 (Nhiệm vụ D):** Kiểm tra tay công thức câu e (`m ≥ 299`, `DE = 6,96`, `n_eff ≈ 859,2`), tính `power ≈ 0,64` ở mức `+5` điểm và tỉ lệ `mo_lai_trong_7_ngay` (`4,25%` toàn mẫu / `3,97%` phạm vi pilot); điền phần chú thích D1, đánh đổi và ngưỡng an toàn vào đầu `report/team/pilot_plan.yaml`.
- **CP5 (Nhiệm vụ E):** Điền bảng **E2 · Rủi ro kinh tế** (3 rủi ro chính kèm số từ `bang_chi_phi.md`, nhãn `simulated` và vai trò phụ trách cụ thể) trong `report/team/chi_so.md`; kiểm tra `yaml.safe_load` cho `pilot_plan.yaml` và rà soát toàn bộ quy tắc nộp bài.
- **Tài liệu thuyết trình nhóm:** Dựng 2 bộ slide trình bày `presentation/slide_checkpoint1.html` và `presentation/slide_checkpoint2.html`.

## 3. Đóng góp cụ thể

- Hoàn thiện 100% nội dung và kiểm số cho [report/team/bang_chi_phi.md](bang_chi_phi.md) (A1–A4, B1–B4), lệch `0%` so với đáp án chuẩn và `src/lab13.py`.
- Hoàn thiện phần chú thích phân tích cỡ mẫu D1, đánh đổi MDE `+6` điểm và tỉ lệ mở lại hiện tại trong [report/team/pilot_plan.yaml](pilot_plan.yaml).
- Hoàn thiện mục **E2 · Rủi ro kinh tế** trong [report/team/chi_so.md](chi_so.md).
- Tạo bộ slide thuyết trình CP1 và CP2 trong thư mục `presentation/`.

## 4. Bằng chứng

- `6d9be46` — Cập nhật phân công Vai trò 2 (`TEAM.md`, `plan_ABC.md`).
- `6886e69`, `be063f1` — Hoàn thiện và kiểm số `report/team/bang_chi_phi.md` (CP1 & CP2).
- `dd714e8`, `47d32a1` — Tạo và tổ chức `presentation/slide_checkpoint1.html`, `presentation/slide_checkpoint2.html`.
- Commit CP4–CP5 trên nhánh `main` — Cập nhật D1 trong `report/team/pilot_plan.yaml`, E2 trong `report/team/chi_so.md` và báo cáo cá nhân `report/team/2A202603859_NguyenTuanDung.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI tích hợp trong IDE (Antigravity).
- **Mục đích sử dụng:** Hỗ trợ viết script Python kiểm tra chéo độc lập từ 2 file CSV (`logix_runs.csv`, `logix_requests.csv`), rà soát nhãn `simulated` / từ cấm / định dạng bảng markdown, kiểm tra tính toán cỡ mẫu `statsmodels` và dựng giao diện HTML cho slide thuyết trình CP1–CP2.
- **Cách tự kiểm tra:** Trực tiếp chạy `src/.venv/Scripts/python.exe lab13.py` đối chiếu từng dòng output với bảng trong `bang_chi_phi.md`; tính tay lại các phép chia chốt (A1 `1,20/1,25/1,25`, A4 `40.000.000 ÷ 33.750 = 1.185 đ`, B1 tính tuyến tính giảm nửa = nửa mức tăng, D1 câu e `20m / (1 + 0,02(m-1)) ≥ 859 → m ≥ 299`); chạy `yaml.safe_load` kiểm tra cú pháp `pilot_plan.yaml`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, đúng tiến độ toàn bộ đầu việc của **Vai trò 2 (Người kiểm số)** qua cả 5 checkpoint (CP1–CP5), đảm bảo số liệu khớp tuyệt đối giữa code (`src/lab13.py`) và các file hồ sơ nhóm (`bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`), tuân thủ nghiêm ngặt 5 quy tắc của lab.
