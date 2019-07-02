import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('diagonal-checkerboard.jpg')
rows, cols, channels = img.shape

# WE NEED FOUR POINTS
# specify the numpy point transformations
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# draw dots to compare transformation
for pts in pts1:
    cv2.circle(img, (pts[0], pts[1]), 10, (0,255,0), -1)

# get transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# warp image via specified transformation matrix
dst = cv2.warpPerspective(img, M, (cols, rows))

# input image
plt.subplot(121)
plt.imshow(img)
plt.title('Input')

# output image
plt.subplot(122)
plt.imshow(dst)
plt.title('Output')

plt.show()
