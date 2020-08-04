import cv2
import os
import shutil

rawPath="./dataset/raw"
rightPath="./dataset/labeled/right"
leftPath="./dataset/labeled/left"
frontPath="./dataset/labeled/front"
nonePath="./dataset/labeled/none"

i=0
for img in os.listdir(rawPath):
    read = cv2.imread(os.path.join(rawPath, img))
    cv2.imshow("raw img", read)
    i+=1;   print(str(i) + " : " + img)
    c=cv2.waitKey(0)

    if c==83: # move to folder right in labeled
        shutil.move(os.path.join(rawPath, img), rightPath)
    elif c==81: # move to folder left in labeled
        shutil.move(os.path.join(rawPath, img), leftPath)
    elif c==82: # move to folder front in labeled
        shutil.move(os.path.join(rawPath, img), frontPath)
    elif c==84: # move to folder none in labeled
        shutil.move(os.path.join(rawPath, img), nonePath)
    else: # avoid labeling errors for wrong key press
        break
