# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
from pprint import pprint

#read in img
I = cv2.imread("wartime.jpg")
Is = cv2.imread("poor.jpg")

#conv to
IbutGray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

tst= cv2.cvtColor(Is, cv2.COLOR_YUV2BGR)
Isbutgray = cv2.cvtColor(tst, cv2.COLOR_BGR2GRAY)
#image with histo reg 
Values = IbutGray.ravel()

plt.figure(1)
plt.subplot(211)
plt.imshow(I) 

plt.subplot(212)
plt.hist(Values,bins=256,range=[0,256])

plt.savefig("imagewithhisto.png")


#image with hist equal
eq = cv2.equalizeHist(IbutGray)
eqValues = eq.ravel()

plt.figure(2)

plt.subplot(211)
plt.imshow(eq)

plt.subplot(212)
plt.hist(eqValues,bins=256,range=[0,256])

plt.savefig("eqimagewithhisto.png")


# poor quality testing
eqs = cv2.equalizeHist(Isbutgray)
eqValuess = eq.ravel()

plt.figure(2)

plt.subplot(211)
plt.imshow(eqs, cmap="gray")

plt.subplot(212)
plt.hist(eqValuess,bins=256,range=[0,256])

plt.savefig("eqpoor.png")






