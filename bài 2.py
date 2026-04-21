from datetime import date

print("--- Nhập thông tin cho ngày thứ nhất ---")
d1 = int(input("Nhập ngày: "))
m1 = int(input("Nhập tháng: "))
y1 = int(input("Nhập năm: "))

print("\n--- Nhập thông tin cho ngày thứ hai ---")
d2 = int(input("Nhập ngày: "))
m2 = int(input("Nhập tháng: "))
y2 = int(input("Nhập năm: "))

# Tạo đối tượng date cho 2 mốc thời gian
ngay_1 = date(y1, m1, d1)
ngay_2 = date(y2, m2, d2)

# Tính toán sự chênh lệch
# Dùng hàm abs() để đảm bảo kết quả luôn dương dù bạn nhập ngày nào trước
khoang_cach = abs((ngay_2 - ngay_1).days)

print(f"\n=> Số ngày cách nhau giữa hai ngày là: {khoang_cach} ngày.")