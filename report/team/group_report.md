# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: **Nhom145**
- Lớp: **L3B**
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

- **Mục tiêu:** Đánh giá hiệu quả kinh tế, phân loại lỗi, thiết kế pilot và lập bộ **hồ sơ launch v0** cho trợ lý hoàn phí LogiX-VN tại cổng **Gate 2a** trên bộ dữ liệu giả lập gồm `1.200` yêu cầu (`1.624` lần chạy).
- **Cách tiếp cận:** Chia 4 vai trò phối hợp song song theo các mốc checkpoint (`src/lab13.py` cho mô hình chi phí và cỡ mẫu; 2 người gắn nhãn độc lập 20 ca lỗi rồi đối chiếu; giữ hồ sơ liên tục từ CP1 tới CP5).

## 3. Giải pháp

- **Nhiệm vụ A & B (Mô hình chi phí & độ nhạy):** Cài đặt hàm `mo_hinh` và các kịch bản trong [src/lab13.py](../../src/lab13.py), đối chiếu tính tay và tổng hợp bảng A1–A4, B1–B4 trong [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Phân loại lỗi & khắc phục):** Hai người gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, thống nhất ca lệch và lập bảng khắc phục 5 ca có event, ngưỡng, tần suất và vai trò phụ trách trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính 5 câu cỡ mẫu D1, kiểm tra 5 câu tách tác động D2, đặt 3 luật dừng 4 vế trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, rủi ro & hồ sơ launch v0):** Tính 3 chỉ số E1, thiết kế 12 event có `trace_id`, phân tích 3 rủi ro kinh tế E2 trong [chi_so.md](chi_so.md) và tổng hợp thành 1 trang tại [ho_so_launch_v0.md](ho_so_launch_v0.md).
- **Duyệt chéo Gate 2a:** Chấm hồ sơ của `Nhom1234` theo 3 tiêu chí tại [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Chi phí mỗi việc thành công:** `4.472 đ` toàn mẫu (`simulated`), gấp `16,3` lần hoá đơn token + tool chia số yêu cầu (`274,7 đ`); giờ nhân viên chiếm `92,5%` tổng chi phí (`làm lại` `51,8%`, `xem lại` `40,7%`, `simulated`).
- **Phạm vi & chi phí cố định:** Loại `quoc_te` (`22.515 đ = 1,88×` so với `12.000 đ`, thành công `27,3%`) và `doi_tac` (`0,85×`), thu hẹp pilot về `noi_dia` (`0,22×`) + `hang_nang` (`0,69×`). Cộng cố định 40 triệu đ/tháng ở quy mô 45.000 yêu cầu/tháng cho `4.599 đ/việc` (`0,38×`, `simulated`).
- **Độ nhạy & xem lại 100%:** Yếu tố nhạy nhất là số ca làm lại (`+51,8%` khi ×2, `simulated`). Nếu phải xem lại 100%, chi phí lên `11.743 đ` (`0,98×`) đến `12.415 đ` (`1,03×` ở mức trung bình `15,3` phút làm lại, `simulated`).
- **Phân loại lỗi:** Đồng thuận `18/20 = 90%` (lệch ca 6 và ca 8 đã thống nhất theo nguyên nhân gốc); hoàn thiện bảng khắc phục 5 ca (`9, 15, 10, 11, 17`).
- **Kế hoạch pilot & chỉ số:** Chọn chia theo nhân viên (`20 + 20`), chấp nhận MDE `+6` điểm (`859` đơn hiệu dụng/nhóm, `m ≥ 299` đơn/người, `DE = 6,96`, bước 20 người ~`10` ngày làm việc, `decision_date: 2027-01-12`). Chỉ số đợt chạy thử: `82,83%` đóng 24h không mở lại 7 ngày, `27,12%` bỏ qua gợi ý, `4,25%` mở lại 7 ngày (`3,97%` trong phạm vi).
- **Đề xuất cuối:** **`Go có điều kiện`** (xử lý khoá chống trùng & đối soát sổ cái ca 7, 20; phê duyệt đánh đổi `power ~0,64` ở mức `+5` điểm; bật đủ 12 event có `trace_id`, thay phút `_simulated` bằng số đo thật sau tuần 1 và có lộ trình giảm xem lại theo bậc).
- **Kết quả duyệt chéo nhận được từ hội đồng:** *(điền điểm/quyết định hội đồng chấm cho Nhom145 nếu có)*. Nhom145 chấm `Nhom1234`: `30/30` (`Go có điều kiện`).

## 5. Khó khăn và cách xử lý

- **Không đủ mẫu ở mức +5 điểm với 40 nhân viên:** Trần `20 / 0,02 = 1.000 < 1.251`, nên nhóm nới MDE lên `+6` điểm (`n = 859`, `m = 299`) và ghi rõ rủi ro `power ~0,64` nếu hiệu ứng thật chỉ `+5` điểm.
- **Lệch nhịp gom đơn và lịch theo dõi 7 ngày:** Do phạm vi `noi_dia + hang_nang` chiếm `81,8%` (`≈ 30,7` đơn/người/ngày), nhóm điều chỉnh bước 20 người lên khoảng `10` ngày và lùi `decision_date` sang `2027-01-12` để đủ 7 ngày theo dõi mở lại.
- **Nguy cơ xung đột Git khi làm song song:** Tách file nháp theo nhánh riêng trước khi người phụ trách chính gộp vào file chung.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu thời gian nhân viên là giả lập (`_simulated`):** Cần thay bằng thời gian đo thật từ event `staff_review_decision` và `staff_rework_completed` ngay sau tuần 1 của pilot.
- **Độ nhạy cao với tỉ lệ xem lại và làm lại:** Cần thiết kế cơ chế giảm tỉ lệ xem lại theo bậc dựa trên độ tin cậy để tránh rơi vào ngưỡng `11.743–12.415 đ/việc` (`simulated`).

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu statsmodels, lớp `NormalIndPower` (`stats.power`)
- Bộ tài liệu hướng dẫn Lab 13 (`docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`)
