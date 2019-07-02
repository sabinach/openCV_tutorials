####################
# IMPORTANT: RUN USING 'python2.7' NOT 'python'
####################

import cv2
import numpy as np

# GOOD
#img1 = cv2.imread('cereal_frostedflakes.jpg', 0)
#img2 = cv2.imread('cereal_frostedflakes_more.jpg',0)

# VERY GOOD 
img1 = cv2.imread('cereal_honeybunches.png', 0)
img2 = cv2.imread('cereal_brands.jpg', 0)

# ERROR
#img1 = cv2.imread('cereal_frootloops.jpeg', 0)
#img2 = cv2.imread('cereal_brands.jpg', 0)

# initiate ORB detector
sift = cv2.xfeatures2d.SIFT_create()

# find keypoints nad descriptors with ORB
kp1, desc1 = sift.detectAndCompute(img1, None)
kp2, desc2 = sift.detectAndCompute(img2, None)

# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50) # or pass empty dictionary

# create flann matcher object
flann = cv2.FlannBasedMatcher(index_params, search_params)

# get the k best matches in two images
# matches objects have: distance, train descriptor index,
# query descriptor index, train image index
matches = flann.knnMatch(desc1, desc2, k=2)

# apply ratio test
good = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good.append(m)

MIN_MATCH_COUNT = 10
if len(good) > MIN_MATCH_COUNT:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp1[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()

    h, w = img1.shape
    pts = np.float32([ [0,0], [0,h-1], [w-1,h-1], [w-1,0] ]).reshape(-1,1,2) 
    dst = cv2.perspectiveTransform(pts, M)

    img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
else:
    print('Not enough matches were found - {}/{}'.format(len(good), MIN_MATCH_COUNT))
    matchesMask = none

# drawing parameters
draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = None,
                   matchesMask = matchesMask,
                   flags = 2)

# draw first 10 matches
img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)

# show image
cv2.imshow('sift matches w/ flann matcher + RANSAC', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

