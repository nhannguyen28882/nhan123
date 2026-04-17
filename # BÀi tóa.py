# Nhập dữ liệu từ bàn phím
dai = float(input("Nhập chiều dài đáy hình chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
so_le = int(input("Số lượng số lẻ cần hiển thị: "))

# Tính toán
dien_tich_day = dai * rong
the_tich = dai * rong * cao

# Định dạng chuỗi để làm tròn theo số chữ số thập phân người dùng yêu cầu
format_str = f"{{:.{so_le}f}}"

# Xuất kết quả
print(f"Diện tích đáy hình chữ nhật = {format_str.format(dien_tich_day)}cm²")
print(f"Thể tích hình khối= {format_str.format(the_tich)}cm³")