def giai_ma_chuoi(cipher_text):
    plain_text = ""
    i = 0
    n = len(cipher_text)
    
    while i < n:
        # Kiểm tra xem có phải bắt đầu cụm nén #nc không
        if cipher_text[i] == '#':
            try:
                # Lấy số lượng (nằm ngay sau dấu #)
                so_luong = int(cipher_text[i+1])
                # Lấy ký tự cần lặp (nằm sau số lượng)
                ky_tu = cipher_text[i+2]
                
                # Thêm ký tự lặp lại vào kết quả
                plain_text += ky_tu * so_luong
                
                # Nhảy qua 3 ký tự đã xử lý (#, số lượng, ký tự)
                i += 3
            except (ValueError, IndexError):
                # Trường hợp lỗi định dạng (ví dụ chuỗi kết thúc bằng #)
                plain_text += cipher_text[i]
                i += 1
        else:
            # Nếu là ký tự bình thường, chỉ việc thêm vào kết quả
            plain_text += cipher_text[i]
            i += 1
            
    return plain_text

# --- Chương trình chính để kiểm tra ---
if __name__ == "__main__":
    # Ví dụ 1 từ đề bài
    cp1 = "XY#6Z1#4023"
    print(f"Cipher text: {cp1}")
    print(f"Plain text:  {giai_ma_chuoi(cp1)}") # Kỳ vọng: XYZZZZZZ1000023
    
    print("-" * 30)
    
    # Ví dụ 2 từ đề bài
    cp2 = "#39+1=1#30"
    print(f"Cipher text: {cp2}")
    print(f"Plain text:  {giai_ma_chuoi(cp2)}") # Kỳ vọng: 999+1=1000
    
    print("-" * 30)
    
    # Cho phép người dùng nhập vào
    nhap = input("Nhập chuỗi cipher text cần khôi phục: ")
    ket_qua = giai_ma_chuoi(nhap)
    print(f"Kết quả plain text: {ket_qua}")