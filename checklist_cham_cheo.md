# Checklist chấm chéo Gate 2a (công cụ nội bộ, không phải file nộp)

> Dùng khi làm hội đồng chấm nhóm n + 1, rồi chép điểm, lý do có số, quyết định và câu hỏi vào `report/team/phieu_cham.md`.
> Cũng dùng để **tự rà hồ sơ nhóm mình** trước 17:00: nhóm khác sẽ chấm mình đúng theo ba tiêu chí này (C6, C7, C8 trong `RUBRIC.md`, tổng 30 điểm).
> Chấm theo bằng chứng, không theo cách trình bày. Điểm và quyết định là phán đoán của nhóm; không dùng AI để bịa kết quả duyệt chéo (`RULES.md`).

## Cần đọc gì của nhóm được chấm

1. `report/team/ho_so_launch_v0.md`: bảy mục và đề xuất (đọc trước, đây là tài liệu chính).
2. `report/team/pilot_plan.yaml`: cho tiêu chí 3.
3. `report/team/bang_chi_phi.md`, `report/team/chi_so.md`: để đối chiếu số khi hồ sơ nhắc tới.

Thời gian 15 phút: đọc hồ sơ 5 phút, đối chiếu yaml và số 5 phút, viết phiếu 5 phút.

---

## Tiêu chí 1 · Đề xuất khớp bằng chứng (0 / 5 / 10)

Kiểm tra:
- [ ] Dòng cuối là **đúng một** trong ba: Go, Go có điều kiện, No-go.
- [ ] Đề xuất không mâu thuẫn với số của chính nhóm đó. Ví dụ mâu thuẫn: ghi Go cho cả quoc_te trong khi bảng A3 của họ cho 1,88×.
- [ ] Hồ sơ **nêu ra** ít nhất một con số bất lợi. Các con số bất lợi hay bị bỏ qua:
  - power chỉ ~0,64 nếu tác động thật là +5 điểm (khi chọn mức chênh 6 điểm);
  - xem lại 100% làm chi phí lên ~11.743 đ = 0,98× (B4), có thể 1,03× nếu dùng 15,3 phút làm lại;
  - chi phí mỗi việc thành công 4.472 đ **chưa tính** 148 ca chuyển nhân viên; cả hệ thống ≈ 5.865 đ/yêu cầu = 0,49×;
  - chi phí cố định 40 triệu/tháng tăng mạnh khi khối lượng nhỏ.
- [ ] Với mỗi con số bất lợi, hồ sơ có **cách xử lý** (điều kiện, luật dừng, kế hoạch giảm xem lại…).
- [ ] Nếu là Go có điều kiện: mỗi điều kiện có **người phụ trách** (một vai trò) và **ngày kiểm tra**. Nếu No-go: có việc phải làm để quay lại cổng.

Chấm:
- **0:** đề xuất mâu thuẫn với số của chính nhóm.
- **5:** khớp, nhưng bỏ qua ít nhất một con số bất lợi quan trọng.
- **10:** khớp, nêu cả con số bất lợi và cách xử lý.

## Tiêu chí 2 · Số giả lập và phạm vi (0 / 5 / 10)

Kiểm tra:
- [ ] Mọi số tính từ `phut_xem_lai_simulated` / `phut_lam_lai_simulated` có nhãn **simulated** (hoặc trạng thái "Giả lập"): chi phí mỗi việc thành công, tiền xem lại, tiền làm lại, tỉ số so với 12.000 đ, bảng độ nhạy, B4, rủi ro kinh tế.
- [ ] Trong hồ sơ, các mục 1, 2, 3, 7 (dựa trên cột `_simulated`) có trạng thái **Giả lập**.
- [ ] Phạm vi pilot **đã thu hẹp**, không phải "mọi yêu cầu".
- [ ] Lý do thu hẹp **có số**. Số tham chiếu (bài mẫu): noi_dia 0,22× · hang_nang 0,69× · quoc_te 1,88× (thành công 27,3%) · doi_tac 0,85×.
- [ ] Không có từ "production".

