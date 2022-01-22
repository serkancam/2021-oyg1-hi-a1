from kisi import Kisi
while True:
    islem = int(input("(0-okuma,1-ekleme,2-yaş ortalaması,3-çıkış)işlem seçiniz:"))
    if islem==0:
        print("okuma")
        dosya = open("kisiler.txt","r",encoding="utf-8")
        for satir in dosya:
            print(satir)
        dosya.close()
    elif islem==1:        
        while True:
            try:
                ad=input("adınız:")
                soyad=input("soyadınız:")
                if len(ad)<2 or len(soyad)<2:
                    print("ad ve soyad en az 2 karakterli olmalı")
                    continue
                yas=int(input("yaşınız:"))
                break
            except:
                print("hata")
                continue
        k=Kisi(ad,soyad,yas)
        k.kayit("kisiler.txt")
    elif islem==2:
        print("yaş ortalaması")
    elif islem==3:
        break
    else:
        print("yanlış seçim")

