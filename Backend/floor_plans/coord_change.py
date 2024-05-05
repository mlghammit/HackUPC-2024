import numpy as np
import matplotlib.pyplot as plt

x1, y1 = (41,3882846, 2,1121803)
x2, y2 = (41,3885235, 2,1125055)

import cv2
from google.colab.patches import cv2_imshow

path = 'blueprint_resaltado.jpg'

img = cv2.imread(path)
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss15 = cv2.GaussianBlur(gris, (15,15), 0)
canny = cv2.Canny(gauss15, 50, 150)
cv2_imshow(canny)

lenF, lenC = canny.shape

sum_columnas = np.sum(canny, axis=0)
plt.plot(sum_columnas)
threshold = np.quantile(sum_columnas, 0.995)
picos = sum_columnas[sum_columnas >= threshold]
xs = [list(sum_columnas).index(p) for p in picos]
print(Xs)

sum_filas = np.sum(canny, axis=1)
plt.plot(sum_filas)
threshold = np.quantile(sum_filas, 0.995)
picos = sum_filas[sum_filas >= threshold]
Ys = [list(sum_filas).index(p) for p in picos]
print(Ys)
