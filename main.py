from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QObject
from mainwindow import *
import sys
import cv2
import numpy as np
import time
import run_detection
import os

class PlayVideo(QObject):
    def __init__(self, parent):
        super(PlayVideo,self).__init__(parent)

    def set_option(self, delay_time, times, callback):
        self.delay_time = delay_time
        self.times = times
        self.cur_call = 0
        self.callback = callback

    def start(self):
        if hasattr(self, "id") and self.id:
            return False
        self.id = self.startTimer(self.delay_time)
        return True

    def timerEvent(self, evt):
        self.callback(self.cur_call)
        self.cur_call+=1
        if self.cur_call>= self.times:
            self.killTimer(self.id)
            self.id = None



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.openButton.clicked.connect(self.openfile)
        self.playButton.clicked.connect(self.start_play)
        self.detectionButton.clicked.connect()


        self.play_video = PlayVideo(self)

    def run_detection_model(self):
        if hasattr(self, "video") and len(self.video)>=4 and os.path.exists(self.video):
            result_path = run_detection.run_video(self.video[3])
            cap = cv2.VideoCapture(result_path)
            n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            # cap.set(cv2.CAP_PROP_POS_FRAMES, 50)
            # a = cap.read()
            self.detection_result = [n_frames, fps, cap, result_path]

    def openfile(self):
        file_name = QFileDialog.getOpenFileName(caption="打开图片文件", filter="Vedio Files(*.mp4)")
        cap = cv2.VideoCapture(file_name[0])
        n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        #cap.set(cv2.CAP_PROP_POS_FRAMES, 50)
        #a = cap.read()
        self.video = [n_frames, fps, cap, file_name[0]]

    @staticmethod
    def draw_image(label_widget, image):
        qimage = QImage(image.tobytes(), image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        size = label_widget.size()
        pixmap = pixmap.scaled(size.width(), size.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label_widget.setPixmap(pixmap)
        label_widget.setAlignment(Qt.AlignCenter)

    def play(self, pos):
        if hasattr(self, "video") and len(self.video) >= 4 and os.path.exists(self.video):
            self.vedio[2].set(cv2.CAP_PROP_POS_FRAMES, pos)
            code, image = self.vedio[2].read()
            if code:
                self.draw_image(self.drawLabel1, image)
        if hasattr(self, "detection_result") and len(self.detection_result) >= 4 and os.path.exists(self.detection_result):
            self.detection_result.set(cv2.CAP_PROP_POS_FRAMES, pos)
            code, image = self.detection_result.read()
            if code:
                self.draw_image(self.drawLabel2, image)

    def start_play(self):
        step_time = 1/self.vedio[1]*1000
        self.play_video.set_option(step_time, self.vedio[0], self.play)
        self.play_video.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())






