import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

# Insan sınıfı için örnek nesneler oluşturulması
insan1 = Insan("64615326223", "Renas", "Aktaş", 30, "Erkek", "Türk")
insan2 = Insan("16006080252", "Erva", "Sarıkan", 25, "Kadın", "Türk")

# Insan sınıfı için örnek nesnelerin bilgilerinin yazdırılması
print("Insan 1:")
print(insan1)
print()

print("Insan 2:")
print(insan2)
print()
# Issiz sınıfı için örnek nesneler oluşturulması
issiz1 = Issiz("45621537925 "Ali", "Kara", 35, "Erkek", "Türk", 0)
issiz2 = Issiz("17952684631", "Sudenaz", "Gürcan", 40, "Kadın", "Türk", 3)
issiz3 = Issiz("31695265781", "Mehmet", "Beyaz", 50, "Erkek", "Türk", 6)

# Issiz sınıfı için örnek nesnelerin bilgilerinin yazdırılması
print("Issiz 1:")
print(issiz1)
issiz1.statu_bul()
print(f"Statü: {issiz1.get_statu()}")
print()

print("Issiz 2:")
print(issiz2)
issiz2.statu_bul()
print(f"Statü: {issiz2.get_statu()}")
print()

print("Issiz 3:")
print(issiz3)
issiz3.statu_bul()
print(f"Statü: {issiz3.get_statu()}")
print()
# Calisan sınıfı için örnek nesneler oluşturulması
calisan1 = Calisan("15648965423", "Fatma", "Can", 28, "Kadın", "Türk", "Bilişim", 5000)
calisan2 = Calisan("23072002169", "Ahmet", "Demir", 35, "Erkek", "Türk", "Muhasebe", 6000)

# Calisan sınıfı için örnek nesnelerin bilgilerinin yazdırılması
print("Calisan 1:")
print(calisan1)
print()

print("Calisan 2:")
print(calisan2)
print()


