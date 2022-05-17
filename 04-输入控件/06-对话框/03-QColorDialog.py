import sys
from PyQt5.Qt import *

'''

QColorDialog 颜色对话框

### 设置选项
QColorDialog.ShowAlphaChannel # 支持设置alpha
QColorDialog.NoButtons # 不显示ok和cancel
QColorDialog.DontUseNativeDialog # 
dlg.setOption(QColorDialog.NoButtons)
    
### 信号
dlg.currentColorChanged[QColor]
dlg.colorSelected[QColor]

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
    dlg = QColorDialog(window)



    # res = dlg.exec() # ok --1 cancel -- 0
    # print(res)

    def dlg_open_slot():
        dlg.show()

    btn1 = QPushButton('按钮颜色变化', window)
    btn1.move(50, 20)
    btn1.clicked.connect(dlg_open_slot)


    def dlg_cur_color_change(color):
        print(color)
        qp = QPalette(color)
        qp.setColor(QPalette.ButtonText, color)
        btn1.setPalette(qp)
    dlg.currentColorChanged.connect(dlg_cur_color_change)

    ####################################

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
