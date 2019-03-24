import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

if cap.isOpened() == False:
    print ("VideoCapture failed")
else:
    ret = True
    while ret != False:
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)

        #cv2.imshow('original', frame)
        if(ret == True):
            cv2.imshow('fg', fgmask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
