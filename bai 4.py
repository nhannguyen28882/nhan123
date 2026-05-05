from datetime import datetime, timedelta

# 1. Lấy thời gian hiện tại
now = datetime.now()
print(f"Thời gian hiện tại:  {now.strftime('%H:%M:%S')}")

# 2. Tạo một khoảng thời gian chênh lệch là 5 giây
khoang_cho = timedelta(seconds=5)

# 3. Cộng thêm vào thời gian hiện tại
thoi_gian_moi = now + khoang_cho

print(f"Thời gian sau 5 giây: {thoi_gian_moi.strftime('%H:%M:%S')}")