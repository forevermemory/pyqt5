
import sys
from PyQt5.Qt import *

'''
QTextEdit 打开超链接

重写QTextEdit 的鼠标按下事件 
通过 anchorAt 找到是否有链接
打开链接 QDesktopServices.openUrl(QUrl(_link))
ps: 链接得写全 http://xxx.com

'''


class MyQTextEdit(QTextEdit):
    def mousePressEvent(self, e: QMouseEvent) -> None:
        pos = e.pos()
        _link = self.anchorAt(pos)
        print(_link)
        ok = QDesktopServices.openUrl(QUrl(_link))
        print(ok)

        return super().mousePressEvent(e)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.t = MyQTextEdit('hello world, china', self)
        self.t.move(50, 100)
        self.t.resize(300, 300)

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())

        self.init_ui()  # 界面绘制交给InitUi方法

        self.t.setText("hello world, a "*100 +'<a name="_name" href="https://www.baidu.com">锚点</a>'+'pyqt5'*100)

    def btn_click(self):



        pass


    def init_ui(self):
        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())