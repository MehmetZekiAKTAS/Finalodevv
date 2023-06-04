from Insan import Insan


class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)
        self.__tecrube = tecrube
        self.__statu = ""

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_statu(self):
        return self.__statu

    def set_statu(self, statu):
        self.__statu = statu

    def statu_bul(self):
        yil = self.__tecrube
        mavi_yaka_etkisi = yil * 0.2
        beyaz_yaka_etkisi = yil * 0.35
        yonetici_etkisi = yil * 0.45
        if yil <= 0:
            self.__statu = "Yok"
        elif mavi_yaka_etkisi > beyaz_yaka_etkisi and mavi_yaka_etkisi > yonetici_etkisi:
            self.__statu = "Mavi Yaka"
        elif beyaz_yaka_etkisi > mavi_yaka_etkisi and beyaz_yaka_etkisi > yonetici_etkisi:
            self.__statu = "Beyaz Yaka"
        else:
            self.__statu = "Yönetici"

    def __str__(self):
        return super().__str__() + f"\nTecrübe: {self.__tecrube} yıl\nStatü: {self.__statu}"

