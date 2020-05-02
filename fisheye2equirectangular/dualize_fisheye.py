import cv2
import numpy as np
import sys

image = cv2.imread(sys.argv[1])

rimage = np.zeros(image.shape, dtype='uint8')

nimage = cv2.hconcat([image, rimage])

cv2.imwrite(sys.argv[2], nimage)
