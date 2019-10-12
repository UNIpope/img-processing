# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
from pprint import pprint

#get image
ora = cv2.imread("orange.png")
wat = cv2.imread("water.jpg")

#scale colour down
ora[:,:,:] = ora * .5
wat[:,:,:] = wat * .5

#may need if np array:
#tst = np.array(ora * .5 , dtype = np.uint8)

# add together
add = cv2.add(ora, wat)
addwe = cv2.addWeighted(ora, 1.2, wat, .1, 0)

# show added im
cv2.imshow("add",add)
cv2.imshow("we",addwe)

key = cv2.waitKey()
