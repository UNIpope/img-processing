# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image

I = cv2.imread("Trump.jpg")
im = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

min_HSV = np.array([5, 58, 30], dtype = "uint8")
max_HSV = np.array([25, 255, 255], dtype = "uint8")

skinRegionHSV = cv2.inRange(im, min_HSV, max_HSV)
skin = cv2.bitwise_and(I, I, mask = skinRegionHSV)

shape = cv2.getStructuringElement(cv2.MORPH_RECT,(15,15))
NewMask = cv2.dilate(skin, shape)

cv2.imshow("skin", skin)
cv2.imshow("image", NewMask)
key = cv2.waitKey(0)
