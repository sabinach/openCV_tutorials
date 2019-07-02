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

# aspect_ratio: width / height
x, y, w, h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
print('aspect_ratio (width / height): {}'.format(aspect_ratio))

# extent: object area / bounding rectangle area
x, y, w, h = cv2.boundingRect(cnt)
area = cv2.contourArea(cnt)
rect_area = w*h
extent = float(area)/rect_area
print('extent (object area / bounding rect area): {}'.format(extent))

# solidity: contour area / convex hull area
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print('solidity (contour area / convex hull area): {}'.format(solidity))

# equivalent diameter
area = cv2.contourArea(cnt)
eq_diam = np.sqrt(4*area/np.pi)
print('equivalent diameter (sqrt(4*contour_area/pi)): {}'.format(eq_diam))

# object angle, major axis, minor axis
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
print('x:{}, y:{}, MA:{}, ma:{}, angle:{}'.format(x, y, MA, ma, angle))

# mask and pixel points
mask = np.zeros(imgray.shape, np.uint8)
pixelpoints = np.transpose(np.nonzero(mask))
print('pixelpoints: {}'.format(pixelpoints))

# min/max val, min/max loc
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray, mask=mask)
print('min_val:{}, max_val:{}, min_loc:{}, max_loc:{}'.format(min_val, max_val,
                                                              min_loc, max_loc))

# mean color
mean_color = cv2.mean(img, mask=mask)
print('mean_color:{}'.format(mean_color))

# extreme points
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
print('leftmost:{}, rightmost:{}, topmost:{}, bottommost:{}'.format(leftmost,
                                                                    rightmost,
                                                                    topmost,
                                                                    bottommost))

# draw contours
cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

# show image
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

