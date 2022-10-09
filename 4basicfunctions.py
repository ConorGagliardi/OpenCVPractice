#fourth initial testing for must know opencv functions

import cv2 as cv
import numpy as np

# Takes a frame and a scale, and scales(resizes) the frame
def rescaleFrame(frame, scale=0.25):

    width = int(frame.shape[1] * scale) #shape[1] represents columns in the matrix
    height = int(frame.shape[0] * scale) #shape[0] represents rows in the matrix

    dimensions = (width, height) #creates a tuple of the size in "pixels" / rows and columns of the frame matrix


    #return the cv function to resize the frame by the tuple dimensions with the interpolation set
    #interpolation calculates new pixels from extra pixels in a bigger image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 


img = cv.imread('images/barracuda.png')
cv.imshow('fish', img)

#1. Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)

#2. Blur an image with the gaussian blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blurred', blur)

#3. edge cascade using canny edge detection technique (uses blurring and gradient algorithms)
canny = cv.Canny(img, 125, 175)
cv.imshow('canny edges', canny)

#3.5 finding contours and hierarchies of an image with canny,
# 2nd param mode (cv.RETR_TREE (hierarchical contours) cv.RETR_EXTERNAL (external contours) or cv.RET_LIST for both
# 3rd param contour approximation method

#contours: list of contours found in the image, hierarchies: hierarchical representation of contours (like a shape inside a shape)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

#[CHALLENGE use canny on video] resize video, and apply canny edge detection
# capture = cv.VideoCapture('videos/scubatest.mov')

# while True:
#     isTrue, frame = capture.read()
#     frame = rescaleFrame(frame)
#     canny = cv.Canny(frame, 125, 175)a
#     cv.imshow('frame', canny)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

#[CHALLENGE] apply blur as well to reduce noise
# capture = cv.VideoCapture('videos/scubatest.mov')

# while True:
#     isTrue, frame = capture.read()
#     frame = rescaleFrame(frame)
#     blur = cv.GaussianBlur(frame, (3,3), cv.BORDER_DEFAULT)
#     canny = cv.Canny(blur, 125, 175)
#     cv.imshow('frame', canny)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break


#4. Manipulating line sizes
#dilating an image (increasing the line sizes)
dilated = cv.dilate(canny, (5,5), iterations=2)
cv.imshow('Dilated', dilated)

#eroding an image (decreasing the line sizes)
eroded = cv.erode(dilated, (5,5), iterations=2)
cv.imshow('Eroded', eroded)

#5. resizing ignoring aspect ratio         
# cv.INTER_AREA useful for shrinking image, cv.INTER_LINEAR / cv.INTER_CUBIC useful for scaling up     
resized = cv.resize(img, (1500,1500), interpolation=cv.INTER_LINEAR)
resized1 = cv.resize(img, (1500,1500), interpolation=cv.INTER_CUBIC)
cv.imshow('linear interpolation resize', resized)
cv.imshow('cubic interpolation resize', resized1)


cv.waitKey(0)