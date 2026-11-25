# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Quang Hưng · Người gắn nhãn 2: Lê Quốc Khánh.

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
| 9 | Hệ thống | Do người dùng | Không | Do người dùng |
| 10 | Giới hạn hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Hệ thống | Ngầm | Không | Ngầm |
| 18 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận ban đầu:** 16 / 20 = **80%**, đạt ngưỡng của lab. Bốn ca khác nhãn là 9, 10, 17 và 18.

## Định nghĩa đã rà soát

| Loại | Quy tắc áp dụng |
| --- | --- |
| Do người dùng | Đầu vào hoặc thao tác của người dùng trực tiếp gây lỗi. |
| Hệ thống | Trợ lý làm sai thiết kế hoặc chính sách, và dấu hiệu sai đã lộ ra trong quá trình xử lý hoặc trong câu trả lời. |
| Ngữ cảnh | Trợ lý làm đúng thiết kế hoặc chính sách, nhưng kết quả hoặc cách trình bày lệch với kỳ vọng hợp lý trong tình huống cụ thể. |
| Giới hạn hệ thống | Trợ lý thiếu dữ liệu, chưa hỗ trợ định dạng đầu vào hoặc gặp yêu cầu ngoài phạm vi xử lý. |
| Ngầm | Kết quả hoặc chi phí sai lệch mà luồng xử lý thông thường không phát hiện, chỉ lộ ra qua kiểm tra hoặc đối soát. |

## Quy tắc phân biệt cho các ca không trùng

- **Ca 9 — Do người dùng.** Đầu vào sai vì khách nhập mã đơn của sàn vào ô mã vận đơn.
- **Ca 10 — Ngữ cảnh.** Trợ lý áp dụng đúng điều khoản bất khả kháng, nhưng cam kết giao trong 24 giờ trên ứng dụng tạo kỳ vọng khách sẽ được hoàn phí.
- **Ca 17 — Ngầm.** Trợ lý dùng bảng giá cũ cho 212 đơn trong 9 ngày và sai lệch không dẫn đến lượt mở lại nào.
- **Ca 18 — Ngữ cảnh.** Hoàn 15.000 đ đúng chính sách, nhưng thiếu cách tính khiến khách tưởng bị hoàn thiếu.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi vượt **2% số yêu cầu/ngày** | Nhận diện mã sàn thương mại điện tử và tra sang mã vận đơn; nếu không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: thông báo “đã hoàn” không có bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng **0 ca** | Chỉ báo “đã hoàn” khi sổ cái trả `ok`; sau 3 lỗi 503 thì báo đang xử lý và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hàng tuần tỉ lệ mở lại với lý do số tiền trong các ca kiểm tra thấy phép tính đúng | Tin nhắn luôn ghi cách tính, ví dụ **30.000 đ × 50% = 15.000 đ** | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason=thieu_du_lieu`, tổng hợp theo loại yêu cầu mỗi tuần | Giữ chuyển nhân viên kèm tóm tắt; đưa `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Đối soát mẫu **100 đơn/tuần** với bảng giá có hiệu lực tại thời điểm xử lý; cảnh báo từ **1 đơn lệch** | Xóa bộ nhớ đệm khi bảng giá đổi và ghi phiên bản bảng giá vào log cùng `trace_id` | Kế toán trưởng |
