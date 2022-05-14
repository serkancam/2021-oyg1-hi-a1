import cv2
import numpy as np
import os

#nature.jpg-->img1
#zebrasmall.png-->img2
# iki görüntüyüde 300*300 yeniden boyutlandırın

yol1=os.path.join(os.getcwd(),"images","chp2","nature.jpg")
yol2=os.path.join(os.getcwd(),"images","chp2","zebrasmall.png")
img1=cv2.imread(yol1)
img2=cv2.imread(yol2)

img1=cv2.resize(src=img1,dsize=(300,300),interpolation=cv2.INTER_AREA)
img2=cv2.resize(src=img2,dsize=(300,300),interpolation=cv2.INTER_AREA)

toplama_resim=cv2.add(img2,img1)
fark_resmi=cv2.subtract(img2,img1)
arti_isareti=img1+img2
eksi_isareti=img1-img2

cv2.imshow("arti_isareti",arti_isareti)
cv2.imshow("eksi_isareti",eksi_isareti)
cv2.imshow("toplama_resim",toplama_resim)
cv2.imshow("fark_resmi",fark_resmi)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()