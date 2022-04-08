
import sys
from PyQt5.Qt import *

'''
QAbstractSlider 滑块

# 信号
self.t.valueChanged.connect(lambda val: self.label.setText(str(val)))

# 设置范围
self.t.setMaximum(28)
self.t.setMinimum(10)

# 设置值或者默认值
self.t.setValue(22)

# 设置步长
self.t.setSingleStep(5) # 向上乡下箭头
self.t.setPageStep(10) # pageup pagedown的步长

# 是否追踪 (滑块滑动时候 值是否会跟随位置变化而变化) 默认true
self.t.setTracking(True)

# 位置设置
self.t.setSliderPosition(88)

# 倒立外观 
self.t.setInvertedAppearance(True)

# 操作外观 (键位)
# self.t.setInvertedControls()

# 滑块方向
# Horizontal = ...  # type: 'Qt.Orientation'
# Vertical = ...  # type: 'Qt.Orientation'

self.t.setOrientation(Qt.Horizontal)


## 信号
self.t.valueChanged.connect(lambda val: self.label.setText(str(val)))
self.t.sliderPressed.connect(lambda: print('sliderPressed'))
self.t.sliderMoved.connect(lambda: print('sliderMoved'))
self.t.sliderReleased.connect(lambda: print('sliderReleased'))

# 范围变化 
self.t.rangeChanged.connect(lambda min, max: print(min, max))
self.t.setMaximum(1000)


# 行为触发
SliderMove = 7
SliderNoAction = 0

SliderPageStepAdd = 3
SliderPageStepSub = 4

SliderSingleStepAdd = 1
SliderSingleStepSub = 2

SliderToMaximum = 6
SliderToMinimum = 5
self.t.actionTriggered.connect(lambda act: print('actionTriggered', act))


'''


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())

        self.label = QLabel('0', self)
        self.label.move(150, 200)
        self.label.resize(300, 50)


        # self.t = QAbstractSlider(self)
        self.t = QSlider(self)
        self.t.move(50, 100)
        self.t.resize(300, 50)

        # 设置范围
        self.t.setMaximum(99)
        self.t.setMinimum(10)

        # 设置值或者默认值
        self.t.setValue(22)

        # 设置步长
        self.t.setSingleStep(5)
        self.t.setPageStep(10)

        # # 是否追踪
        # self.t.setTracking(True)
        #
        # self.t.setSliderPosition(88)

        # # 倒立外观
        # self.t.setInvertedAppearance(True)
        #
        # # 操作外观 (键位)
        # # self.t.setInvertedControls()
        #
        # # 滑块方向
        # # Horizontal = ...  # type: 'Qt.Orientation'
        # # Vertical = ...  # type: 'Qt.Orientation'
        #
        # self.t.setOrientation(Qt.Horizontal)

        self.label.setText(str(self.t.value()))
        self.t.valueChanged.connect(lambda val: self.label.setText(str(val)))
        self.t.sliderPressed.connect(lambda: print('sliderPressed'))
        self.t.sliderMoved.connect(lambda: print('sliderMoved'))
        self.t.sliderReleased.connect(lambda: print('sliderReleased'))

        self.t.rangeChanged.connect(lambda min, max: print(min, max))
        self.t.setMaximum(1000)

        SliderMove = 7
        SliderNoAction = 0

        SliderPageStepAdd = 3
        SliderPageStepSub = 4

        SliderSingleStepAdd = 1
        SliderSingleStepSub = 2

        SliderToMaximum = 6
        SliderToMinimum = 5
        self.t.actionTriggered.connect(lambda act: print('actionTriggered', act))


    def btn_click(self):


        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())