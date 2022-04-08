import sys
from PyQt5.Qt import *


# 方式一:
# 重写 contextMenuEvent 方法

# 方式二:
# # Qt.CustomContextMenu # 捕获信号即可
# # Qt.DefaultContextMenu # 默认值
# window.setContextMenuPolicy(Qt.CustomContextMenu)
# window.customContextMenuRequested.connect(add_menus)
# menus.exec_(window.mapToGlobal(a))

class Window(QWidget):
    # 方式一:
    # 重写 contextMenuEvent 方法
    def contextMenuEvent(self, a0: QContextMenuEvent) -> None:

        print("触发鼠标右键")

        menus = QMenu(self)

        # 创建Action
        new_action = QAction("新建", menus)
        new_action.triggered.connect(lambda: print("新建被打开了"))
        open_action = QAction("打开", menus)
        about_action = QAction("关于", menus)
        exit_action = QAction("退出", menus)

        # 二级菜单
        sub_menu = QMenu(self)
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

        # 显示菜单
        # menus.exec_(a0.pos())
        menus.exec_(a0.globalPos())




def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    def add_menus(a: QPoint):
        print(a)
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

        # 显示菜单
        # 把当前点转换为全局的点
        menus.exec_(window.mapToGlobal(a))
        # menus.exec_(a0.globalPos())



    # code
    # Qt.CustomContextMenu # 捕获信号即可
    # Qt.DefaultContextMenu # 默认值
    window.setContextMenuPolicy(Qt.CustomContextMenu)
    window.customContextMenuRequested.connect(add_menus)


    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
