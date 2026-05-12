# Cho phép bạn nhập chuỗi văn bản tùy ý
S = input("Mời bạn nhập chuỗi (S): ")

# Tách chuỗi thành danh sách các từ (dựa vào khoảng trắng)
danh_sach_tu = S.split()

da_gap = set() # Nơi lưu trữ những từ đã duyệt qua
ket_qua = "None" # Mặc định là None nếu không tìm thấy từ lặp

for tu in danh_sach_tu:
    # Nếu từ này đã nằm trong 'da_gap' nghĩa là nó bị lặp lại lần 2
    if tu in da_gap:
        ket_qua = tu
        break # Thoát vòng lặp ngay khi tìm thấy từ lặp đầu tiên
    
    # Nếu chưa gặp thì thêm từ đó vào tập hợp để đánh dấu
    da_gap.add(tu)

# In kết quả
print(f"Từ đầu tiên lặp lại là: {ket_qua}")