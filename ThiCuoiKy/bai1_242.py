#Nhập thông tin ( chiều dài,rộng,cao và số lẻ cần hiện)
chieu_dai = float(input("Nhập chiều dài đáy HCN :"))
chieu_rong = float(input("Nhập chiều rộng HCN :"))
chieu_cao = float(input("Nhập chiều cao HCN :"))
so_le = int(input("Số Lượng số lẻ cần hiển thị là : "))

#Tính diện tích và thẻ tích
dien_tich = chieu_dai * chieu_rong
the_tich = dien_tich * chieu_cao

#số mũ sử dụng bảng UNICODE
mu_2 = "\u00b2"
mu_3 = "\u00b3"

print(f" Diện tích đáy hình chữ nhật = {dien_tich:.{so_le}f}cm{mu_2}")
print(f"Thể tích HCN là : {the_tich:.{so_le}f}cm{mu_3}")