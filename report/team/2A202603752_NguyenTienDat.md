# Báo cáo cá nhân — Nguyễn Tiến Đạt

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tiến Đạt
- MSSV: 2A202603752
- Email: nguyentiendatqb126@gmail.com
- GitHub: [chesschillchill](https://github.com/chesschillchill)
- Vai trong nhóm: Người viết code, phụ trách A–B

## 2. Phần việc phụ trách

A1–A4 về mô hình chi phí mỗi việc thành công và B1–B4 về độ nhạy, giới hạn chạy lại và kịch bản xem lại 100%.

## 3. Đóng góp cụ thể

- Viết và chạy mô hình chi phí từ trace. Ba phép thử A1 đạt **1,20 · 1,25 · 1,25**. A2 tính được **4.472 đ/việc thành công** trên **978 việc thành công** (chi phí `simulated`).
- Tách chi phí theo 4 loại yêu cầu và tính chi phí cố định cho `noi_dia` + `hang_nang` ở hai mức khối lượng.
- Tính 9 kịch bản B1 và một kịch bản B2. B3 cho thấy giới hạn **2 lượt** có chi phí hệ thống thấp nhất, **6.901.220 đ**. B4 cho **11.743–12.415 đ/việc thành công** khi xem lại 100%, tùy giả định về số phút làm lại. Các mức chi phí này là `simulated`.

## 4. Bằng chứng

- Commit `2b9ce2f` · Việc 1: Checkpoint A, B.
- [Code tính A–B](../../src/lab13.py) và [bảng chi phí](bang_chi_phi.md).
- Kết quả chạy `python lab13.py` trong `src/` xác nhận cả ba phép thử A1 đạt và in đủ các mục A–B.

## 5. Công cụ AI đã dùng

Dùng Codex để đọc yêu cầu, hỗ trợ triển khai code và rà bảng chi phí. Kết quả được kiểm tra bằng cách chạy lại `lab13.py`, tính độc lập từ hai CSV cho 20 tổ hợp phạm vi và giới hạn chạy, rồi đối chiếu các mốc A–B trong báo cáo.

## 6. Tự đánh giá

Khi trình bày A2, cần ghi rõ **4.472 đ/việc thành công** của trợ lý và **5.865 đ/yêu cầu** của cả hệ thống (cả hai là `simulated`).
