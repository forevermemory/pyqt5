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

    # 菜单设置
    btn = QPushButton("PyCharm", window)

    # 创建菜单 菜单分为 行为、子菜单、分割线
    menus = QMenu(window)

    # 创建Action
    new_action = QAction("新建", menus)
    new_action.triggered.connect(lambda: print("新建被打开了"))
    open_action = QAction("打开", menus)
    about_action = QAction("关于", menus)
    exit_action = QAction("退出", menus)

    # 二级菜单
    sub_menu = QMenu(window)
    sub_menu.setTitle("最近打开")

    resent_act = QAction("python-study", sub_menu)
    resent_act2 = QAction("python-pyqt", sub_menu)
    resent_act3 = QAction("python-django", sub_menu)
    sub_menu.addAction(resent_act)
    sub_menu.addAction(resent_act2)
    sub_menu.addAction(resent_act3)

    menus.addAction(new_action)
    menus.addAction(open_action)
    menus.addAction(about_action)
    menus.addMenu(sub_menu)
    menus.addSeparator()
    menus.addAction(exit_action)
    # 设置菜单
    btn.setMenu(menus)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
