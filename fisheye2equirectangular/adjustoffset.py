import cv2
import numpy as np
import sys

image = cv2.imread(sys.argv[1])
height, width = image.shape[0], image.shape[1]
print(f"{height},{width}")

center = (int(width/2), int(height/2))
radius = int(height/2)

while True:
    vimg = image.copy()

    cv2.circle(vimg, center, radius, (0, 255, 0), 2)

    print(f"center:{center[0]}({center[0] - int(width/2)}),{center[1]}({center[1] - int(height/2)}), radius:{radius}({radius - int(height/2)})")

    cv2.imshow('frame', vimg)

    k = cv2.waitKey(0)
    if k == 0: # up
        center = (center[0], center[1] - 1)
    elif k == 1: # down
        center = (center[0], center[1] + 1)
    elif k == 2: # left
        center = (center[0] - 1, center[1])
    elif k == 3: # right
        center = (center[0] + 1, center[1])
    elif k == ord('u'):
        radius += 1
    elif k == ord('d'):
        radius -= 1
    elif k == ord('q'):
        break

cv2.destroyAllWindows()
