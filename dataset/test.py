import cv2

def click_event(event, x, y, flags, param):
    global img 
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        img = cv2.imread(img_path)
        print("cleaned")
        cv2.imshow('image', img)

img_path = "/media/davidzechm/LaCie/dataset/labeled/right/0a7b4aeb1649d8.jpg"   
global img        
img = cv2.imread(img_path)        

while(1):
    cv2.setMouseCallback('image', click_event)
    cv2.imshow('image', img)
    k=cv2.waitKey(1) & 0xFF
    if k==27: #Escape KEY
        break

    cv2.imshow('image', img)

cv2.destroyAllWindows()    