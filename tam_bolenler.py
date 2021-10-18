# kullanıcı tarafından girien sayının tam bolenlerini bulup ekrana yazdıran 
# program yazınız.

# 15 --> 1 3 5 15
# 8 --> 1 2 4 8
# 7 --> 1 7
# 60--> 1 2 3 4 5 6 10 15 20 30 60

sayi = int(input("say giriniz:"))
for deger in range(1,sayi+1):
    if sayi%deger==0:
        print(deger,end=" ")
