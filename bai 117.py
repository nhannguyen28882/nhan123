def tinh_tong_binh_phuong_so_con():
    # Bước 1: Nhập số nguyên dương n từ bàn phím (nhập dưới dạng chuỗi)
    n_str = input("Nhập số nguyên dương n: ")
    
    # Kiểm tra tính hợp lệ của đầu vào
    if not n_str.isdigit() or int(n_str) <= 0:
        print("Vui lòng nhập một số nguyên dương!")
        return

    tong_S = 0
    bieu_thuc_mo_phong = [] # Dùng để in ra các bước tính giống ví dụ
    do_dai_n = len(n_str)

    # Bước 2: Tìm tất cả "số con" theo thứ tự độ dài giảm dần (giống ví dụ trong đề)
    # i là độ dài của số con (từ độ dài lớn nhất n đến 1)
    for length in range(do_dai_n, 0, -1):
        # j là vị trí bắt đầu cắt chuỗi con
        for j in range(do_dai_n - length + 1):
            sub_str = n_str[j : j + length] # Cắt chuỗi con
            
            # Lưu lại để in biểu thức giống ví dụ
            bieu_thuc_mo_phong.append(f"{sub_str}^2")
            
            # Chuyển chuỗi con thành số (ví dụ "07" thành 7) và cộng bình phương vào tổng
            tong_S += int(sub_str)**2

    # Bước 3: In kết quả ra màn hình
    print(f"\nVới n = {n_str}:")
    # Nối các phần tử bình phương lại bằng dấu '+' để hiển thị giống ví dụ
    print(f"S = {' + '.join(bieu_thuc_mo_phong)}")
    print(f"Kết quả cuối cùng: S = {tong_S}")

# Chạy chương trình
if __name__ == "__main__":
    tinh_tong_binh_phuong_so_con()