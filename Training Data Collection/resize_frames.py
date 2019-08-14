#!/usr/bin/env python
"""This program will resize any images which are bigger than 1200x800
   This has been done in order for the image to be completely rendered
   in the Annotation Tool for monitors with lower resolution.

   Usage: Run the program and follow the on-screen directions to specify
          directory.

"""

__author__ = "Abhisek Dey"
__email__ = "ad4529@rit.edu"
__maintainer__ = "Ravi Gunda, Fritz Ebner"
__copyright__ = "Xerox Corp."


import os
import glob
import cv2
from tqdm import tqdm

os.chdir('/home/abhisek/Desktop/YoloImages/Yolo-Annotation-Tool-New-/Images')
sub_dir = input('Enter the image subdirectory to resize inside /home/abhisek/Desktop/YoloImages/Yolo-Annotation-Tool-New-/Images: ')
dirs = [sub_dir]

for dir in dirs:
    for file in tqdm(glob.glob(dir+'/*.jpg')):
        im = cv2.imread(file)
        height, width = im.shape[:2]
        if height > 800 or width > 1200:
            im = cv2.resize(im, (1200, 800))
            cv2.imwrite(file, im)
