#first initial testing for reading in images and videos using opencv

import cv2 as cv

#read and display an image

img = cv.imread("images/barracuda.png")

cv.imshow('barracuda', img)

#read a video
#capture = cv.VideoCapture('videos/scubatest.mov')

#read a webcam
capture = cv.VideoCapture(0)

#display each frame of the video for a time limit
while True:
    isTrue, frame = capture.read()
    cv.imshow('MyVid', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#close everything up
capture.release()
cv.destroyAllWindows()