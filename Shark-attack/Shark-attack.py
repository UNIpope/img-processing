# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
from pprint import pprint

def get_shark(I):
    # convert to contrasty color space 
    Y = cv2.cvtColor(I, cv2.COLOR_BGR2LUV)
    G = cv2.cvtColor(Y, cv2.COLOR_BGR2GRAY)
    eqs = cv2.equalizeHist(G)

    # Get an apply threshold
    T = np.mean(eqs) + np.std(eqs) - 15
    T, B = cv2.threshold(eqs, thresh = T, maxval= 255,type = cv2.THRESH_BINARY)

    return B

def get_shark2(I):
    # convert to contrasty color space 
    Y = cv2.cvtColor(I, cv2.COLOR_BGR2HLS)
    G = cv2.cvtColor(Y, cv2.COLOR_BGR2GRAY)
    eqs = cv2.equalizeHist(G)

    # Get an apply threshold
    T = np.mean(eqs) + np.std(eqs)
    T, B = cv2.threshold(eqs, thresh = T, maxval= 255,type = cv2.THRESH_BINARY)

    return eqs

#get image
I = cv2.imread("Shark 1.PNG")
B = get_shark(I)
C = get_shark2(I)

# write out 
plt.imshow(B, cmap="gray")
plt.savefig("tst.png")

plt.imshow(C, cmap="gray")
plt.savefig("tst2.png")
