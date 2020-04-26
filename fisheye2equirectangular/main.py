import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(sys.argv[1])

f = 0
while True:
    f += 1
    print(f"f:{f}")

    ret, frame = cap.read()
    if not ret:
        break

    if f == 49:
        cv2.imwrite('test.png', frame)
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()