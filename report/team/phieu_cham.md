# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): ...
- Nhóm được chấm: ...

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Nêu chi phí xem lại 100% có thể vượt **12.000 đ/việc thành công** (`simulated`) và yêu cầu có kế hoạch giảm xem lại theo kết quả an toàn. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 5 | Chỉ pilot `noi_dia` và `hang_nang`, có lý do bằng số. Một số kết quả độ nhạy, như mức tăng **51,8%** khi làm lại gấp đôi, thiếu nhãn `simulated` tại mục trình bày. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Có đối chứng, **20 cụm mỗi nhóm**, mục tiêu **859 mẫu hiệu dụng mỗi nhóm** cho mức chênh 6 điểm phần trăm, và luật dừng có ngưỡng, thời hạn, người có quyền dừng. |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Chỉ pilot `noi_dia` và `hang_nang`. Xem lại 100% có thể tốn **12.415 đ/việc thành công** (`simulated`), vượt mức **12.000 đ** khi nhân viên tự làm.
Trước khi bắt đầu, cần sửa chống hoàn trùng, đối soát sổ cái và được Giám đốc vận hành chấp thuận mức chênh tối thiểu **6 điểm phần trăm**.

**Một câu hỏi cho đội trình:** Nhóm bạn báo chi phí mỗi việc thành công là bao nhiêu? Nếu cộng chi phí cho các yêu cầu `chuyen_nhan_vien`, chi phí cả hệ thống trên mỗi yêu cầu là bao nhiêu? Nhóm đang tối ưu chi phí mỗi việc thành công hay chi phí toàn hệ thống?

**Câu trả lời của đội trình (ghi lại tại buổi):**

1. Chi phí là **4.472 đ/việc thành công** (`simulated`). Tính mọi lượt chạy, kể cả lượt lỗi, cộng tiền xem lại và làm lại rồi chia cho **978 việc thành công**. Mức này gấp **16,3 lần** hóa đơn token và tool bình quân (**274,7 đ/yêu cầu**).
2. Cộng **148** ca `chuyen_nhan_vien` với **12.000 đ/ca** cho **5.125 đ/yêu cầu**. Nếu tính đủ **222** ca không thành công (gồm **74** ca làm lại), chi phí cả hệ thống là **(4.373.585 + 222 × 12.000) / 1.200 ≈ 5.865 đ/yêu cầu**, bằng **0,49×** mức nhân viên tự làm (cả hai mức chi phí là `simulated`).
3. Nhóm tối ưu **chi phí toàn hệ thống**. Giới hạn **2 lượt** rẻ nhất cho hệ thống (**6.901.220 đ**). Giới hạn **1 lượt** rẻ nhất theo chi phí mỗi việc thành công (**4.111 đ**) và đẩy thêm **85** ca sang nhân viên, làm tổng chi phí tăng lên **7.449.781 đ** (chi phí `simulated`).
