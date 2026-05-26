import math

# Hàm bổ trợ: Kiểm tra một số có phải là số nguyên tố hay không (Dùng cho bài 2, 3, 4, 5)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# --- BÀI 1 ---
def cau_1():
    print("\n--- Câu 1: In bảng cửu chương ---")
    try:
        input_str = input("Nhập 2 số a, b cách nhau bởi dấu phẩy (vd: 3,5): ")
        a, b = map(int, input_str.split(','))
        
        start = min(a, b)
        end = max(a, b)
        
        for i in range(start, end + 1):
            print(f"Bảng cửu chương {i}:")
            for j in range(1, 11):
                print(f"{i} x {j} = {i * j}")
            print("-" * 15)
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng số_a, số_b")

# --- BÀI 2 ---
def cau_2():
    print("\n--- Câu 2: Kiểm tra số nguyên tố ---")
    n = int(input("Nhập số nguyên dương n: "))
    if is_prime(n):
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")

# --- BÀI 3 ---
def cau_3():
    print("\n--- Câu 3: Liệt kê các số nguyên tố < n ---")
    n = int(input("Nhập số nguyên dương n: "))
    primes = [i for i in range(2, n) if is_prime(i)]
    print(f"Các số nguyên tố nhỏ hơn {n} là: {primes}")

# --- BÀI 4 ---
def cau_4():
    print("\n--- Câu 4: Đếm các số nguyên tố < n ---")
    n = int(input("Nhập số nguyên dương n: "))
    count = sum(1 for i in range(2, n) if is_prime(i))
    print(f"Có {count} số nguyên tố nhỏ hơn {n}.")

# --- BÀI 5 ---
def cau_5():
    print("\n--- Câu 5: Liệt kê các ước số của n là số nguyên tố ---")
    n = int(input("Nhập số nguyên dương n: "))
    prime_divisors = []
    # Tìm các ước số của n
    for i in range(1, n + 1):
        if n % i == 0:
            # Kiểm tra xem ước số đó có là số nguyên tố không
            if is_prime(i):
                prime_divisors.append(i)
    
    print(f"Ví dụ: Nhập n={n}.")
    print(f"Các số vừa là ước số của {n}, vừa là số nguyên tố: {', '.join(map(str, prime_divisors))}")

# --- CHƯƠNG TRÌNH CHÍNH ---
if __name__ == "__main__":
    # Bạn có thể gọi từng hàm để kiểm tra kết quả
    cau_1()
    cau_2()
    cau_3()
    cau_4()
    cau_5()