# konturlari_cizdirme.py
import cv2
import numpy as np
import os 

# yol = os.path.join(os.getcwd(),"images","blm2","sekil_geo.jpg")
yol = os.path.join(os.getcwd(),"images","blm2","rice_1.jpg")

img = cv2.imread(yol)
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# _,sb=cv2.threshold(gri,60,255,cv2.THRESH_BINARY)
blur=cv2.GaussianBlur(gri,(3,3),0)
canny=cv2.Canny(blur,40,140)

#konturları tespit etmek
konturlar,_=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#konturları çizdir
cv2.drawContours(img,konturlar,-1,(0,0,255),1)


cv2.imshow("sonuc",img)
cv2.imshow("canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()