import cv2
import numpy as np

#1. convert the gray scale

# img = cv2.imread('resources/lena.png')

# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# print("Original_shape",img.shape)

# print("Original_shape",img_gray.shape)

# cv2.imshow("Color_img",img)

# cv2.imshow("Gray_img",img_gray)

# cv2.waitKey(0)



## Blur image 

# img = cv2.imread('resources/lena.png')

# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray,(7,7),0.5)

# print("Original_shape",img.shape)

# print("Original_shape",img_gray.shape)
# print("Original_shape",img_blur.shape)

# cv2.imshow("Color_img",img)

# cv2.imshow("Gray_img",img_gray)
# cv2.imshow("blur_img",img_blur)

# cv2.waitKey(0)


##convert to the canny image

img = cv2.imread('resources/lena.png')

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7),500)
img_canny = cv2.Canny(img_blur,50,40)
print("Original_shape",img.shape)

print("Original_shape",img_gray.shape)
print("Original_shape",img_blur.shape)
print("Original_shape",img_canny.shape)

cv2.imshow("Color_img",img)

cv2.imshow("Gray_img",img_gray)
cv2.imshow("blur_img",img_blur)
cv2.imshow("img_canny",img_canny)
cv2.waitKey(0)


