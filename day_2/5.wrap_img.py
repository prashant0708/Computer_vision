import cv2
import numpy as np

width , height = 256,500


img = cv2.imread("resources/cards.jpg")
cv2.imshow('cards', img)
cv2.waitKey(0)

pts1 = np.float32([[755,119],[1120,263],[516,676],[857,833]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width, height]])

metrix = cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(img, metrix, (width, height))

cv2.imshow('cards', img)
cv2.imshow('cards_warp', img_out)
cv2.waitKey(0)

"""   
This function is used to make any photo vertical


"""