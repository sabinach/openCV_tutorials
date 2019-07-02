import cv2
import numpy as np

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# get edges
edges = cv2.Canny(gray, 50, 100, apertureSize=3) # vary min/max val

# detect optimized hough lines
min_line_length = 300
max_line_gap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi/180.0, 100, min_line_length, max_line_gap)

for line in lines:
    # get line coordinates
    x1, y1, x2, y2 = line[0][0:4]

    # draw lines on image
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

# show images
cv2.imshow('edges', edges)
cv2.imshow('hough lines', img)

# wait for keypress to exit 
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
