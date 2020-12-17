# -*- coding: utf-8 -*-

from __future__ import division
import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

# Importar imagen del dataset
ruta_img = 'E:/UTN/PES/TP/Datasets/BSDS/BSDS300/images/train/314016.jpg'

cv2.namedWindow('contornos')
cv2.createTrackbar('umbral','contornos',0,255,nothing)

while(1):

    # Se probará findContour
    imagen = cv2.imread(ruta_img)
    imagen_gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

    umbral = cv2.getTrackbarPos('umbral','contornos')

    ret, thresh = cv2.threshold(imagen_gray,umbral,255,0)
    contours, hierarchy = cv2.findContours(
        thresh,                  # imagen a contornear
        cv2.RETR_TREE,           # contour retrieval mode
        cv2.CHAIN_APPROX_SIMPLE  # contour approximation method
    )  
    # para graficar todos los contornos de la imagen
    cv2.drawContours(imagen, contours, -1, (180,100,0), 3)

    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
    fig = plt.figure(figsize=(10,7))
    plt.xticks([]),plt.yticks([])
    plt.imshow(imagen)
    plt.show()
    plt.pause(0.01)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWinows()