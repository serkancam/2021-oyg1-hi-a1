import random
dizi=[]#list()
for i in range(10):
    t=random.randint(1,100)
    dizi.append(t)

print(dizi)

enk=dizi[0]
yer=0

for p in range(len(dizi)):
    if dizi[p]<enk:
        enk=dizi[p]
        yer=p

print(enk)

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
    
    


