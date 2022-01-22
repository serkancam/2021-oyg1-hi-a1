# fonksiyonlara 2 şekilde parametre gönderilir
# 1- pozisyona dayalı paramtere gönderimi
# 2- isme dayalı parametre gönderimi

#tanımlama
def yamuk_cevresi(a,b,c,d):
    cevre=a+b+c+d
    return cevre

# çağırma

c1=yamuk_cevresi(3,12,10,17)
c2=yamuk_cevresi(c=5,a=10,d=8,b=25)
c3=yamuk_cevresi(1,c=5,d=2,b=4)#brkere isme dayalı gönderim yaptıysan sağa doğruda o şekilde gidecek
# c4=yamuk_cevresi(3,d=8,10,9)#hatalı parametre geçme yolu
c5=yamuk_cevresi(3,b=5,c=8,d=9)
