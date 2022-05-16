import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    fc=frame.copy()
    
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gri,(3,3),0)
    canny=cv2.Canny(blur,40,100)
    konturlar,_=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,konturlar,-1,(0,0,255),2)
    #adaptif eşikleme
    sb=cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,3)
    konturlar2,_=cv2.findContours(sb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(fc,konturlar2,-1,(0,255,0),1)

    cv2.imshow("canny",canny)
    cv2.imshow("frame",frame)
    cv2.imshow("sb",sb)
    cv2.imshow("fc",fc)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()


