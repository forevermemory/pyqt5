import sys
from PyQt5.Qt import *

'''
QFileDialog 文件对话框

### 功能作用
 dlg = QFileDialog(window, "caption", "../../", "")

# 接收模式
dlg.setAcceptMode(QFileDialog.AcceptOpen)
# dlg.setAcceptMode(QFileDialog.AcceptSave)

# 默认后缀名
# dlg.setDefaultSuffix("py")

# 设置文件模式
dlg.setFileMode(QFileDialog.AnyFile) # 文件的名称 无论是否存在
dlg.setFileMode(QFileDialog.ExistingFile) # 单个现有文件名称
dlg.setFileMode(QFileDialog.Directory) # 目录名称
dlg.setFileMode(QFileDialog.ExistingFiles) # 0或多个现有文件的名称

# 设置名称过滤器
dlg.setNameFilter("图片(*.png *.jpg)")
dlg.setNameFilters(["图片(*.png *.jpg)", "python(*.py)"])

# 更改标签名称
QFileDialog.FileName
QFileDialog.Accept
QFileDialog.Reject
QFileDialog.FileType
QFileDialog.LookIn
dlg.setLabelText(QFileDialog.Accept, "接收")
dlg.setLabelText(QFileDialog.Reject, "拒绝")


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
    def dlg_open_slot():
        dlg = QFileDialog(window, "caption", "../../", "")

        # 接收模式
        dlg.setAcceptMode(QFileDialog.AcceptOpen)
        # dlg.setAcceptMode(QFileDialog.AcceptSave)

        # 默认后缀名
        # dlg.setDefaultSuffix("py")

        # 设置文件模式
        dlg.setFileMode(QFileDialog.AnyFile) # 文件的名称 无论是否存在
        dlg.setFileMode(QFileDialog.ExistingFile) # 单个现有文件名称
        dlg.setFileMode(QFileDialog.Directory) # 目录名称
        dlg.setFileMode(QFileDialog.ExistingFiles) # 0或多个现有文件的名称
        #
        # # 设置名称过滤器
        # dlg.setNameFilter("图片(*.png *.jpg)")
        # dlg.setNameFilters(["图片(*.png *.jpg)", "python(*.py)"])

        # 更改标签名称
        QFileDialog.FileName
        QFileDialog.Accept
        QFileDialog.Reject
        QFileDialog.FileType
        QFileDialog.LookIn
        dlg.setLabelText(QFileDialog.Accept, "接收")
        dlg.setLabelText(QFileDialog.Reject, "拒绝")

        dlg.open()

        # dlg.accepted.connect()

    btn1 = QPushButton('文件对话框', window)
    btn1.move(50, 50)
    btn1.clicked.connect(dlg_open_slot)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
