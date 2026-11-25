# Báo cáo cá nhân — Trần Quang Hưng (2A202603767)

## 1. Thông tin thành viên

- Họ tên: Trần Quang Hưng
- MSSV: 2A202603767
- Email: tqhungdl26@gmail.com
- Vai trong nhóm: Người gắn nhãn 1, phụ trách nhiệm vụ C và D.

## 2. Phần việc phụ trách

- **C:** Gắn nhãn 20 ca lỗi, đối chiếu với người gắn nhãn 2 và hoàn thiện bảng khắc phục.
- **D:** Hoàn thiện phần tính cỡ mẫu D1, trả lời năm câu D2 và điền kế hoạch pilot D3.

## 3. Đóng góp cụ thể

- **C:** Gắn nhãn theo nguyên nhân gốc và đối chiếu với bộ nhãn của Lê Quốc Khánh. Hai bộ nhãn trùng 16/20 ca (80%). Báo cáo giải thích bốn ca khác nhãn (9, 10, 17, 18) và đề xuất cách phát hiện, cách khắc phục cùng vai trò phụ trách cho một ca ở mỗi loại lỗi.
- **D:** Hoàn thiện phép tính cho ba cách chia nhóm theo yêu cầu, nhân viên và depot. Kế hoạch chọn chia ngẫu nhiên theo nhân viên, phân tầng theo depot, với 20 người mỗi nhóm. Chấp nhận mức chênh tối thiểu phát hiện được là 6 điểm phần trăm và cần ít nhất 299 yêu cầu mỗi nhân viên.
- **D:** Đối chiếu tỉ lệ mở lại trong 7 ngày trên dữ liệu giả lập: 51/1.200 (4,25%) toàn mẫu và 39/982 (3,97%) trong phạm vi pilot. Kế hoạch có ba luật dừng về an toàn, chi phí và mức sử dụng, cùng quy trình tắt trợ lý và chuyển về nhân viên xử lý.

## 4. Bằng chứng

- [Bảng lỗi và cách khắc phục](bang_loi.md) ghi hai bộ nhãn, tỉ lệ đồng thuận và bảng khắc phục năm ca.
- [Mã tính D1 và D3](../../src/lab13.py) in cỡ mẫu theo từng phương án và tỉ lệ mở lại trong 7 ngày.
- [Kế hoạch pilot](pilot_plan.yaml) ghi kết quả D1, năm câu trả lời D2, cách chia nhóm và ba luật dừng.

## 5. Công cụ AI đã dùng

- Dùng ChatGPT (Codex) để hỗ trợ soạn báo cáo C, viết mã tính cỡ mẫu D1, tính tỉ lệ mở lại từ CSV và rà soát kế hoạch D.
- Kiểm tra bằng cách đối chiếu hai cột nhãn theo từng ca và đếm lại 16 dòng trùng. Chạy toàn bộ `lab13.py`, đối chiếu kết quả với công thức trong tài liệu lab và dùng `yaml.safe_load` để kiểm tra kế hoạch pilot.

## 6. Tự đánh giá

Tôi cần tiếp tục luyện phân biệt lỗi hệ thống với lỗi ngầm. Ca 17 giúp tôi thấy cách đối soát có thể phát hiện sai lệch kéo dài dù khách không mở lại yêu cầu. Với D, tôi hiểu vì sao số nhân viên giới hạn cỡ mẫu hiệu dụng và vì sao kế hoạch chọn mức 6 điểm phần trăm.
