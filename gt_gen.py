import json
import shutil
import os
gt_path = "/home/diva/MASK_LABEL/gt/all"
split_path = "/home/diva/MASK_LABEL/gt/tst"
if not os.path.exists(split_path):
    os.makedirs(split_path)


indexes = os.listdir("./json/json_test")
for index in indexes:
    src = os.path.join(gt_path,index)
    dst = os.path.join(split_path,index)
    shutil.copy(src,dst)
