import os, shutil

partList="/media/davidzechm/LaCie/dataset/compcars/train_test_split/part/test_part_1.txt"
basePath="/media/davidzechm/LaCie/dataset/compcars/part"
dst="/media/davidzechm/LaCie/dataset/indicators"

paths = open(partList).read()
files = paths.split()

i=0
for each in files:
    i+=1
    path=os.path.join(basePath, each)
    shutil.copy(path, dst)
    print(str(i)+": copied" + str(each))


