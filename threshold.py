import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from PIL import Image

plt.gray()

img = Image.open('img/cameraman.png')
arr = np.asarray(img)
a = deepcopy(arr)

def getGrayColor(rgb):
    return rgb[0]

def setGrayColor(color):
    return color


count = 0 
sum = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        count = count + 1
        sum += arr[i][j]
k = sum / count


for i in range(len(arr)):
    for j in range(len(arr)):
        y = arr[i][j]
        if(y < k):
            a[i][j] = setGrayColor(0) 
        elif(y >= k):
            a[i][j] = setGrayColor(255)



plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(a)
plt.show()
