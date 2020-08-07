import os
from PIL import Image

rightPath="/media/davidzechm/LaCie/dataset/labeled/right"
leftPath="/media/davidzechm/LaCie/dataset/labeled/left"
frontPath="/media/davidzechm/LaCie/dataset/labeled/front"

resWidth=900
resHeight=600

for img in os.listdir(leftPath):
    read = Image.open(os.path.join(leftPath, img))
    resImage = read.resize((resWidth, resHeight))
    resImage.save(os.path.join(leftPath, img))
