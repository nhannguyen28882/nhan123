def is_prime(n):
    """Kiểm tra số nguyên tố."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def rotate_number(n, extended=False):
    """
    Xoay một số 180 độ.
    Nếu số chứa chữ số không xoay được, trả về None.
    """
    s = str(n)
    # Bảng ánh xạ xoay
    mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    if extended:
        # Trong bài này, ví dụ cho thấy 2 và 5 được coi là tự xoay thành chính mình
        mapping.update({'2': '2', '5': '5'})
    
    res = ""
    # Khi xoay 180 độ, thứ tự các chữ số bị đảo ngược và mỗi chữ số được thay thế
    for char in reversed(s):
        if char not in mapping:
            return None
        res += mapping[char]
    
    # Loại bỏ trường hợp số có nhiều chữ số bắt đầu bằng '0' sau khi xoay (ví dụ 60 xoay thành 09 -> 9)
    # Tuy nhiên trong toán học thường giữ nguyên giá trị số.
    return int(res)

def solve():
    limit = 1000000
    
    # Danh sách kết quả cho từng câu
    res_a = []
    res_b = []
    res_c = []
    res_d = []
    res_e = []

    for i in range(limit):
        # Kiểm tra strobogrammatic chuẩn (câu a, b)
        rot_std = rotate_number(i, extended=False)
        is_strobo_std = (rot_std is not None and rot_std == i)
        
        if is_strobo_std:
            res_a.append(i)
            if is_prime(i):
                res_b.append(i)

        # Kiểm tra strobogrammatic mở rộng (câu c, d)
        rot_ext = rotate_number(i, extended=True)
        is_strobo_ext = (rot_ext is not None and rot_ext == i)
        
        if is_strobo_ext:
            res_c.append(i)
            if is_prime(i):
                res_d.append(i)
        
        # Câu e: không phải strobo mở rộng, không phải nguyên tố, nhưng xoay xong là nguyên tố
        if rot_ext is not None: # Phải là số xoay được
            if not is_strobo_ext and not is_prime(i):
                if is_prime(rot_ext):
                    res_e.append(i)

    # In kết quả
    print("a. Các số strobogrammatic nhỏ hơn 1 triệu:")
    print(res_a[:20], "...", f"(Tổng cộng: {len(res_a)} số)")
    
    print("\nb. Các số nguyên tố strobogrammatic nhỏ hơn 1 triệu:")
    print(", ".join(map(str, res_b)))

    print("\nc. Các số strobogrammatic mở rộng nhỏ hơn 1 triệu:")
    print(res_c[:20], "...", f"(Tổng cộng: {len(res_c)} số)")

    print("\nd. Các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1 triệu:")
    print(", ".join(map(str, res_d)))

    print("\ne. Các số không phải strobogrammatic, không phải số nguyên tố, nhưng xoay 180 độ là số nguyên tố:")
    print(res_e[:20], "...")
    print(f"(Tổng cộng tìm được {len(res_e)} số)")

if __name__ == "__main__":
    solve()