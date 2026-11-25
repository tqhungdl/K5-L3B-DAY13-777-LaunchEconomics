# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Tiến Đạt | 2A202603752 | nguyentiendatqb126@gmail.com | [chesschillchill](https://github.com/chesschillchill) | Người viết code, phụ trách A–B |
|   2 | Trần Quang Hưng | 2A202603767 | tqhungdl26@gmail.com | [tqhungdl](https://github.com/tqhungdl) | Người gắn nhãn 1, phụ trách C–D |
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

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

## Nguyễn Tiến Đạt — 2A202603752

### Phần việc phụ trách

- A1–A4 và B1–B4, gồm mô hình chi phí và phân tích độ nhạy.

### Đóng góp cụ thể

- Hoàn thiện `src/lab13.py` và bảng chi phí. Ba phép thử A1 đạt 1,20 · 1,25 · 1,25.
- Đối chiếu 9 kịch bản độ nhạy, so chi phí hệ thống với 3 giới hạn chạy và tính kịch bản xem lại 100%.

### Bằng chứng

- Commit `2b9ce2f`, [bảng chi phí](report/team/bang_chi_phi.md) và [báo cáo cá nhân](report/team/2A202603752_NguyenTienDat.md).

## Trần Quang Hưng — 2A202603767

### Phần việc phụ trách

- C: Phân loại lỗi và lập bảng khắc phục.
- D1–D3: Tính cỡ mẫu, kiểm tra khả năng tách tác động và lập kế hoạch pilot.

### Đóng góp cụ thể

- Gắn nhãn 20 ca lỗi và đối chiếu với Lê Quốc Khánh. Hai bộ nhãn trùng 16/20 ca (80%). Giải thích bốn ca khác nhãn và đề xuất cách phát hiện, cách khắc phục và vai trò phụ trách cho năm loại lỗi.
- Hoàn thiện phần tính cỡ mẫu và kế hoạch chia ngẫu nhiên theo nhân viên với 20 người mỗi nhóm. Tính tỉ lệ mở lại trong 7 ngày và lập ba luật dừng về an toàn, chi phí và mức sử dụng.

### Bằng chứng

- [Bảng lỗi](report/team/bang_loi.md), [mã tính D1 và D3](src/lab13.py), [kế hoạch pilot](report/team/pilot_plan.yaml) và [báo cáo cá nhân](report/team/2A202603767_TranQuangHung.md).