Chấm:
- **0:** không có nhãn giả lập, phạm vi là "mọi yêu cầu".
- **5:** có nhãn **hoặc** có thu hẹp phạm vi (thiếu một trong hai, hoặc có nhưng thiếu số).
- **10:** nhãn ở **mọi** số giả lập **và** phạm vi thu hẹp có lý do bằng số.

## Tiêu chí 3 · Pilot ra được quyết định (0 / 5 / 10)

Kiểm tra trong `pilot_plan.yaml`:
- [ ] Có **nhóm đối chứng** chạy cùng thời gian, chia **ngẫu nhiên**.
- [ ] Đơn vị chia hợp lý. Theo depot (6 + 6) chỉ có 6 cụm, trần 300: thường là thiếu mẫu.
- [ ] **Cỡ mẫu**: có `n_per_arm`, `design_effect`, `clusters_per_arm`. Số tham chiếu: theo yêu cầu 1.251/nhóm; 20 người/nhóm trần 1.000; mức 6 điểm cần 859/nhóm, m ≥ 299, DE 6,96.
- [ ] Ít nhất **20 cụm mỗi nhóm**, hoặc ghi rõ đánh đổi đã chấp nhận.
- [ ] Ít nhất **3 luật dừng** (an toàn, chi phí, sử dụng), mỗi luật đủ **NẾU – TRONG – THÌ – KHÔNG THÌ**.
- [ ] Mỗi luật có **ngưỡng bằng số**, **thời hạn**, và **người có quyền dừng** (một vai trò).
- [ ] Ngưỡng an toàn không làm pilot dừng ngay tuần đầu: tỉ lệ mở lại hiện tại 4,25% toàn mẫu, 3,97% trong noi_dia + hang_nang. Ngưỡng tuyệt đối 3% là sai.
- [ ] Có `rollback` (ai bấm, bao lâu, khách được phục vụ bằng gì) và `decision_date`.
- [ ] File không còn dấu `?` ngoài dòng chú thích.

Chấm:
- **0:** không có đối chứng **hoặc** thiếu cỡ mẫu (không có số, hoặc số sai mà không ghi đánh đổi).
- **5:** đủ cỡ mẫu, nhưng luật dừng chung chung (thiếu ngưỡng, thời hạn hoặc người dừng).
- **10:** tách được tác động, đủ mẫu (hoặc đánh đổi rõ), luật dừng có ngưỡng, thời hạn, người có quyền dừng.

---

## Quyết định của hội đồng và câu hỏi

- Quyết định: Go · Go có điều kiện · No-go. Quyết định của hội đồng có thể khác đề xuất của nhóm được chấm; lý do phải có số.
- Chọn **một** câu hỏi nhắm vào chỗ yếu nhất vừa tìm được. Ngân hàng câu hỏi:
  - "Chi phí mỗi việc thành công là bao nhiêu nếu tuần đầu phải xem lại 100%?"
  - "Cách chia của nhóm có ít nhất 20 cụm mỗi nhóm không?"
  - "Với tỉ lệ mở lại 4,25% hiện tại, ngưỡng an toàn của nhóm có làm pilot dừng ngay tuần đầu không?"
  - "Nếu tác động thật chỉ +5 điểm, pilot của nhóm có power bao nhiêu, và nhóm chấp nhận rủi ro đó thế nào?"
  - "Con số 4.472 đ đã tính phần nhân viên làm thay các ca chuyển nhân viên chưa?"
  - "Luật dừng chi phí của nhóm có cộng 40 triệu cố định không? Ở bước 4 người thì có bị kích hoạt ngay không?"

## Chép sang `phieu_cham.md`

- Nhóm chấm (hội đồng): nhóm mình · Nhóm được chấm: số nhóm n + 1 (hỏi coach).
- Mỗi tiêu chí: điểm (0/5/10) và **lý do có số** (trích con số hoặc dòng cụ thể trong hồ sơ họ).
- Tổng /30, quyết định, lý do, một câu hỏi; câu trả lời của đội trình ghi lại tại buổi.
