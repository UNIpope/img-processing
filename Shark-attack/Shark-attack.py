"""
Name: Jack duggan
Stu number: C16350866
Assignment: 1; Transformation; SHARK ATTACK!!!

Assignment brief:
    SHARK ATTACK!!!
    ... or is it? It's a bit blurry.

    Use your new-found image processing skills to bring this fish to life!
        1. Convert to an appropriate colourspace to exaggerate the fish/sea difference;
        2. Enhance the images to increase contrast and definition;
        3. Extract the fish from the images and convert the background to white;
        4. Enhance the fish portion of the image;
        5. The final image should be an enhanced image of the fish with a white background;
        6. Optional: automatically crop and rotate the image to contain only the shark/fish.

    Your design should work on the attached images but also on similar images of fish underwater. Refer to the General Assignment Guidelines to maximise your marks. Submit your fully-commented py file here.


"""
# import the necessary packages:
import numpy as np
import cv2, easygui
from matplotlib import pyplot as plt
from matplotlib import image as image

def set_black(I):
    h, w, d = I.shape
    for row in range(h):
        for col in range(w):
            if I[row,col][2] == 0:
                I[row,col] = 255

    return I

def set_image(I,mask):
    ROI = cv2.bitwise_and(I,I,mask=mask)
    w = set_black(ROI)
    out = cv2.cvtColor(w, cv2.COLOR_BGR2RGB)

    return out

def remove_edge(I):
    # Get with and height of image
    h, w = I.shape

    # Loop edeges and floof fill if white
    for row in range(h):
        if I[row, 0] == 255:
            cv2.floodFill(I, None, (0, row), 0)
        if I[row, w-1] == 255:
            cv2.floodFill(I, None, (w-1, row), 0)

    for col in range(w):
        if I[0, col] == 255:
            cv2.floodFill(I, None, (col, 0), 0)
        if I[h-1, col] == 255:
            cv2.floodFill(I, None, (col, h-1), 0)

    return I


def prep_shark(I):
    #Prepare input image.
    #Remove noise, convert to a sutibale color space,
    #grayscale image, equalizeimage and threshold image.
    #
    #This outputs a black and white image of the most stand out colors.

    # Sharpen or blur gives a worse image
    #k = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    #sharp = cv2.filter2D(noise, -1, k)
    #gray = cv2.GaussianBlur(noise, (7, 7), 0)

    # Remove noise
    noise = cv2.fastNlMeansDenoisingColored(I, None, 10,10,7,21)

    # convert to contrasty color space
    LUVim = cv2.cvtColor(noise, cv2.COLOR_BGR2LUV)
    Gim = cv2.cvtColor(LUVim, cv2.COLOR_BGR2GRAY)
    EQim = cv2.equalizeHist(Gim)

    # Get an apply threshold
    T = np.mean(EQim) + np.std(EQim) - 15
    T, B = cv2.threshold(EQim, thresh = T, maxval= 255,type = cv2.THRESH_BINARY)

    return B


f = easygui.fileopenbox()
I = cv2.imread(f)#

B = prep_shark(I)
C = remove_edge(B)
D = set_image(I, C)


cv2.imshow("image", D)
key = cv2.waitKey(0)
