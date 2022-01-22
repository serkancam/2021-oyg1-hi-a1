# break döngüyü kırar(kendine yakın döngüyü.)
# continue döngü bloğuna geri döner.

#for ve while

for i in range(10):
    if i%2==0:
        continue
    print(i)

t=0
while t<10:
    t=t+1
    if t%2==0:
        continue
    print(t)

print(30*"*")
for k in range(10):
    if k==4:
        break
    print(k)

print(30*"*")
h=-1
while h<10:
    h=h+1
    if h==4:
        break
    print(h)
    
