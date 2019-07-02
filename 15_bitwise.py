import cv2
import numpy as np

# load images
img1 = cv2.imread('scenic_background.jpg')
img2 = cv2.imread('tweety_bird.jpg')

# put logo in top corner 
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# create mask of logo
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) # convert to gray color space
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY) 
mask_inv = cv2.bitwise_not(mask)

# black out area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# take only region of logo from logo image
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
