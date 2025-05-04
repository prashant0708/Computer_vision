import cv2


## Reading images
img=cv2.imread('Resources/lena.png')
#print(img.shape)
## to see the image in console
#cv2.imshow('Output', img)
#cv2.waitKey(0) #it is important to keep showing in the console

## reading videos
# cap = cv2.VideoCapture('Resources/elon.mp4')
# while True:
#     success, img = cap.read()
#     print(img.shape) ## check the shape of the video
#     cv2.imshow('Output', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#      break


## reading the web camera

cap = cv2.VideoCapture(1)
cap.set(3,640) ## set width
cap.set(4,480) ##  set height
while True:
    success, img = cap.read()
    print(img.shape) ## check the shape of the video
    cv2.imshow('Output', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break

