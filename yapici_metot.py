class Personel():
    def __init__(self,ad="-",soyad="-",yas=0,maas=500,gorev="-"):
        self.ad=ad
        self.soyad=soyad
        self.yas=int(yas)
        self.maas=float(maas)
        self.gorev=gorev


#programın kendisi
ad1=input("ad giriniz:")

ayse=Personel(ad1,"gül",28,6300.0,"müdür")
ali=Personel(ad="ali",soyad="kan",yas=38,maas=10300.0,gorev="genel müdür")
mesut=Personel()
mesut.yas=-20


print(ali.ad,ali.maas)
print(ayse.ad,ayse.gorev)
print(mesut.maas)
print(mesut.gorev)
print(mesut.yas)