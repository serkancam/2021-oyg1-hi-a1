import cv2
import numpy as np
import os

# resim gürültüsü azaltmada için yapılan işlemler
# * smoothing(yumuşatma)
# * blurring(bulanıklaştırma)

# gürültü(noise)
#mean filter
yol1=os.path.join(os.getcwd(),"images","chp2","nature.jpg")
doga = cv2.imread(yol1)
smooth1=cv2.blur(doga,(3,3))
smooth2=cv2.blur(doga,(9,9))

#median filter
yol2=os.path.join(os.getcwd(),"images","chp2","salt-pepper.jpg")
salt_pepper=cv2.imread(yol2)
salt_pepper_temiz=cv2.medianBlur(salt_pepper,469)



cv2.imshow("gurultulu",salt_pepper)
cv2.imshow("temiz",salt_pepper_temiz)

cv2.imshow("doga original",doga)
cv2.imshow("smooth1",smooth1)
cv2.imshow("smooth2",smooth2)
cv2.waitKey(0)
cv2.destroyAllWindows()