import cv2
import numpy as np

# read image
img = cv2.imread('pupper.jpg')

# get image shape
rows, cols, channels = img.shape

# resize image
#res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# translate image, shift: 100 -> 50
M = np.float32([[1, 0, 100], [0, 1, 50]])
shifted = cv2.warpAffine(img, M, (cols, rows))

# rotate image 90 degrees wrt to center 
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rot = cv2.warpAffine(shifted, M, (cols, rows))

# show image
cv2.imshow('resized', rot)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
