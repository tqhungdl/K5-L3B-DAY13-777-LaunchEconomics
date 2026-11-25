# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: Chưa cung cấp · Lớp: L3B

Phạm vi hồ sơ là kế hoạch pilot, không phải phê duyệt chạy chính thức. Các số dựa trên dữ liệu giả lập hoặc cột `_simulated` được đánh dấu **[simulated]**.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ/việc thành công [simulated]**; tổng chi phí **4.373.585 đ**, 978 việc thành công | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi: **+51,8%**; xem lại gấp đôi: **+40,7%**; lương tăng 25%: **+23,1%** | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Cả hệ thống khoảng **5.865 đ/yêu cầu = 0,49×** mức 12.000 đ [simulated]; đã cộng 222 ca chuyển nhân viên | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính **82,83% (994/1.200)**; bỏ qua gợi ý **27,12% (48/177)**; mở lại 7 ngày **4,25% (51/1.200)** | Giả lập | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Phân loại 20 ca lỗi theo 5 loại; bộ tham khảo đạt **20/20 = 100%**; cần xác nhận hai bộ nhãn độc lập thực tế; có event, ngưỡng và vai trò khắc phục | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên **20 + 20**, đối chứng đồng thời; **859** mẫu hiệu dụng mỗi nhóm cho MDE 6 điểm; chấp nhận power khoảng **0,64** nếu tác động thật là 5 điểm | Giả lập | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi lên **6.787 đ [simulated]**; xem lại 100% lên **11.743 đ** hoặc **12.414 đ [simulated]**; cố định tăng **2.370 đ/việc [simulated]** khi giảm nửa khối lượng | Giả lập | PM trợ lý hoàn phí |

## Phạm vi và điều kiện kiểm soát

- Chỉ đưa `noi_dia` và `hang_nang` vào pilot; loại `quoc_te` vì chi phí **22.515 đ = 1,88×** nhân viên tự làm và tỉ lệ thành công **27,3%** [simulated]. `doi_tac` cũng chưa đưa vào vì có điều khoản riêng.
- Trước khi mở rộng, phải sửa khóa chống trùng và đối soát sổ cái, bật đầy đủ event có `trace_id`, và thay các phút `simulated` bằng phút đo thật sau tuần đầu.
- Giám đốc vận hành phải xác nhận chấp nhận đánh đổi MDE 6 điểm; kế hoạch phải có nhóm đối chứng cùng thời gian, phân bổ ngẫu nhiên theo tầng depot và ít nhất 20 cụm mỗi nhóm.
- Phải có kế hoạch giảm xem lại theo bậc; nếu xem lại 100% kéo dài, chi phí gần bằng hoặc cao hơn nhân viên tự làm.

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`. Điều kiện là hoàn thành đối soát sổ cái và khóa chống trùng trước ngày bắt đầu (Kỹ sư trưởng agent), Giám đốc vận hành ký chấp nhận MDE 6 điểm trước ngày bắt đầu, bật event có `trace_id` trước rollout 0,10, thay phút `simulated` bằng phút đo thật sau tuần 1 (PM trợ lý hoàn phí), và chỉ giảm mức xem lại khi dữ liệu an toàn đạt ngưỡng đã viết trước (Trưởng nhóm CSKH).
