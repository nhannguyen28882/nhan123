# Danh sách các loại tiền
menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Nhập số tiền
x = int(input("Nhap so tien X: "))

tong_to = 0
so_tien_goc = x

print("\nSo tien", so_tien_goc, "duoc doi thanh:")

# Đổi tiền
for tien in menh_gia:
    so_to = x // tien
    x = x % tien
    tong_to += so_to

    print("Loai", tien, "gom", so_to, "to")

print("TONG CONG CO", tong_to, "TO")