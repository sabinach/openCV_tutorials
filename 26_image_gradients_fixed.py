import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png',0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)

# output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

# original
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('original')
plt.xticks([]), plt.yticks([])

# sobel x
plt.subplot(1, 3, 2)
plt.imshow(sobelx8u, cmap='gray')
plt.title('sobelx8u')
plt.xticks([]), plt.yticks([])

# sobel y
plt.subplot(1, 3, 3)
plt.imshow(sobel_8u, cmap='gray')
plt.title('sobel abs(CV_64F)')
plt.xticks([]), plt.yticks([])

plt.show()
