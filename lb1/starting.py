# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image


I = cv2.imread("lunar.jpg")
#print(type(I))

#show video
"""
Video = cv2.VideoCapture(0)
(check, I) = Video.read()

while check:
	cv2.imshow("image", I)	
	key = cv2.waitKey(1)

	if key == ord("q"):
	    break

	(check, I) = Video.read()

Video.release()
"""

#write file
#cv2.imwrite("we.jpg",I)


#I[:,100:200] = (0,255,255)

#I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
#plt.imshow(I) 
#plt.show()


size = np.shape(I)
print(size)
cv2.line(img = I, pt1 = (100,0), pt2 = (100,size[1]), color = (255,255,255), thickness = 5) 

cv2.circle(img = I, center = (800,400), radius = 200, color = (0,0,255), thickness = -1)
cv2.circle(img = I, center = (800,400), radius = 50, color = (0,0,0), thickness = -1)
cv2.circle(img = I, center = (800,400), radius = 20, color = (255,255,255), thickness = -1)

I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
plt.imshow(I) 
plt.show()