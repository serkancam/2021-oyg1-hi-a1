

# tanımlama
def merhaba():
    print("merhaba")

def merhaba2(adet):
    for i in range(adet):
        print("*merhaba*")

def topla(sayi1,sayi2):
    toplam=sayi1+sayi2
    print(toplam)

def kare_farki(sayi1,sayi2):
    kf = sayi1**2-sayi2**2
    return kf
        
#çağırma
merhaba()
merhaba()
merhaba2(3)
topla(20,30.0)
# topla(20,30,40)#hatalı çağırma
fark=kare_farki(20,5)
print(fark)
print(kare_farki(2,1))
print(merhaba())



