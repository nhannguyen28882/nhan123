import math

# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# --- 1. Nhập dữ liệu ---
L = []
while True:
    try:
        num = int(input("Nhập một số nguyên: "))
        L.append(num)
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")
        continue
    
    # Hỏi người dùng có muốn tiếp tục không
    choice = input("Bạn có muốn nhập nữa hay không? (Yes/No): ").strip().lower()
    if choice in ['n', 'no']:
        break

if not L:
    print("Danh sách rỗng.")
else:
    print("\n--- KẾT QUẢ ---")
    print(f"Danh sách đã nhập: {L}")

    # a) In ra các số nguyên tố có trong list
    primes = [x for x in L if la_so_nguyen_to(x)]
    print(f"a) Các số nguyên tố trong list: {primes}")

    # b) Tính trung bình cộng các số âm, trung bình các số dương
    so_am = [x for x in L if x < 0]
    so_duong = [x for x in L if x > 0]
    
    tbc_am = sum(so_am) / len(so_am) if so_am else 0
    tbc_duong = sum(so_duong) / len(so_duong) if so_duong else 0
    
    print(f"b) Trung bình cộng số âm: {tbc_am}")
    print(f"   Trung bình cộng số dương: {tbc_duong}")

    # c) Số lớn nhất, số nhỏ nhất
    print(f"c) Số lớn nhất: {max(L)}")
    print(f"   Số nhỏ nhất: {min(L)}")

    # d) Cho biết các số trong list có được sắp xếp tăng dần hay chưa?
    is_sorted = (L == sorted(L))
    if is_sorted:
        print("d) Danh sách ĐÃ được sắp xếp tăng dần.")
    else:
        print("d) Danh sách CHƯA được sắp xếp tăng dần.")
        