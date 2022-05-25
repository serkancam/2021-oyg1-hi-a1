import cv2 
import numpy as np
import os
yol_cascade = os.path.join(os.getcwd(),"images","blm2","haarcascade_frontalface.xml")

yuz_cascade=cv2.CascadeClassifier(yol_cascade)

cap = cv2.VideoCapture(0)
while True:
    durum,frame = cap.read()
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler = yuz_cascade.detectMultiScale(gri,1.3,5)    
    for yuz in yuzler:
        (x,y,w,h)=yuz
        parca = frame[y:y+h,x:x+w]
        frame = cv2.GaussianBlur(frame,(105,105),0)
        frame[y:y+h,x:x+w]=parca
       
    cv2.imshow("sonuc",frame)

    if cv2.waitKey(1)==27:#27 onluk değeri escape tuşu
        break

cap.release()
cv2.destroyAllWindows()