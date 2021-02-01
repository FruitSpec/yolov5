import detect
import sklearn
import os
import subprocess

if __name__ == '__main__':
    os.chdir('/home/yotam/PycharmProjects/YOLOv5/yolov5/')
    weights = '/home/yotam/PycharmProjects/YOLOv5/yolov5/weights/best_grape.pt'
    source = '/home/yotam/PycharmProjects/YOLOv5/yolov5/test/images'

    img = '416'
    conf = '0.3'
    iou = '0.3'

    subprocess.run(["python", "detect.py", "--weights", weights, "--source", source, "--img-size", img, "--conf-thres", conf, "--iou-thres", iou])
