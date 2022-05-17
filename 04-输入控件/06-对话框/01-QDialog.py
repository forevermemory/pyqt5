import sys
from PyQt5.Qt import *


'''
QDialog 对话框

模态和非模态
dlg = QDialog()
# 1.应用程序级别 用户必须先对对话框交互 知道关闭对话框 才会执行其它
# dlg.exec()

# 2. 窗口级别 模态对话框 应用场景 文件选择 是否同意。。。
# dlg.open()

# 3. 非模态
dlg.show()

### 非模态-->模态
# 方式一
dlg.setModal(True) 

# 方式二
dlg.setWindowModality(Qt.WindowModal)
dlg.setWindowModality(Qt.ApplicationModal)



# 操作
dlg.accept() # 返回1
dlg.reject() # 返回0
dlg.done(100) # 返回100

dlg.result() 获取返回值
    
    
# 信号
accepted
finished(val)
rejected
    
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
    dlg = QDialog(window)
    dlg.setWindowTitle("我是QDialog")
    dlg.resize(300, 300)
    # 1.应用程序级别 用户必须先对对话框交互 知道关闭对话框 才会执行其它
    # dlg.exec()

    # 2. 窗口级别 模态对话框 应用场景 文件选择 是否同意。。。
    # dlg.open()

    # 3. 非模态
    # dlg.show()
    # dlg.setModal(True) # 使非模态-->模态
    # dlg.setWindowModality(Qt.WindowModal)
    # dlg.setWindowModality(Qt.ApplicationModal)

    dlg.setSizeGripEnabled(True)



    # 常用操作槽
    btn1 = QPushButton('accept', dlg)
    btn1.move(50, 20)
    btn1.clicked.connect(lambda: dlg.accept())

    btn2 = QPushButton('reject', dlg)
    btn2.move(50, 120)
    btn2.clicked.connect(lambda: dlg.reject())

    btn3 = QPushButton('done', dlg)
    btn3.move(50, 220)
    btn3.clicked.connect(lambda: dlg.done(100))

    dlg.accepted.connect(lambda: print('accepted'))
    dlg.rejected.connect(lambda: print('rejected'))
    dlg.finished.connect(lambda val: print('finished', val))

    dlg.show()
    print(dlg.result())

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
