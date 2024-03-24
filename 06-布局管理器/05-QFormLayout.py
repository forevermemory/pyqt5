
import sys
from PyQt5.Qt import *

'''
### QFormLayout 表单布局

### 行操作
## 添加行
layout.addRow("姓名:", name_input)

## 插入行
layout.insertRow()

## 修改
layout.setLayout()
layout.setWidget()

# 角色
FieldRole = 1
LabelRole = 0
SpanningRole = 2

# 获取标签
layout.labelForField(name_input)

## 删除
layout.removeRow() # 删除子控件
layout.takeRow() # 不删除子控件

### 行的包装策略
layout.setRowWrapPolicy(QFormLayout.DontWrapRows) # 字段在标签旁边
layout.setRowWrapPolicy(QFormLayout.WrapLongRows) 
layout.setRowWrapPolicy(QFormLayout.WrapAllRows)# 字段在变迁下边

### 对齐方式
layout.setFormAlignment(Qt.AlignRight)
layout.setLabelAlignment(Qt.AlignCenter)

### 间距
layout.setVerticalSpacing(30)
layout.setHorizontalSpacing(30)

'''

import sys
from PyQt5.Qt import *


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("title-")
    window.resize(500, 500)
    window.move(300, 200)
    # label1 = QLabel("标签1", window)

    # 1. 创建一个布局管理器
    layout = QFormLayout()

    # 2. 把布局管理器设置给需要布局的父控件
    window.setLayout(layout)

    # 3. 把需要布局的子控件添加到布局管理器
    name_input = QLineEdit()
    age_input = QSpinBox()

    male_input = QRadioButton("男")
    female_input = QRadioButton("女")
    nomale_input = QRadioButton("未知")
    sex_lay = QHBoxLayout()
    sex_lay.addWidget(male_input)
    sex_lay.addWidget(female_input)
    sex_lay.addWidget(nomale_input)

    btn_input = QPushButton("注册")
    layout.addRow("姓名(name):", name_input)
    layout.addRow("年龄:", age_input)
    layout.addRow("性别:", sex_lay)
    layout.addRow(btn_input)

    ## 插入行
    # layout.insertRow()
    # layout.setLayout()
    # layout.setWidget()
    print(layout.labelForField(sex_lay))

    # layout.removeRow()
    # layout.takeRow()

    # ### 行的包装策略
    # layout.setRowWrapPolicy(QFormLayout.DontWrapRows) # 字段在标签旁边
    # layout.setRowWrapPolicy(QFormLayout.WrapLongRows)
    # layout.setRowWrapPolicy(QFormLayout.WrapAllRows)# 字段在变迁下边

    # ### 对齐方式
    # layout.setFormAlignment(Qt.AlignRight)
    # layout.setLabelAlignment(Qt.AlignCenter)

    ### 间距
    layout.setVerticalSpacing(30)
    layout.setHorizontalSpacing(30)

    window.show()
    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
