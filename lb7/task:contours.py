import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image

I = cv2.imread("Micro.jpg")
noise = cv2.fastNlMeansDenoisingColored(I, None, 10,10,7,21)
G = cv2.cvtColor(noise, cv2.COLOR_BGR2GRAY)

c,_ =cv2.findContours(G, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

I =cv2.drawContours(I,c,contourIdx=-1,color=(0,0,255),thickness=5)

cv2.imshow("out", I)
key = cv2.waitKey(0)