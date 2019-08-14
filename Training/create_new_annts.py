import os
import glob

os.chdir('/home/abhisek/Desktop/keras-yolo3/model_data')

with open('coco_annotations.txt', 'r') as f:
    lines = f.readlines()
f.close()

lines = [l.strip('\n') for l in lines]

os.chdir('/home/abhisek/Downloads/')

with open('coco_classes_ranked.txt','r') as f:
    c_lines = f.readlines()
f.close()

c_lines = [c.strip('\n') for c in c_lines]
new_c = []
new_classes = ''

for idx,line in enumerate(c_lines):
    if '3' in line:
        new_c.append(idx)
        new_classes += (line[2:] + '\n')

os.chdir('/home/abhisek/Desktop/keras-yolo3/model_data')
with open('reduced_coco_classes.txt', 'w') as f:
    f.writelines(new_classes)
f.close()

new_ann = ''
cnt = 0
for line in lines:
    new_line = ''
    l_vals = line.split()
    new_line += (l_vals[0] + ' ')
    for vals in l_vals[1:]:
        val = vals.split(',')
        if int(val[-1]) in new_c:
            for v in val[:-1]:
                new_line += (v + ',')
            new_line += (str(new_c.index(int(val[-1]))) + ' ')

    if not new_line == (l_vals[0] + ' '):
        new_ann += (new_line + '\n')
        cnt += 1
os.chdir('/home/abhisek/Desktop/keras-yolo3/model_data')

with open('only_coco_reduced_v2.txt', 'w') as f:
    f.write(new_ann)
f.close()
