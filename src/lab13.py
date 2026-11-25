"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist

import pandas as pd

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError("p phải nằm trong khoảng (0, 1].")
    if k is None:
        return 1 / p
    if k < 1:
        raise ValueError("k phải lớn hơn hoặc bằng 1.")
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1:
        raise ValueError("p phải nằm trong khoảng (0, 1].")
    if k is None:
        return 1.0
    if k < 1:
        raise ValueError("k phải lớn hơn hoặc bằng 1.")
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs.loc[runs["request_id"].isin(reqs["request_id"])]

    if max_lan_chay is not None:
        runs = runs.loc[runs["attempt"] <= max_lan_chay]
        vuot_gioi_han = reqs["so_lan_chay"] > max_lan_chay
        reqs.loc[vuot_gioi_han, "ket_qua"] = "chuyen_nhan_vien"
        reqs.loc[
            vuot_gioi_han,
            ["phut_xem_lai_simulated", "phut_lam_lai_simulated"],
        ] = 0

    tien_token = (
        runs["tokens_in"] / 1000 * gia_vao
        + runs["tokens_out"] / 1000 * gia_ra
    )
    tien_tool = runs["tool_calls"] * gia_tool
    tien_xem_lai = (
        reqs["phut_xem_lai_simulated"].sum()
        * luong_phut
        * he_so_xem_lai
    )
    tien_lam_lai = (
        reqs["phut_lam_lai_simulated"].sum()
        * luong_phut
        * he_so_lam_lai
    )
    tong = tien_token.sum() + tien_tool.sum() + tien_xem_lai + tien_lam_lai
    thanh_cong = int((reqs["ket_qua"] == "thanh_cong").sum())
    if thanh_cong == 0:
        raise ValueError("Không có yêu cầu thành công để tính chi phí mỗi việc.")
    if len(reqs) == 0:
        raise ValueError("Không có yêu cầu để tính hoá đơn trung bình.")

    return {
        "token": tien_token.sum(),
        "tool": tien_tool.sum(),
        "chay_lai": (tien_token + tien_tool).loc[runs["attempt"] > 1].sum(),
        "xem_lai": tien_xem_lai,
        "lam_lai": tien_lam_lai,
        "tong": tong,
        "thanh_cong": thanh_cong,
        "cps": tong / thanh_cong,
        "hoa_don_moi_yc": (tien_token.sum() + tien_tool.sum()) / len(reqs),
    }


def in_a3(runs, reqs):
    print("\nA3 · Chi phí theo loại yêu cầu")
    print(
        "loai         so_yc  thanh_cong  lan_chay/yc"
        "   CPS (đ, simulated)   so_voi_12.000"
    )
    for loai in sorted(reqs["loai"].unique()):
        reqs_loai = reqs.loc[reqs["loai"] == loai]
        ket_qua = mo_hinh(runs, reqs_loai)
        so_yc = len(reqs_loai)
        so_lan_chay = runs["request_id"].isin(reqs_loai["request_id"]).sum()
        ti_le = ket_qua["thanh_cong"] / so_yc
        print(
            f"{loai:12s} {so_yc:5d}  {ti_le:9.1%}"
            f"  {so_lan_chay / so_yc:10.2f}"
            f"  {ket_qua['cps']:9,.0f}  {ket_qua['cps'] / BASELINE:10.2f}x"
        )

    theo_lan = runs.merge(
        reqs[["request_id", "loai"]], on="request_id", how="inner"
    )
    ti_le_ok = theo_lan.pivot_table(
        index="loai",
        columns="attempt",
        values="status",
        aggfunc=lambda values: (values == "ok").mean(),
    )
    print("\nTỉ lệ status=ok theo lần chạy:")
    print(ti_le_ok.to_string(float_format=lambda value: f"{value:.1%}"))


