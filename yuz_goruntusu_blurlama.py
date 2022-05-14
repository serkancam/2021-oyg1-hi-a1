# yuz_goruntusu_blurlama.py
import cv2
import numpy as np
import os

yol = os.path.join(os.getcwd(), "images", "yuz.jpg")
goruntu = cv2.imread(yol)
bulanik = cv2.blur(goruntu, (35, 35))
# 90:360,200:400---->360:90,400:200 yazımı hatalıdır
parca = goruntu[90:360, 200:400]
parca = cv2.blur(parca, (35, 35))

goruntu[90:360,200:400]=parca
goruntu=goruntu.T
cv2.imshow("sonuc", goruntu)
# cv2.imshow("orijinal",goruntu)
# cv2.imshow("bulanik",bulanik)
cv2.waitKey(0)
cv2.destroyAllWindows()
