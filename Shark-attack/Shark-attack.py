# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
from pprint import pprint


#get image
I = cv2.imread("Shark 1.PNG")

IbutYUV = cv2.cvtColor(I, cv2.COLOR_BGR2YUV)
Ibut = cv2.cvtColor(I, cv2.COLOR_BGR2YUV_I420)

plt.imshow(Ibut)
plt.savefig("tst.png")
