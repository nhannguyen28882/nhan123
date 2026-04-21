from datetime import datetime

# Lấy thời gian hiện tại từ hệ thống
now = datetime.now()

print(f"{'THÔNG TIN CẦN HIỂN THỊ':<40} | {'KẾT QUẢ'}")
print("-" * 60)

# 1. Năm hiện tại
print(f"{'Năm hiện tại':<40} | {now.year}")

# 2. Tháng hiện tại bằng chữ
print(f"{'Tháng hiện tại bằng chữ':<40} | {now.strftime('%B')}")

# 3. Tuần hiện tại là tuần thứ mấy trong năm
print(f"{'Tuần hiện tại là tuần thứ mấy trong năm':<40} | {now.strftime('%U')}")

# 4. Tuần hiện tại là tuần thứ mấy trong tháng
# Công thức: (ngày - 1) // 7 + 1
week_of_month = (now.day - 1) // 7 + 1
print(f"{'Tuần hiện tại là tuần thứ mấy trong tháng':<40} | {week_of_month}")

# 5. Ngày hiện tại là ngày thứ mấy trong năm
print(f"{'Ngày hiện tại là ngày thứ mấy trong năm':<40} | {now.strftime('%j')}")

# 6. Ngày dương lịch hiện tại là ngày
print(f"{'Ngày dương lịch hiện tại là ngày':<40} | {now.day}")

# 7. Thứ của ngày hiện tại
print(f"{'Thứ của ngày hiện tại':<40} | {now.strftime('%A')}")

# 8. Giờ phút giây hiện tại
print(f"{'Giờ phút giây hiện tại':<40} | {now.strftime('%H:%M:%S')}")