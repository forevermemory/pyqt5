
import sys
from PyQt5.Qt import *


class MyLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super(MyLabel, self).__init__(*args, **kwargs)

        self.setText("10")
        self.move(100,100)
        self.setStyleSheet("font-size:30px")

        self.time_id = self.startTimer(300)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        # print("a0", a0)
        cur = int(self.text()) -1
        self.setText(str(cur))

        if cur ==0:
            self.killTimer(self.time_id)



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        label = MyLabel(self)
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())