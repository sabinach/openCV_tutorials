import cv2
import numpy as np

img1 = cv2.imread('cereal_frostedflakes.jpg', 0)
img2 = cv2.imread('cereal_frostedflakes_more.jpg',0)

# initiate ORB detector
orb = cv2.ORB_create()

# find keypoints nad descriptors with ORB
kp1, desc1 = orb.detectAndCompute(img1, None)
kp2, desc2 = orb.detectAndCompute(img2, None)

# create matcher, use norm_hamming for ORB
bf_matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# get the best matches in two images
# matches objects have: distance, train descriptor index,
# query descriptor index, train image index
matches = bf_matcher.match(desc1, desc2)

# sort so best matches (lower distances) are first
matches = sorted(matches, key = lambda x: x.distance)

# draw first 10 matches
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

# show image
cv2.imshow('orb matches', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

