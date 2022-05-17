
import sys
from PyQt5.Qt import *

'''
QLabel

### 对齐方式
label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

### 缩进和边距
label.setIndent(2)
label.setMargin(5)

### 富文本设置
label.setTextFormat(Qt.PlainText)
label.setTextFormat(Qt.RichText)

### 小伙伴 
buddy

### 内容缩放 (仅支持图片)
label.setPixmap(QPixmap('../images/web.png'))

### 自动调整大小
label.setScaledContents(True)

### 文本交互标志
Qt.NoTextInteraction
Qt.TextSelectableByMouse
Qt.TextSelectableByKeyboard
Qt.TextEditable
label.setTextInteractionFlags(Qt.TextSelectableByMouse)

### 打开外部链接
label.setText('<a href="https://www.baidu.com">百度</a>')
label.setOpenExternalLinks(True)

### 换行
label.setWordWrap(True)

### 文字竖着排列
label.setText('\n'.join('文字竖着排列'))

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

        label = QLabel("Qlabel-hello(&s)", self)
        label.move(100, 100)
        label.resize(300, 300)
        label.setStyleSheet("background-color: pink")

        # label.setScaledContents(True)

        ### 对齐方式
        # label.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        # ### 缩进和边距
        # label.setIndent(2)
        # label.setMargin(5)

        # ### 富文本设置
        # label.setTextFormat(Qt.PlainText)
        # label.setTextFormat(Qt.RichText)

        # ### buddy
        # l1 = QLineEdit(self)
        # l1.move(100, 100)
        #
        # l2 = QLineEdit(self)
        # l2.move(100, 200)
        #
        # label.setBuddy(l2)

        # label.setPixmap(QPixmap('../images/web.png'))
        # label.setScaledContents(True)

        # ### 文本交互标志
        # Qt.NoTextInteraction
        # Qt.TextSelectableByMouse
        # Qt.TextSelectableByKeyboard
        # Qt.TextEditable
        # label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        # label.setText('<a href="https://www.baidu.com">百度</a>')
        # label.setOpenExternalLinks(True)

        # label.setWordWrap(True)
        label.setText("\n".join('文字竖着排列'))


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())