import cv2
import numpy as np

#img = cv2.imread('checkerboard.jpg')
img = cv2.imread('lego_blocks.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# consider overflow
gray = np.float32(gray)

# harris
# img, neighborhood blocksize, aperture parameter for Sobel, Harris detector
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# dilate for marking corners, not important to alg itself
dst = cv2.dilate(dst, None)

# threshold for optimal value, may change depending on image
img[dst > 0.01*dst.max()] = [0, 0, 255]

# show image
cv2.imshow('harris', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
