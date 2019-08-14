import os
import glob

os.chdir('/home/abhisek/Desktop/YoloImages/Yolo-Annotation-Tool-New-/Labels/New_Frames')
annts = []

for file in glob.glob('*.txt'):
    with open(file, 'r') as f:
        annts.append(f.read())
    f.close()

os.chdir('/home/abhisek/Desktop/keras-yolo3/model_data')
cnt = 0
with open('paper_bin_annotations.txt', 'a') as f:
    for file in glob.glob('/home/abhisek/Desktop/YoloImages/Yolo-Annotation-Tool-New-/Labels/New_Frames/*.txt'):
        file = file.replace('Labels', 'Images')
        f.write(file[:-3] + 'jpg' + ' ')
        anns = annts[cnt].split('\n')
        for i in anns:
            f.write(i)
            f.write(' ')
        f.write('\n')
        cnt += 1
f.close()
