import cv2
import sys

image = cv2.imread(sys.argv[1])

rimage = cv2.flip(image, 1)

nimage = cv2.hconcat([image, rimage])

cv2.imwrite(sys.argv[2], nimage)
