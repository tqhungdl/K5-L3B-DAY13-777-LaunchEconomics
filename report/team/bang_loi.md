# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Thành viên phụ trách gắn nhãn 1 · Người gắn nhãn 2: Le Quoc Khanh (gắn trong 8 phút, không trao đổi trước khi so nhãn). Hai bộ dưới đây phải được xác nhận lại với người đã trực tiếp gắn nhãn; không tự nhận thay việc gắn nhãn độc lập.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = **100%**. Đây là bộ nhãn tham khảo theo hướng dẫn; nhóm phải xác nhận rằng hai bộ nhãn thực tế đã được gắn độc lập trước khi điền tên và nộp bài.

## Quy tắc phân biệt cho các ca không trùng

Trong bộ tham khảo không có ca không trùng. Nếu hai nhãn thực tế khác nhau, giữ nguyên hai nhãn ban đầu, ghi nhãn thống nhất sau khi trao đổi và bổ sung một câu quy tắc cho đúng ca; không sửa ngược bộ nhãn độc lập.

- Ca 6 và 9 là **Do người dùng** vì nguyên nhân gốc là khách chọn sai mục hoặc nhập sai mã; việc trợ lý thiếu gợi ý là khắc phục, không phải nhãn nguyên nhân.
- Ca 13 là **Giới hạn hệ thống** vì yêu cầu nằm ngoài phạm vi/dữ liệu xử lý, dù cách trợ lý trả lời còn kém.
- Ca 8 và 15 là **Hệ thống** vì sai đã lộ ra và có người hoặc hệ thống bắt được; **Ngầm** chỉ dùng khi không ai nhận ra cho tới khi kiểm tra.
- Ca 18 là **Ngữ cảnh** vì phép tính đúng chính sách nhưng cách truyền đạt không khớp kỳ vọng của khách.
- Ca 12 là **Ngầm** vì chi phí bất thường kéo dài mà không ai phát hiện cho tới khi kiểm tra.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi vượt **2% số yêu cầu/ngày** | Nhận diện mã sàn thương mại điện tử và tra sang mã vận đơn; nếu không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: thông báo “đã hoàn” không có bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng **0 ca** | Chỉ báo “đã hoàn” khi sổ cái trả `ok`; sau 3 lỗi 503 thì báo đang xử lý và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hàng tuần tỉ lệ mở lại với lý do số tiền trong các ca kiểm tra thấy phép tính đúng | Tin nhắn luôn ghi cách tính, ví dụ **30.000 đ × 50% = 15.000 đ** | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason=thieu_du_lieu`, tổng hợp theo loại yêu cầu mỗi tuần | Giữ chuyển nhân viên kèm tóm tắt; đưa `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu **100 đơn/tuần** so với bảng giá hiện hành; cảnh báo nếu lệch trên **1%** | Xóa bộ nhớ đệm khi bảng giá đổi và ghi phiên bản bảng giá vào `trace_id` | Kế toán trưởng |
