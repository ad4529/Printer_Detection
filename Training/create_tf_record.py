import tensorflow as tf
from random import shuffle
import cv2
import sys
sys.path.insert(0, '/home/abhisek/Desktop/models/research/object_detection')
import os
from utils import dataset_util
import numpy as np
from tqdm import tqdm
import contextlib2
import io
from PIL import Image

def create_tf_example(instance, classes_list):
    vals = instance.split()
    filename = bytes(vals[0], 'utf-8')
    with tf.gfile.GFile(vals[0], 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)

    if image.format != 'JPEG':
        raise ValueError('Image format not JPEG! -> %s' % vals[0])
    width, height = image.size

    image_format = b'jpeg'

    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    vals = vals[1:]
    try:

        for val in vals:
            cords = val.split(',')
            xmins.append(float(cords[0])/width)
            ymins.append(float(cords[1])/height)
            xmaxs.append(float(cords[2])/width)
            ymaxs.append(float(cords[3])/height)
            classes.append(int(cords[4]) + 1)
            classes_text.append(bytes(classes_list[int(cords[4])], 'utf-8'))
    except:
        print('OOps! Error in encoding with this instance')
        print(instance)
        exit(1)

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))

    return tf_example



def main():
    os.chdir('/home/abhisek/Desktop/keras-yolo3/model_data')

    with open('coco_reduced_v3.txt', 'r') as f:
        lines = f.readlines()
    f.close()

    lines = [l.strip('\n') for l in lines]
    shuffle(lines)
    tot = len(lines)
    val_split = int(0.1*tot)

    validation = lines[:val_split]
    training = lines

    sets = [training, validation]

    out_paths = ['/home/abhisek/Desktop/MobileSSD/train_dataset.record', '/home/abhisek/Desktop/MobileSSD/val_dataset.record']
    num_shards = 10

    with open('/home/abhisek/Desktop/keras-yolo3/model_data/reduced_coco_classes.txt', 'r') as f:
        classes = f.readlines()
        classes = [c.strip('\n') for c in classes]
    f.close()

    for id, data in enumerate(sets):

        writer = tf.python_io.TFRecordWriter(out_paths[id])
        for idx, instance in enumerate(tqdm(data)):

            tf_example = create_tf_example(instance, classes)
            writer.write(tf_example.SerializeToString())
        writer.close()

if __name__ == '__main__':
    main()
