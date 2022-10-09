#second initial testing for resizing image and video inputs in opencv

import cv2 as cv

#set up video capture
capture = cv.VideoCapture('videos/scubatest.mov')

# Takes a frame and a scale, and scales(resizes) the frame
def rescaleFrame(frame, scale=0.25):

    width = int(frame.shape[1] * scale) #shape[1] represents columns in the matrix
    height = int(frame.shape[0] * scale) #shape[0] represents rows in the matrix

    dimensions = (width, height) #creates a tuple of the size in "pixels" / rows and columns of the frame matrix


    #return the cv function to resize the frame by the tuple dimensions with the interpolation set
    #interpolation calculates new pixels from extra pixels in a bigger image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 


#get image
img = cv.imread('images/tokyo.png')

#show rescaled image
cv.imshow('toyko', rescaleFrame(img, scale = 0.75))

#loop for displaying all video frames with rescaling
while True:
    isTrue, frame = capture.read()
    frame = rescaleFrame(frame)
    cv.imshow('MyVid', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#close everything
capture.release()
cv.destroyAllWindows()