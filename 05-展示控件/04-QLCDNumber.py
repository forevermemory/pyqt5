
import sys
from PyQt5.Qt import *

'''
QLCDNumber lcd展示控件

### 构造函数
lcd = QLCDNumber(5, self) # 5为显示位数
lcd.move(100, 100)
lcd.resize(200, 50)

lcd.display(982)

### 设置位数 
lcd.setDigitCount(5)

### 设置模式 进制模式
Bin = 3
Dec = 1
Hex = 0
Oct = 2
lcd.setMode(QLCDNumber.Oct)

### 溢出判定 和信号
print(lcd.checkOverflow(1000))
lcd.overflow.connect(lambda: print('overflow'))

lcd.display(1000)

### 分段样式
Filled = 1
Flat = 2
Outline = 0
lcd.setSegmentStyle(QLCDNumber.Outline)
lcd.display(888)

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

        lcd = QLCDNumber(3, self)
        lcd.move(100, 100)
        lcd.resize(200, 50)

        # # lcd.setDigitCount(5)
        # Bin = 3
        # Dec = 1
        # Hex = 0
        # Oct = 2
        # lcd.setMode(3)
        # lcd.display(11)
        #
        # print(lcd.checkOverflow(1000))
        # lcd.overflow.connect(lambda: print('overflow'))
        #
        # lcd.display(1000)
        Filled = 1
        Flat = 2
        Outline = 0
        lcd.setSegmentStyle(QLCDNumber.Outline)
        lcd.display(888)





if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())