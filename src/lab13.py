"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if p == 0:
        return math.inf if k is None else k
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    if p == 1:
        return float(k > 0)
    return -math.expm1(k * math.log1p(-p))


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    toi_da_hai_lan = so_lan_chay_ky_vong(0.8, 2)
    chay_den_khi_dung = so_lan_chay_ky_vong(0.8)
    he_so_ba_lan = he_so_chi_phi_moi_viec_thanh_cong(0.8, 3)
    assert abs(toi_da_hai_lan - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(chay_den_khi_dung - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_ba_lan - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')
    print(f'A1 · {toi_da_hai_lan:.2f} · {chay_den_khi_dung:.2f} · {he_so_ba_lan:.2f}')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính chi phí trợ lý cho tập yêu cầu được chọn.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    phut_xu_ly = reqs[['phut_xem_lai_simulated', 'phut_lam_lai_simulated']]
    thanh_cong = reqs['ket_qua'].eq('thanh_cong')
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        trong_gioi_han = reqs['so_lan_chay'] <= max_lan_chay
        phut_xu_ly = phut_xu_ly.loc[trong_gioi_han]
        thanh_cong = thanh_cong & trong_gioi_han

    tien_token = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    token = tien_token.sum()
    tool = tien_tool.sum()
    xem_lai = phut_xu_ly['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = phut_xu_ly['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    so_thanh_cong = thanh_cong.sum()
    return {
        'token': token,
        'tool': tool,
        'chay_lai': (tien_token + tien_tool).loc[runs['attempt'] > 1].sum(),
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': so_thanh_cong,
        'cps': tong / so_thanh_cong if so_thanh_cong else math.inf,
        'hoa_don_moi_yc': (token + tool) / len(reqs) if len(reqs) else math.nan,
    }


def co_mau_hai_ti_le(ti_le_goc, ti_le_muc_tieu, alpha, power):
    """Cỡ mẫu mỗi nhóm cho kiểm định hai phía với hai nhóm bằng nhau."""
    phan_vi = NormalDist().inv_cdf
    z_alpha = phan_vi(1 - alpha / 2)
    z_power = phan_vi(power)
    ti_le_tb = (ti_le_goc + ti_le_muc_tieu) / 2
    do_lech_chuan_gop = math.sqrt(2 * ti_le_tb * (1 - ti_le_tb))
    do_lech_chuan_rieng = math.sqrt(
        ti_le_goc * (1 - ti_le_goc) + ti_le_muc_tieu * (1 - ti_le_muc_tieu)
    )
    muc_chenh = ti_le_muc_tieu - ti_le_goc
    return math.ceil(((z_alpha * do_lech_chuan_gop + z_power * do_lech_chuan_rieng) / muc_chenh) ** 2)


def in_co_mau_pilot():
    """So sánh cỡ mẫu của ba cách chia nhóm trong D1."""
    ti_le_goc = 0.70
    alpha = 0.05
    power = 0.80
    icc = 0.02
    yeu_cau_moi_nhan_vien = 75
    nhan_vien_moi_nhom = 20
    depot_moi_nhom = 6

    mau_5_diem = co_mau_hai_ti_le(ti_le_goc, 0.75, alpha, power)
    he_so_thiet_ke = 1 + (yeu_cau_moi_nhan_vien - 1) * icc
    mau_thuc_te = math.ceil(mau_5_diem * he_so_thiet_ke)
    nhan_vien_can = math.ceil(mau_thuc_te / yeu_cau_moi_nhan_vien)

    mau_6_diem = co_mau_hai_ti_le(ti_le_goc, 0.76, alpha, power)
    # Giải c*m / (1 + (m - 1)*ICC) >= n cho m.
    yeu_cau_can = math.ceil(mau_6_diem * (1 - icc) / (nhan_vien_moi_nhom - mau_6_diem * icc))
    he_so_6_diem = 1 + (yeu_cau_can - 1) * icc
    mau_hieu_dung = nhan_vien_moi_nhom * yeu_cau_can / he_so_6_diem

    print('\nD1 · Cỡ mẫu pilot')
    print(f'a) Chia theo yêu cầu, +5 điểm: {mau_5_diem:,} yêu cầu mỗi nhóm')
    print(f'b) Chia theo nhân viên, {yeu_cau_moi_nhan_vien} yêu cầu/người: '
          f'DE {he_so_thiet_ke:.2f} | {mau_thuc_te:,} yêu cầu thực tế mỗi nhóm | '
          f'{nhan_vien_can} nhân viên mỗi nhóm ({2 * nhan_vien_can} người, hiện có {2 * nhan_vien_moi_nhom})')
    print(f'c) {nhan_vien_moi_nhom} nhân viên mỗi nhóm: '
          f'cỡ mẫu hiệu dụng < {nhan_vien_moi_nhom / icc:,.0f}, cần {mau_5_diem:,}')
    print(f'd) {depot_moi_nhom} depot mỗi nhóm: '
          f'cỡ mẫu hiệu dụng < {depot_moi_nhom / icc:,.0f}, cần {mau_5_diem:,}')
    print(f'e) +6 điểm, {nhan_vien_moi_nhom} nhân viên mỗi nhóm: cần {mau_6_diem:,} yêu cầu hiệu dụng mỗi nhóm | '
          f'ít nhất {yeu_cau_can} yêu cầu/người | DE {he_so_6_diem:.2f} | đạt {mau_hieu_dung:,.2f} hiệu dụng mỗi nhóm')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    print('\nA2 · Chi phí từ trace')
    ket_qua = mo_hinh(runs, reqs)
    cac_khoan_simulated = {'xem_lai', 'lam_lai', 'tong', 'cps'}
    for ten, gia_tri in ket_qua.items():
        nhan = ' simulated' if ten in cac_khoan_simulated else ''
        dinh_dang = ',.1f' if ten == 'hoa_don_moi_yc' else ',.0f'
        print(f'{ten:16s} {format(gia_tri, dinh_dang):>14s}{nhan}')
    ti_so_hoa_don = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    ti_trong_lam_lai = ket_qua['lam_lai'] / ket_qua['tong']
    ca_lam_thay = len(reqs) - ket_qua['thanh_cong']
    chi_phi_he_thong_moi_yeu_cau = (ket_qua['tong'] + BASELINE * ca_lam_thay) / len(reqs)
    print(f'CPS / hóa đơn mỗi yêu cầu: {ti_so_hoa_don:.1f}× simulated')
    print(f'Tỉ trọng làm lại: {ti_trong_lam_lai:.1%} simulated')
    print(f'Cả hệ thống: {chi_phi_he_thong_moi_yeu_cau:,.0f} đ/yêu cầu simulated')

    print('\nA3 · Chi phí mỗi việc thành công theo loại (simulated)')
    for loai, nhom in reqs.groupby('loai'):
        ket_qua_nhom = mo_hinh(runs, nhom)
        ti_le = ket_qua_nhom['thanh_cong'] / len(nhom)
        cps = ket_qua_nhom['cps']
        print(f'{loai:9s} {len(nhom):4d} yêu cầu | {ti_le:5.1%} thành công | '
              f'{nhom["so_lan_chay"].mean():.2f} lần/yêu cầu | {cps:,.0f} đ | {cps / BASELINE:.2f}×')
    runs_quoc_te = runs[runs['request_id'].isin(reqs.loc[reqs['loai'].eq('quoc_te'), 'request_id'])]
    ti_le_ok = runs_quoc_te['status'].eq('ok').groupby(runs_quoc_te['attempt']).mean()
    for attempt, ti_le in ti_le_ok.items():
        print(f'quoc_te, lượt {attempt}: {ti_le:.1%} chạy ok')

    print('\nA4 · Chi phí cố định cho noi_dia + hang_nang (tổng và tỉ số simulated)')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    chi_phi_pham_vi = mo_hinh(runs, pham_vi)
    # Khối lượng tháng gồm mọi loại yêu cầu, nên dùng tỉ trọng trên toàn mẫu.
    ti_le_thanh_cong_pham_vi = chi_phi_pham_vi['thanh_cong'] / len(reqs)
    for khoi_luong in (45_000, 22_500):
        viec_thanh_cong = khoi_luong * ti_le_thanh_cong_pham_vi
        co_dinh_moi_viec = 40_000_000 / viec_thanh_cong
        cps = chi_phi_pham_vi['cps'] + co_dinh_moi_viec
        print(f'{khoi_luong:,} yêu cầu/tháng | {viec_thanh_cong:,.0f} việc thành công | '
              f'{co_dinh_moi_viec:,.0f} đ cố định/việc | {cps:,.0f} đ | {cps / BASELINE:.2f}×')

    print('\nB1–B2 · Độ nhạy chi phí mỗi việc thành công (simulated)')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA),
        'Giá token giảm một nửa': dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=LUONG_PHUT * 1.25),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
        'Giá token và xem lại cùng gấp đôi': dict(
            gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA, he_so_xem_lai=2
        ),
    }
    cps_goc = ket_qua['cps']
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        print(f'{ten:34s} {cps:8,.0f} đ  {cps / cps_goc - 1:+.1%}')

    print('\nB3 · Giới hạn chạy lại (chi phí simulated)')
    for gioi_han in (1, 2, 3):
        ket_qua_gioi_han = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        ca_lam_thay = len(reqs) - ket_qua_gioi_han['thanh_cong']
        tong_tro_ly = ket_qua_gioi_han['tong']
        tong_he_thong = tong_tro_ly + BASELINE * ca_lam_thay
        print(f'{gioi_han} lần | {tong_tro_ly:,.0f} đ trợ lý | {ca_lam_thay} việc làm thay | '
              f'{tong_he_thong:,.0f} đ cả hệ thống | {ket_qua_gioi_han["cps"]:,.0f} đ/việc thành công')

    print('\nB4 · Xem lại 100% câu trả lời trong phạm vi (simulated)')
    co_cau_tra_loi = runs['request_id'].isin(pham_vi['request_id']) & runs['status'].eq('ok')
    so_ca_xem_lai = runs.loc[co_cau_tra_loi, 'request_id'].nunique()
    so_ca_lam_lai = pham_vi['ket_qua'].eq('lam_lai').sum()
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].mean()
    hoa_don_pham_vi = chi_phi_pham_vi['token'] + chi_phi_pham_vi['tool']
    so_viec_thanh_cong = chi_phi_pham_vi['thanh_cong']
    print(f'{len(pham_vi)} yêu cầu | {so_ca_xem_lai} xem lại | {so_ca_lam_lai} làm lại | '
          f'{so_viec_thanh_cong} thành công | {hoa_don_pham_vi:,.0f} đ token + tool')
    for phut_lam_lai in (9, phut_lam_lai_tb):
        tien_lam_lai = so_ca_lam_lai * phut_lam_lai * LUONG_PHUT
        chi_phi = hoa_don_pham_vi + 5 * so_ca_xem_lai * LUONG_PHUT + tien_lam_lai
        cps = chi_phi / so_viec_thanh_cong
        phut_xem_lai_hoa_von = (
            (BASELINE * so_viec_thanh_cong - hoa_don_pham_vi - tien_lam_lai)
            / (so_ca_xem_lai * LUONG_PHUT)
        )
        print(f'{phut_lam_lai:.2f} phút làm lại/ca | {cps:,.0f} đ/việc thành công | '
              f'{cps / BASELINE:.2f}× | hòa vốn ở {phut_xem_lai_hoa_von:.2f} phút xem lại/ca')

    in_co_mau_pilot()
