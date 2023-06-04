from Insan import Insan


class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)
        self.__tecrube = tecrube
        self.__statu = ""
