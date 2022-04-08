
import sys
from PyQt5.Qt import *

'''

主要为 文本光标的方法

QTextEdit 文本
1. 纯文本
setPlainText("设置")
insertPlainText("insertPlainText")
toPlainText()

2 html
setHtml('<h2>我是h2标签</h2> <h3>我是h3标签</h3> ')
insertHtml('<h4>我是h4标签</h4>')
print(self.t.toHtml())

# 3 设置文本 自动判断
self.t.setText()

4 append 向光标出追加
5 clear 清空输入框

6. 文本光标  t.textCursor() -> QTextCursor
    t.document() 可以获取文本对象 QTextDocument
    t.textCursor() 获取光标对象 QTextCursor
    
6.1   添加内容 
    插入文本 insertText insertHtml
    插入图片 insertImage(QTextImageFormat)
    插入句子 insertFragment
    插入列表 insertList/createList
        insertList(self, QTextListFormat) -> QTextList
        insertList(self, QTextListFormat.Style) -> QTextList
    插入表格        
        # 方式一: insertTable(rows, cols)
        # 方式2: insertTable(rows, cols, QTextTableFormat)
    插入文本块
        insertBlock
    插入框架 相当于插入一个区域 这个区域和QTextEdit类似
        insertFrame
    
6.2  设置和合并格式
    设置块的char格式 setBlockCharFormat
    设置当前块格式(或者选择中包含的所有块) setBlockFormat
    将光标的当前字符格式设置为给定格式 如果光标有选择 则给定格式应用于当前选择 setCharFormat
    合并当前块char格式 mergeBlockCharFormat
    合并当前块格式 mergeBlockFormat
    合并当前字符格式 mergeCharFormat
    
6.3 获取内容和格式
    # 获取光标所在文本块 block()
    # 获取光标所在文本块格式 blockFormat()
    # 获取光标所在文本块字符格式 blockCharFormat()
    # 获取光标所在文本块编号 blockNumber()
    # 获取文本字符格式 charFormat()
    # 获取当前所在框架 currentFrame()
    # 获取当前所在的文本列表 currentList()
    # 获取当前表格 currentTable()

6.4 文本选中和清空
    选中
        setPosition(1)
        movePosition()
        select()
    选中内容获取
        selectedText()
        print(text_cursor.selection())
        selectedTableCells()
    选中位置获取
        selectionStart()
        selectionEnd()
        clearSelection()
        hasSelection()
    选中文本移除
        removeSelectedText()
    清空和判定

6.5 删除内容
    (类似于 backspace和del_)
    deleteChar() # 没有选中文本删除光标后一个字符 有删除选中文本
    deletePreviousChar() # 没有选中文本删除光标前一个字符 有删除选中文本

6.6 位置相关
    atStart() # 是否在文档开始
    atEnd() #  是否在文档末尾
    atBlockEnd() # 是否在文本块末尾
    atBlockStart() # 是否在文本块开始
    columnNumber() # 在第几列
    position() # 光标位置
    positionInBlock() # 在文本块中的位置
    
6.7 开始和结束编辑标识
    beginEditBlock()
    endEditBlock()

'''

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.t = QTextEdit('hello world, china', self)
        self.t.move(50, 100)
        self.t.resize(300, 300)

        self.btn = QPushButton('button', self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.btn_click)

        self.btn = QPushButton('clear', self)
        self.btn.move(150, 20)
        self.btn.clicked.connect(lambda: self.t.clear())

        self.init_ui()  # 界面绘制交给InitUi方法

    def btn_click(self):
        # self.文本内容_设置和insert()
        # self.文本内容_append和clear()
        # self.设置和合并格式()
        # self.testCursor_获取内容和格式()
        self.textCursor_文本选中和清空()

    def init_ui(self):
        pass

    def textCursor_开始和结束编辑标识(self):
        # 获取光标
        text_cursor = self.t.textCursor()

        text_cursor.beginEditBlock()
        text_cursor.endEditBlock()


    def textCursor_位置相关(self):
        # 获取光标
        text_cursor = self.t.textCursor()

        text_cursor.atStart() # 是否在文档开始
        text_cursor.atEnd() #  是否在文档末尾
        text_cursor.atBlockEnd() # 是否在文本块末尾
        text_cursor.atBlockStart() # 是否在文本块开始
        text_cursor.columnNumber() # 在第几列
        text_cursor.position() # 光标位置
        text_cursor.positionInBlock() # 在文本块中的位置

    def textCursor_删除内容(self):

        # 获取光标
        text_cursor = self.t.textCursor()

        text_cursor.deleteChar() # 没有选中文本删除光标后一个字符 有删除选中文本

        text_cursor.deletePreviousChar() # 没有选中文本删除光标前一个字符 有删除选中文本


    def textCursor_文本选中和清空(self):
        # 获取光标
        text_cursor = self.t.textCursor()

        # 设置位置
        # MoveAnchor 移动光标 锚点不动
        # KeepAnchor 移动光标 有选中效果
        text_cursor.setPosition(1)

        text_cursor.movePosition()
        # QTextCursor.SelectionType
        text_cursor.select()

        # 选中内容获取
        text_cursor.selectedText()
        print(text_cursor.selection())
        text_cursor.selectedTableCells()
        # 选中位置获取
        text_cursor.selectionStart()
        text_cursor.selectionEnd()
        text_cursor.clearSelection()
        text_cursor.hasSelection()
        text_cursor.removeSelectedText()

        # 选中文本移除
        # 清空和判定


    def testCursor_获取内容和格式(self):

        # 获取光标
        text_cursor = self.t.textCursor()

        # 获取光标所在文本块
        text_cursor.block()

        # 获取光标所在文本块格式
        text_cursor.blockFormat()

        # 获取光标所在文本块字符格式
        text_cursor.blockCharFormat()

        # 获取光标所在文本块编号
        text_cursor.blockNumber()

        # 获取文本字符格式
        text_cursor.charFormat()

        # 获取当前所在框架
        text_cursor.currentFrame()

        # 获取当前所在的文本列表
        text_cursor.currentList()

        # 获取当前表格
        text_cursor.currentTable()

        pass

    def textCursor_设置和合并格式(self):

        # 获取光标
        text_cursor = self.t.textCursor()

        # 设置块的char格式
        text_cursor.setBlockCharFormat()

        # 设置当前块格式(或者选择中包含的所有块)
        text_cursor.setBlockFormat()

        # 将光标的当前字符格式设置为给定格式 如果光标有选择 则给定格式应用于当前选择
        text_cursor.setCharFormat()

        # 合并当前块char格式
        text_cursor.mergeBlockCharFormat()

        # 合并当前块格式
        text_cursor.mergeBlockFormat()

        # 合并当前字符格式
        text_cursor.mergeCharFormat()

    def textCursor_添加内容(self):

        # 获取光标
        text_cursor = self.t.textCursor()

        # 插入文本
        text_cursor.insertText("插入普通文本\n")

        _format = QTextCharFormat()
        _format.setFontFamily("宋体")
        text_cursor.insertText('带格式的\n', _format)
        text_cursor.insertHtml('<h4>insertHtml</h4>')


        # 插入图片
        img = QTextImageFormat() # 建议使用这种
        img.setName("../../images/web.png")
        img.setWidth(30)
        # text_cursor.insertImage(img)

        # 插入句子
        qdf = QTextDocumentFragment()
        # qdf.fromPlainText(' fromPlainText <h4>insertHtml</h4>')
        qdf.fromPlainText(' fromPlainText \n ')
        text_cursor.insertFragment(qdf) # mac未生效

        # 插入列表
        # insert会在光标处插入
        # create会把当前行当成一个列表项
        # 使用方式一 直接传 QTextListFormat的枚举
        QTextListFormat.ListDisc # 一个圆圈
        QTextListFormat.ListCircle # 一个空的圆圈
        QTextListFormat.ListSquare # 一个方块
        QTextListFormat.ListDecimal # 十进制按升序排列
        QTextListFormat.ListLowerAlpha # 小写拉丁字母
        QTextListFormat.ListUpperAlpha # 大写拉丁字母
        QTextListFormat.ListLowerRoman # 小写罗马数字
        QTextListFormat.ListUpperRoman # 大写罗马数字

        # lst = text_cursor.insertList(QTextListFormat.ListDisc) # QTextList


        # 使用方式二 传QTextListFormat对象
        tlf = QTextListFormat()
        tlf.setIndent(3)
        tlf.setNumberPrefix("start")
        tlf.setNumberSuffix("-end")
        tlf.setStyle(QTextListFormat.ListDecimal)
        # lst = text_cursor.insertList(tlf) # QTextList

        # 插入表格
        # 方式一: insertTable(rows, cols)
        # text_cursor.insertTable(5, 3)

        # 方式2: insertTable(rows, cols, QTextTableFormat)

        tab_format = QTextTableFormat()
        tab_format.setAlignment(Qt.AlignLeft) # 设置对齐方式
        tab_format.setCellPadding(3) # 内边距
        tab_format.setCellSpacing(5) # 外边距

        # 设置宽度限制 传元组吧 有几列传几个值     FixedLength PercentageLength VariableLength
        _constraints = (QTextLength(QTextLength.PercentageLength, 50),
                            QTextLength(QTextLength.PercentageLength, 20),
                            QTextLength(QTextLength.PercentageLength, 30))
        tab_format.setColumnWidthConstraints(_constraints)

        # text_cursor.insertTable(5, 3, tab_format)

        # 插入文本块
        text_cursor.insertBlock()
        # 插入框架
        _tframe = QTextFrameFormat()
        _tframe.setBorder(3)
        text_cursor.insertFrame(_tframe)
        pass


    def 文本内容_append和clear(self):
        self.t.append("append")

    def 文本内容_设置和insert(self):
        # 纯文本
        # self.t.setPlainText("设置")
        # self.t.insertPlainText("insertPlainText")
        # print(self.t.toPlainText())

        # html
        self.t.setHtml('<h2>我是h2标签</h2> <h3>我是h3标签</h3> ')
        self.t.insertHtml('<h4>我是h4标签</h4>')
        print(self.t.toHtml())

        # 设置文本 自动判断
        self.t.setText()

        pass


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())