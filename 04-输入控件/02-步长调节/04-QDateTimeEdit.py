import sys
from PyQt5.Qt import *

'''
QDateTimeEdit 日期时间选择器

# self.t = QDateTimeEdit(self) 
# self.t = QDateTimeEdit(QDate.currentDate(), self)
# self.t = QDateTimeEdit(QTime.currentTime(), self)
# self.t = QDateTimeEdit(QDateTime.currentDateTime(), self)


# section控制 年月日时分秒
print(self.t.sectionCount())
print(self.t.currentSectionIndex())

# self.t.setCurrentSectionIndex()

self.t.setFocus()
self.t.setCurrentSection(QDateTimeEdit.DaySection)
    AmPmSection = 1
    DaySection = 256
    HourSection = 16
    MinuteSection = 8
    MonthSection = 512
    MSecSection = 2
    NoSection = 0
    SecondSection = 4
    YearSection = 1024
    
print(self.t.sectionText(QDateTimeEdit.DaySection))


# 日期时间范围
self.t.setMaximumDateTime()
self.t.setMaximumDate()
self.t.setMaximumTime()
self.t.setDateRange()
self.t.setDateTimeRange()
self.t.setTimeRange()
        
# 弹出日历选择控件 
self.t.setCalendarPopup(True)

# 获取值
 self.t.date()
self.t.time()
self.t.dateTime()

# 信号
self.t.dateChanged
self.t.timeChanged
self.t.dateTimeChanged
        
'''

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        # self.t = QDateTimeEdit(self)
        # self.t = QDateTimeEdit(QDate.currentDate(), self)
        self.t = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.t.move(50, 100)
        self.t.resize(300, 50)

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())

    def btn_click(self):

        # print(self.t.sectionCount())
        # print(self.t.currentSectionIndex())
        #
        # # self.t.setCurrentSectionIndex()
        # AmPmSection = 1
        # DaySection = 256
        # HourSection = 16
        # MinuteSection = 8
        # MonthSection = 512
        # MSecSection = 2
        # NoSection = 0
        # SecondSection = 4
        # YearSection = 1024
        # self.t.setFocus()
        # self.t.setCurrentSection(QDateTimeEdit.DaySection)
        #
        # print(self.t.sectionText(QDateTimeEdit.DaySection))


        # 日期时间范围
        # self.t.setMaximumDateTime()
        # self.t.setMaximumDate()
        # self.t.setMaximumTime()
        # self.t.setDateRange()
        # self.t.setDateTimeRange()
        # self.t.setTimeRange()

        # self.t.setCalendarPopup(True)
        #
        # self.t.date()
        # self.t.time()
        # self.t.dateTime()

        # 信号
        # self.t.dateChanged
        # self.t.timeChanged
        # self.t.dateTimeChanged

        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())