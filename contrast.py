import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from PIL import Image

plt.gray()
img = Image.open('img/pollen.jpg')
arr = np.asarray(img)
a = deepcopy(arr)

print(arr[0])

size = len(arr)
sub = len(arr[1])
print(size)
print(sub)

def contrast(y):
    if(y >= 0 & y <= 100):
        ny=y*0.5
    elif(y > 100 & y <= 150):
        ny=(y-100)+50
    elif(y > 150 & y < 255):
        ny=(y-150)*(55/105)+200
    #ny = int(ny)
    #ny=((y-0) / (256-0))*255
    return ny


for i in range(len(arr)):
    for j in range(len(arr)):
        y = arr[i][j]
        a[i][j]= contrast(y)
        
plt.imshow(a)
print(a[0])
plt.show()
