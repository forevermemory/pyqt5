import sys
from PyQt5.Qt import *


# QLineEdit 单行文本输入框

# # 内容长度显示
# line1.setMaxLength(3)
# print(line1.maxLength())

# 只读限制
# line1.setReadOnly(True)
# line1.setText("readonly")
# print(line1.isReadOnly())

# 验证器1 继承
# 重写validate 和 fixup 方法
class AgeValidator(QValidator):
    # def validate(self, a0: str, a1: int) -> typing.Tuple['QValidator.State', str, int]:
    def validate(self, input_str: str, pos: int):
        # QValidator.Acceptable
        # QValidator.Intermediate
        # QValidator.Invalid

        print('validate',input_str, pos)
        try:
            val = int(input_str)
            print('val', val)
            if val <= 100 and val >=10:
                return (QValidator.Acceptable, input_str, pos)
            elif val <10 and val >0:
                return (QValidator.Intermediate, input_str, pos)
            else:
                return (QValidator.Invalid, input_str, pos)
        except Exception as _:
            return (QValidator.Acceptable, '', pos)

        return (QValidator.Invalid, input_str, pos)

    def fixup(self, input_str: str) -> str:
        # 如果validate最后的状态为 Intermediate,在失去焦点后 会调用fixup进行一次纠错
        print('fixup ', input_str)
        return "18"

# 验证器2 使用提供好的类
# QIntValidator
# QDoubleValidator
# QRegExpValidator
# 可以继承上面的类 然后重写fixup方法


### 掩码设置


def main():
    # 1. 创建应用程序对象,
    app = QApplication(sys.argv)

    # 2. 创建控件
    window = QWidget()
    window.setWindowTitle("晴天的pyqt学习-")
    window.resize(500, 500)
    window.move(300, 200)

    # code
    line1 = QLineEdit("", window)
    line1.move(100, 100)
    line1.setPlaceholderText("请输入用户名")

    line2 = QLineEdit("", window)
    line2.move(100, 200)
    line2.setPlaceholderText("请输入密码")
    line2.setEchoMode(QLineEdit.Password)

    # # 内容长度显示
    # line1.setMaxLength(3)
    # print(line1.maxLength())

    # 只读限制
    # line1.setReadOnly(True)
    # line1.setText("readonly")
    # print(line1.isReadOnly())

    # 验证器1
    # line1.setValidator(AgeValidator())

    # 掩码 以-为分隔符 A代表字母 9代表数字 其它字符参考搜索: 掩码字符
    # line1.setInputMask("AAAA-999A")



    btn = QPushButton("按钮", window)
    btn.move(100, 300)

    def cao():
        pass
    btn.clicked.connect(cao)

    # 展示控件
    window.show()

    # 进入消息循环
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
