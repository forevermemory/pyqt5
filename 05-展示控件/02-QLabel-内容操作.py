
import sys
from PyQt5.Qt import *

'''
QLabel

### 文本字符串
setText()

### 数值数据
setNum()

### 图形
label.setPixmap()
label.setPicture()

### gif

movie = QMovie('../images/dog.gif')
label.setMovie(movie)

label.setScaledContents(True)
movie.start()
movie.setSpeed(300) # 300为三倍速

### 清空

'''


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法



    def btn_click(self):
       pass

    def init_ui(self):

        label = QLabel("Qlabel-hello(&s)", self)
        label.move(100, 100)
        # label.resize(300, 300)
        label.setStyleSheet("border: 1px solid pink")


        # label.setPixmap()
        # label.setPicture()

        movie = QMovie('../images/dog.gif')
        label.setMovie(movie)

        label.setScaledContents(True)
        movie.start()
        # movie.setSpeed(300) #设置播放速度





if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())