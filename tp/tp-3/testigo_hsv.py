from __future__ import division
import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

testigo = np.zeros((150,400,3), np.uint8)
cv2.namedWindow('testigo')
cv2.createTrackbar('H','testigo',0,180,nothing)
cv2.createTrackbar('S','testigo',0,255,nothing)
cv2.createTrackbar('V','testigo',0,255,nothing)

while(1):
    h = cv2.getTrackbarPos('H','testigo')
    s = cv2.getTrackbarPos('S','testigo')
    v = cv2.getTrackbarPos('V','testigo')

    testigo[:] = [h,s,v]
    cv2.imshow('testigo',testigo)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()