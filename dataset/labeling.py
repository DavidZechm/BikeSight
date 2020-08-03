import cv2
import os
import shutil

rawPath="./raw"
leftPath="./labeled/left"
rightPath="./labeled/right"



img = cv2.imread("raw/1.jpeg")
print(img)

for img in os.listdir(rawPath):
    read = cv2.imread(os.path.join(rawPath, img))
    cv2.imshow("raw img", read)
    c=cv2.waitKey(0)

    if c==83: # move to folder right in labeled
        shutil.move(os.path.join(rawPath, img), rightPath)
    elif c==81: # move to folder left in labeled
        shutil.move(os.path.join(rawPath, img), leftPath)
    else: # avoid labeling errors for wrong key press
        break
    
