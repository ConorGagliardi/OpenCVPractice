import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.25):

    width = int(frame.shape[1] * scale) #shape[1] represents columns in the matrix
    height = int(frame.shape[0] * scale) #shape[0] represents rows in the matrix

    dimensions = (width, height) #creates a tuple of the size in "pixels" / rows and columns of the frame matrix


    #return the cv function to resize the frame by the tuple dimensions with the interpolation set
    #interpolation calculates new pixels from extra pixels in a bigger image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 



img = cv.imread('images/stella.png', 0)
img = rescaleFrame(img)
cv.imshow('fish', img)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny edges', canny)

blur = cv.GaussianBlur(img, (5,5), 0)

canny1 = cv.Canny(blur, 125, 175)
cv.imshow('canny1 edges', canny1)

ret, thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

contours1, hierarchies1 = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

contours2, hierarchies2 = cv.findContours(canny1, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cnt = contours[50]

rect = cv.maxAreaRect(cnt)
rect1 = cv.minAreaRect(cnt)
rect2 = cv.minAreaRect(cnt)



box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img, [box], 0, (0,0,255), 2)

cv.imshow('box?' , img)

cv.imshow('thresh' , thresh)

cv.waitKey(0)