import cv2
import numpy as np
import os

#şu anda çalışan python dosyasının dizinini bulalım
# cd - şu andaki dizin(current directory)
cd = os.getcwd()
# print("**",cd,"***")#/home/serkan/Belgeler/2021-oyg1-hi-a1

resim_yolu=os.path.join(cd,"images","chp1","marsrover.png")
# print(resim_yolu)
resim=cv2.imread(resim_yolu)

print("resim şekli",resim.shape)
print("resim boyutu",resim.ndim)
print("resim yükseklik",resim.shape[0])
print("resim genişlik",resim.shape[1])
print("resim renk kanal sayısı",resim.shape[2])
#resimden bir parça alalım
parca1=resim[0:200,0:320]
parca2=resim[0:200,320:]
parca3=resim[200:,0:320]
parca4=resim[200:,320:]

#resmi 4 eşit parçaya böldük
cv2.imshow("parca1",parca1)
cv2.imshow("parca2",parca2)
cv2.imshow("parca3",parca3)
cv2.imshow("parca4",parca4)
#resme şekiller ekleyelim
baslangic=(100,70)
bitis=(350,380)
renk=(0,0,255)
cv2.rectangle(resim,baslangic,bitis,renk,4)
renkd=(0,255,0)
cv2.circle(resim,baslangic,30,renkd,4)
cv2.circle(resim,(350,70),30,renkd,4)


cv2.imshow("resim",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()

