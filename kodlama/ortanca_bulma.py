import random
dizi=[]#list()
for i in range(random.randint(5,13)):
    t=random.randint(1,100)
    dizi.append(t)
sirali_dizi=[]
while len(dizi)!=0:
    enk=dizi[0]
    yer=0
    for p in range(len(dizi)):
        if dizi[p]<enk:
            enk=dizi[p]
            yer=p
    e=dizi.pop(yer)
    sirali_dizi.append(e)
print(sirali_dizi)
boyut=len(sirali_dizi)
ortanca_yeri=boyut//2
if boyut%2==1:
    ortanca=sirali_dizi[ortanca_yeri]
else:
    ortanca=sirali_dizi[ortanca_yeri]+sirali_dizi[ortanca_yeri-1]

print(ortanca)
    
    


