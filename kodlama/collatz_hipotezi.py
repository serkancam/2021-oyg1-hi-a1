# kullanıcının girdiği sayının collatz_hipotezi yardımı ile 1'e dönmesini sağlayan kodu yazınız
# ve her adımda oluşan değeri ekrana yazdırınız.
# sayı çift ise ikiye bölün
# tek ise 3 ile çarpıp 1 ekleyin
# sayi=int(input("sayı giriniz:"))

for sayi in range(2,1000000):
    test=sayi
    say=1
    adim=1
    while sayi!=1:# bir olana kadar --- birden farklı olduğu sürece
        if sayi%2==0:
            sayi=sayi/2
        else:
            sayi=sayi*3+1
        # print(f" {adim}. adım  {int(sayi)}")
        adim=adim+1
    if(sayi==1):
        print(f"{test} sayısı {adim} adımda 1'e döndü")