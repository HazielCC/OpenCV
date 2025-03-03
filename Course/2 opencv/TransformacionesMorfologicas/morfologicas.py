# -*- coding: utf-8 -*-

import cv2
import numpy as np

# img = cv2.imread("coins.png", 0)
# _, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# kernel = np.ones((3,3), np.uint8)
# # erosion = cv2.erode(th, kernel, iterations = 1)
# dilatacion = cv2.dilate(th, kernel, iterations = 2)
# erosion = cv2.erode(dilatacion, kernel, iterations = 5)
# cv2.namedWindow("original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("imgErode", cv2.WINDOW_NORMAL)
# # cv2.namedWindow("imgDilate", cv2.WINDOW_NORMAL)
# cv2.imshow("original", img)
# cv2.imshow("imgErode", erosion)
# cv2.imshow("imgDilate", dilatacion)

# cv2.waitKey()
# cv2.destroyAllWindows()


# img = cv2.imread("coins.png", 0)
# _, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# kernel = np.ones((3,3), np.uint8)
# closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
# cv2.namedWindow("original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("close", cv2.WINDOW_NORMAL)
# cv2.imshow("original", img)
# cv2.imshow("close", closing)
# cv2.waitKey()
# cv2.destroyAllWindows()


# img = cv2.imread("opening.png", 0)
# _, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
# kernel = np.ones((3,3), np.uint8)
# erosion = cv2.erode(th, kernel, iterations = 1)
# dilatacion = cv2.dilate(erosion, kernel, iterations = 1)
# cv2.namedWindow("original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("erode", cv2.WINDOW_NORMAL)
# cv2.namedWindow("dilate", cv2.WINDOW_NORMAL)
# cv2.imshow("original", img)
# cv2.imshow("erode", erosion)
# cv2.imshow("dilate", dilatacion)
# cv2.waitKey()
# cv2.destroyAllWindows()


img = cv2.imread("opening.png", 0)
_, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
kernel = np.ones((3,3), np.uint8)
openX = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("open", cv2.WINDOW_NORMAL)
cv2.imshow("original", img)
cv2.imshow("open", openX)
cv2.waitKey()
cv2.destroyAllWindows()






