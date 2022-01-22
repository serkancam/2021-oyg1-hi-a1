# veri_gizleme_soyutlama.py
class Araba():
    def __init__(self):
        self.__renk="-"
        self.__marka="-"
        self.__model=1983
        self.__hiz=190
        self.__vites=5
    def hiz_ayarla(self,deger):
        if deger>100 and deger<350:
            self.__hiz=deger
    def hiz_bilgisi(self):
        return self.__hiz
    def vites_ayarla(self,vites):
        if vites>=4 and vites<=7:
            self.__vites=vites
    def vites_bilgisi(self):
        return self.__vites
    def model_ayarla(self,model):
        if model>=1983 and model<=2021:
            self.__model=model
    def model_bilgisi(self):
        return self.__model

a1 = Araba()
a2 = Araba()
a3 = Araba()
a1.hiz_ayarla(300)
a2.hiz_ayarla(-100)
a3.hiz_ayarla(200)
print(a1.hiz_bilgisi())
print(a2.hiz_bilgisi())
print(a3.hiz_bilgisi())