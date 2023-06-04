from Insan import Insan


class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, maas):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__maas = maas

