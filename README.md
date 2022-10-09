﻿# OpenCVPractice
1read.py - learn how to open images and videos using opencv

2rescale.py - first attempted preprocessing concept for changing the scale of the input frames

3draw.py - draw on an input frame with various shapes lines, also learned how coordinates are represented in a frame matrix

4basicfunctions.py - practiced using some commonly used processing functions such as, converting to grayscale, blurring, edge detection using canny or thresholding, and finding contours

5contour features test.py - testing contour applications such as creating rectangles and drawing contours

6face mesh tutorial.py - followed this tutorial https://www.youtube.com/watch?v=ARDlO_y3O8w in order to create a basic facemesh with mediapipe

7basicmotiondetection.py - used various documentation, stack overflow, and youtube videos in an attempt to get a decently working motion detection. It is able to detect and draw a bounding box around moving objects on a video / livestream provided that the contrast permits. Also uses pafy as a means to capture youtube livestreams. Currently it is set to view https://www.youtube.com/watch?v=JJqXeRFsLjE a livestream of penguins.
NOTE:: had to use "pip install youtube-dl==2020.12.2" in order for pafy to work with youtube videos
