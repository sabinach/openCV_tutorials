#################
# IMPORTANT: RUN USING 'python2.7' NOT 'python' 
#################

# SURF: faster version of SIFT

import cv2

img = cv2.imread('mit_stata_center.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create surf object, set hessian threshold to 400
surf = cv2.xfeatures2d.SURF_create(400)

# check present Hessian threshold
print('initial Hessian threshold: {}'.format(surf.getHessianThreshold))

# keypoint attributes: (x,y), meaningful neighborhood, angle, strength, etc.
(keypoints, descriptors) = surf.detectAndCompute(gray, None) # img, mask
print('# keypoints: {}, descriptors: {}'.format(len(keypoints),
                                                descriptors.shape))

# set higher hessian threshold
surf.setHessianThreshold(10000)

# keypoint attributes: (x,y), meaningful neighborhood, angle, strength, etc.
(keypoints, descriptors) = surf.detectAndCompute(gray, None) # img, mask
print('# keypoints: {}, descriptors: {}'.format(len(keypoints),
                                                descriptors.shape))

# [flags] 0: kp + grayscale, 1: kp + color, etc.
#flag = 1
flag = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS # draws kp size + orient)

# draw keypoints on image: src, keypoints, output, flags
cv2.drawKeypoints(gray, keypoints, img, flags=flag)
cv2.imshow('img',img)

#img2 = cv2.drawKeypoints(gray, keypoints, None, (0,0,255), 4)
#cv2.imshow('img', img2)

# wait for exit keypress
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

