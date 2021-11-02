def daire_cevresi_hesapla(yaricap:float,pi:float=3.14)->float:
    cevre= 2*pi*yaricap
    return cevre


# bir sayının küpünün karesine küpüne farkını bulan kodu yazınız
# eğer paramtre gelmez ise sayı 5 kabul edilsin
# sayı tipi int olsun
# geriye dönüş tipide int olsun
#  
def kup_kare_farki(sayi:int=5)->int:
    fark=sayi**3-sayi**2
    return fark
print(daire_cevresi_hesapla(10,3.0))
print(daire_cevresi_hesapla(10,3.14))
print(daire_cevresi_hesapla(20))