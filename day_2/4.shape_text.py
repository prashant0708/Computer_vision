import cv2
import numpy as np

## create shape like line ,rectangle and circle


img = np.zeros((512,512,3),np.uint8)  
"""   
np.uint8 : it mean numpy will create array 
and each value in array range from 0 to 255 
it take 1 byte per value
it does not support negative value
"""
print(img.shape)
img[:] = 255,255,0 #BGR 0,0,0 # Make entire image blue ,img[:] is equivalent to img[:, :, :] in a 3D image array.
# cv2.imshow('Image', img)
# cv2.waitKey(0)


# creatre a line

#cv2.line(img,(0,0),(250,350),(0,0,255),5)
"""  
(0,0) - starting point of line(x,y)cordinate
(250,350) - ending points of line
(0,0,255) - color of the line
5 - thickness of the line

"""

# cv2.imshow('Image', img)
# cv2.waitKey(0)

## create horizental line in the center of the frame 
# cv2.line(img,(10,256),(492,256),(0,0,255),5)

# """ 
# tottal frame size is 512 x 512 amd half of that is 256 vertically 

# """

# cv2.imshow('Image', img)
# cv2.waitKey(0)

# create rectangle
# cv2.rectangle(img,(10,100),(492,256),(0,0,255),7)## first rectangle
# cv2.rectangle(img,(10,266),(492,412),(0,0,255),7) ## second rectangle
# cv2.imshow('Image', img)
# cv2.waitKey(0)


### Create circle at the center of the frame with radious 100

# cv2.circle(img,(256,256),100,(0,50,100),4)
# cv2.imshow('Image', img)
# cv2.waitKey(0)

### Put texts
cv2.putText(img,"Data Den Prashant",(100,256),cv2.FONT_HERSHEY_COMPLEX,1, (0,0,0), 5)
cv2.imshow("Image",img)
cv2.waitKey(0)
