import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QObject, QSize
from mainwindow import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.openButton.clicked.connect(self.openfile)
    def openfile(self):
        file_name = QFileDialog.getOpenFileName(caption="打开视频文件", filter="Vedio Files(*.mp4)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())






