"""
Name: Jack duggan
Stu number: C16350866
Assignment: 1; Transformation; SHARK ATTACK!!!

Assignment brief:
Back in the days before the internet, a football-themed game called Spot the Ball used to entertain us for aeons. Staring at a ball-devoid picture, we would guess and debate where the elusive ball was supposed to be. It was thrilling (eyeroll emoji). 

Use your new-found image processing skills to hide that ball.
    1.Convert the image "spottheball.jpg" to an appropriate colour space to segment the ball from the grass;
    2.Extract the ball from the image;
    3.Replace the hole left by the ball with "grass";
    4.The final image should be an ball-free image, as shown in "spottheballresult.jpg" ;
    5.Test the performance of your algorithm by comparing to "spottheballresult.jpg" and by trying snooker.jpg and golf.jpg.

Your design should work on the attached images but also on similar images of white balls against grassy backgrounds. Refer to the General Assignment Guidelines to maximise your marks. Submit your fully-commented py file here.

"""
# import the necessary packages:
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image


def set_cspace(I):
    HSVim = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
    return HSVim


def get_ball(I):
    #                   h   s   v
    min_HSV = np.array([0, 0, 80], dtype = "uint8")
    max_HSV = np.array([360, 30, 100], dtype = "uint8")

    whiteregHSV = cv2.inRange(I, min_HSV, max_HSV)
    return whiteregHSV

def grass(I):
    pass

def set_image(I):
    cv2.imshow("image", I)
    key = cv2.waitKey(0)

I = cv2.imread("spottheball.jpg")
Icolor = set_cspace(I)
ball = get_ball(Icolor)

set_image(ball)