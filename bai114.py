import math

def dao_nguoc_so(n):
    # Chuyển số thành chuỗi, đảo ngược chuỗi rồi chuyển lại thành số
    return int(str(n)[::-1])

def tim_so_than_thien():
    try:
        a = int(input("Nhập số nguyên a (a >= 10): "))
        b = int(input("Nhập số nguyên b (b <= 30000): "))
        
        if not (10 <= a <= b <= 30000):
            print("Vui lòng nhập đúng điều kiện 10 <= a <= b <= 30000")
            return

        ds_than_thien = []
        for i in range(a, b + 1):
            so_dao = dao_nguoc_so(i)
            # Kiểm tra GCD của số đó và số đảo ngược
            if math.gcd(i, so_dao) == 1:
                ds_than_thien.append(i)
        
        print(f"\nCác số thân thiện trong khoảng từ {a} đến {b} là:")
        # In các số cách nhau bởi dấu phẩy
        print(", ".join(map(str, ds_than_thien)))
        print(f"\nSố lượng số thân thiện đã in ra: {len(ds_than_thien)}")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")

# Chạy bài 114
tim_so_than_thien()