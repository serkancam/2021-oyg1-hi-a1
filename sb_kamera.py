import cv2

cap = cv2.VideoCapture(0)

while True:
    durum,cerceve=cap.read()
    cerceve = cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    t,cerceve = cv2.threshold(cerceve,40,255,cv2.THRESH_BINARY)
    cv2.imshow("kamera",cerceve)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()