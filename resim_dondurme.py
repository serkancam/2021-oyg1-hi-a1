# resim_dondurme.py
import cv2
import os
import numpy as np

img_path=os.path.join(os.getcwd(),"images","chp2","zebrasmall.png")
img=cv2.imread(img_path)
h,w,c=img.shape
merkez=(h//2,w//2)
aci=-45
olcek=1.0
img_flip1=cv2.flip(img,flipCode=1)
img_flip0=cv2.flip(img,flipCode=0)
cv2.imshow("flip1",img_flip1)
cv2.imshow("flip0",img_flip0)
cv2.imshow("orijinal",img)
while True:
    donme_matrisi=cv2.getRotationMatrix2D(merkez,aci,olcek)
    donmus_resim=cv2.warpAffine(img,donme_matrisi,(w,h))
    cv2.imshow("donmus resim",donmus_resim)    
    aci+=5    
    if cv2.waitKey(20) & 0xFF==ord("q") :
        break
cv2.destroyAllWindows()