from datetime import datetime

# 1. Cho nhập chuỗi từ bàn phím (hoặc gán trực tiếp theo đề bài)
# Chuỗi mẫu: Sep 18 2019 2:43PM
chuoi_s = input("Nhập chuỗi ngày tháng (Ví dụ: Sep 18 2019 2:43PM): ")

# 2. Định nghĩa định dạng (format) của chuỗi đầu vào
# %b: Tháng viết tắt (Sep)
# %d: Ngày (18)
# %Y: Năm 4 chữ số (2019)
# %I:%M%p: Giờ (12h):Phút và AM/PM
dinh_dang = "%b %d %Y %I:%M%p"

try:
    # 3. Chuyển đổi chuỗi sang đối tượng datetime
    ngay_chuyen_doi = datetime.strptime(chuoi_s, dinh_dang)

    print("\n--- Kết quả sau khi chuyển đổi ---")
    print(f"Kiểu dữ liệu: {type(ngay_chuyen_doi)}")
    print(f"Giá trị ngày: {ngay_chuyen_doi}")
    
except ValueError:
    print("\nLỗi: Định dạng chuỗi bạn nhập không khớp với mẫu 'Sep 18 2019 2:43PM'")