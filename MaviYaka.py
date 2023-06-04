from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, maas)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        yil = self.get_yaş()
        maas = self.get_maas()
        if yil <= 2:
            zam_orani = self.__yipranma_payi * 10
        elif yil <= 4 and maas < 15000:
            zam_orani = (maas % yil) / 2 + self.__yipranma_payi * 10
        elif maas < 25000:
            zam_orani = (maas % yil) / 3 + self.__yipranma_payi * 10
        else:
            zam_orani = 0

        yeni_maas = maas + (maas * zam_orani) / 100
        if yeni_maas == maas:
            yeni_maas = maas

        self.set_maas(yeni_maas)

    def __str__(self):
        return super().__str__() + f"\nYıpranma Payı: {self.__yipranma_payi}\nYeni Maaş: {self.get_maas()} TL"


