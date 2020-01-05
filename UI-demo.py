import sys

from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QFrame, QPushButton, QWidget, QLabel, QComboBox


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.query = None  # path of query image
        self.gallery = None  # path of gallery image

        self.btn1 = QPushButton("Choose query image", self)
        self.btn1.move(350, 20)
        self.btn1.clicked.connect(self.showDialog)

        self.btn2 = QPushButton("Choose gallery image", self)
        self.btn2.move(1350, 20)
        self.btn2.clicked.connect(self.showDialog)

        self.btn3 = QPushButton("Search", self)
        self.btn3.move(900, 450)
        self.btn3.clicked.connect(self.person_search)

        self.label1 = QLabel(self)
        self.label1.setGeometry(200, 100, 500, 700)
        self.label1.setStyleSheet("border: 2px solid black")
        self.label1.setScaledContents(True)

        self.label2 = QLabel(self)
        self.label2.setGeometry(1200, 100, 500, 700)
        self.label2.setStyleSheet("border: 2px solid black")
        self.label2.setScaledContents(True)

        self.method_box = QComboBox(self)
        self.method_box.addItem('CVPR 2017')
        self.method_box.addItem('faster-rcnn')
        self.method_box.addItem('ssy')
        self.method_box.move(900, 400)

        self.setGeometry(1000, 500, 2000, 1000)
        self.setWindowTitle("Person search demo")
        self.show()

    def showDialog(self):
        sender = self.sender()
        img_path, _ = QFileDialog.getOpenFileName(self, "Choose image", "./images", "All Files (*)")
        pix = QPixmap(img_path)

        if sender == self.btn1:
            self.query = img_path
            self.label1.setPixmap(pix)
        else:
            self.gallery = img_path
            self.label2.setPixmap(pix)

    def person_search(self):
        if self.method_box.currentText() == 'CVPR 2017':
            print("search")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())
