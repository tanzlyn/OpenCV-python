import cv2 as cv
import numpy as np
"""
Tan2022/12/31
保存XML文件和YAM文件
"""

if __name__ == '__main__':
    # 创建fileStorage对象file，用于写入数据。
    file = cv.FileStorage('./myfile.xml',cv.FileStorage_WRITE)

    # 写入数据
    file.write('name','Tan')
    file.write('age',18)
    file.write('date','20221231')
    scores = np.array([[90,90],[80,78]])
    file.write('scores',scores)

    # 释放对象
    file.release()

    # 创建FileStorage对象file1,用于读取数据
    file1 = cv.FileStorage('./myfile.xml',cv.FILE_STORAGE_READ)

    # 判断myfile.xml文件是否读取成功
    if file1.isOpened():
        # 读取数据
        name1 = file1.getNode('name').string()
        nage1 = file1.getNode('age').real()
        date1 = file1.getNode('date').string()
        scores1 = file1.getNode('scores').mat()

        # 展示读取结果
        print('姓名：{}'.format(name1))
        print('年龄：{}'.format(nage1))
        print('记录日期：{}'.format(date1))
        print('分数：{}'.format(scores1))
    else:
        print('cant open')

    # 释放对象
    file1.release()



