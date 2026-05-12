def giai_quyet_bai_20():
    try:
        # 1. Nhập dữ liệu theo phần mở rộng
        a = int(input("Nhập số tiền hàng cần trả (a): "))
        b = int(input("Nhập số tiền khách đưa (b): "))

        # 2. Kiểm tra các trường hợp
        if a > b:
            # Trường hợp thiếu tiền
            print(f"Số tiền khách hàng còn thiếu là {a - b}. Kết thúc chương trình.")
            
        elif a == b:
            # Trường hợp đủ tiền
            print("Cám ơn khách hàng. Hẹn gặp lại.")
            
        else:
            # Trường hợp thừa tiền (a < b) -> Cần thối lại X
            X = b - a
            so_tien_thoi = X # Lưu lại giá trị ban đầu để in
            
            print(f"\nSố tiền cần thối lại là: {so_tien_thoi}")
            print(f"So tien {so_tien_thoi} duoc doi thanh:")

            menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
            tong_so_to = 0
            tong_so_loai = 0

            # Thuật toán đổi tiền
            for loai in menh_gia:
                so_to = X // loai
                X = X % loai
                
                # CHỈ IN NHỮNG LOẠI CÓ SỐ TỜ LỚN HƠN 0
                if so_to > 0:
                    print(f"Loai {loai:>3} gom {so_to} to")
                    tong_so_to += so_to
                    tong_so_loai += 1
            
            # In tổng kết
            print(f"TỔNG CỘNG CÓ {tong_so_to} TỜ")
            print(f"Tong so loai = {tong_so_loai}")
            
            # Nhấn Enter để kết thúc
            input("\nNhấn phím Enter để tiếp tục...")
            print("Cám ơn khách hàng. Hẹn gặp lại.")

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên.")

if __name__ == "__main__":
    giai_quyet_bai_20()