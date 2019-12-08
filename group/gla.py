# import the necessary packages:
import numpy as np
import cv2, easygui
from matplotlib import pyplot as plt
from matplotlib import image as image

def color_space(I):
    out = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

    return out

def get_contours(I):
    
    c,_ =cv2.findContours(G, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    I =cv2.drawContours(I,c,contourIdx=-1,color=(0,0,255),thickness=5)

def aline_im():
    pass


I = cv2.imread("")


cv2.imshow("out", I)
key = cv2.waitKey(0)