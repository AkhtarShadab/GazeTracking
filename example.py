"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
import pandas as pd
from gaze_tracking import GazeTracking
import time
import numpy as np
 
# record start time
start = time.time()

gaze = GazeTracking()
webcam = cv2.VideoCapture("../../Data/video.mp4")
left = []
right = []

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    list1 = [0,0]
    list2 = [0,0]
    if left_pupil!=None:
        list1 = list(left_pupil)
    if right_pupil!=None:
        list2 = list(right_pupil)
    left.append(list1)
    right.append(list2)
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)
    end = time.time()
    
    if((end-start)*10**3>6000):
        left = np.array(left)
        right = np.array(right)
        print(left,right)
        df = pd.DataFrame(left,columns=['Left_x','Left_y'])
        df1 = pd.DataFrame(right,columns=['Right_x','Right_y'])
        result = pd.concat([df, df1], axis=1)
        result.to_csv('./media_2_data.csv',index = False)
        break
        
    if cv2.waitKey(1) == 27:
        break
   

webcam.release()
cv2.destroyAllWindows()
