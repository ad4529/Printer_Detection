import os
os.chdir('/home/abhisek/Desktop/keras-yolo3/model_data')

with open('coco_reduced_v3.txt', 'r') as f:
    lines = f.readlines()
f.close()

lines = [l.strip('\n') for l in lines]

cnt = 0
for i in lines:
    vals = i.split()
    vals = vals[1:]
    for j in vals:
        nums = j.split(',')
        if len(nums) < 5 or len(nums) > 5:
            print(i)
            cnt += 1

print(cnt)
