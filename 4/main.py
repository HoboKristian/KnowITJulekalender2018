import numpy as np
import cv2

img = (cv2.imread("./input-pokemon-jakt.png") & 15) * 16
cv2.imshow(" ", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
