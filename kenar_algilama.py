import cv2
import numpy as np
import os

# sobel filtresi
# laplacian yaklaşımı
# canny kenar tespit yöntemi(canny operatörü)

yol=os.path.join(os.getcwd(),"images","chp2","sudoku.jpg")
goruntu=cv2.imread(yol)

gri=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

# t,sb=cv2.threshold(gri,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# gri=cv2.blur(gri,(7,7))
canny = cv2.Canny(gri,50,170)

cv2.imshow("canny",canny)
cv2.imshow("goruntu",goruntu)

cv2.waitKey(0)
cv2.destroyAllWindows()



