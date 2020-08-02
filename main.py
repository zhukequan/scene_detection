from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QObject, QSize
from mainwindow import *
from playchooseview import PlayChoose
import sys
import cv2
import numpy as np
import time
import run_detection
import run_segment
import run_instance_segmentation
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
    def stop(self):
        if hasattr(self, "id") and self.id:
            self.killTimer(self.id)
            self.id=None

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.openButton.clicked.connect(self.openfile)
        self.playButton.clicked.connect(self.start_play)
        self.detectionButton.clicked.connect(self.run_detection_model)
        self.segmentButton.clicked.connect(self.run_instance_model)
        self.stopButton.clicked.connect(self.stop_play)
        self.openimgButton.clicked(self.openimgButton)
        self.lastButton.clicked(self.last_image)
        self.nextButton.clicked(self.next_image)
        self.segmentButton.clicked(self.image_seg)
        self.play_choose = PlayChoose(self)
        self.play_choose.setModal(True)
        self.play_video = PlayVideo(self)

        #self.drawLabel1.adjustSize()
        #self.drawLabel2.adjustSize()
        self.image1 = None
        self.image2 = None

    def paintEvent(self, event):
        self.drawLabel1.clear()
        self.drawLabel2.clear()
        size = self.widget_2.size()
        size1 = QSize()
        size2 = QSize()
        size2.setHeight(size.height()*0.45)
        size2.setWidth(size.width())
        size1.setHeight(size.height()*0.45)
        size1.setHeight(size.height()*0.45)
        size1.setWidth(size.width())
        self.drawLabel1.resize(size1)
        self.drawLabel2.resize(size2)
        if not self.image1 is None:

            size1 = self.drawLabel1.size()
            qimage1 = QImage(self.image1.tobytes(), self.image1.shape[1], self.image1.shape[0], QImage.Format_RGB888)
            pixmap1 = QPixmap(qimage1)
            pixmap1 = pixmap1.scaled(size1.width(), size1.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.drawLabel1.setPixmap(pixmap1)
            self.drawLabel1.setAlignment(Qt.AlignCenter)
        if not self.image2 is None:
            self.drawLabel2.clear()
            size2 = self.drawLabel2.size()
            qimage2 = QImage(self.image2.tobytes(), self.image2.shape[1], self.image2.shape[0], QImage.Format_RGB888)
            pixmap2 = QPixmap(qimage2)
            pixmap2 = pixmap2.scaled(size2.width(), size2.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.drawLabel2.setPixmap(pixmap2)
            self.drawLabel2.setAlignment(Qt.AlignCenter)
        QMainWindow.paintEvent(self, event)

    def run_detection_model(self):
        if hasattr(self, "video") and len(self.video)>=4 and os.path.exists(self.video[3]):
            result_path = run_detection.run_video(self.video[3])
            cap = cv2.VideoCapture(result_path)
            n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            # cap.set(cv2.CAP_PROP_POS_FRAMES, 50)
            # a = cap.read()
            self.detection_result = [n_frames, fps, cap, result_path]

    def run_instance_model(self):
        if hasattr(self, "video") and len(self.video)>=4 and os.path.exists(self.video[3]):
            result_path = run_segment.run_video(self.video[3])
            cap = cv2.VideoCapture(result_path)
            n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            # cap.set(cv2.CAP_PROP_POS_FRAMES, 50)
            # a = cap.read()
            self.instance_result = [n_frames, fps, cap, result_path]

    def stop_play(self):
        self.play_video.stop()

    def openpath(self):
        self.dir_path = QFileDialog.getExistingDirectory(parent=self, caption="打开图片文件",options=QFileDialog.ShowDirsOnly)

        self.result_list = sorted(self.result_list)
        self.image_list = os.listdir(self.dir_path)
        self.image_list = sorted(self.image_list)
        self.image_pos = 0
        self.play_video.stop()
        self.image1 = cv2.imread(os.path.join(self.dir_path, self.image_list[self.image_pos]))
        self.image2 = None
        self.imgEdit.setText(self.image_list[self.image_pos])
        self.repaint()

    def next_image(self):
        self.image_pos = (self.image_pos + 1)% len(self.image_list)
        self.image1 = cv2.imread(os.path.join(self.dir_path, self.image_list[self.image_pos]))
        if hasattr(self, "result_path"):
            self.image2 = self.image2 = cv2.imread(os.path.join(self.result_path, self.result_list[self.image_pos]))
        else:
            self.image2 = None
        self.imgEdit.setText(self.image_list[self.image_pos])
        self.repaint()

    def last_image(self):
        self.image_pos = (self.image_pos - 1 + len(self.image_list)) % len(self.image_list)
        self.image1 = cv2.imread(os.path.join(self.dir_path, self.image_list[self.image_pos]))
        if hasattr(self, "result_path"):
            self.image2 = self.image2 = cv2.imread(os.path.join(self.result_path, self.result_list[self.image_pos]))
        else:
            self.image2 = None
        self.imgEdit.setText(self.image_list[self.image_pos])
        self.repaint()

    def image_seg(self):
        self.result_path = "/home/jhvision-3/xu/SHU_FLH/detection_model/results/8-2"
        self.result_list = os.listdir(self.result_path)
        precision = run_instance_segmentation.run(range(0, len(self.result_list)))
        self.detEdit.setText(str(precision[0]))
        self.apEdit.setText(str(precision[0]))
        self.FPEdit.setText(str(precision[0]))

    def openfile(self):
        file_name = QFileDialog.getOpenFileName(caption="打开视频文件", filter="Vedio Files(*.mp4)")
        if not file_name:
            return
        cap = cv2.VideoCapture(file_name[0])
        n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        #cap.set(cv2.CAP_PROP_POS_FRAMES, 50)
        #a = cap.read()
        self.video = [n_frames, fps, cap, file_name[0]]
        self.video[2].set(cv2.CAP_PROP_POS_FRAMES, 0)
        code, image = self.video[2].read()
        if code:
            self.image1 = image
            self.image2 = None
            #self.draw_image(self.drawLabel1, image)
        if hasattr(self, "detection_result"):
            delattr(self, "detection_result")
        if hasattr(self, "instance_result"):
            delattr(self, "instance_result")
        self.repaint()

    @staticmethod
    def draw_image(label_widget, image):
        qimage = QImage(image.tobytes(), image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        size = label_widget.size()
        pixmap = pixmap.scaled(size.width(), size.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label_widget.setPixmap(pixmap)
        label_widget.setAlignment(Qt.AlignCenter)

    def play(self, pos):
        if hasattr(self, "video") and len(self.video) >= 4 and os.path.exists(self.video[3]):
            self.video[2].set(cv2.CAP_PROP_POS_FRAMES, pos)
            code, image = self.video[2].read()

            if code:
                self.image1 = image
                #self.draw_image(self.drawLabel1, image)
        if hasattr(self, "detection_result") and len(self.detection_result) >= 4 and os.path.exists(self.detection_result[3]):
            if self.play_choose.chooseed == 1:
                self.detection_result[2].set(cv2.CAP_PROP_POS_FRAMES, pos)
                code, image = self.detection_result[2].read()

                if code:
                    self.image2 = image
                    #self.draw_image(self.drawLabel2, image)

        if hasattr(self, "instance_result") and len(self.instance_result) >= 4 and os.path.exists(self.instance_result[3]):
            if self.play_choose.chooseed == 2:
                self.instance_result[2].set(cv2.CAP_PROP_POS_FRAMES, pos)
                code, image = self.instance_result[2].read()

                if code:
                    self.image2 = image
                    #self.draw_image(self.drawLabel2, image)
        self.repaint()

    def start_play(self):
        self.play_video.stop()
        self.play_choose.exec()
        if not (hasattr(self, "video") and len(self.video) >= 4 and os.path.exists(self.video[3])):
            return
        step_time = 1/self.video[1]*1000
        self.play_video.set_option(step_time, self.video[0], self.play)
        self.play_video.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())






