import math

# ==============================================================================
# HÀM HỖ TRỢ
# ==============================================================================

# Tổng ước thực sự (không tính chính nó)
def sum_proper_divisors(n):
    if n <= 1:
        return 0

    total = 1
    sqrt_n = int(math.sqrt(n))

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i

            other = n // i

            if other != i:
                total += other

    return total


# ==============================================================================
# ĐỊNH NGHĨA CÁC HÀM LAMBDA
# ==============================================================================

# a) Số thân thiện
is_friendly = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

# b) Số chính phương
is_square = lambda n: math.isqrt(n) ** 2 == n

# c) Số đồng nhất
is_repdigit_all = lambda n: all(d == str(n)[0] for d in str(n))
is_repdigit_any = lambda n: not any(d != str(n)[0] for d in str(n))

# d) Số hoàn thiện
is_perfect = lambda n: n > 1 and sum_proper_divisors(n) == n

# e) Số phong phú
is_abundant = lambda n: n > 1 and sum_proper_divisors(n) > n

# f) Số tăng dần (không giảm)
is_increasing = lambda n: (
    lambda s: all(s[i] <= s[i + 1] for i in range(len(s) - 1))
)(str(n))

# g) Số Armstrong
is_armstrong = lambda n: (
    lambda s: sum(int(d) ** len(s) for d in s) == n
)(str(n))

# h) Số nguyên tố
is_prime_c1 = lambda n: len([i for i in range(1, n + 1) if n % i == 0]) == 2

is_prime_c2 = lambda n: (
    sum(i for i in range(1, n + 1) if n % i == 0) == n + 1
)

is_prime_c3 = lambda n: (
    n > 1 and
    not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))
)

# Hàm F dùng filter
def F(k):
    return len(list(filter(lambda x: k % x == 0, range(1, k + 1)))) == 2

# i) Số palindrome
is_palindrome = lambda n: str(n) == str(n)[::-1]

# j) Số nguyên tố palindrome
is_prime_palin = lambda n: (
    str(n) == str(n)[::-1]
    and
    n > 1
    and
    not any(n % i == 0 for i in range(2, int(math.sqrt(n)) + 1))
)

# k) Số lộc phát
is_loc_phat_all = lambda n: all(d in "68" for d in str(n))

is_loc_phat_count = lambda n: (
    str(n).count("6") + str(n).count("8") == len(str(n))
)

# l) Số lộc phát palindrome
is_loc_phat_palin = lambda n: (
    all(d in "68" for d in str(n))
    and
    str(n) == str(n)[::-1]
)


# ==============================================================================
# DICTIONARY QUẢN LÝ CÁC LOẠI SỐ
# ==============================================================================

number_types = {
    "a) Số thân thiện": is_friendly,
    "b) Số chính phương": is_square,
    "c) Số đồng nhất": is_repdigit_all,
    "d) Số hoàn thiện": is_perfect,
    "e) Số phong phú": is_abundant,
    "f) Số tăng dần": is_increasing,
    "g) Số Armstrong": is_armstrong,
    "h) Số nguyên tố": is_prime_c3,
    "i) Số Palindrome": is_palindrome,
    "j) Số nguyên tố Palindrome": is_prime_palin,
    "k) Số lộc phát": is_loc_phat_all,
    "l) Số lộc phát Palindrome": is_loc_phat_palin
}


# ==============================================================================
# HÀM IN KẾT QUẢ
# ==============================================================================

def print_result_list(title, result, limit=50):
    if len(result) > limit:
        print(f"{title}: {result[:limit]} ...")
        print(f"   -> Tổng cộng: {len(result)} số")
    else:
        print(f"{title}: {result}")


# ==============================================================================
# KIỂM TRA 1 SỐ
# ==============================================================================

def check_single_number():
    try:
        num = int(input("Nhập số cần kiểm tra: "))

        if num < 0:
            print("Vui lòng nhập số nguyên không âm!")
            return

        print(f"\n===== KẾT QUẢ CHO SỐ {num} =====")

        for name, func in number_types.items():
            print(f"{name}: {func(num)}")

        print(f"Hàm F kiểm tra nguyên tố: {F(num)}")

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")


# ==============================================================================
# KIỂM TRA TRONG KHOẢNG
# ==============================================================================

def check_range():
    try:
        start = int(input("Từ số: "))
        end = int(input("Đến số: "))

        # Hoán đổi nếu nhập ngược
        if start > end:
            start, end = end, start

        if start < 0:
            print("Vui lòng nhập số không âm!")
            return

        print(f"\n===== KIỂM TRA TỪ {start} ĐẾN {end} =====")

        for name, func in number_types.items():
            result = [i for i in range(start, end + 1) if func(i)]
            print_result_list(name, result)

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")


# ==============================================================================
# MENU CHÍNH
# ==============================================================================

def main():
    print("==========================================")
    print(" CHƯƠNG TRÌNH KIỂM TRA CÁC LOẠI SỐ ")
    print("==========================================")

    print("1. Kiểm tra 1 số")
    print("2. Kiểm tra trong khoảng")

    choice = input("Lựa chọn của bạn (1/2): ")

    if choice == "1":
        check_single_number()

    elif choice == "2":
        check_range()

    else:
        print("Lựa chọn không hợp lệ!")


# ==============================================================================
# CHẠY CHƯƠNG TRÌNH
# ==============================================================================

main()

print("\n===== HOÀN THÀNH =====")