import json
import os
import re

def thuc_hanh_nen_theo_huong_2():
    file_goc = 'fileName.txt'
    file_nen = 'file_nen_huong2.txt'

    # --- BƯỚC 0: TẠO FILE GỐC (Nội dung giống hệt trong ảnh) ---
    noi_dung_tho = """Thuyền và biển
Chỉ có thuyền mới hiểu
Biển mênh mông nhường nào
Chỉ có biển mới biết
Thuyền đi đâu về đâu"""

    with open(file_goc, 'w', encoding='utf-8') as f:
        f.write(noi_dung_tho)

    # --- BƯỚC 1: NÉN (Theo gợi ý Hướng 2) ---
    with open(file_goc, 'r', encoding='utf-8') as f:
        van_ban = f.read()

    # Sử dụng Regex để tách từ nhưng GIỮ LẠI dấu xuống dòng (\n) 
    # để đảm bảo "trả về định dạng ban đầu"
    tokens = re.findall(r'\S+|\n', van_ban)

    # Dictionary lưu trữ vị trí xuất hiện của từng từ: { "từ": [vị trí 1, vị trí 2...] }
    tu_dien_vi_tri = {}
    for index, word in enumerate(tokens):
        if word not in tu_dien_vi_tri:
            tu_dien_vi_tri[word] = []
        tu_dien_vi_tri[word].append(index)

    # Xuất ra file mới (giảm dung lượng cho văn bản lớn)
    with open(file_nen, 'w', encoding='utf-8') as f:
        json.dump(tu_dien_vi_tri, f, ensure_ascii=False)

    print(f"(1) Đã xuất ra file nén: {file_nen}")
    print(f"    Dung lượng gốc: {os.path.getsize(file_goc)} bytes")
    print(f"    Dung lượng sau nén: {os.path.getsize(file_nen)} bytes")


    # --- BƯỚC 2: GIẢI NÉN (Trả về định dạng ban đầu) ---
    with open(file_nen, 'r', encoding='utf-8') as f:
        data_da_nen = json.load(f)

    # Tìm tổng số lượng từ/ký tự xuống dòng để tạo mảng khôi phục
    tong_so_luong = sum(len(v) for v in data_da_nen.values())
    mang_khoi_phuc = [None] * tong_so_luong

    # Đặt các từ vào đúng vị trí đã lưu trữ
    for word, positions in data_da_nen.items():
        for pos in positions:
            mang_khoi_phuc[pos] = word

    # Ghép lại thành văn bản (Xử lý thông minh để dấu xuống dòng không bị dư khoảng trắng)
    van_ban_goc = ""
    for i, token in enumerate(mang_khoi_phuc):
        if token == '\n':
            van_ban_goc += token
        else:
            # Thêm khoảng trắng nếu từ tiếp theo không phải là xuống dòng
            tiep_theo_la_xuong_dong = (i + 1 < len(mang_khoi_phuc) and mang_khoi_phuc[i+1] == '\n')
            la_tu_cuoi_cung = (i == len(mang_khoi_phuc) - 1)
            
            van_ban_goc += token
            if not tiep_theo_la_xuong_dong and not la_tu_cuoi_cung:
                van_ban_goc += " "

    print("\n(2) Nội dung file sau khi khôi phục định dạng ban đầu:")
    print("-" * 35)
    print(van_ban_goc)
    print("-" * 35)

if __name__ == "__main__":
    thuc_hanh_nen_theo_huong_2()