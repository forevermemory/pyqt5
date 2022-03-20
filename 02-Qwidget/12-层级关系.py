import sys
from PyQt5.Qt import *

# raise_()  # 提升到最上级
# lower() # 放到最下面
# stackUnder(other) # 提升到某个上面

class MyLabel(QLabel):

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.raise_()
        # self.lower()
        # self.stackUnder(other)

def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    


    label1 = MyLabel(window)
    label1.resize(150,150)
    label1.move(30,30)
    label1.setText("点击切换层级")
    label1.setStyleSheet("background-color:pink")


    label2 = MyLabel(window)
    label2.resize(150,150)
    label2.move(120,120)
    label2.setText("点击切换层级")
    label2.setStyleSheet("background-color:#ccc")



    # 展示控件
    window.show()
    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
