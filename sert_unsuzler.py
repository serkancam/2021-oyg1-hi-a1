# kullanıcı tarafından girilen metindeki sert ünsüz sayısını bulup;
# sonucu ekrana yazdıran python kodunu yazınız.

metin=input("metni giriniz:")
sert_unsuz_sayisi=0
sert_unsuzler="fstkçşhp"

for harf in metin:
    if harf in sert_unsuzler:
        sert_unsuz_sayisi+=1
print(f"{metin} metni içinde {sert_unsuz_sayisi} adet sert ünsüz vardır. ")