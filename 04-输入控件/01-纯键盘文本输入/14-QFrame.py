import sys
from PyQt5.Qt import *


# QFrame
# 形状
# QFrame.NoFrame  # 什么都没有
# QFrame.Box  # 画个框
# QFrame.Panel  # 面板 是内容凸起或者凹陷
# QFrame.HLine  # 没有框架的=水平线 用作分隔符
# QFrame.VLine  # 没有框架的=垂直 用作分隔符
# QFrame.StyledPanel  # 绘制矩形面板 外观取决于当前的gui样式
# QFrame.WinPanel  # 建议使用StyledPanel
#
# f.setFrameShape(QFrame.Panel)
# # 阴影
# QFrame.Plain  # 框架和内容与周围环境呈现水平 无3d效果
# QFrame.Raised  # 框架和内容凸起 使用当前颜色组的浅色和深色绘制3d凸起线
# QFrame.Sunken  # 框架和内容 使用当前颜色组的浅色和深色绘制3d凹线
# f.setFrameShadow(QFrame.Raised)
#
# ### 线宽
# # 外线
# f.setLineWidth(5)
# print(f.lineWidth())
# # 中线宽度
# f.setMidLineWidth(3)
# print(f.midLineWidth())
# # 总宽度
# print(f.frameWidth())

def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code

    f = QFrame(window)
    f.resize(200, 100)
    f.move(50, 50)
    f.setStyleSheet("background-color: #ccc")

    # 形状
    QFrame.NoFrame # 什么都没有
    QFrame.Box # 画个框
    QFrame.Panel # 面板 是内容凸起或者凹陷
    QFrame.HLine # 没有框架的=水平线 用作分隔符
    QFrame.VLine  # 没有框架的=垂直 用作分隔符
    QFrame.StyledPanel  # 绘制矩形面板 外观取决于当前的gui样式
    QFrame.WinPanel # 建议使用StyledPanel

    f.setFrameShape(QFrame.Panel)
    # 阴影
    QFrame.Plain # 框架和内容与周围环境呈现水平 无3d效果
    QFrame.Raised # 框架和内容凸起 使用当前颜色组的浅色和深色绘制3d凸起线
    QFrame.Sunken # 框架和内容 使用当前颜色组的浅色和深色绘制3d凹线
    f.setFrameShadow(QFrame.Raised)

    ### 线宽
    # 外线
    f.setLineWidth(5)
    print(f.lineWidth())
    # 中线宽度
    f.setMidLineWidth(3)
    print(f.midLineWidth())
    # 总宽度
    print(f.frameWidth())


    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
