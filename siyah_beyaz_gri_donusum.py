# siyah_beyaz_gri_donusum.py
import cv2 
import numpy as np
import os

#resimdeki nesne tespit için gereksiz ayrıntılaran kaçınılması gerekir
# bu ayrıntılardan biri de 3 kanallı renk bilgisidir.
yol = os.path.join(os.getcwd(),"images","yuz.jpg")

goruntu=cv2.imread(yol)
print(goruntu.shape)
gri = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
print(gri.shape)
t,sb=cv2.threshold(gri,80,255,cv2.THRESH_BINARY)
print(sb.shape)

yol2=os.path.join(os.getcwd(),"images","chp2","scanned_doc.png")
belge=cv2.imread(yol2)
belge_gri=cv2.cvtColor(belge,cv2.COLOR_BGR2GRAY)
t,belge_sb=cv2.threshold(belge_gri,60,255,cv2.THRESH_BINARY)



cv2.imshow("orijinal",goruntu)
cv2.imshow("gri",gri)
cv2.imshow("sb",sb)
cv2.imshow("belge sb",belge_sb)
cv2.waitKey(0)
cv2.destroyAllWindows()