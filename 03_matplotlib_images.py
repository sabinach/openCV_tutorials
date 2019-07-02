import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('pupper.jpg',0)
plt.imshow(img, cmap='gray', interpolation='bicubic')

# hide x and y -axis tick values
plt.xticks([])
plt.yticks([])
plt.show()
