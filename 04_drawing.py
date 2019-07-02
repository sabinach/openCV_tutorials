import numpy as np
import cv2

# create a black image
img = np.zeros((512,512,3),np.uint8)

# draw diagonal blue line w/ thickness 5px
# need: top-left corner, bottom-right corner coords
cv2.line(img,(0,0),(511,511),(255,0,0),5)   # BGR

# draw top-right corner green rectangle w/ thickness 3px
# need: top-left corner, bottom-right corner coordinates
cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

# draw circle inside rectangle, fill the circle
# need: center coordinate, radius
cv2.circle(img, (447,63), 63, (0,0,255), -1)

# draw ellipse
cv2.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)

# draw polygon
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
pts = pts.reshape((-1,1,2)) # shape: ROWS x 1 x 2
cv2.polylines(img, [pts], True, (0,255,255)) # is_closed: True

'''
# draw multiple lines using polylines
lines = np.array([(375, 193), (364, 113), (277, 20), (271, 16), (52, 106), 
                  (133, 266), (289, 296), (372, 282)])
cv2.polylines(img, [lines], False, (0, 255, 0), linetype=cv2.LINE_AA)
'''

# adding text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 2, cv2.LINE_AA)

# show image
cv2.imshow('shape drawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
