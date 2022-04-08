
import sys
from PyQt5.Qt import *


class Window(QWidget):
    obj = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-Qobject")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        # self.test_obj_api()
        # self.test_obj_parent()
        # self.test_obj_event()
        # self.test_obj_demo()
        # self.test_obj_类型判断()
        # self.test_obj_对象删除()
        self.test_obj_事件处理()

        pass


    def test_obj_parent(self):
        '''父子'''

        pass

    def test_obj_api(self):
        '''对象名称、属性'''
        o = QObject()

        # 一般用于样式 QLabel#notify
        # 一般用于样式 QLabel#notify[notify_level="warning"]
        print(o.objectName())
        o.setObjectName("notify")
        print(o.objectName())

        print(o.dynamicPropertyNames())
        o.setProperty("notify_level", "warning")
        print(o.property("users"))
        print(o.dynamicPropertyNames())

        # btn = QPushButton()
        # btn.setParent(o)
        # btn.setStyleSheet()
        # o.findChildren()


    def test_obj_event(self):

        def obj_name_change(val):
            print('obj name changed ', val)
        obj1 = QObject()

        # 对象名字变化信号
        obj1.objectNameChanged.connect(obj_name_change)

        obj1.setObjectName("111")
        # obj1.setObjectName("222")

        print(obj1)

        def obj_destroyed(o: QObject):
            print('obj obj_destroyed', o, o.objectName())

        # 信号阻塞
        print(obj1.signalsBlocked())
        obj1.blockSignals(True)
        print('---', obj1.signalsBlocked())

        obj1.setObjectName("222233")
        obj1.blockSignals(False)
        # 被销毁时候的信号
        obj1.destroyed.connect(obj_destroyed)

        # 某个信号的槽函数列表
        print('===', obj1.receivers(obj1.destroyed))  # 销毁还有其它的槽函数
        print(obj1.dynamicPropertyNames())
        print('===', obj1.receivers(obj1.objectNameChanged))


    def test_obj_demo(self):
        btn = QPushButton(self)
        btn.setText("click me")

        def btn_func():
            print('clicked')
        btn.clicked.connect(btn_func)

    def test_obj_类型判断(self):
        btn = QPushButton()
        obj = QObject()
        a = [btn, obj]

        for i in a:
            # print(i.isWidgetType())
            print(i.inherits("QPushButton"))

    def test_obj_对象删除(self):
        o1 = QObject()
        o2 = QObject()
        o3 = QObject()

        o3.setParent(o2)
        o2.setParent(o1)

        o3.destroyed.connect(lambda: print("obj3 被释放了"))
        o2.destroyed.connect(lambda: print("obj2 被释放了"))

        # del o2 没有删除 只是清楚引用
        # 延时删除
        o2.deleteLater()

        # 可以使用o2
        print(o2)

        pass

    def test_obj_事件处理(self):

        btn = Btn(self)
        btn.setText("click me")
        btn.clicked.connect(lambda: print("btn clicked"))
        pass

class Btn(QPushButton):
    def event(self, e: QEvent) -> bool:
        if e.type() == QEvent.MouseButtonPress:
            print('btn event')
        return super().event(e)

class App(QApplication):

    def notify(self, a0: QObject, a1: QEvent) -> bool:
        if a0.inherits("QPushButton") and a1.type() == QEvent.MouseButtonPress:
            print(a0,a1)
        return  super().notify(a0,a1)

if __name__ == '__main__':
    # 创建应用程序和对象
    app = App(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    #################################
    # wid = QWidget()
    # wid.move(50, 20)
    # wid.setStyleSheet("background-color: cyan")
    # wid.setWindowTitle('hello world')
    #
    # def wid_change(s):
    #     wid.blockSignals(True)
    #     wid.setWindowTitle('QQQQQQQQQQ+'+s)
    #     wid.blockSignals(False)
    #
    # wid.windowTitleChanged.connect(wid_change)
    # wid.setWindowTitle('hello world')
    # wid.setWindowTitle('hello')
    # wid.show()
    ##################################


    window.show()
    sys.exit(app.exec_())
