#! /usr/bin/env python
# coding=utf-8
import time

import torch


image_path = "./docs/find2.png"


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def predict(image_path):
    s = time.time()
    support_objects_coco = ["bicycle", "bus", "car", "traffic light", "fire hydrant", "parking meter", "motorcycle"]
    results = model(image_path)
    results.show()

if __name__ == '__main__':
    image_path = "./docs/find.png"
    predict(image_path)