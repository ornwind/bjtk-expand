import sys
import pyperclip
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_main import Ui_MainWindow
import text
import web
import webbrowser
import qr


class window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setup()
        self.show()
        self.statement()
        QApplication.processEvents()

    def setup(self):
        self.setupUi(self)
        self.setWindowIcon(QIcon("img/IMAGE_iP2SjlZhb_1690890042506.png"))
        self.setWindowTitle("北京题库拓展")
        self.setWid(False)
        self.github.setEnabled(False)
        self.setting.setEnabled(False)
        self.Search = web.Search()
        self.update_hotlist()
        self.connection()
        self.github.hide()
        self.setting.hide()
        self.get_grade.hide()
        self.get_subject.hide()
        self.Get = web.Get()

    def connection(self):
        self.developer.clicked.connect(self.contract_us)
        self.agreement.stateChanged.connect(self.agree)
        self.pb_sm.clicked.connect(self.statement)
        self.pb_am.clicked.connect(self.user_agreement)
        for i in range(1, 6):
            eval(f"self.hot{i}.clicked.connect(self.write_{i})")
        self.search.clicked.connect(self.searchs)
        self.search_list.itemSelectionChanged.connect(self.search_change)
        self.pdf_browser.clicked.connect(self.browser_search_download)
        self.pdf_url.clicked.connect(self.copy_search_download)
        self.phone_pdf.clicked.connect(self.qrcode_search_download)
        self.browser_pan.clicked.connect(self.browser_search_download)
        self.phone_pan.clicked.connect(self.qrcode_search_download)
        self.get.clicked.connect(self.getting)
        self.get_tp.currentTextChanged.connect(self.get_changed)
        self.get_list.itemSelectionChanged.connect(self.get_change)
        self.get_browser.clicked.connect(self.browser_get_download)
        self.get_url.clicked.connect(self.copy_get_download)
        self.get_phone.clicked.connect(self.qrcode_get_download)
        self.get_browser_pan.clicked.connect(self.browser_get_download)
        self.get_phone_pan.clicked.connect(self.qrcode_get_download)

    def update_hotlist(self):
        hotlist = self.Search.get_hotlist()
        hots = [self.hot1, self.hot2, self.hot3, self.hot4, self.hot5]
        for i in range(5):
            hots[i].setText(hotlist[i])
        QApplication.processEvents()

    def setWid(self, flag):
        for i in [self.get, self.get_list, self.get_tp, self.get_grade, self.get_browser, self.get_browser_pan,
                  self.get_choose, self.get_phone_pan, self.get_subject, self.get_url, self.get_phone,
                  self.search_choose, self.search, self.search_list, self.search_keyword, self.pdf_url,
                  self.pdf_browser, self.phone_pdf, self.search_num, self.hot1, self.hot2, self.hot3, self.hot5,
                  self.hot4, self.browser_pan, self.phone_pan]:
            i.setEnabled(flag)
        QApplication.processEvents()

    def agree(self):
        self.setWid(self.agreement.isChecked())

    def user_agreement(self):
        QMessageBox.about(self, '用户协议', text.USER_AGREEMENT)

    def statement(self):
        QMessageBox.about(self, '声明', text.STATEMENT)

    def contract_us(self):
        QMessageBox.about(self, '联系开发者', text.CONTRACT)

    def write(self, num):
        QApplication.processEvents()
        text = eval(f"self.hot{num}.text()")
        self.search_keyword.setText(self.search_keyword.text() + text)

    def write_1(self):
        self.write(1)

    def write_2(self):
        self.write(2)

    def write_3(self):
        self.write(3)

    def write_4(self):
        self.write(4)

    def write_5(self):
        self.write(5)

    def searchs(self):
        keyword = self.search_keyword.text()
        self.status_message(f"正在搜索“{keyword}”...", 1000)
        if keyword == "":
            QMessageBox.warning(self, '警告', text.EMPTY_INPUT)
            return
        self.search_download_statius(0, False)
        self.search_list.clear()
        QApplication.processEvents()
        keyword = self.search_keyword.text()
        num = self.search_num.text()
        data = self.Search.search(keyword, num)
        self.status_message(f"搜索“{keyword}”成功！共{len(data)}个结果", 5000)
        self.search_data = data
        for i in data:
            item = QListWidgetItem()
            item.setText(str(data.index(i)) + "." + i["name"] + "(" + i["time"] + ")")
            self.search_list.addItem(item)
        QApplication.processEvents()

    def search_download_statius(self, n, f):
        if n == 0:
            self.pdf_browser.setEnabled(f)
            self.pdf_url.setEnabled(f)
            self.phone_pdf.setEnabled(f)
            self.browser_pan.setEnabled(f)
            self.phone_pan.setEnabled(f)
        elif n == 1:
            self.pdf_browser.setEnabled(f)
            self.pdf_url.setEnabled(f)
            self.phone_pdf.setEnabled(f)
            self.browser_pan.setEnabled(not f)
            self.phone_pan.setEnabled(not f)
        else:
            self.pdf_browser.setEnabled(not f)
            self.pdf_url.setEnabled(not f)
            self.phone_pdf.setEnabled(not f)
            self.browser_pan.setEnabled(f)
            self.phone_pan.setEnabled(f)

    def search_change(self):
        try:
            index = self.search_list.selectedItems()[0].text().split(".")[0]
            data = self.search_data[int(index)]
            self.search_choose.setText(data["name"])
            self.search_url = data["url"]
            if data["is_pdf"]:
                self.search_download_statius(1, True)
            else:
                self.search_download_statius(2, True)
        except:
            pass

    def browser_search_download(self):
        webbrowser.open(self.search_url)

    def copy_search_download(self):
        pyperclip.copy(self.search_url)

    def qrcode_search_download(self):
        qr.make_qrcode(self.search_url)

    def status_message(self, text, time):
        self.statusbar.showMessage(text, time)

    def get_hotlist(self):
        self.status_message("正在获取热榜...", 1000)
        data = self.Get.get_hotlist()
        self.get_download_statius(0, False)
        self.get_list.clear()
        self.status_message(f"获取“热榜”成功！共{len(data)}个结果", 5000)
        QApplication.processEvents()
        self.get_data = data
        for i in data:
            item = QListWidgetItem()
            item.setText(str(data.index(i)) + "." + str(i["name"]) + "(" + str(i["time"]) + ")")
            self.get_list.addItem(item)
        QApplication.processEvents()

    def get_changed(self):
        if self.get_tp.currentText() == "电子课本":
            self.get_grade.show()
            self.get_subject.show()
        else:
            self.get_grade.hide()
            self.get_subject.hide()

    def get_download_statius(self, n, f):
        if n == 0:
            self.get_browser.setEnabled(f)
            self.get_url.setEnabled(f)
            self.get_phone.setEnabled(f)
            self.get_browser_pan.setEnabled(f)
            self.get_phone_pan.setEnabled(f)
        elif n == 1:
            self.get_browser.setEnabled(f)
            self.get_url.setEnabled(f)
            self.get_phone.setEnabled(f)
            self.get_browser_pan.setEnabled(not f)
            self.get_phone_pan.setEnabled(not f)
        else:

            self.get_browser.setEnabled(not f)
            self.get_url.setEnabled(not f)
            self.get_phone.setEnabled(not f)
            self.get_browser_pan.setEnabled(f)
            self.get_phone_pan.setEnabled(f)

    def get_change(self):
        try:
            index = self.get_list.selectedItems()[0].text().split(".")[0]
            data = self.get_data[int(index)]
            self.get_choose.setText(data["name"])
            self.get_download_url = data["url"]
            if data["is_pdf"]:
                self.get_download_statius(1, True)
            else:
                self.get_download_statius(2, True)
        except:
            pass

    def browser_get_download(self):
        webbrowser.open(self.get_download_url)

    def copy_get_download(self):
        pyperclip.copy(self.get_download_url)

    def qrcode_get_download(self):
        qr.make_qrcode(self.get_download_url)

    def getting(self):
        if self.get_tp.currentText() == "热榜":
            self.get_hotlist()
        elif self.get_tp.currentText() == "电子课本":
            pass
        else:
            pass


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    window = window()
    sys.exit(app.exec_())
