
import sys
from datetime import  datetime

from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        btn = QPushButton(self)
        btn.move(200, 200)
        btn.resize(200, 100)
        btn.setText("&abc更新时间")

        label = QLabel(self)
        label.setText("label")
        label.move(200, 100)

        def btn_click():
            # label.setText(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            label.setText(str(datetime.now().timestamp() * 1000)[0:13])

            label.adjustSize()

        btn.clicked.connect( btn_click)



        ##########
        # 自动重复 点击事件
        btn.setAutoRepeat(True)
        btn.setAutoRepeatInterval(500) # 毫秒
        btn.setAutoRepeatDelay(1000)  # 毫秒

        # btn.autoRepeat()
        # btn.autoRepeatDelay()
        # btn.autoRepeatInterval()



if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())