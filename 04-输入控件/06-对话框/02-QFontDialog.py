import sys
from PyQt5.Qt import *

'''
QFontDialog 字体对话框

### 使用
# 方式1
dlg = QFontDialog(window)

# 方式二
f = QFont("华文黑体")
f.setPointSize(20)
dlg = QFontDialog(f, window)

### 功能
# 1. 打开的时候可以传递函数 无参数
dlg.open(dlg_open_slot)

# 2. 获取当前字体
dlg.currentFont()

# 3. 获取最终选中字体
dlg.selectedFont()


### 选项控制
    QFontDialog.NoButtons # 不限时确定和取消按钮
    QFontDialog.DontUseNativeDialog # mac
    QFontDialog.ScalableFonts # 显示可缩放字体
    QFontDialog.NonScalableFonts # 显示不可缩放字体
    QFontDialog.MonospacedFonts #  显示等宽字体
    QFontDialog.ProportionalFonts # 显示比例字体
    
    dlg2.setOption(QFontDialog.NoButtons, True)
    
### 信号
# 当前选中字体变化
dlg2.currentFontChanged.connect(f_currentFontChanged)
dlg2.fontSelected.connect(lambda f: print(f))

'''


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    # dlg = QFontDialog(window)

    f = QFont("华文黑体")
    f.setPointSize(20)
    dlg = QFontDialog(f, window)

    def dlg_open_slot():
        _dlg = dlg.currentFont()
        print("font click ok", _dlg.family())
        print('selectedFont', dlg.selectedFont())

    btn1 = QPushButton('accept', window)
    btn1.move(50, 20)
    btn1.clicked.connect(lambda: dlg.open(dlg_open_slot))

    ####################################
    dlg2 = QFontDialog(window)

    # QFontDialog.NoButtons # 不限时确定和取消按钮
    # QFontDialog.DontUseNativeDialog # mac
    # QFontDialog.ScalableFonts # 显示可缩放字体
    # QFontDialog.NonScalableFonts # 显示不可缩放字体
    # QFontDialog.MonospacedFonts #  显示等宽字体
    # QFontDialog.ProportionalFonts # 显示比例字体

    dlg2.setOption(QFontDialog.NoButtons, True)

    label = QLabel('选项控制', window)
    label.move(150, 50)

    btn2 = QPushButton('accept2', window)
    btn2.move(50, 150)

    def btn2_click():
        print("click")
        dlg2.show()
        # label.setFont(dlg.selectedFont())
        # label.adjustSize()

    btn2.clicked.connect(btn2_click)

    def f_currentFontChanged(f):
        label.setFont(f)
        label.adjustSize()

    dlg2.currentFontChanged.connect(f_currentFontChanged)
    dlg2.fontSelected.connect(lambda f: print(f))

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
