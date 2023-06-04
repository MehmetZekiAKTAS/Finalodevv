from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, maas)
        self.__tesvik_primi = tesvik_primi


    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        yil = self.get_yaş()
        maas = self.get_maas()
        if yil <= 2:
            zam_orani = self.__tesvik_primi
        elif yil <= 4 and maas < 15000:
            zam_orani = (maas % yil) * 5 + self.__tesvik_primi
        elif maas < 25000:
            zam_orani = (maas % yil) * 4 + self.__tesvik_primi
        else:
            zam_orani = 0

        yeni_maas = maas + (maas * zam_orani) / 100
        if yeni_maas == maas:
            yeni_maas = maas

        self.set_maas(yeni_maas)

    def __str__(self):
        return super().__str__() + f"\nTeşvik Prim: {self.__tesvik_primi}\nYeni Maaş: {self.get_maas()} TL"

