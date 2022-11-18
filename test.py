# -*- coding: utf-8 -*-
# @Author: mykko
# @Date:   2022/11/17 14:48


import os.path
import cv2
import numpy as np
from matplotlib import pyplot as plt

image_dir = "/Users/mykko/Documents/project/decision/data/videos_images/"
video_name = "video1"
image_name = "00000140.jpg"


def callback(x):
    print(x)

def main():
    image_path = os.path.join(image_dir, video_name, image_name)

    src = cv2.imread(image_path)
    src_crop = src[0:200, 550:750]
    src = src_crop

    HSV = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    minGreen = np.array([60, 50, 50])
    maxGreen = np.array([110, 255, 255])

    # 通过掩码控制的按位与运算，锁定蓝色、绿色、红色区域
    mask = cv2.inRange(HSV, minGreen, maxGreen)
    green = cv2.bitwise_and(src, src, mask=mask)

    imgadd1 = cv2.add(src, green)
    img = cv2.addWeighted(src, 0.5, green, 1, 0)

    cv2.namedWindow('show', cv2.WINDOW_NORMAL)

    h, w, _ = img.shape
    cv2.createTrackbar('kernel', 'show', 3, min(h, w), callback)
    cv2.setTrackbarMin('kernel', 'show', 3)

    src_img = img
    while (1):
        cv2.imshow('show', img)
        if cv2.waitKey(1) == 27:
            break
        # 获取窗口'show'滑动条'kernel'当前值
        k = cv2.getTrackbarPos('kernel', 'show')
        img = cv2.blur(src_img, (k, k))


if __name__ == '__main__':
    main()
    print('done')