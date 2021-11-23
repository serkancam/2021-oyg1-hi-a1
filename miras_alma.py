import datetime
class UlasimAraci():
    def __init__(self, marka,yili,hizi,renk):
        self.marka=marka
        self.yili=yili
        self.hizi=hizi
        self.renk=renk
    def yasi_kac(self):
        yas = datetime.date.today().year - self.yili
        return yas


class KaraAraci(UlasimAraci):
    def __init__(self,marka,yili,hizi,renk,tekerlek_sayisi,yakit_turu):
        super().__init__(marka,yili,hizi,renk)
        self.tekelek_sayisi=tekerlek_sayisi
        self.yakit_turu=yakit_turu

class HavaAraci(UlasimAraci):
    def __init__(self, marka, yili, hizi, renk,kanat_sayisi,model):
        super().__init__(marka, yili, hizi, renk)
        self.kanat_sayisi=kanat_sayisi
        self.model=model

class SuAraci(UlasimAraci):
    pass


arac2=KaraAraci("Mercedes",2014,285,"siyah",4,"dizel")


print(arac2.yasi_kac())

arac1=UlasimAraci("ford",2018,310,"mavi")
# arac2=UlasimAraci("ford",2018,310,"mavi")
# arac3=UlasimAraci("ford",2018,310,"mavi")
# arac4=UlasimAraci("ford",2018,310,"mavi")
# arac5=UlasimAraci("ford",2018,310,"mavi")
# arac6=UlasimAraci("ford",2018,310,"mavi")
# arac7=UlasimAraci("ford",2018,310,"mavi")
# arac8=UlasimAraci("ford",2018,310,"mavi")