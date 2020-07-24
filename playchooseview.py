from playchoose import *
from PyQt5.QtWidgets import *


class PlayChoose(Ui_Dialog, QDialog):

    def __init__(self, parent=None):
        super(PlayChoose, self).__init__(parent)
        self.setupUi(self)
        self.originRadio.setChecked(True)
        self.okButton.clicked.connect(self.okbottun_action)
        self.originRadio.clicked.connect(self.origin_ckecked)
        self.detectionRadio.clicked.connect(self.detection_ckecked)
        self.instanceRadio.clicked.connect(self.instance_ckecked)
        self.chooseed = 0

    def origin_ckecked(self):
        self.chooseed = 0

    def detection_checked(self):
        self.chooseed = 1

    def instance_checked(self):
        self.chooseed = 2

    def okbottun_action(self):
        self.close()
