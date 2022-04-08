
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
        btn.move(150, 200)
        btn.resize(200, 100)
        btn.setText("测试状态")

        ##########
        # 状态
        push_button = QPushButton(self)
        push_button.setText("QPushButton")
        push_button.move(150, 10)

        radio_button = QRadioButton(self)
        radio_button.setText("QRadioButton")
        radio_button.move(150, 50)

        checkbox_button = QCheckBox(self)
        checkbox_button.setText("QCheckBox")
        checkbox_button.move(150, 90)

        # 是否被按下
        btn.isDown()

        # 是否被选中
        btn.isChecked()
        # btn.isEnabled() # 继承QWidget


        def btn_click():
            # label.setText(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            radio_button.setChecked(not radio_button.isChecked())
            checkbox_button.setChecked(not checkbox_button.isChecked())

        btn.clicked.connect(btn_click)



if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())