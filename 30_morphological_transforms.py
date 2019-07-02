import cv2
import numpy as np
from matplotlib import pyplot as plt

# read image
img = cv2.imread('cursive_j.png',0)

# kernel
kernel = np.ones((5,5), np.uint8)

# erosion
erosion = cv2.erode(img, kernel, iterations=1)

# dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# opening -> erosion followed by dilation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# closing -> dilation followed by erosion
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# morphological gradient -> difference between dilation and erosion
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# top hat -> difference between input and opening
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# black hat -> difference between closing and input
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# show image
plt.subplot(2,4,1), plt.imshow(img, cmap='gray')
plt.title('original')
plt.xticks([]), plt.yticks([])

plt.subplot(2,4,2), plt.imshow(erosion, cmap='gray')
plt.title('erosion')
plt.xticks([]), plt.yticks([])

plt.subplot(2,4,3), plt.imshow(dilation, cmap='gray')
plt.title('dilation')
plt.xticks([]), plt.yticks([])

plt.subplot(2,4,4), plt.imshow(opening, cmap='gray')
plt.title('opening')
plt.xticks([]), plt.yticks([])

plt.subplot(2,4,5), plt.imshow(closing, cmap='gray')
plt.title('closing')
plt.xticks([]), plt.yticks([])

plt.subplot(2,4,6), plt.imshow(gradient, cmap='gray')
plt.title('gradient')
plt.xticks([]), plt.yticks([])

plt.subplot(2,4,7), plt.imshow(tophat, cmap='gray')
plt.title('tophat')
plt.xticks([]), plt.yticks([])

plt.subplot(2,4,8), plt.imshow(blackhat, cmap='gray')
plt.title('blackhat')
plt.xticks([]), plt.yticks([])

plt.show()

'''
# show image
cv2.imshow('original', img)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
cv2.imshow('gradient', gradient)
cv2.imshow('tophat', tophat)
cv2.imshow('blackhat', blackhat)

# wait for keypress to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
'''
