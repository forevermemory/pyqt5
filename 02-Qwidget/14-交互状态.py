
import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        # 是否可用
        btn = QPushButton(self)
        btn.setText("click me")
        btn.pressed.connect(lambda: print("click"))
        print(btn.isEnabled())
        btn.setEnabled(False) # 变成灰色的了

        # 是否显示和隐藏
        btn.setVisible(True)
        # btn.show() # 马甲
        # btn.hide()# 马甲

        # btn.isVisible() # 获取最终的状态是否可见
        # btn.isHidden()   # s是否隐藏 基于父控件

        # 是否是编辑状态  只能是 [*]
        self.setWindowTitle("正在编辑[*]")
        self.setWindowModality(True)

        # 是否是活跃窗口
        self.isActiveWindow()

        # 关闭后释放资源
        btn.setAttribute(Qt.WA_DeleteOnClose, True) # 设置了之后 close会释放btn
        btn.close() # 默认不会释放btn


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())