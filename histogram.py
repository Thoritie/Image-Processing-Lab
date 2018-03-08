import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('img/hill.jpg')

img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)

hist = cv2.calcHist([img],[0],None,[256],[0,256])

hist = cv2.calcHist([hist_equalization_result],[0],None,[256],[0,256])

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(hist_equalization_result)
plt.subplot(2, 2, 3)
plt.hist(img.ravel(),256,[0,256])

plt.subplot(2, 2, 4)
plt.hist(hist_equalization_result.ravel(),256,[0,256])
plt.show() 
