from typing import Counter
import cv2 as cv
import numpy as np
import math

capture = cv.VideoCapture(0)

while True:
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    cv.rectangle(frame, (200,200), (0,0), (0,255,0),0)
    corpped = frame[0:200, 0:200]
    grey = cv.cvtColor(corpped, cv.COLOR_BGR2GRAY)
    blur = cv.bilateralFilter(grey, 20, 30, 30)
    # blur = cv.GaussianBlur(grey, (35,35), 0)
    ret, thresh = cv.threshold(blur, 127, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    cv.imshow("Web",thresh)

    contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    cut = max(contours, key = lambda x:cv.contourArea(x))

    x, y, w, h = cv.boundingRect(cut)
    cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 0)


    cv.imshow("Frame",frame)
    if cv.waitKey(1) == ord('q'):
        break
capture.release()
cv.destroyAllWindows()