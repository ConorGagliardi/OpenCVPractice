#third initial testing for drawing on image and video inputs in opencv

import cv2 as cv
import numpy as np

#create array of zeros in numpy with the datatype typical of an image shape=(height,width,color channels 3 for bluegreenred)
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blankimg', blank)

#set pixel colors for a copy of the blank canvas
blank[:] = 255,0,0 #change pixel values in given range to this color(Blue)
cv.imshow('blue', blank)

#draw a rectangle on a canvas
#cv.rectangle takes a frame, 2 tuples of (
#       (left line distance from left, top line distance from top) and (right line distance from left, bottom line distance from top), 
# a color (bluegreenred for 3 color channels), and can set thickness to the following:
#thickness = 2(desired width of line), OR to fill in use one of these (thickness=cv.FILLED or #thickness=-1)
cv.rectangle(blank, (100,100), (350,255), (0,0,255), thickness=2)
cv.imshow('Rectangle', blank) #notice that cv.rectangle globally modifies 'blank'

#draw a circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 3), 50, (150, 255, 0), thickness = -1)
cv.imshow('add a circle', blank)

#draw a line [SELF CHALLENGE](from bottom left corner of rectangle to left edge of circle)
cv.line(blank, (100, 255), (((blank.shape[1] // 2) - 50, blank.shape[0] // 3)), (255,255,255), thickness=3)
cv.imshow('line', blank)

#put text on an image
cv.putText(blank, "This is input text", (255,255), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 2)
cv.imshow('text input', blank)

#use to keep opened windows from closing instantly
cv.waitKey(0)
