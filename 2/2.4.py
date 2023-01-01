import cv2 as cv
import sys
import matplotlib.pyplot as plt
import numpy as np

"""
Tan2022/12/31
保存图像
"""
if __name__ == '__main__':
    img = cv.imread('C:/Users/1/Pictures/timg.jpg')
    if img is None:
        print('Failed to read')
        sys.exit()
    else:
        # 添加alpha通道
        zeros = np.ones(img.shape[:2],dtype=img.dtype)*100
        result = cv.merge(([img,zeros]))
        print('原通道数为{}'.format(img.shape[2]))
        print('处理后的通道数{}'.format(result.shape[2]))

        # 展示图像
        plt.imshow(result)
        plt.show()

        # 保存图像
        # cv.imwrite('保存路径',result)


