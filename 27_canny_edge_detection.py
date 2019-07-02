import cv2
import numpy as np
from  matplotlib import  pyplot as plt

img = cv2.imread('pupper.jpg',0) # grayscale image
edges = cv2.Canny(img, 100, 200) # src, minVal, maxVal, aperture_size (default=3)

# show original
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.xticks([]), plt.yticks([])

# show edges
plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title('Edge Image')
plt.xticks([]), plt.yticks([])

plt.show()
