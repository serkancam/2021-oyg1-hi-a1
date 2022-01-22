# in anahtar kelimesi iki farklı şekilde kullanılır
# 1- for döngüsünde içinde gezilecek diziye işaret eder.
# 2- bir liste içinde bir parçanın olup olmadığını True veya False olarak  bildirir.

# v = "a" in "ali" #True
# print(v)
# print("A" in "serkan")
# print("ali" in "Bizim ali çok komik.")

# print("euıoüaiöEUIOÜAİÖ" in "merhaba dünya.")
# print("A" in "euıoüaiöEUIOÜAİÖ")

sesliler="euıoüaiöEUIOÜAİÖ"
metin="merhaba dünya."
hece_sayisi=0
for harf in metin:
    # print(harf)
    if harf in sesliler:
        print(harf)
        hece_sayisi+=1#hece_sayisi=hece_sayisi+1

print(hece_sayisi)
