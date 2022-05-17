
import sys
from PyQt5.Qt import *

'''
QProgressBar 进度条 
bar = QProgressBar(self)

### 设置范围和当前值
bar.setMinimum(0)
bar.setMaximum(100)
# bar.setRange(0, 100)
bar.setValue(20) ## 如果最大值和最小值都为0 则显示繁忙
        
### 格式设置 --mac上不生效
bar.setFormat("当前进度为%p")
bar.setFormat("当前值为%v")
bar.setFormat("当前总值为%m")

## 格式字符对齐方式 文本显示在什么位置
bar.setAlignment(Qt.AlignHCenter)

### 文本操作  --mac上不生效
bar.setTextVisible(True)
bar.setTextDirection(QProgressBar.BottomToTop)
bar.setTextDirection(QProgressBar.TopToBottom)


### 设置方向
bar.setOrientation(Qt.Horizontal)
bar.setOrientation(Qt.Vertical)

### 进度条反向
bar.setInvertedAppearance(True)

### 信号
        
'''


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法



    def btn_click(self):
       pass

    def init_ui(self):

        bar = QProgressBar(self)

        bar.move(100, 100)
        bar.resize(200, 50)

        # bar.setMinimum(0)
        # bar.setMaximum(0)
        # bar.setRange(0, 100)

        bar.setValue(20)
        #
        # bar.setFormat("当前进度为%p")
        # bar.setFormat("当前值为%v")
        # bar.setFormat("当前总值为%m")
        # print(bar.format())
        bar.setTextVisible(True)
        bar.setTextDirection(QProgressBar.BottomToTop)
        bar.setTextDirection(QProgressBar.TopToBottom)

        # bar.setVisible(True)

        # bar.setOrientation(Qt.Horizontal)
        # bar.setOrientation(Qt.Vertical)
        # bar.resize(30, 200)

        # bar.setAlignment(Qt.AlignHCenter)
        #
        # bar.setInvertedAppearance()

        timer = QTimer(bar)
        def timer_timeout():
            bar.setValue(bar.value()+1)
        timer.timeout.connect(timer_timeout)
        timer.start(100)

        def bar_valueChanged(val):
            print(val)
        bar.valueChanged.connect(bar_valueChanged)





if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())