class Kisi():
    def __init__(self,ad:str,soyad:str,yas:int):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
    def kayit(self,adres):
        dosya=open(adres,"a",encoding="utf-8")
        satir = self.ad+","+self.soyad+","+str(self.yas)+"\n"
        dosya.write(satir)
        dosya.close()

        