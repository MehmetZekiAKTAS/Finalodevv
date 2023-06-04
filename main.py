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

# MaviYaka sınıfı için örnek nesneler oluşturulması
mavi_yaka1 = MaviYaka("56423136987", "Ayşe", "Kara", 32, "Kadın", "Türk", "Üretim", 4500, 200)
mavi_yaka2 = MaviYaka("16022003192", "Mehmet", "Yeşil", 40, "Erkek", "Türk", "Lojistik", 5500, 250)

# MaviYaka sınıfı için örnek nesnelerin bilgilerinin yazdırılması
print("Mavi Yaka 1:")
print(mavi_yaka1)
mavi_yaka1.zam_hakki()
print(f"Yeni Maaş: {mavi_yaka1.get_maas()} TL")
print()

print("Mavi Yaka 2:")
print(mavi_yaka2)
mavi_yaka2.zam_hakki()
print(f"Yeni Maaş: {mavi_yaka2.get_maas()} TL")
print()

# BeyazYaka sınıfı için örnek nesneler oluşturulması
beyaz_yaka1 = BeyazYaka("85426933125", "Ali", "Beyaz", 38, "Erkek", "Türk", "Finans", 8000, 300)
beyaz_yaka2 = BeyazYaka("53403422475", "Fatma", "Can", 42, "Kadın", "Türk", "Pazarlama", 9000, 400)

# BeyazYaka sınıfı için örnek nesnelerin bilgilerinin yazdırılması
print("Beyaz Yaka 1:")
print(beyaz_yaka1)
beyaz_yaka1.zam_hakki()
print(f"Yeni Maaş: {beyaz_yaka1.get_maas()} TL")
print()

print("Beyaz Yaka 2:")
print(beyaz_yaka2)
beyaz_yaka2.zam_hakki()
print(f"Yeni Maaş: {beyaz_yaka2.get_maas()} TL")
print()





