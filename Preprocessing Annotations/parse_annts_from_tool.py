import glob
import os

os.chdir('/home/abhisek/Desktop/YoloImages/Yolo-Annotation-Tool-New-/Labels/extra_class_frames')

annts = []
cnt = 0

for file in glob.glob('*.txt'):
    with open(file, 'r') as f:
        annts = f.read()
    f.close()
    if len(annts) == 0:
        os.remove(file)
    else:
        annt = annts.split()

        lines = ''
        # for i,val in enumerate(annt):
        #     if i%5 == 4 and val == '0':
        #         annt[i] = '81'

        for i,val in enumerate(annt):

            if i % 5 == 4 and len(val) <= 2:
                lines += (val + '\n')
            elif len(val) <= 4:
                lines += (val + ',')

        if len(lines) > 0:
            with open(file, 'w') as f:
                f.write(lines)
            f.close()
        else:
            os.remove(file)