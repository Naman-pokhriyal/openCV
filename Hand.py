import cv2 as cv
import numpy as np
import mediapipe as mp
import time

# FPS
cTime=0
pTime=0


cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    _, img = cap.read()
    img = cv.flip(img, 1)
    # sub_img = img[0:250, 0:250]

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    # print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # cv.putText(sub_img, str(id), (cx, cy), cv.FONT_HERSHEY_PLAIN, 1, (255,0,255),2)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)




    # fps
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (0, 15), cv.FONT_HERSHEY_PLAIN, 1, (255,0,255), 2)
    cv.imshow("Cam", img)
    if cv.waitKey(1) == ord('q'):
        break
