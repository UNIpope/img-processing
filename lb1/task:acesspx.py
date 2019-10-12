# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
from pprint import pprint

#1.read in
I = cv2.imread("day.jpg")

#2.convert to YUV
IbutYUV = cv2.cvtColor(I, cv2.COLOR_BGR2YUV)

#3.extract y channel
ychan = IbutYUV[:,:,0]
#plt.imshow(ychan) 
#plt.show()


#4.convert to grey 
IbutGray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
#plt.imshow(IbutGray, cmap="gray") 
#plt.show()

#5.image show cv2.imshow()
#cv2.imshow("YUV", IbutYUV)
#cv2.imshow("Grayscale", IbutGray)

#6.luminesssence becide gray

plt.figure(1)
plt.subplot(ychan)
#plt.imshow(ychan)

plt.subplot(IbutGray, cmap="gray")
#plt.imshow(IbutGray, cmap="gray") 
plt.show()
