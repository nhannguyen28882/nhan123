import math

# Trị tuyệt đối của n
tri_tuyet_doi = lambda n: abs(n)
print(f"Trị tuyệt đối của -5 là: {tri_tuyet_doi(-5)}")

# Kiểm tra n có là bội của 13 hoặc 19 không
la_boi_so = lambda n:(
     "đúng" if (n % 13 == 0 or n % 19 == 0) else "sai")
print(f"26 có là bội của 13 hoặc 19? {la_boi_so(26)}")

# Kiểm tra là tam giác gì
kiem_tra_tam_giac = lambda a, b, c: (
    "Không phải tam giác" if not (a+b > c and a+c > b and b+c > a) else
    "Tam giác đều" if a == b == c else
    "Tam giác cân" if a == b or b == c or a == c else
    "Tam giác vuông" if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) else
    "Tam giác thường"
)
print(f"Bộ ba (3, 4, 5) là: {kiem_tra_tam_giac(3, 4, 5)}")
print(f"Bộ ba (3, 3, 3) là: {kiem_tra_tam_giac(3, 3, 3)}")