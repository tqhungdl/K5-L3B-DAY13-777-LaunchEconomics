# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Phạm vi đề xuất: pilot chỉ gồm `noi_dia` và `hang_nang`. Các số tính từ dữ liệu giả lập hoặc các cột `_simulated` được ghi nhãn `simulated`; chưa được diễn giải như kết quả nhân quả vì đợt chạy thử chưa có nhóm đối chứng.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83% (994/1.200)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Chỉ số trong đợt chạy thử là **27,12% (48/177)** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25% (51/1.200)** |
| Dùng | Tỉ lệ yêu cầu của nhóm can thiệp được mở bằng trợ lý | Số yêu cầu có event `agent_suggestion_shown`, chia tổng số yêu cầu của nhóm can thiệp | Chưa tính; cần event `agent_suggestion_shown` có `arm` và `trace_id` |
| An toàn | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn sai tiền trong `audit_sample_checked`, chia số đơn được kiểm tra | Chưa tính; cần event kiểm tra mẫu có số tiền đúng/sai và `trace_id` |

Không viết “trợ lý đã nâng chỉ số”: đợt chạy thử chưa có nhóm đối chứng. Các giá trị trên là chỉ số quan sát trong đợt chạy thử.

## Danh sách event

Mỗi event đều phải có `trace_id` để nối với trace của agent và các bước xử lý liên quan.

| Event | Ai tạo | Thuộc tính chính | Thời điểm | Chỉ số dùng |
| --- | --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu | Mẫu số của chỉ số chính và phạm vi pilot |
| `agent_run_completed` | Agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lỗi | Chi phí, số lần chạy và lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `arm`, `trace_id` | Khi gợi ý hiện ra | Tỉ lệ sử dụng trợ lý |
| `staff_review_decision` | Nhân viên | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id` | Khi nhân viên giữ, sửa hoặc bỏ gợi ý | Tỉ lệ bỏ qua gợi ý và chi phí xem lại |
| `staff_rework_completed` | Nhân viên | `request_id`, `phut_lam_lai`, `ly_do`, `trace_id` | Khi làm lại xong | Tỉ lệ làm lại và chi phí làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi sổ cái | An toàn tiền và đối soát hoàn tiền |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi chuyển ca cho nhân viên | Tỉ lệ chuyển người và phạm vi ngoài khả năng |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi yêu cầu được đóng | Tử số của chỉ số đóng trong 24 giờ |
| `ticket_reopened` | Khách/hệ thống ticket | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi yêu cầu mở lại | Chỉ số an toàn: mở lại trong 7 ngày |
| `audit_sample_checked` | Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `ket_qua`, `trace_id` | Hằng tuần khi kiểm tra mẫu | Chỉ số an toàn đề xuất và lỗi ngầm |

**Kiểm tra chéo chỉ số – event:** chỉ số chính dùng `refund_request_created`, `ticket_closed`, `ticket_reopened`; chỉ số dùng hiện tại dùng `agent_suggestion_shown` và `staff_review_decision`; chỉ số an toàn hiện tại dùng `ticket_reopened`; chỉ số dùng đề xuất dùng `agent_suggestion_shown`; chỉ số an toàn đề xuất dùng `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Các số dưới đây lấy từ bảng độ nhạy và hướng dẫn lab. Số dựa trên thời gian `_simulated` phải giữ nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **51,8%**, lên **6.787 đ [simulated]** | Tỉ lệ làm lại theo tuần vượt 7% | Thu hẹp về `noi_dia`, rà soát 20 trace làm lại và kiểm tra nguyên nhân | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí là **11.743 đ = 0,98×** nhân viên; nếu làm lại 15,3 phút theo dữ liệu thì **12.414 đ = 1,03× [simulated]** | Tỉ lệ yêu cầu được xem lại vẫn trên 50% ở cuối bước rollout 0,25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15%; không mở rộng nếu chưa đạt | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định tăng từ **1.185 đ/việc** ở 45.000 yêu cầu/tháng lên **2.370 đ/việc** khi còn một nửa [simulated] | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot; rà soát lại phạm vi và chi phí cố định | PM trợ lý hoàn phí |
