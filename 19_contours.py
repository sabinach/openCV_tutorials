import cv2
import numpy as np

img = cv2.imread('colored_shapes.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 200, 255, 0)

# src image, contour retrieval mode, contour approx
# cv2.CHAIN_APPROX_NONE: stores all boundary points
# cv2.CHAIN_APPROX_SIMPLE: removes redundant points
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

# src image, contours list, index of contours
# -1 -> draw all contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# select the 3rd contour
#cv2.drawContours(img, contours, 1, (0, 255, 0), 3)

# select specific contour
#cnt = contours[1]
#cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
