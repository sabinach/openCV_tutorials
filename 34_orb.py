import cv2

img = cv2.imread('lego_blocks.jpeg')

# initiate ORB detector
orb = cv2.ORB_create()

# find keypoints and descriptors
#keypoints = orb.detect(img, None)
#keypoints, descriptors = orb.compute(img, keypoints)
keypoints, descriptors = orb.detectAndCompute(img, None)

# draw only keypoint locations, not size or orientation
cv2.drawKeypoints(img, keypoints, img, color=(0,255,0), flags=0)

cv2.imshow('orb', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
