#!/usr/bin/env python
"""This program will parse a video stream into it's component frames.

   Usage: Run the program and follow the on-screen directions to specify
          directory.

"""

__author__ = "Abhisek Dey"
__email__ = "ad4529@rit.edu"
__maintainer__ = "Ravi Gunda, Fritz Ebner"
__copyright__ = "Xerox Corp."

import cv2
import glob
import os

dir = input('Enter the video folder name inside the current directory (should be .mp4 videos only): ')
cnt = 0
os.mkdir(dir+'_frames')
for vid in glob.glob(dir + '/*.mp4'):
    vidcap = cv2.VideoCapture(vid)
    success,image = vidcap.read()

    while success:
        cv2.imwrite(dir + '_frames' + '/frame%d.jpg' % cnt, image)
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        cnt += 1
