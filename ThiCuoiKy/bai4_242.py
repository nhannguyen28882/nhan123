# Số đồng nhất: k > 0 và các chữ số giống nhau
check_dong_nhat_all = lambda k: k > 0 and all(d == str(k)[0] for d in str(k))

# Dùng any để kiểm tra nếu có bất kỳ chữ số nào khác với chữ số đầu tiên thì trả về False
check_dong_nhat_any = lambda k: k > 0 and not any(d != str(k)[0] for d in str(k))

# Số hoàn thiện: tổng các ước nhỏ hơn n bằng chính nó
check_so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

print("--- KIỂM TRA SỐ BẤT KỲ ---")
so_nhap = int(input("Nhập một số nguyên để kiểm tra: "))

# Kiểm tra đồng nhất
if check_dong_nhat_all(so_nhap):
    print(f"-> {so_nhap} là số ĐỒNG NHẤT.")
else:
    print(f"-> {so_nhap} KHÔNG PHẢI số đồng nhất.")

# Kiểm tra số hoàn thiện
if check_so_hoan_thien(so_nhap):
    print(f"-> {so_nhap} là số HOÀN THIỆN.")
else:
    print(f"-> {so_nhap} KHÔNG PHẢI số hoàn thiện.")

#Liệt kê các số thỏa mãn từ 1 đến 10000
print("\n" + "="*30)
print("DANH SÁCH CÁC SỐ THỎA MÃN TỪ 1 ĐẾN 10000")

print("\n1. Các số đồng nhất:")
for i in range(1, 10001):
    if check_dong_nhat_all(i):
        print(i, end=" ")

print("\n\n2. Các số hoàn thiện:")
for i in range(1, 10001):
    if check_so_hoan_thien(i):
        print(i, end=" ")
print()