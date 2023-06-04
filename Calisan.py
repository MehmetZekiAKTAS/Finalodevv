from Insan import Insan


class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, maas):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        pass

    def __str__(self):
        return super().__str__() + f"\nSektör: {self.__sektor}\nMaaş: {self.__maas} TL"











