import cv2
import numpy as np

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# get edges
edges = cv2.Canny(gray, 50, 100, apertureSize=3) # vary min/max val

# detect hough lines
lines = cv2.HoughLines(edges, 1, np.pi/180.0, 200)
for line in lines:
    rho = line[0][0]
    theta = line[0][1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    # draw lines on image
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

# show images
cv2.imshow('edges', edges)
cv2.imshow('hough lines', img)

# wait for keypress to exit 
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
