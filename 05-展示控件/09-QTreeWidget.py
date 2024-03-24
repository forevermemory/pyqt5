
import sys
from PyQt5.Qt import *

'''
QTreeWidget  可以只有一列，也可以有多列
城市         学校数量
  江苏         10
    南京        8
    无锡        2
  安徽          6

 
构造函数
    tree = QTreeWidget(QWidget * parent = 0)

顶级条目
    设置列数量和标题
        tree.setColumnCount(2)
        tree.setHeaderLabels(["城市", "数量"])

子节点
    QTreeWidgetItem() 

    item = QTreeWidgetItem(['江苏', "10"])
    item_1 = QTreeWidgetItem(['南京', '8'])
    item_2 = QTreeWidgetItem(['无锡', '2'])
    item.addChild(item_1)
    item.addChild(item_2)
    tree.addTopLevelItem(item)
 
信号
    itemActivated(QTreeWidgetItem * item, int column) // 条目列被激活
    itemChanged(QTreeWidgetItem * item, int column)   // 条目列的数据发生变化，比如文本或图标修改了
    itemClicked(QTreeWidgetItem * item, int column)  // 条目列被单击
    itemDoubleClicked(QTreeWidgetItem * item, int column) // 条目列被双击
    itemEntered(QTreeWidgetItem * item, int column) // 进入条目列
    itemPressed(QTreeWidgetItem * item, int column) // 条目列被点 击按下

    itemExpanded(QTreeWidgetItem * item)  // 条目展开时发送信号
    itemCollapsed(QTreeWidgetItem * item) // 条目折叠时发送信号

槽函数
    clear() // 清空整个树形控件
    collapseItem(QTreeWidgetItem * item) // 折叠指定的条目
    expandItem(QTreeWidgetItem * item)  // 展开指定 条目
    scrollToItem(QTreeWidgetItem * item, QAbstractItemView::ScrollHint hint=EnsureVisible) // 滚动到指定条目
    
父类 QTreeView
    expandAll()  // 展开所有子孙条目
    collapseAll() // 折叠所有子孙条目
    expandToDepth(int depth) // 展开 depth 层级的子节点

    
    备注
        如果调用槽函数  expandAll() 展开所有子孙条目，那么不会触发 itemExpanded() 信号
        类似地，如果用槽函数 collapseAll() 折叠所有子孙条目，也不会触发itemCollapsed() 信号

'''


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("晴天的pyqt学习-")
        self.resize(500, 500)
        self.move(300, 200)

        self.init_ui()  # 界面绘制交给InitUi方法


    def tree_itemClick(self, item: QTreeWidgetItem, column: int):
        print(item.text(0), column)

    def tree_itemExpanded(self, item: QTreeWidgetItem):
        print('展开', item.text(0))

    def tree_itemCollapsed(self, item: QTreeWidgetItem):
        print('折叠', item.text(0))

    def init_ui(self):

        tree = QTreeWidget(self)

        tree.setColumnCount(2)
        tree.setHeaderLabels(['城市', '学校数量'])
        # item = QTreeWidgetItem()
        # item.setText(0, "jiangsu")

        item = QTreeWidgetItem(['江苏', "10"])
        item_1 = QTreeWidgetItem(['南京', '8'])
        item_2 = QTreeWidgetItem(['无锡', '2'])
        item.addChild(item_1)
        item.addChild(item_2)
        tree.addTopLevelItem(item)

        item2 = QTreeWidgetItem(['安徽', '7'])
        item2_1 = QTreeWidgetItem(['合肥', '3'])
        item2_2 = QTreeWidgetItem(['马鞍山', '4'])
        item2.addChild(item2_1)
        item2.addChild(item2_2)
        tree.addTopLevelItem(item2)

        # tree.expandItem(item2)
        # tree.expandAll()

        tree.move(100, 100)

        tree.itemClicked.connect(self.tree_itemClick)
        tree.itemExpanded.connect(self.tree_itemExpanded)
        tree.itemCollapsed.connect(self.tree_itemCollapsed)

        tree.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    # print(QWidget.__subclasses__())

    window.show()
    sys.exit(app.exec_())