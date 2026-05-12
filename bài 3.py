# Cho phép bạn nhập số điện thoại tùy ý từ bàn phím
S = input("Mời bạn nhập số điện thoại (S): ")

# Tạo tập hợp chứa đầy đủ các ký số từ '0' đến '9'
tat_ca_so = set("0123456789")

# Tạo tập hợp các ký số có mặt trong chuỗi bạn vừa nhập
so_da_nhap = set(S)

# Tìm các số không xuất hiện bằng cách lấy (Tất cả) trừ đi (Số đã nhập)
# Sau đó chuyển về list và sắp xếp theo thứ tự tăng dần
ket_qua = sorted(list(tat_ca_so - so_da_nhap))

# In kết quả ra màn hình
print(f"Trong số điện thoại {S} không chứa các ký số: {ket_qua}")