# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: Chưa cung cấp
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng hồ sơ Gate 2a cho trợ lý hoàn phí LogiX-VN từ mẫu 1.200 yêu cầu và 1.624 lần chạy agent. Mục tiêu là tính chi phí thật, xác định yếu tố kinh tế nhạy nhất, phân loại lỗi, thiết kế pilot có đối chứng và viết chỉ số có thể đo bằng event có `trace_id`. Toàn bộ số liệu của lab là giả lập; các số dùng cột `_simulated` được đánh dấu `simulated`.

Nhóm chia theo module: A–B phụ trách mô hình chi phí và độ nhạy; C–D phụ trách bảng lỗi và kế hoạch pilot; E phụ trách chỉ số, rủi ro và hồ sơ launch.

## 3. Giải pháp

- **A–B:** Hoàn thiện `src/lab13.py`, kiểm tra ba phép thử A1, tính chi phí từ mọi lần chạy kể cả lần lỗi, tách theo loại yêu cầu và lập bảng độ nhạy trong `report/team/bang_chi_phi.md`.
- **C:** Gắn nhãn độc lập 20 ca lỗi theo năm loại Google PAIR, so đồng thuận và ghi cách phát hiện/khắc phục trong `report/team/bang_loi.md`. Bộ nhãn tham khảo đạt 20/20 = 100%; nhóm phải xác nhận tên người gắn nhãn và bộ nhãn thực tế trước khi nộp.
- **D:** Tính cỡ mẫu, hệ số thiết kế, kiểm tra khả năng tách tác động và hoàn thiện `report/team/pilot_plan.yaml` với nhóm đối chứng và luật dừng.
- **E:** Đặc tả chỉ số, event, rủi ro kinh tế trong `report/team/chi_so.md`; tổng hợp bảy mục và đề xuất trong `report/team/ho_so_launch_v0.md`.

## 4. Kết quả

Chi phí mỗi việc thành công là **4.472 đ [simulated]**, trên 978 việc thành công và tổng chi phí 4.373.585 đ. Khi cộng chi phí nhân viên cho 222 ca chuyển người, chi phí cả hệ thống khoảng **5.865 đ/yêu cầu = 0,49×** mức 12.000 đ [simulated]. Ba yếu tố nhạy nhất là số ca làm lại, tỉ lệ xem lại và lương nhân viên.

Chỉ số trong đợt chạy thử gồm: chỉ số chính **82,83% (994/1.200)**, tỉ lệ bỏ qua gợi ý **27,12% (48/177)** và tỉ lệ mở lại trong 7 ngày **4,25% (51/1.200)**. Đây là số quan sát của đợt chạy thử, chưa phải bằng chứng trợ lý đã nâng chỉ số vì chưa có nhóm đối chứng.

Kế hoạch chọn pilot `noi_dia` + `hang_nang`, chia theo nhân viên với 20 cụm mỗi nhóm, đối chứng chạy cùng thời gian và MDE 6 điểm. Số mẫu hiệu dụng yêu cầu là 859 mỗi nhóm; nhóm chấp nhận power khoảng 0,64 nếu tác động thật chỉ là 5 điểm. Đề xuất cuối trong `ho_so_launch_v0.md` là **Go có điều kiện**.

## 5. Khó khăn và cách xử lý

Khó khăn chính là chi phí mỗi việc thành công không thể tính bằng hóa đơn token chia tổng yêu cầu; phải cộng chi phí xem lại, làm lại và mọi lần chạy lỗi, rồi chia cho số việc thành công. Nhóm cũng phải phân biệt tối ưu chi phí mỗi việc thành công với chi phí cả hệ thống, vì giới hạn một lần chạy có thể rẻ theo một chỉ số nhưng đẩy thêm yêu cầu sang nhân viên. Với thiết kế pilot, 40 nhân viên không đủ mẫu cho mức chênh 5 điểm khi chia theo cụm, nên nhóm ghi rõ đánh đổi và chọn MDE 6 điểm.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp và bằng chứng của từng thành viên nằm trong `TEAM.md` và các báo cáo cá nhân. Người phụ trách từng module phải tự kiểm tra số liệu và giải thích được cách tính trước khi nhóm chốt hồ sơ.

## 7. Hạn chế và hướng cải thiện

Dữ liệu là giả lập và thời gian xem lại/làm lại hiện dựa trên các cột `simulated`, nên cần thay bằng phút đo thật sau tuần đầu pilot. Đợt chạy thử ban đầu chưa có nhóm đối chứng nên không được kết luận tác động nhân quả. Cần hoàn thiện đối soát sổ cái, khóa chống trùng, event có `trace_id`, kiểm tra mẫu hàng tuần và luật dừng trước khi rollout.

## 8. Tài liệu tham khảo

- `README.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `RULES.md`, `SUBMISSION.md`.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- `docs/du_lieu_va_cong_thuc.md`.
- Google PAIR, *People + AI Guidebook*, chương “Errors + Graceful Failure”.
