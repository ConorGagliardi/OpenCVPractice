import cv2 as cv
import numpy as np
import pafy


def rescaleFrame(frame, scale=0.35):

    width = int(frame.shape[1] * scale) #shape[1] represents columns in the matrix
    height = int(frame.shape[0] * scale) #shape[0] represents rows in the matrix

    dimensions = (width, height) #creates a tuple of the size in "pixels" / rows and columns of the frame matrix

    #return the cv function to resize the frame by the tuple dimensions with the interpolation set
    #interpolation calculates new pixels from extra pixels in a bigger image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 

url = "https://www.youtube.com/watch?v=JJqXeRFsLjE"

video = pafy.new(url)

best = video.getbest(preftype="mp4")

capture = cv.VideoCapture(best.url)

ret, firstFrame = capture.read()
firstFrame = rescaleFrame(firstFrame)


ret1, secondFrame = capture.read()
secondFrame = rescaleFrame(secondFrame)

background = cv.bgsegm.createBackgroundSubtractorMOG()


while capture.isOpened():

    diff = cv.absdiff(firstFrame, secondFrame) #calculates per element absolute difference between a first and second matrix

    diff = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

    fgmask = background.apply(diff)

    blur = cv.GaussianBlur(fgmask, (7,7), 0)

    #canny = cv.Canny(blur, 50, 150) #calculate edges using the canny function

    _, thresh = cv.threshold(blur, 25, 255, cv.THRESH_BINARY)

    dilated = cv.dilate(thresh, None, iterations=3)

    contours, hierarchies = cv.findContours(dilated, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        
        if cv.contourArea(contour) > 300 and cv.contourArea(contour) < 2500:
            (x, y, w, h) = cv.boundingRect(contour) #create bounding box for the contours
            cv.rectangle(firstFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            

    #cv.drawContours(firstFrame, contours, -1, (0,0,255), 2)

    cv.imshow("video", firstFrame)

    firstFrame = secondFrame

    ret2, secondFrame = capture.read()
    secondFrame = rescaleFrame(secondFrame)


    if cv.waitKey(50) == 27:
        break

cv.destroyAllWindows()
capture.release()