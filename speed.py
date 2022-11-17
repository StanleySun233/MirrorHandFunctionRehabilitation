# 代码描述：改变视频流的播放速度
#
# 创建时间： 2020-04-09
# 创建人: Wupke
# 修改时间:
# 版本:
import os

import cv2
from cv2 import VideoWriter, VideoWriter_fourcc
import argparse


def video_speed(video_root, out_root, scale=1):
    # 当fps和scale同时指定时，fps占主导地位"""
    cap = cv2.VideoCapture(video_root)  # 读入视频文件
    video_width = int(cap.get(3))  # 获取视频流的宽度
    video_height = int(cap.get(4))  # # 获取视频流的高度

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # VideoWriter_fourcc对象为视频编解码器，不同参数确定的文件类型不同

    fps = int(cap.get(cv2.CAP_PROP_FPS) * scale)
    # cv2.CAP_PROP_FPS：          为帧率值

    videoWriter = cv2.VideoWriter(out_root, fourcc, fps, (video_width, video_height))
    flag = cap.isOpened()

    while flag:
        flag, frame = cap.read()
        videoWriter.write(frame)
    videoWriter.release()
    # cv2.VideoCapture.release() 关闭视频文件


load_path = "D:/python/1.25/"
save_path = "D:/python/1/"
for i in os.listdir(load_path):
    if i.count("_") == 2:
        name = i.split("_")[0] + "_" + i.split("_")[1] + "_1.mp4"
    else:
        name = i.split("_")[0] + "_1.mp4"
        print(i)
    # print(name)
    if os.path.exists(f"D:/python/1/{name}"):
        continue
    video_speed(f"D:/python/1.25/{i}", f"D:/python/1/{name}", scale=0.8)
