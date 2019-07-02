import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('diagonal-checkerboard.jpg')
rows, cols, channels = img.shape

# ONLY NEED THREE POINTS
# specify the numpy point transformations
pts1 = np.float32([[50, 50], [200, 50],[50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# draw dots to compare transformation
for pts in pts1:
    cv2.circle(img, (pts[0], pts[1]), 10, (0,255,0), -1)

# get transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# warp image via specified transformation matrix
dst = cv2.warpAffine(img, M, (cols, rows))

# input image
plt.subplot(121)
plt.imshow(img)
plt.title('Input')

# output image
plt.subplot(122)
plt.imshow(dst)
plt.title('Output')

plt.show()
