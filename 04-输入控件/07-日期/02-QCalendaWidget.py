
import sys
from PyQt5.Qt import *

'''

### QCalendarWidget 日期
## 日期范围
qc = QCalendarWidget(self)
qc.setMaximumDate(QDate(2022, 11, 1))
qc.setMinimumDate(QDate(2020, 11, 1))

qc.setDateRange()

## 日期编辑
qc.setDateEditEnabled(True)
qc.setDateEditAcceptDelay(3000) # 3s后自动保存

## 日期获取
qc.yearShown()
qc.monthShown()
qc.selectedDate()

## 格式外观
qc.setNavigationBarVisible(False)
qc.setFirstDayOfWeek(Qt.Sunday)
qc.setGridVisible(True)

# 头部样式
hft = QTextCharFormat()
hft.setFontPointSize(18)
qc.setHeaderTextFormat(hft)

# 周几字符串显示
qc.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
qc.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)

# 不显示左边第几周
qc.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

# 选中
# qc.setSelectedDate()
qc.setSelectionMode(QCalendarWidget.NoSelection)  # 不可选中


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
        qc = QCalendarWidget(self)

        # qc.setMaximumDate(QDate(2022, 11, 1))
        # qc.setMinimumDate(QDate(2020, 11, 1))
        # qc.setDateRange()

        # qc.setDateEditEnabled(True)
        # qc.setDateEditAcceptDelay(3000)

        # 日期获取

        qc.yearShown()
        qc.monthShown()
        qc.selectedDate()

        # 格式外观

        # qc.setNavigationBarVisible(False)
        # qc.setFirstDayOfWeek(Qt.Sunday)
        # qc.setGridVisible(True)
        #
        # hft = QTextCharFormat()
        # hft.setFontPointSize(18)
        # qc.setHeaderTextFormat(hft)

        # qc.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
        # qc.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)

        # qc.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        # 选中
        # qc.setSelectedDate()
        qc.setSelectionMode(QCalendarWidget.NoSelection)

        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())