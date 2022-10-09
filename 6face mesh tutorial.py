import cv2 as cv
import numpy as np
import mediapipe as mp

#face mesh detection
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh


drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

#cap = cv.VideoCapture('videos/stella.mov')
cap = cv.VideoCapture(0, cv.CAP_DSHOW)



def rescaleFrame(frame, scale=0.25):

    width = int(frame.shape[1] * scale) #shape[1] represents columns in the matrix
    height = int(frame.shape[0] * scale) #shape[0] represents rows in the matrix

    dimensions = (width, height) #creates a tuple of the size in "pixels" / rows and columns of the frame matrix

    #return the cv function to resize the frame by the tuple dimensions with the interpolation set
    #interpolation calculates new pixels from extra pixels in a bigger image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 

with mp_face_mesh.FaceMesh(
    refine_landmarks=True,
    min_detection_confidence=0.5) as face_mesh:

    while cap.isOpened():

        isTrue, frame = cap.read()

        frame = rescaleFrame(frame, scale=0.9)

        #convert BGR color of image to RGB
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        frame.flags.writeable = False #improves performance for passing by reference

        #process image using process method from face_mesh object
        results = face_mesh.process(frame)

        frame.flags.writeable = True

        #convert RGB back to BGR to display
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                #print(face_landmarks)

                mp_drawing.draw_landmarks(frame, landmark_list = face_landmarks,
                                            connections = mp_face_mesh.FACEMESH_CONTOURS,
                                            landmark_drawing_spec = drawing_spec,
                                            connection_drawing_spec = drawing_spec)

        cv.imshow('mediapipe facemesh', frame)

        if cv.waitKey(5) & 0xFF == 27:
            break

    
cap.release()

