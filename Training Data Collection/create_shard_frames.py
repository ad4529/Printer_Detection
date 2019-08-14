import os
import glob
from shutil import copyfile

cnt = 0

shard_id = 1
shard_start_path = '/home/abhisek/Desktop/Shards/Shard-'
shard_end_path = '/Yolo-Annotation-Tool-New-/Images/Frames/'

os.chdir('/home/abhisek/Desktop/YoloImages/Yolo-Annotation-Tool-New-/Images/Xerox_Aug1_Frames/')
home_dir = '/home/abhisek/Desktop/YoloImages/Yolo-Annotation-Tool-New-/Images/Xerox_Aug1_Frames/'
for frame in glob.glob('*.jpg'):
    copyfile(home_dir+frame, shard_start_path+str(shard_id)+shard_end_path+frame)
    cnt += 1

    if cnt % 500 == 0:
        shard_id += 1
