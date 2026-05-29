import math

def la_so_nguyen_to(n):
    if n<2:
        return False
    #Kiểm tra từ 2 đến căn bậc 2 của n
    for i in range(2, int (math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        return True
#nhập dữ liệu và tách bằng dấu phẩy
a,b = map(int , input("nhap a, b :").split(','))

#Xác định điểm bắt đầu và kết thúc (để xử lý trường hợp a và b)
bat_dau =min(a,b)
ket_thuc =max(a,b)

for i in range(bat_dau , ket_thuc + 1):
    print ("---bang cuu chuong {i}---")
    for j in range(1,11):
        print (f"{i} x {j} = {i * j}")
        print()
           
n = int (input ("nhap so nguyen duong n :"))
print("cac so nguyen to nho hon n la :")
for i in range(2,n):
    if la_so_nguyen_to(i):
        print(i,end=" ")
        print()
        
n = int(input("nhap so nguyen duong n :"))
print("cac uoc so la so nguyen to cua n la : ", end=" ")
for i in range(1 , n+1):
    #điều kiện : i là ước của n và i là số nguyên tố
    if n % i == 0 and la_so_nguyen_to(i):
        print(i,end=" ")
        print()