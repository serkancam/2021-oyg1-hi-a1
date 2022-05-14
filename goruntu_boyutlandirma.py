# goruntu_boyutlandirma.py
import cv2
import numpy as np
import os


img_path=os.path.join(os.getcwd(),"images","chp2","zebra.png")

img=cv2.imread(img_path)

h,w,c = img.shape
print(img.shape)
#resmin en boy oranını bulalım
en_boy=w/h
# şimdi yüksekliği 400px yapalım
h_yeni=400
w_yeni=int(h_yeni*en_boy)
boyut=(w_yeni,h_yeni)
# oluşan yeni h w (boyut) ile resmi yeniden boyutlandıralım
r1_img=cv2.resize(img,boyut,interpolation=cv2.INTER_AREA)
r2_img=cv2.resize(img,(300,300),interpolation=cv2.INTER_AREA)

#2. yöntem genişlik ve yükseliği oran ile belirleyelim yeniden boyutlandırmak
r3_img=cv2.resize(img,None,fx=0.5,fy=0.5, interpolation=cv2.INTER_AREA)


cv2.imshow("Normal",img)
cv2.imshow("r1",r1_img)
cv2.imshow("r2",r2_img)
cv2.imshow("r3",r3_img)

cv2.waitKey(0)
cv2.destroyAllWindows()