
import sys
from PyQt5.Qt import *

'''
QProgressDialog 进度条对话框  默认等4s弹出

### 构造函数
box = QProgressDialog(parent)

#     box = QProgressDialog("标签文本", "按钮文本", 0, 100, window)
box = QProgressDialog(str, str, int, int, parent)
        
### 自动弹出 - 最小展示时长
# 设置进度条对话框展示之前的等待时间
# 如果在等待内 进度条到了max 不会弹出 ，否则会被弹出
box.setMinimumDuration(0)

### 界面内容设置
box.setWindowTitle("标题")
box.setLabelText("当前下载进度")
box.setCancelButtonText("取消下载")

### 是否取消

### 自动操作


'''

import sys
from PyQt5.Qt import *


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    btn = QPushButton('button', window)
    btn.move(50, 20)


    # code
    # box = QProgressDialog(window)
    box = QProgressDialog("当前下载进度", "取消下载", 0, 100, window)
    box.setValue(60)

    # box.setAutoClose(False)
    # box.setAutoReset(False)

    # 设置进度条对话框展示之前的等待时间
    # 如果在等待内 进度条到了max 不会弹出 ，否则会被弹出
    # box.setMinimumDuration(0)

    # 界面内容设置
    # box.setWindowTitle("标题")
    # box.setLabelText("当前下载进度")
    # box.setCancelButtonText("取消下载")


    box.open(lambda: print("对话框被取消"))

    timer = QTimer(box)

    def timer_timeout():
        print("val:", box.value(), box.wasCanceled())
        if box.wasCanceled() or box.value()+1 >= box.maximum():
            timer.stop()
        box.setValue(box.value() + 1)

    timer.timeout.connect(timer_timeout)
    timer.start(500)


    def box_cancel():
        print('box_cancel')
        timer.stop()
    box.canceled.connect(box_cancel)


    def btn_click():
        # box.show()
        # box.showMessage("okok")
        # box.showMessage("okok")
        # box.showMessage("okok2")
        pass

    btn.clicked.connect(btn_click)
    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
