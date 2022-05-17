import sys
from PyQt5.Qt import *

'''
QFileDialog 文件对话框

### 静态方法
res = QFileDialog.getOpenFileName(window, "选择一个py文件", "./", "All(*.*);;图片(*.png *.jpg);;Python(*.py)",
                                  "Python(*.py)")
print(res) # (fpath, 类型)

# 参数同上
        QFileDialog.getOpenFileNames()
        QFileDialog.getOpenFileUrl() # 以file:///xxxx/xx打开
        QFileDialog.getOpenFileUrls()
        QFileDialog.getSaveFileName() # 保存形式
        QFileDialog.getSaveFileUrl()

# 获取文件夹
        # res = QFileDialog.getExistingDirectory(window, "选择一个py文件", "./") # str
        # res = QFileDialog.getExistingDirectoryUrl(window, "选择一个py文件", QUrl("./")) # Qurl
        print(res)
        


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
        # 静态方法
        # res = QFileDialog.getOpenFileName(window, "选择一个py文件", "./", "All(*.*);;图片(*.png *.jpg);;Python(*.py)",
                                          # "Python(*.py)")
        # QFileDialog.getOpenFileNames()
        # QFileDialog.getOpenFileUrl()
        # QFileDialog.getOpenFileUrls()
        # QFileDialog.getSaveFileName()
        # QFileDialog.getSaveFileUrl()
        # print(res) # (fpath, 类型)

        # res = QFileDialog.getExistingDirectory(window, "选择一个py文件", "./")
        res = QFileDialog.getExistingDirectoryUrl(window, "选择一个py文件", QUrl("./"))
        print(res)


    btn1 = QPushButton('文件对话框', window)
    btn1.move(50, 50)
    btn1.clicked.connect(dlg_open_slot)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
