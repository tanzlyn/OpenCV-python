import cv2 as cv
import numpy as np
import datetime
import sys

"""
Tan2022/12/30
NumPy相关函数操作:创建对象、切片索引、生成随机数
"""

if __name__ == '__main__':
    # 创建5×5、数据类型为float32的矩阵
    a = np.array([[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20],
                  [21,22,23,24,25]],dtype='float32')
    # 创建一个5×5数据类型为uint8的全1矩阵
    b = np.ones((5,5),dtype='uint8')
    # 创建一个5×5数据类型为float32的全0矩阵
    c = np.zeros((5,5),dtype='float32')

    print('创建对象(np.array):\n{}'.format(a))
    print('创建对象(np.array):\n{}'.format(b))
    print('创建对象(np.array):\n{}'.format(c))

    image = cv.imread("C:/Users/1/Pictures/timg.jpg")
    # 判断是否读取成功
    if image is None:
        print("Failed to read image")
        sys.exit()

    # 切片和索引
    gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    print("位于（45，45）的像素值为{}".format(gray[45,45]))
    # 剪裁
    res_gray = gray[40:280,60:340]
    res_color1 = image[40:280,60:340,:]



    # 通道分离
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]

    cv.imshow('res_gray',res_gray)
    cv.imshow('res_color1',res_color1)
    cv.imshow('b',b)
    cv.imshow('g', g)
    cv.imshow('r', r)

    # 生成一个5×5，取值范围为0~100
    value1 = np.random.randint(0,100,(5,5),dtype='uint8')
    # 生成一个2×3、元素服从均值为0，标准差为1的正态分布
    value2 = np.random.randn(2,3)
    print("随机数：\n{}".format(value1))
    print("随机数：\n{}".format(value2))



    cv.waitKey(0)
    cv.destroyAllWindows()







