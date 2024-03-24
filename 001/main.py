
import sys
from PyQt5.Qt import *
from test import Ui_MainWindow

import  os
import requests

from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


R_K_URL = 'http://webquoteklinepic.eastmoney.com/GetPic.aspx?nid={}.{}&type=&unitWidth=-6&ef=&formula=RSI&imageType=KXL&timespan='

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'webquotepic.eastmoney.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}


def download(params: tuple):
    code, name, _dir, index, fn = params
    _url = R_K_URL.format(str(index), code)
    _url = _url + str(int(datetime.now().timestamp()))
    i = 1

    print('--download-tmp')
    # print('downloading ',code,name)
    while i < 3:
        try:
            raw_data = requests.get(_url, headers=headers, timeout=3).content
            f_name = os.path.join(_dir, 'tmp.png')

            with open(f_name, 'wb') as fp:
                fp.write(raw_data)

        except Exception as err:
            print('正在重试...', code, i)
            i += 1
    print('--download-tmp -end')
    fn()


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("可转债")

        self.current_date = datetime.now().strftime('%Y-%m-%d')
        self.items_code = {} # code -- 路径
        self.items_name = {} # name -- 路径
        self.items_name_code = {} # name -- code
        self.items_code_name = {} # code -- name


        self.com1 = '' # 选中的债券名称
        self.com1_max_index = 1
        self.com2 = '' # 选中的日期
        self.com2_max_index = 1

        self.executor = ThreadPoolExecutor(max_workers=10)

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        self.setupUi(self)

        self._init_read_kezhuanzhai_list()




    def _init_read_kezhuanzhai_list(self):

        tmp = []
        for root, dirs, files in os.walk('/Users/liuqt/tonghuashun/images'):
            # print("1:",root) #当前主目录
            # print("2:",dirs) #当前主目录下的所有目录
            # print("3:",files)  #当前主目录下的所有文件

            self.items_code[root[32:38]] = root
            self.items_name[root[38:]] = root

            self.items_code_name[root[32:38]] = root[38:]
            self.items_name_code[root[38:]] = root[32:38]

            tmp.append(root[38:])

        tmp = [a for a in tmp if a != ""]
        tmp.sort()
        self.comboBox.addItems(tmp)

        self.comboBox.setEditable(True)
        c = QCompleter(tmp)
        self.comboBox.setCompleter(c)

        # 日期选择
        self.comboBox_2.addItems([self.current_date])
        # self.comboBox_2.currentIndexChanged[str]

        # self.checkBox_2.clicked.connect(lambda x : print("vvv", x))




    ################### 信号

    @pyqtSlot(bool)
    def on_checkBox_2_clicked(self, is_check):

        if not is_check:
            self.label_5.clear()
            return

        if is_check:
            # 显示图片
            # download(())

            code_index_fname = os.path.join(self.items_name[self.com1], "config.env")
            index = 0
            with open(code_index_fname, 'r') as fp:
                _s = fp.read()
                index = int(_s[11:])  # index_code=

            # code name dir index

            def callback():
                f_path = os.path.join(self.items_name[self.com1], 'tmp.png')
                print('---', f_path)
                pm = QPixmap(f_path)
                # 578 276
                pm.scaled(self.label_5.size(), Qt.KeepAspectRatio)
                self.label_5.setScaledContents(True)
                self.label_5.setPixmap(pm)

            params = (self.items_name_code[self.com1], self.com1, self.items_name[self.com1], index, callback)
            self.executor.submit(download, params)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        _index = self.comboBox_2.currentIndex()
        if _index == 0:
            return
        self.comboBox_2.setCurrentIndex(_index - 1)


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        _index = self.comboBox_2.currentIndex()
        if _index + 1 == self.com2_max_index:
            return
        self.comboBox_2.setCurrentIndex(_index + 1)


    @pyqtSlot(str)
    def on_comboBox_2_currentIndexChanged(self, val):
        self.com2 = val

        # 获取图片
        f_path = os.path.join(self.items_name[self.com1], val)

        pm = QPixmap(f_path)
        # 578 276
        pm.scaled(self.label.size(), Qt.KeepAspectRatio)
        self.label.setScaledContents(True)
        self.label.setPixmap(pm)
        # self.label.adjustSize()


    @pyqtSlot(str)
    def on_comboBox_currentIndexChanged(self, val):
        self.com1 = val
        _root = self.items_name[val]

        self.comboBox_2.clear()

        for root, dirs, files in os.walk(_root):
            # print("1:",root) #当前主目录
            # print("2:",dirs) #当前主目录下的所有目录
            # print("3:",files)  #当前主目录下的所有文件

            print(files)

            tmp = []
            files.sort()
            for a in files:
                if a.endswith("png"):
                    # tmp.append(a[0:10])
                    tmp.append(a)

            self.comboBox_2.addItems(tmp)
            self.com2_max_index = len(tmp)




if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())