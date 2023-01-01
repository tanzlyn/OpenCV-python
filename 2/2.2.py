import cv2 as cv
import numpy as np
import datetime
import sys

"""
Tan2022/12/30
NumPy和OpenCV对比
"""
if __name__ == '__main__':
    image = cv.imread('C:/Users/1/Pictures/timg.jpg')
    # 判断是否读取成功
    if image is None:
        print('failed to read timg.jpg')
        sys.exit()

    ## 对比通道分离

    # 使用opencv的cv.split()
    begin1 = datetime.datetime.now()
    for i in range(100000):
        b1,g1,r1 = cv.split(image)
    end1 = datetime.datetime.now()
    print('通道分离（opencv）：{}'.format((end1-begin1).total_seconds()))

    # 使用NumPy的切片和索引
    begin2 = datetime.datetime.now()
    for i in range(100000):
        b2 = image[:,:,0]
        g2 = image[:, :, 0]
        r2 = image[:, :, 0]
    end2 = datetime.datetime.now()
    print('通道分离（numpy）：{}'.format((end2 - begin2).total_seconds()))

    ## 将BGR图像转化为RGB图像

    # 使用opencv中的cv.cvtcolor函数
    begin3 = datetime.datetime.now()
    for i in range(100000):
        image_grb = cv.cvtColor(image,cv.COLOR_RGB2RGB)
    end3 = datetime.datetime.now()
    print('RGB转BRG（opencv）：{}'.format((end3 - begin3).total_seconds()))

    # 使用NumPy中的切片和索引
    begin4 = datetime.datetime.now()
    for i in range(100000):
        image_grb = image[:,:,::-1]
    end4 = datetime.datetime.now()
    print('RGB转BRG（numpy）：{}'.format((end4 - begin4).total_seconds()))




