
import sys
from PyQt5.Qt import *
from demo import Ui_MainWindow
import  os
import requests
from requests.auth import HTTPBasicAuth

from datetime import datetime,timedelta
from concurrent.futures import ThreadPoolExecutor
import  csv

USERNAME = 'root'
PASSWORD = 'taosdata'

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.current_date = datetime.now().strftime('%Y-%m-%d')

        self.init_ui()  # 界面绘制交给InitUi方法

        self.session = requests.session()
        self.box = QMessageBox(self)
        self.box.setIcon(QMessageBox.NoIcon)

        self._host = 'http://%s:6041/rest/sql' % (self.edit_ip.text())


    def init_ui(self):
        self.setupUi(self)
        self.edit_ip.setText('192.168.80.120')

        self.date_start.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.date_end.setDisplayFormat("yyyy-MM-dd HH:mm:ss")

        # today = datetime.now()
        today = datetime.now() - timedelta(days=11)
        self.date_end.setDateTime(today)

        # previous_date = today - timedelta(days=1)
        previous_date = today - timedelta(hours=1)
        self.date_start.setDateTime(previous_date)


    @pyqtSlot()
    def on_export_data_clicked(self):
        # print('11')
        start = self.date_start.dateTime().toPyDateTime()
        end = self.date_end.dateTime().toPyDateTime()

        if start.timestamp() > end.timestamp():
            self.statusBar.showMessage("牛逼", -1)
            return

        sql = "select * from zhipu.hardware_informations where ts > '%s' and ts < '%s' " % (
            start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')
        )

        print(sql)

        self.export_data.setEnabled(False)
        self.statusBar.showMessage("正在请求中,请稍后", -1)

        res = None
        try:
            res = self.session.post(
                url=self._host,
                data=sql,
                auth=HTTPBasicAuth(USERNAME, PASSWORD),
                # timeout=3,
            )
        except Exception as err:
            print(err)
            self.box.setText("请求失败:"+str(err))
            self.box.show()
            self.export_data.setEnabled(True)
            return

        response_data = res.json()
        if response_data['code'] != 0:
            msg = '获取数据失败:%s' % (response_data['desc'])
            self.statusBar.showMessage(msg, -1)
            self.export_data.setEnabled(True)
            return

        msg = '获取数据成功,累计:%d' % (len(response_data['data']))
        self.statusBar.showMessage(msg, -1)

        # print(response_data)

        rows_header = []
        for m in response_data['column_meta']:
            rows_header.append(m[0])

        filename = "data_%s--%s.csv" %(
            start.strftime('%Y-%m-%d_%H_%M_%S'), end.strftime('%Y-%m-%d_%H_%M_%S')
        )

        fp = open(filename, 'w', newline='')
        writer = csv.writer(fp)

        writer.writerow(rows_header)

        self.statusBar.showMessage("写入数据中", -1)
        for d in response_data['data']:
            # d[0] ==> ts
            utc_format = "%Y-%m-%dT%H:%M:%S.%fZ"
            utc_time = datetime.strptime(d[0], utc_format)
            localtime = utc_time + timedelta(hours=8)
            d[0] = localtime.strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow(d)

        fp.close()
        self.statusBar.showMessage("写入数据完成", -1)

        self.export_data.setEnabled(True)

    @pyqtSlot()
    def on_connect_test_clicked(self):
        if self.edit_ip.text() == '':
            self.statusBar.showMessage("请输入合法的ip地址", -1)

        self._host = 'http://' + self.edit_ip.text() + ':6041/rest/sql'

        res = None
        try:
            res = self.session.post(
                url=self._host,
                data='show databases',
                auth=HTTPBasicAuth(USERNAME, PASSWORD),
                timeout=1,
            )
        except Exception as err:
            print(err)
            self.statusBar.showMessage("测试失败:"+str(err), -1)
            return

        # print(res)
        data = res.json()
        if data['code'] == 0:
            self.statusBar.showMessage("测试通过", -1)


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())