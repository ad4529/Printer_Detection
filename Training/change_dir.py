import os
os.chdir('/home/abhisek/Desktop/keras-yolo3/model_data')

with open('coco_reduced_v2.txt', 'r') as f:
    lines = f.readlines()
f.close()

new_lines = ''
for line in lines:
    if 'ad0915' in line:
        new_lines += line.replace('ad0915', 'abhisek')
    else:
        new_lines += line

with open('coco_reduced_v3.txt', 'w') as f:
    f.write(new_lines)
f.close()