def in_a4(runs, reqs):
    print("\nA4 · Chi phí cố định (noi_dia + hang_nang)")
    reqs_trong_pham_vi = reqs.loc[
        reqs["loai"].isin(["noi_dia", "hang_nang"])
    ]
    ket_qua = mo_hinh(runs, reqs_trong_pham_vi)
    luong_yeu_cau_thang = 45000
    chi_phi_co_dinh = 40_000_000
    thanh_cong_thang = (
        luong_yeu_cau_thang * ket_qua["thanh_cong"] / len(reqs)
    )
    for he_so_khoi_luong in (1, 0.5):
        thanh_cong_thang_kich_ban = thanh_cong_thang * he_so_khoi_luong
        co_dinh_moi_viec = chi_phi_co_dinh / thanh_cong_thang_kich_ban
        tong_moi_viec = ket_qua["cps"] + co_dinh_moi_viec
        ten = "45.000" if he_so_khoi_luong == 1 else "22.500"
        print(
            f"{ten} yêu cầu/tháng: {thanh_cong_thang_kich_ban:,.0f}"
            f" thành công, cố định {co_dinh_moi_viec:,.0f} đ/việc,"
            f" tổng {tong_moi_viec:,.0f} đ/việc"
            f" ({tong_moi_viec / BASELINE:.2f}x nhân viên, simulated)."
        )


def in_b(runs, reqs, ket_qua_goc):
    print("\nB1 · Độ nhạy từng yếu tố (CPS simulated)")
    kich_ban = [
        ("Giá token gấp đôi", {"gia_vao": 52, "gia_ra": 260}),
        ("Giá token giảm một nửa", {"gia_vao": 13, "gia_ra": 65}),
        ("Xem lại gấp đôi", {"he_so_xem_lai": 2}),
        ("Xem lại giảm một nửa", {"he_so_xem_lai": 0.5}),
        ("Làm lại gấp đôi", {"he_so_lam_lai": 2}),
        ("Làm lại giảm một nửa", {"he_so_lam_lai": 0.5}),
        ("Lương tăng 25%", {"luong_phut": 2500}),
        ("Tối đa 2 lần chạy", {"max_lan_chay": 2}),
        ("Chỉ 1 lần chạy", {"max_lan_chay": 1}),
    ]
    for ten, tham_so in kich_ban:
        cps = mo_hinh(runs, reqs, **tham_so)["cps"]
        thay_doi = (cps / ket_qua_goc["cps"] - 1) * 100
        print(f"{ten:26s} {cps:9,.0f} đ  {thay_doi:+6.1f}%")

    print("\nB2 · Giá token gấp đôi + xem lại gấp đôi (simulated)")
    cps_kep = mo_hinh(
        runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2
    )["cps"]
    print(
        f"{cps_kep:,.0f} đ/việc, "
        f"{(cps_kep / ket_qua_goc['cps'] - 1) * 100:+.1f}% so với gốc."
    )

    print("\nB3 · Chi phí cả hệ thống theo giới hạn chạy")
    for gioi_han in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        that_bai = len(reqs) - ket_qua["thanh_cong"]
        chi_phi_nhan_vien = that_bai * BASELINE
        tong_he_thong = ket_qua["tong"] + chi_phi_nhan_vien
        print(
            f"{gioi_han} lần: trợ lý {ket_qua['tong']:,.0f} đ,"
            f" {that_bai} yêu cầu chuyển nhân viên,"
            f" cả hệ thống {tong_he_thong:,.0f} đ,"
            f" CPS {ket_qua['cps']:,.0f} đ (simulated)."
        )

    print("\nB4 · Xem lại 100% (noi_dia + hang_nang)")
    reqs_pham_vi = reqs.loc[
        reqs["loai"].isin(["noi_dia", "hang_nang"])
    ]
    runs_pham_vi = runs.loc[
        runs["request_id"].isin(reqs_pham_vi["request_id"])
    ]
    co_run_ok = runs_pham_vi.loc[
        runs_pham_vi["status"] == "ok", "request_id"
    ].nunique()
    so_lam_lai = int((reqs_pham_vi["ket_qua"] == "lam_lai").sum())
    tong_token_tool = mo_hinh(runs_pham_vi, reqs_pham_vi)
    tien_xem_lai = co_run_ok * 5 * LUONG_PHUT
    tien_lam_lai_9_phut = so_lam_lai * 9 * LUONG_PHUT
    so_viec_thanh_cong = tong_token_tool["thanh_cong"]
    tong_9_phut = (
        tong_token_tool["token"]
        + tong_token_tool["tool"]
        + tien_xem_lai
        + tien_lam_lai_9_phut
    )
    cps_9_phut = tong_9_phut / so_viec_thanh_cong
    print(
        f"Giả định 9 phút làm lại: {cps_9_phut:,.0f} đ/việc "
        f"({cps_9_phut / BASELINE:.2f}x nhân viên)."
    )

    phut_lam_lai_trung_binh = reqs.loc[
        reqs["ket_qua"] == "lam_lai", "phut_lam_lai_simulated"
    ].mean()
    tien_lam_lai_simulated = (
        so_lam_lai * phut_lam_lai_trung_binh * LUONG_PHUT
    )
    tong_simulated = (
        tong_token_tool["token"]
        + tong_token_tool["tool"]
        + tien_xem_lai
        + tien_lam_lai_simulated
    )
    cps_simulated = tong_simulated / so_viec_thanh_cong
    print(
        f"Dùng mức làm lại trung bình toàn bộ ca lam_lai "
        f"({phut_lam_lai_trung_binh:.1f} phút): "
        f"{cps_simulated:,.0f} đ/việc "
        f"({cps_simulated / BASELINE:.2f}x nhân viên, simulated)."
    )


