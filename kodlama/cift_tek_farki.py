# cift_tek_farki.py
# kullanıcının girdiği iki sayı arasındaki(girilen sayılar dahil) 
# çift sayıların toplamını tek sayıların toplamından çıkararak sonucu ekrana yazdıran programı yazınız.
#2 7   (2+4+6)-(3+5+7)-->-3

s1=int(input("küçük sayıyı giriniz:"))
s2=int(input("büyük sayıyı giriniz:"))
cift=0
tek=0
for sayi in range(s1,s2+1):
    if sayi%2==0:
        cift=cift+sayi
    else:
        tek=tek+sayi

print(f"ilk yol:{cift-tek}")

# fark=(s2+s1)//2-1
# print(f"ikinci yol:{fark}")
