# nesne yönelimli programlama gerçek dünyadaki nesene ve yapıları kod içinde tanımlama ve kullanmamızı sağlayan bir yazılım geliştirme tekniğidir.
# sınıf(class): gerçek dünyadaki tanımlamak istediğim nesne veya kavramların şablonudur.
# nesne(object): sınıftan türetilen her bir sınıf şablonundan oluşturulmuş yazılım öğesi.
# bir fonksiyon sınıf(class) içinde tanımlanrsa adı metot olur.
#sınıf tanımalaması
class Insan():
    def __init__(self): #nesne türetilirken ilk çalışan metot       
        self.ad=""
        self.soyad=""
        self.boy=1.0
        self.cinsiyet=""
        self.goz_rengi=""
        self.kilo=float()#0.0
        print("yapıcı çalıştı")

    def yemek_ye(self,miktar):
        self.kilo+=miktar/1000
    def spor_yap(self,sure):
        self.kilo-=sure/3600

#nesne türetme
insan1=Insan()
insan2=Insan()
insan3=Insan()
ali=Insan()
insan1.ad="ali"
insan1.soyad="gül"
insan1.boy=1.74
insan1.goz_rengi="siyah"
insan1.kilo=80
print(insan1.ad)
print(insan1.boy)
print(insan1.soyad)
print(insan1.goz_rengi)
# print(Insan.ad) sınıf nesene özelliklerine/değişkenleirne ulaşamaz
insan1.yemek_ye(2000)
print(insan1.kilo)
insan1.spor_yap(5000)
print(insan1.kilo)