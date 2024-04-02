## Developed by : Sanjay S
## Reg no       : 212221243002

## Read image and convert it to grayscale image
import numpy as np
import cv2
import matplotlib.pyplot as plt
my_img=cv2.imread("300.webp",0)
img=cv2.imread("300.webp",1)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(my_img,cv2.COLOR_GRAY2RGB)
gray = cv2.GaussianBlur(gray,(3,3),0)
plt.figure(figsize=(13,13))
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(gray)
plt.title("Gray Image")
plt.axis("off")
plt.show()

## Find the edges in the image using canny detector and display
canny=cv2.Canny(gray,120,150)
plt.imshow(canny)
plt.title("Canny Edge Detector")
plt.axis("off")
plt.show()

## Detect points that form a line using HoughLinesP
lines=cv2.HoughLinesP(canny,1,np.pi/180,threshold=80,minLineLength=50,maxLineGap=250)

## Draw lines on the image
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)

## Display the result
plt.imshow(img)
plt.title("Final Result")
plt.axis("off")
plt.show()

