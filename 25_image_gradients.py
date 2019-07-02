import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png',0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

'''
# threshold negative values to 0
laplacian[laplacian < 0] = 0
sobelx[sobelx < 0] = 0
sobely[sobely < 0] = 0
'''
'''
# invert the mask
laplacian_inv = cv2.bitwise_not(laplacian)
sobelx_inv = cv2.bitwise_not(sobelx)
sobely_inv = cv2.bitwise_not(sobely)
'''

# original
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('original')
plt.xticks([]), plt.yticks([])

# laplacian
plt.subplot(2, 2, 2)
plt.imshow(laplacian, cmap='gray')
plt.title('laplacian')
plt.xticks([]), plt.yticks([])

# sobel x
plt.subplot(2, 2, 3)
plt.imshow(sobelx, cmap='gray')
plt.title('sobelx')
plt.xticks([]), plt.yticks([])

# sobel y
plt.subplot(2, 2, 4)
plt.imshow(sobely, cmap='gray')
plt.title('sobely')
plt.xticks([]), plt.yticks([])

plt.show()
