import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

def draw(event,x,y,flags,param): 
    x1 = x - 100
    y1 = y - 100

    x2 = x + 100
    y2 = y + 100

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img = I, pt1 = (x1,y1), pt2 = (x2,y2), color = (255,0,255), thickness = 10)
        I[y1:y2,x1:x2] = cv2.cvtColor(I[y1:y2,x1:x2], cv2.COLOR_BGR2YUV)

        cv2.imshow("image", I) 

        
f = easygui.fileopenbox()
I = cv2.imread(f)

while True:
    cv2.imshow("image", I)
    cv2.setMouseCallback("image", draw) 

    Original = I.copy()

    key = cv2.waitKey(0)
    # # if the 'r' key is pressed, reset the image:
    if key == ord("r"):
        I = Original.copy()

	# # if the 'q' key is pressed, quit:
    elif key == ord("q"):
        exit()

