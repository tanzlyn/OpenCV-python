import cv2 as cv

"""
Tan2022/12/31
读取视频
"""
if __name__ == '__main__':
    video = cv.VideoCapture('E:\嗨格式录屏文件\\20220714-165307.mp4')

    # 判断是否创建视频流
    while video.isOpened():
        ret,frame = video.read()  # 读取每一帧图像
        if ret is True:  # ret表示是否读取成功
            cv.imshow('Video',frame)

            # 设置视频播放速度
            cv.waitKey(int(1000/video.get(cv.CAP_PROP_FPS)))
            # 按下Q键退出
            if cv.waitKey(1)&0xFF == ord('q'):
                break
        else:
            break

    # 输出视频信息
    print('视频中图像的宽度为{}'.format(video.get(cv.CAP_PROP_FRAME_WIDTH)))
    print('视频中图像的高度为{}'.format(video.get(cv.CAP_PROP_FRAME_HEIGHT)))
    print('视频频率{}'.format(video.get(cv.CAP_PROP_FPS)))
    print('视频总帧数{}'.format(video.get(cv.CAP_PROP_FRAME_COUNT)))

    video.release()
    cv.destroyAllWindows()



