import cv2
import os
import numpy as np
import re
import run_instance_segmentation
import shutil


digit_com = re.compile("[\d]+")


def run_video(input_data):
    cap = cv2.VideoCapture(input_data)
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(cur_dir, "data")
    if os.path.exists(image_path):
        shutil.rmtree(image_path)
    os.makedirs(image_path)
    pos = 0
    while pos < n_frames:
        code, image = cap.read()
        image_file = os.path.join(image_path, "%05d.jpg"%(pos))
        cv2.imwrite(image_file, image)
        pos+=1
    output_image_path = run_instance_segmentation.run_video(image_path)
    img_files = os.listdir(output_image_path)
    img_files = [img_file for img_file in img_files if img_file.endswith(".png")]
    img_files = sorted(img_files, key=lambda x: int(digit_com.findall(x)[-1]))
    img_arr = cv2.imread(os.path.join(output_image_path, img_files[0]))
    mp4_file = os.path.join(output_image_path, "video.mp4")
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    writer = cv2.VideoWriter(mp4_file, apiPreference=cv2.CAP_ANY, fourcc=fourcc, fps=fps,
                             frameSize=img_arr.shape[:-1][::-1], isColor=True)

    for img_file in img_files:
        cur_img = cv2.imread(os.path.join(output_image_path, img_file))
        writer.write(cur_img)
    writer.release()
    return mp4_file
