import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    ret,frame=kamera.read()
    donmus=cv2.flip(frame,1)
    cv2.imshow("orijinal",frame)
    cv2.imshow("donmus",donmus)
    if cv2.waitKey(1) & 0xFF == ord('q'):     #cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
kamera.release()
