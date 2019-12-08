import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image

I = cv2.imread("sn.jpg")
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

Ix =cv2.Sobel(G,ddepth=cv2.CV_64F,dx=1,dy=0)
Iy=cv2.Sobel(G,ddepth=cv2.CV_64F,dx=0,dy=1)

E =cv2.Canny(I,threshold1=0,threshold2=80)

#show 
plt.imshow(Ix)
plt.savefig("IX.png")
plt.imshow(Ix)
plt.savefig("IX.png")
plt.imshow(Iy)
plt.savefig("IY.png")


cv2.imshow("Image", I)
cv2.imshow("IX", Ix)
cv2.imshow("IY", Iy)
cv2.imshow("canny", E)

key = cv2.waitKey(0)


