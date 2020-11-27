from __future__ import division
import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

# Importar imagen del dataset
imagen = cv2.imread('E:/UTN/PES/TP/Datasets/BSDS/BSDS300/images/train/314016.jpg',1)
# Se transforma la imagen BRG a HSV
imagen = cv2.cvtColor(imagen, cv2.cv.CV_BGR2HSV)

#valores = int(fseg_humano.readline().split('\n')[0])

# lectura del encabezado
estado = 0
header = 1
debug = 1
vector_img = []
segmento_img = []
fila_img = []
columna_img = []
with open(
    'F:/UTN/PES/TP/Datasets/BSDS/BSDS300/human/color/1107/314016.seg'
    ) as fseg_humano:    
    for linea in fseg_humano:
        linea = linea.replace('\n','')
        a = linea.split(' ')
        if header == 1:
            if (a[0] == 'width'):
                largo_img = int(a[1])
            if (a[0] == 'height'):
                alto_img = int(a[1])
            if (a[0] == 'segments'):
                segs_img = int(a[1])
            if (a[0] == 'data'):
                #segmentos = np.empty((segs_img, largo_img, alto_img), np.uint16)
                header = 0
        else:
            # lectura de los segmentos
            vector_img.append([[int(a[0]), int(a[1]), c] for c in np.arange(
                    int(a[2]),
                    int(a[3])
                    )])
            # 
            for c in np.arange(int(a[2]),int(a[3])):
                segmento_img.append(int(a[0]))
                fila_img.append(int(a[1]))
                columna_img.append(c)

colores = {
    '0': [0, 160, 160],
    '1': [10, 160, 160],
    '2': [20, 160, 160],
    '3': [30, 160, 160],
    '4': [40, 160, 160],
    '5': [50, 160, 160],
    '6': [60, 160, 160],
    '7': [70, 160, 160],
    '8': [80, 160, 160],
    '9': [90, 160, 160],
    '10': [100, 160, 160],
    '11': [110, 160, 160],
    '12': [120, 160, 160],
    '13': [130, 160, 160],
    '14': [140, 160, 160],
    '15': [150, 160, 160],
    '16': [160, 160, 160],
    '17': [170, 160, 160],
    '18': [180, 160, 160],
    '19': [0, 200, 200],
    '20': [20, 200, 200],
    '21': [40, 200, 200],
    '22': [60, 200, 200],
    '23': [80, 200, 200],
    '24': [100, 200, 200]
}

# Se obtienen los segmentos para graficar
img_segmentada = np.zeros((alto_img,largo_img,3), np.uint8)
try:
    for a in vector_img:
        for b in a:
            img_segmentada[b[1],b[2]] = colores.get(str(b[0]), [150,200,200])
except Exception as e:
    print("{} error: {}".format(a,e))

# Se arma las mascaras para cada uno de los segmentos
segmentos = np.zeros((segs_img,alto_img,largo_img,3), np.uint8)
try:
    for a in vector_img:
        for b in a:
            segmentos[b[0]][b[1],b[2]] = colores.get(str(b[0]), [150,200,200])
except Exception as e:
    print("{} error: {}".format(a,e))

# Se grafican los segmentos
fig = plt.figure(figsize=(10,6))
imagen_segmentos = np.zeros((segs_img,alto_img,largo_img,3), np.uint8)
for a in range(len(segmentos)):
    imagen_segmentos[a] = cv2.cvtColor(segmentos[a], cv2.COLOR_HSV2RGB)
    plt.subplot(4,6,a+1),plt.imshow(imagen_segmentos[a])
    plt.subplots_adjust(wspace=0.0)
    plt.title("Seg {}".format(a))
    plt.xticks([]),plt.yticks([])

plt.show()


# Los delfines están en los segmentos: 2, 3, 6, 8, 11
# Mientras que gran parte del fondo esta en los segmentos 0 y 1


# Se suman los segmentos a la imagen original y se grafica
fig = plt.figure(figsize=(10,6))
imagen_segmentada = np.zeros((segs_img,alto_img,largo_img,3), np.uint8)
for a in range(len(segmentos)):
    imagen_segmentada[a] = cv2.addWeighted(imagen,1,segmentos[a],0.4,0)
    imagen_segmentada[a] = cv2.cvtColor(imagen_segmentada[a], cv2.COLOR_HSV2RGB)
    plt.subplot(4,6,a+1),plt.imshow(imagen_segmentada[a])
    plt.subplots_adjust(wspace=0.0)
    plt.title("Seg {}".format(a))
    plt.xticks([]),plt.yticks([])

plt.show()



# Se grafican los segmentos con MATPLOTLIB
img_segmentada_rgb = cv2.cvtColor(img_segmentada, cv2.COLOR_HSV2RGB)
plt.imshow(img_segmentada_rgb)

# Se grafica la imagen con MATPLOTLIB
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_HSV2RGB)
plt.imshow(imagen_rgb)

plt.show()







# aplicar funcion a funcion y ver que devuelve
# mostrar distintos umbrales aplicados
# leer y redesarrollar


# Se grafican los segmentos con OPENCV
#img_segmentada_bgr = cv2.cvtColor(img_segmentada, cv2.COLOR_HSV2BGR)
#cv2.imshow('img_segmentada',img_segmentada_bgr)
