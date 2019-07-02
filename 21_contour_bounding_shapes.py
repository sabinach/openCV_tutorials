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

# get straight bounding rectangle
x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# get rotated bounding rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)

# get minimum enclosing circle
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
cv2.circle(img, center, radius, (255, 0, 0), 2)

# fit an ellipse
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img, ellipse, (255, 0, 0), 2)

# fit a line
# points, distType, param (0: optimal value), radius accuracy, angle accuracy
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
extreme_left = int((-x*vy/vx) + y) # get extreme left point
extreme_right = int(((cols-x)*vy/vx)+y) # get extreme right point

# draw line
# img, pt1, pt2, color, thickness
cv2.line(img, (cols-1, extreme_right), (0, extreme_left), 255, 2)

# draw contours
cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)


# show image
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
