import cv2
import numpy as np
import sys

image = cv2.imread(sys.argv[1])
cv2.imshow('frame', image)
cv2.waitKey(1)

input()

cv2.destroyAllWindows()
