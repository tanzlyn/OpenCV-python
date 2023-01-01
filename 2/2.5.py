import cv2 as cv
"""
Tan2022/12/31
保存视频
"""

if __name__ == '__main__':
    # 设置编/解码方式
    fourcc = cv.VideoWriter_fourcc(*'DIVX')

    # 采用摄像头获取视屏
    video = cv.VideoCapture(0)

    # 1.使用cv.VIdeoWriter()原型保存视频
    result = cv.VideoWriter()
    # result.open('E:\嗨格式录屏文件\\202.avi',fourcc,2000.0,(640,480))

    # 2.使用cv.VIdeoWriter()构造函数保存视频
    result = cv.VideoWriter('E:\\20220.avi' ,fourcc ,20.0 ,(640 ,480))

    # 判断是否成功创建视频流
    while video.isOpened():
        ret ,frame = video.read()
        if ret is True:
            # 将每一帧视频图像进行水平翻转
            frame = cv.flip(frame ,1)

            # 将每一帧图像写入视频
            result.write(frame)
            cv.imshow('Video' ,frame)
            cv.waitKey(40)

            # 按下q退出
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # 释放关闭窗口
    video.release()
    result.release()
    cv.destroyAllWindows()