def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm để so sánh hai tỉ lệ độc lập."""
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_power = NormalDist().inv_cdf(power)
    p_trung_binh = (p1 + p2) / 2
    so_hang_tu = (
        z_alpha * math.sqrt(2 * p_trung_binh * (1 - p_trung_binh))
        + z_power
        * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    )
    return math.ceil(so_hang_tu**2 / (p2 - p1) ** 2)


def in_d1():
    print("\nD1 · Cỡ mẫu pilot")
    p1, p2, alpha, power, icc = 0.70, 0.75, 0.05, 0.80, 0.02
    n_5_diem = co_mau_hai_ti_le(p1, p2, alpha, power)

    m_nhan_vien = 75
    de_nhan_vien = 1 + (m_nhan_vien - 1) * icc
    n_phan_cum = math.ceil(n_5_diem * de_nhan_vien)
    nhan_vien_moi_nhom = math.ceil(n_phan_cum / m_nhan_vien)

    print(f"a) Chia theo yêu cầu: {n_5_diem:,} yêu cầu mỗi nhóm.")
    print(
        f"b) Chia theo nhân viên, m=75: DE={de_nhan_vien:.2f}, "
        f"{n_phan_cum:,} yêu cầu hiệu chỉnh/nhóm, "
        f"khoảng {nhan_vien_moi_nhom} nhân viên/nhóm "
        f"({2 * nhan_vien_moi_nhom} tổng cộng)."
    )
    print(
        f"c) 20 nhân viên/nhóm: c/ICC = {20 / icc:,.0f} "
        f"yêu cầu hiệu dụng tối đa, thấp hơn {n_5_diem:,}."
    )
    print(
        f"d) 6 depot/nhóm: c/ICC = {6 / icc:,.0f} "
        "yêu cầu hiệu dụng tối đa."
    )

    p2_6_diem = 0.76
    n_6_diem = co_mau_hai_ti_le(p1, p2_6_diem, alpha, power)
    so_cum = 20
    mau_moi_nhan_vien = math.ceil(
        n_6_diem * (1 - icc) / (so_cum - n_6_diem * icc)
    )
    de_6_diem = 1 + (mau_moi_nhan_vien - 1) * icc
    n_hieu_dung = so_cum * mau_moi_nhan_vien / de_6_diem
    print(
        f"e) Chênh 6 điểm: {n_6_diem:,}/nhóm; với 20 nhân viên/nhóm "
        f"cần {mau_moi_nhan_vien} yêu cầu/người, DE={de_6_diem:.2f}, "
        f"n hiệu dụng≈{n_hieu_dung:.0f}."
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print("\nA2 · Mô hình chi phí")
    for ten, gia_tri in ket_qua.items():
        nhan = f"{ten} [simulated]" if ten in {
            "xem_lai", "lam_lai", "tong", "cps"
        } else ten
        if ten == "hoa_don_moi_yc":
            print(f"{nhan:26s} {gia_tri:14,.1f}")
        else:
            print(f"{nhan:26s} {gia_tri:14,.0f}")
    in_a3(runs, reqs)
    in_a4(runs, reqs)
    in_b(runs, reqs, ket_qua)
    in_d1()
