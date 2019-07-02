import cv2
import numpy as np

# load image
img = cv2.imread('colored_shapes.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# get contours based on threshold
ret, thresh = cv2.threshold(imgray, 200, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, 
                                       cv2.CHAIN_APPROX_SIMPLE)

# get specific contour
cnt = contours[1]

# get contour area
area = cv2.contourArea(cnt)
print('area: {}'.format(area))

# get contour moment
M = cv2.moments(cnt)
print('moment: {}'.format(M))

# get contour perimeter
perimeter = cv2.arcLength(cnt, True)
print('perimeter: {}'.format(perimeter))

# check if convex
convex = cv2.isContourConvex(cnt)
print('convex: {}'.format(convex))

# get contour approx
epsilon = 0.1*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)

# draw contour
cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

# show image
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
