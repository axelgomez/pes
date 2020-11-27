from __future__ import division
import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

hminsv = np.zeros((100,200,3), np.uint8)
hmaxsv = np.zeros((100,200,3), np.uint8)
hsvmin1 = np.zeros((100,200,3), np.uint8)
hsvmax1 = np.zeros((100,200,3), np.uint8)
hsvmin2 = np.zeros((100,200,3), np.uint8)
hsvmax2 = np.zeros((100,200,3), np.uint8)

cv2.namedWindow('mask')
cap = cv2.VideoCapture(0)
# create trackbars for color change
cv2.createTrackbar('Hmin','mask',0,180,nothing)
cv2.createTrackbar('Hmax','mask',0,180,nothing)
cv2.createTrackbar('S','mask',0,255,nothing)
cv2.createTrackbar('Vmin','mask',0,255,nothing)
cv2.createTrackbar('Vmax','mask',0,255,nothing)

while(1):

    # Captura un frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    hmin = cv2.getTrackbarPos('Hmin','mask')
    hmax = cv2.getTrackbarPos('Hmax','mask')
    s = cv2.getTrackbarPos('S','mask')
    vmin = cv2.getTrackbarPos('Vmin','mask')
    vmax = cv2.getTrackbarPos('Vmax','mask')
    lower_green = np.array([hmin,s,vmin])
    upper_green = np.array([hmax,255,vmax])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask= mask)
    
    # para graficar los hsv minimos y maximos
    hminsv[:] = [hmin,s,(vmin+vmax)/2]
    hsv_min = cv2.cvtColor(hminsv, cv2.COLOR_HSV2BGR)
    hmaxsv[:] = [hmax,s,(vmin+vmax)/2]
    hsv_max = cv2.cvtColor(hmaxsv, cv2.COLOR_HSV2BGR)

    hsvmin1[:] = [hmin,s,vmin]
    hsv_min1 = cv2.cvtColor(hsvmin1, cv2.COLOR_HSV2BGR)
    hsvmax1[:] = [hmin,s,vmax]
    hsv_max1 = cv2.cvtColor(hsvmax1, cv2.COLOR_HSV2BGR)

    hsvmin2[:] = [hmax,s,vmin]
    hsv_min1 = cv2.cvtColor(hsvmin1, cv2.COLOR_HSV2BGR)
    hsvmax2[:] = [hmax,s,vmin]
    hsv_max1 = cv2.cvtColor(hsvmax1, cv2.COLOR_HSV2BGR)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('hsv_min',hminsv)
    cv2.imshow('hsv_max',hmaxsv)
    cv2.imshow('hsv_min1',hsvmin1)
    cv2.imshow('hsv_max1',hsvmax1)
    cv2.imshow('hsv_min2',hsvmin2)
    cv2.imshow('hsv_max2',hsvmax2)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()