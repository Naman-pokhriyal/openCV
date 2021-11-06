import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    _, frame = capture.read()


    cv.imshow("frame", frame)
    # RGB
    imgRGB = cv.cvtColor(frame, cv.COLOR_BGRA2RGB)
    # cv.imshow("RGB",imgRGB)


    # MonoScale
    grey = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    # cv.imshow("Grey",grey)
    
    
    # Blur
    Ablur = cv.blur(frame, (7,7))
    # cv.imshow("Blur",Ablur)
 

    if cv.waitKey(1) == ord('q'):
        break
















# import numpy as np

#     # Flip
#      imgflip = cv.flip(frame, 1)
#    # Smooth
#     Bblur = cv.bilateralFilter(frame, 15, 30, 30)
#    # Edge Cascade
#     canny = cv.Canny(frame, 120,170)
#    # Dilate
#     dilated = cv.dilate(canny, (1,1), iterations=1)
#    # Resize
#     resize = cv.resize(frame, (1000,800), interpolation=cv.INTER_CUBIC)
#    # Crop
#     cropped = frame[100:200, 200:400]
#    # threshold
#     ret, thresh = cv.threshold(grey, 100,220, cv.THRESH_BINARY)
#    # Blur
#     Gblur = cv.GaussianBlur(frame, (7,7), 0)
#     Mblur = cv.medianBlur(frame, 7)
# # -----------------------------------------------------------------
#     # Contours
#     contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#     # Blank Board
#     blank = np.zeros(frame.shape, dtype='uint8')
#     cv.drawContours(blank, contours, -1, (0,255,0), 2)
# # -----------------------------------------------------------------


# capture.release()
# cv.destroyAllWindows()

