import os

os.chdir('/home/abhisek/Desktop/keras-yolo3/model_data')

with open('reduced_coco_classes.txt', 'r') as f:
    classes = f.readlines()
f.close()

classes = [clas.strip('\n') for clas in classes]

class_map = {}

out = ''
for ID, name in enumerate(classes):
    out += 'item' + ' ' + '{' + '\n'
    out += '  ' + 'id:' + ' ' + str(ID+1) + '\n'
    out += '  ' + 'name: ' + '\'' + name + '\'\n'
    out += '}' + '\n\n'

os.chdir('/home/abhisek/Desktop/MobileSSD')

with open('printer_classes.pbtxt', 'w') as f:
    f.write(out)
f.close()
