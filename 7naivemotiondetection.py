import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=0.25):

    width = int(frame.shape[1] * scale) #shape[1] represents columns in the matrix
    height = int(frame.shape[0] * scale) #shape[0] represents rows in the matrix

    dimensions = (width, height) #creates a tuple of the size in "pixels" / rows and columns of the frame matrix

    #return the cv function to resize the frame by the tuple dimensions with the interpolation set
    #interpolation calculates new pixels from extra pixels in a bigger image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 