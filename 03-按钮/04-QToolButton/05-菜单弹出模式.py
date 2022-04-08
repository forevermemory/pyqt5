import sys
from PyQt5.Qt import *

# 更改菜单弹出模式
# QToolButton.DelayedPopup # 鼠标按下延时一会弹出菜单 类似于浏览器的后退按钮
# QToolButton.MenuButtonPopup # 有一个分开的箭头 点击箭头才会显示菜单
# QToolButton.InstantPopup # 点击了不会发射信号
# btn.setPopupMode(QToolButton.DelayedPopup)

def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    # 如果图标和文本同时设置 只会显示图标
    btn = QToolButton(window)
    btn.setText("我是按钮")
    btn.setIcon(QIcon("../../images/web.png"))
    btn.setIconSize(QSize(30, 30))

    ##############################################
    menus = QMenu(btn)
    # 创建Action
    new_action = QAction("新建", menus)
    new_action.triggered.connect(lambda: print("新建被打开了"))
    open_action = QAction("打开", menus)
    about_action = QAction("关于", menus)
    exit_action = QAction("退出", menus)

    # 二级菜单
    sub_menu = QMenu(btn)
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
    ##############################################

    btn.setMenu(menus)
    btn.clicked.connect(lambda: print("click"))
    # 更改菜单弹出模式
    # QToolButton.DelayedPopup # 鼠标按下延时一会弹出菜单 类似于浏览器的后退按钮
    # QToolButton.MenuButtonPopup # 有一个分开的箭头 点击箭头才会显示菜单
    # QToolButton.InstantPopup # 点击了不会发射信号
    btn.setPopupMode(QToolButton.MenuButtonPopup)



    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
