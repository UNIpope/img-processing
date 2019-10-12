#import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
from pprint import pprint

#get image
ora = cv2.imread("orange.png")

#kernal + apply kernal
sharp = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
hor = np.array([[0,1,0], [1,-4,1], [0,1,0]])

im = cv2.filter2D(ora, -1, sharp)

#diff
diff = cv2.subtract(ora, im)

#show added im
cv2.imshow("sharpen",im)
cv2.imshow("diff",diff)
key = cv2.waitKey()
