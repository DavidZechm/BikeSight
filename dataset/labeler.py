import cv2, os
import numpy as np

curPath="/media/davidzechm/LaCie/dataset/labeled/right"

xmin=0
ymin=0
def boundingBox(event,x,y,flags,param):
    global xmin,ymin
    if event == cv2.EVENT_LBUTTONDOWN:
        xmin=x
        ymin=y
        cv2.circle(img, (xmin,ymin), 5, (255,0,255))
        cv2.imshow('image',img)
    if event==cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, (xmin,ymin), (x,y), (255,0,0), 3)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        img = cv2.imread(curPath)
        print("cleaned")
        cv2.imshow('image', img)

        f= open(os.path.join(str(curPath), str(imageName)+".txt"),"w+")
        f.write(str(each)+","+str(xmin)+","+str(ymin)+","+str(x)+","+str(y))
        f.write("\nlbl_name,xmin,ymin,xmax,ymax")
        f.close()

global img
for each in os.listdir(curPath):
    cur=each.split(".")
    imageName=cur[0]

    img=cv2.imread(os.path.join(curPath, each))
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',boundingBox)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20)
    if k == 13:
        break
    cv2.imshow('image',img)

cv2.destroyWindow("image")


