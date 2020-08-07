import cv2
import os

curFolder="./dataset/labeled/front"
xml="./dataset/labeled/xml"

for img in os.listdir(curFolder):
    read = cv2.imread(os.path.join(curFolder, img))

    if cv2.EVENT_LBUTTONDOWN:
        print("XXX")

    sp=(0,0)
    ep=(100,100)
    color = (0, 255, 0)

    draw = cv2.rectangle(read, sp, ep, color, 2)
    cv2.imshow("raw", draw)
    c=cv2.waitKey(0)