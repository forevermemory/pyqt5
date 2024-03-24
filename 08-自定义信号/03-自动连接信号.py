
import sys
from PyQt5.Qt import *


''' 
# 解耦合
# 规则 
1. 对象设置 btn.setObjectName("btn_objname")
2. 定义装饰器 on_成员的objectname_信号的名称 
    @pyqtSlot(bool)
    def on_btn_objname_clicked(self, val):
        print("btn clicked", val)
        
        
'''

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        btn = QPushButton("按钮", self)
        btn.move(100, 100)
        btn.setObjectName("btn_objname")

        QMetaObject.connectSlotsByName(self)



    @pyqtSlot(bool)
    def on_btn_objname_clicked(self, val):
        print("btn clicked", val)

if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())