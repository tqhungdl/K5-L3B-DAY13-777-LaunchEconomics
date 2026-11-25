# Báo cáo cá nhân — Le Quoc Khanh

## 1. Thông tin thành viên

- Họ tên: Lê Quốc Khánh
- MSSV: 2A202603742
- Email: lqkhanh0@gmail.com
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ / phụ trách module C và E

## 2. Phần việc phụ trách

Phụ trách nhiệm vụ C và E cùng phần tổng hợp hồ sơ: gắn nhãn độc lập 20 ca lỗi theo Google PAIR, đặc tả chỉ số, thiết kế danh sách event có `trace_id`, phân tích rủi ro kinh tế, hoàn thiện `ho_so_launch_v0.md`, cập nhật `group_report.md` và kiểm tra tính nhất quán của đề xuất cuối với các kết quả A–D.

## 3. Đóng góp cụ thể

- Hoàn thiện `report/team/bang_loi.md` với hai bộ nhãn độc lập cho 20 ca, tỉ lệ đồng thuận, quy tắc phân biệt và bảng khắc phục đủ 5 loại lỗi. Bộ nhãn tham khảo hiện đạt 20/20 = 100%; cần xác nhận lại với người gắn nhãn 1 trước khi nộp.
- Hoàn thiện `report/team/chi_so.md` với ba chỉ số tính thử, hai chỉ số đề xuất, danh sách event và ánh xạ event–chỉ số.
- Hoàn thiện `report/team/ho_so_launch_v0.md` gồm bảy mục, trạng thái, con số chính, vai trò phụ trách và đề xuất **Go có điều kiện**.
- Cập nhật `report/team/group_report.md` với mục tiêu, phương pháp, kết quả, hạn chế và hướng cải thiện.
- Tổng hợp các rủi ro kinh tế từ bảng độ nhạy: làm lại tăng gấp đôi, xem lại 100% và khối lượng giảm.
- Giữ nhãn `[simulated]` cho các số dựa trên dữ liệu giả lập hoặc cột `_simulated`, không diễn giải đợt chạy thử thành bằng chứng nhân quả.

## 4. Bằng chứng

- `report/team/chi_so.md`
- `report/team/ho_so_launch_v0.md`
- `report/team/group_report.md`
- Nhánh làm việc: `lequockhanh`

Các số chính được đối chiếu với `CHECKPOINTS.md`, `RUBRIC.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. Trước khi nộp cần điền MSSV, email, tên nhóm và cập nhật tên các vai trò thực tế trong `TEAM.md`.

## 5. Công cụ AI đã dùng

Dùng trợ lý AI để đọc và đối chiếu các file Markdown, gợi ý cấu trúc phân công và rà soát các yêu cầu của phần C và E. Tôi tự kiểm tra bằng cách đối chiếu số liệu với `bang_chi_phi.md`, `pilot_plan.yaml`, `CHECKPOINTS.md`, `RUBRIC.md`, kiểm tra các event đều có `trace_id`, số giả lập có nhãn và bảng lỗi đủ 20 ca trước khi ghi nhận đồng thuận.

## 6. Tự đánh giá

Đã hoàn thiện phần gán nhãn C, chỉ số, event, rủi ro và hồ sơ tổng hợp. Cần phối hợp với các thành viên để điền thông tin nhóm, xác nhận hai bộ nhãn thực tế đã được gắn độc lập, xác nhận số cuối từ code, kiểm tra `pilot_plan.yaml` và chạy checklist trước khi commit/push.
