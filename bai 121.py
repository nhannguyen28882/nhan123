def generate_strobogrammatic(n, total_n, is_extended=False):
    """
    Hàm đệ quy để tạo ra các số strobogrammatic có n chữ số.
    total_n dùng để kiểm tra không cho số 0 đứng đầu.
    """
    # Khai báo các cặp số xoay tương ứng
    if not is_extended:
        # Chuẩn: 0, 1, 8 tự xoay; 6-9 xoay cho nhau
        pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
        middle_digits = ['0', '1', '8']
    else:
        # Mở rộng: Thêm 2 và 5 (tự xoay chính nó theo đề bài 119)
        pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6'), ('2', '2'), ('5', '5')]
        middle_digits = ['0', '1', '8', '2', '5']

    # Trường hợp cơ bản của đệ quy
    if n == 0: return [""]
    if n == 1: return middle_digits

    # Đệ quy lấy danh sách các số có độ dài n-2
    sub_list = generate_strobogrammatic(n - 2, total_n, is_extended)
    res = []

    for s in sub_list:
        for p in pairs:
            # Không được thêm số '0' ở vị trí ngoài cùng (vị trí bắt đầu)
            if n == total_n and p[0] == '0':
                continue
            res.append(p[0] + s + p[1])
    
    return res

def solve_121():
    try:
        n = int(input("Nhập số nguyên n (2 <= n <= 10): "))
        if not (2 <= n <= 10):
            print("Vui lòng nhập n trong khoảng từ 2 đến 10.")
            return
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên.")
        return

    # a. Các số strobogrammatic chuẩn
    res_a = generate_strobogrammatic(n, n, is_extended=False)
    res_a.sort() # Sắp xếp để dễ quan sát
    print(f"\na. Tất cả các số strobogrammatic gồm {n} chữ số:")
    print(", ".join(res_a))
    print(f"--> Tổng cộng có: {len(res_a)} số.")

    # b. Các số strobogrammatic mở rộng
    res_b = generate_strobogrammatic(n, n, is_extended=True)
    res_b.sort()
    print(f"\nb. Tất cả các số strobogrammatic mở rộng gồm {n} chữ số:")
    print(", ".join(res_b))
    print(f"--> Tổng cộng có: {len(res_b)} số.")

if __name__ == "__main__":
    solve_121()