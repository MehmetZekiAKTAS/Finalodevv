from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, maas)
        self.__tesvik_primi = tesvik_primi

