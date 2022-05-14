import cv2
import numpy as np
import os

resim= np.zeros((400,400,3),dtype=np.uint8)

# ekranın tam ortasına 40 piksel yarıçap a sahip mavi renkli kenar kalınlığı 3 piksel olan bir daire çiziniz.
# çizdiğiniz daireyi tam olarak kapsayan  kırmızı renkkli bir kare çiziniz

cv2.circle(resim,(200,200),40,(255,0,0),3)
cv2.rectangle(resim,(160,160),(240,240),(0,0,255),3)
cv2.imshow("resim",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
#dosya calisma1.jpg olarak images/chp1 dizini içine kaydeilecek
# bunun ilk önce dosya yolunu tanımlanıyor
dosya_yolu = os.path.join(os.getcwd(),"images","chp1","calisma1.jpg")
cv2.imwrite(dosya_yolu,resim)