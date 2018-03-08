import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#im = Image.open('img/LenaLow.jpg')
img = cv2.imread('img/LenaLow.png')
img = img/255.0
img_power_law_transformation = cv2.pow(img,3)


plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(img_power_law_transformation)
plt.show()
