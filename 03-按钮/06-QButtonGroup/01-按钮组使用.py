import sys
from PyQt5.Qt import *


# QButtonGroup 继承Object是个抽象的类 而且为不可视控件
# 为按钮分组

def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    r1 = QRadioButton("男", window)
    r1.move(10, 10)
    r1.setChecked(True)
    r2 = QRadioButton("女", window)
    r2.move(50, 10)

    # 创建按钮组
    group1 = QButtonGroup(window)

    # 添加按钮
    group1.addButton(r1, 1)
    group1.addButton(r2, 2)

    # 获取组内按钮
    print(group1.buttons())
    # 根据id获取
    print(group1.button(1))
    # 获取选中
    print(group1.checkedButton())

    # 两组互斥
    r3 = QRadioButton("是", window)
    r3.move(10, 60)
    r4 = QRadioButton("否", window)
    r4.move(50, 60)
    group2 = QButtonGroup(window)
    group2.addButton(r3)
    group2.addButton(r4)

    ## id操作
    group2.setId(r3, 3)
    group2.setId(r4, 4)
    print(group2.id(r3))
    print(group2.id(r4))

    # 没有选中为-1
    print(group2.checkedId())

    r4.setChecked(True)
    print(group2.checkedId())



    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
