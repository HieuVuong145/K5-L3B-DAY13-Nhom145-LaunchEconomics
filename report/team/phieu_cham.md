# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Nhom145 (L3B — K5-L3B-DAY13-Nhom145-LaunchEconomics)

- Nhóm được chấm: Nhom1234 (L3B — K5-L3B-DAY13-Nhom1234-LaunchEconomics)


| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Chọn **Go có điều kiện** khớp với số `4.472 đ` CPS và `0,49×` cả hệ thống (`simulated`), đồng thời nêu rõ cả 3 con số bất lợi (xem lại 100% lên `11.743–12.415 đ` `0,98–1,03×`, `power ~0,64` ở mức 5 điểm, 40 triệu cố định ở 4 người lên `~15.300 đ`) kèm 5 điều kiện có người phụ trách và ngày kiểm tra. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số từ `_simulated` đều có nhãn `[simulated]` / `simulated`; phạm vi thu hẹp về `noi_dia` (`0,22×`) + `hang_nang` (`0,69×`), loại `quoc_te` (`22.515 đ = 1,88×`) và `doi_tac` (`10.215 đ = 0,85×`); hồ sơ không dùng từ bị cấm theo quy tắc 5 của lab. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | `pilot_plan.yaml` hợp lệ (`yaml.safe_load` OK, không còn `?`); tách tác động với 20+20 nhân viên ngẫu nhiên phân tầng theo depot, `m ≥ 299`, `859`/nhóm (`DE = 6,96`), `decision_date: 2027-01-14`; đủ 4 luật dừng 4 vế có ngưỡng, thời hạn và người có quyền dừng (`Giám đốc vận hành`, `PM trợ lý hoàn phí`, `Trưởng nhóm CSKH`). |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ đầy đủ, nhất quán giữa số liệu và đề xuất `Go có điều kiện`: nêu rõ cả mặt lợi (`4.472 đ` `simulated`, `0,49×` cả hệ thống) lẫn các con số bất lợi (`power ~0,64` ở 5 điểm, xem lại 100% lên `12.415 đ = 1,03×`, cố định 40 triệu ở quy mô nhỏ), kế hoạch pilot 20+20 nhân viên tách được tác động và có 4 luật dừng cụ thể.

**Một câu hỏi cho đội trình:** Mục 3 trong `ho_so_launch_v0.md` ghi chưa cộng 40 triệu cố định (chờ A4) — vậy nếu cộng 40 triệu đ/tháng ở quy mô 45.000 đơn/tháng và ở nửa khối lượng thì chi phí mỗi việc thành công trong phạm vi pilot là bao nhiêu, có làm đổi đề xuất `Go có điều kiện` không?

**Câu trả lời của đội trình (ghi lại tại buổi):** ...
