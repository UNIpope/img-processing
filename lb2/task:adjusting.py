# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
from pprint import pprint

#read in img
I = cv2.imread("wartime.jpg")

#extracto
h, w, d = I.shape

sec4 = I[int(h/2):,int(w/2):]

#new image
tmp = np.zeros((2000,2000,3),np.uint8)
h, w, d = sec4.shape
tmp[1000: 1000+h, 1000: 1000+w] = sec4[:,:]

# trans matrix
h1, w1, d = tmp.shape

cx = 1000
cy = 1000
d = 45
s = 1
M = cv2.getRotationMatrix2D(center=(cx,cy),angle=d, scale=s)
R = cv2.warpAffine(tmp, M = M,dsize=(w1,h1))


#show
plt.imshow(R)
plt.savefig("tst.png")


