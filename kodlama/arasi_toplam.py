ilk=int(input("ilk sayıyı giriniz:"))
son=int(input("son sayıyı giriniz:"))
toplam=0
for i in range(ilk,son+1):
    toplam+=i
toplamA=son*(son+1)/2
toplamB=ilk*(ilk-1)/2
toplam2=toplamA-toplamB
print(f"{ilk} ile {son} arasındaki sayıların toplamı={toplam}")
print(f"{ilk} ile {son} arasındaki sayıların toplamı={toplam2}")