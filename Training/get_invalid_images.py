import tensorflow as tf
from PIL import Image
import io
from tqdm import tqdm

with open('/home/abhisek/Desktop/keras-yolo3/model_data/coco_reduced_v3.txt', 'r') as f:
    lines = f.readlines()
f.close()

lines = [l.strip('\n') for l in lines]

for line in tqdm(lines):
    vals = line.split()

    with tf.gfile.GFile(vals[0], 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)

    if image.format != 'JPEG':
        print(vals[0])
