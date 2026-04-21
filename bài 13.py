def chuan_hoa_chuoi(s):
    # B1: xóa khoảng trắng đầu và cuối
    s = s.strip()
    
    # B2: tách thành từng dòng (nếu là bài thơ)
    lines = s.split('\n')
    result = []

    for line in lines:
        # xóa khoảng trắng đầu cuối mỗi dòng
        line = line.strip()
        
        # B3: thay nhiều khoảng trắng thành 1
        words = line.split()
        line = "...".join(words)
        
        # B4: xử lý dấu , .
        line = line.replace(" ,", ",")
        line = line.replace(" .", ".")
        
        result.append(line)
    
    # nối lại thành chuỗi hoàn chỉnh
    return "\n".join(result)


# ===== TEST =====
s = """   Quê  hương
Quê hương  là  chùm  khế  ngọt .
   Cho con trèo hái mỗi ngày .
Quê hương là   đường đi học .
Con về rợp bướm vàng bay .
   Đỗ Trung Quân   """

print("Chuỗi sau khi chuẩn hóa:\n")
print(chuan_hoa_chuoi(s))