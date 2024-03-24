
import sys
from PyQt5.Qt import *

'''
### 尺寸策略



'''


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("title-")
    window.resize(500, 500)
    window.move(300, 200)
    # label1 = QLabel("标签1", window)

    # 1. 创建一个布局管理器
    layout = QVBoxLayout()

    # 2. 把布局管理器设置给需要布局的父控件
    window.setLayout(layout)

    # 3. 把需要布局的子控件添加到布局管理器
    label1 = QPushButton("标签1")
    label2 = QPushButton("标签2")
    label3 = QPushButton("标签3")
    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(label3)

    window.show()
    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
