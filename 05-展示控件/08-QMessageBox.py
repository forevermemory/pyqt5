
import sys
from PyQt5.Qt import *

'''
QMessageBox 消息对话框  

### 构造函数
box = QProgressDialog(parent)

### 设置图标
box.setIcon(QMessageBox.NoIcon)
box.setIcon(QMessageBox.Information)
box.setIcon(QMessageBox.Question)
box.setIcon(QMessageBox.Warning)
box.setIcon(QMessageBox.Critical)

box.setIconPixmap(QPixmap("../images/web.png"))

### 设置文本
box.setTextFormat(Qt.PlainText)
box.setTextFormat(Qt.RichText)
box.setText("<h2>文件内容已经修改</h2>")
box.setInformativeText("<h4>是否直接关闭，不保存？</h4>")
box.setCheckBox(QCheckBox("下次不再提醒", box))
box.setDetailedText("你修改的内容是.......")

### 设置按钮
# 标准按钮
QMessageBox.Open
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Discard
QMessageBox.Apply
QMessageBox.Reset
QMessageBox.RestoreDefaults
QMessageBox.Help
QMessageBox.SaveAll
QMessageBox.Yes
QMessageBox.YesToAll
QMessageBox.No
QMessageBox.NoToAll
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore

# 角色
QMessageBox.InvalidRole
QMessageBox.AcceptRole
QMessageBox.RejectRole
QMessageBox.DestructiveRole
QMessageBox.ActionRole
QMessageBox.HelpRole
QMessageBox.YesRole
QMessageBox.NoRole
QMessageBox.ApplyRole
QMessageBox.ResetRole

## 设置标准按钮
box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

## 自定义按钮
box.addButton("xx1", QMessageBox.RejectRole)
box.addButton("xx2", QMessageBox.ApplyRole)

# 获取按钮角色
box.buttonRole(btn1)

## 设置默认按钮
box.setDefaultButton(QMessageBox.Yes / btn)

## esc 快捷按钮
box.setEscapeButton(QMessageBox.No)

### 信号
box.buttonClicked.connect(test)

### 静态方法
QMessageBox.about(window, "xx1", "xx2")
QMessageBox.aboutQt(window, "xx1")
QMessageBox.critical()
QMessageBox.information()
QMessageBox.question()
QMessageBox.warning()

'''

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

    btn = QPushButton('button', window)
    btn.move(50, 20)




    box = QMessageBox(window)
    box.setWindowTitle("消息提示")
    box.setIcon(QMessageBox.NoIcon)
    box.setIcon(QMessageBox.Information)
    box.setIcon(QMessageBox.Question)
    box.setIcon(QMessageBox.Warning)
    box.setIcon(QMessageBox.Critical)

    box.setIconPixmap(QPixmap("../images/web.png"))

    box.setTextFormat(Qt.PlainText)
    box.setTextFormat(Qt.RichText)
    box.setText("<h2>文件内容已经修改</h2>")
    box.setInformativeText("<h4>是否直接关闭，不保存？</h4>")
    box.setCheckBox(QCheckBox("下次不再提醒", box))
    box.setDetailedText("你修改的内容是.......")

    ### 设置按钮
    # 标准按钮
    QMessageBox.Open
    QMessageBox.Save
    QMessageBox.Cancel
    QMessageBox.Close
    QMessageBox.Discard
    QMessageBox.Apply
    QMessageBox.Reset
    QMessageBox.RestoreDefaults
    QMessageBox.Help
    QMessageBox.SaveAll
    QMessageBox.Yes
    QMessageBox.YesToAll
    QMessageBox.No
    QMessageBox.NoToAll
    QMessageBox.Abort
    QMessageBox.Retry
    QMessageBox.Ignore

    # 角色
    QMessageBox.InvalidRole
    QMessageBox.AcceptRole
    QMessageBox.RejectRole
    QMessageBox.DestructiveRole
    QMessageBox.ActionRole
    QMessageBox.HelpRole
    QMessageBox.YesRole
    QMessageBox.NoRole
    QMessageBox.ApplyRole
    QMessageBox.ResetRole

    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    box.addButton("xx1", QMessageBox.RejectRole)
    box.addButton("xx2", QMessageBox.ApplyRole)
    box.setDefaultButton(QMessageBox.Yes)

    box.setEscapeButton(QMessageBox.No)

    yes_btn = box.button(QMessageBox.Yes)
    no_btn = box.button(QMessageBox.No)
    print(yes_btn, no_btn)

    def test(btn1):

        print(box.buttonRole(btn1))
        print(btn1)
    box.buttonClicked.connect(test)
    box.show()


    def btn_click():
        # box.show()
        # box.showMessage("okok")
        # box.showMessage("okok")
        # box.showMessage("okok2")
        pass

    btn.clicked.connect(btn_click)
    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
