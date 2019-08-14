import os

os.chdir('/home/abhisek/Desktop/keras-yolo3/model_data')
with open('printer_annotations_hp_aug1.txt', 'r') as f:
    lines = f.readlines()
f.close()

lines = [l.strip('\n') for l in lines]

new_lines = ''
for line in lines:
    elements = line.split()
    new_lines += elements[0] + ' '
    for element in elements[1:]:
        vals = element.split(',')
        for id,val in enumerate(vals):
            if id == 4 and val == '8':
                new_lines += '9' + ' '
            elif id == 4 and val == '9':
                new_lines += '10' + ' '
            else:
                new_lines += val + ','
    new_lines += '\n'

with open('hp_aug1_id_changed.txt', 'w') as f:
    f.write(new_lines)
f.close()
