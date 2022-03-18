from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from functools import partial
from PyQt5.QtGui import QIcon, QTextCursor
from .uicore import UI
from core import getPortList, myserial
import time

class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    print = pyqtSignal(str)

    _serialComboBoxResetItems = pyqtSignal(list)
    _serialComboBoxClear = pyqtSignal()
    _setButtonText = pyqtSignal(str)
    _lineClear = pyqtSignal()
    print = pyqtSignal(str)

ms = MySignals()

class Action():
    def __init__(self, ui: QWidget) -> None:
        self.ui = ui

    def _serialComboBoxResetItems(self, texts: list):
        self.ui.serialComboBox.clear()
        self.ui.serialComboBox.addItems(texts)

    def _serialComboBoxclear(self):
        self.ui.serialComboBox.clear()

    def _setButtonText(self, text: str):
        self.ui.connectButton.setText(text)

    def _lineClear(self):
        self.ui.sendEdit.clear()

    def print(self, t:str):
        tc = self.ui.tb.textCursor()
        tc.movePosition(QTextCursor.End)
        if self.ui.showTimeCheckBox.isChecked():
            nowtime = time.strftime("%H:%M:%S", time.localtime())
            tc.insertText("[" + nowtime + "]")
        tc.insertText(t)

        
        if self.ui.autoWrapCheckBox.isChecked():
            # self.ui.tb.ensureCursorVisible()
            self.ui.tb.setTextCursor(tc)
        
        


class MainWindow(QWidget):
    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = UI()
        self.ui.Init_UI(self)
        
        self.a = Action(self.ui)
        self.initMS()
        self.ports = []
        self.selectPort = ""
        self.selectBund = ""
        self.ser = myserial()
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.initSerial)
        self.timer2.start(1000)


    def initMS(self):
        self.ui.connectButton.clicked.connect(self.openPort)
        ms._serialComboBoxResetItems.connect(self.a._serialComboBoxResetItems)
        ms._serialComboBoxClear.connect(self.a._serialComboBoxclear)
        ms._setButtonText.connect(self.a._setButtonText)
        ms.print.connect(self.a.print)
        ms._lineClear.connect(self.a._lineClear)
        self.ui.sendButton.clicked.connect(self.send)
        self.ui.serialLabel.button_doubleclicked_signal.connect(self.showAbout)
        self.ui.saveButton.clicked.connect(self.savefile)
        self.ui.clearButton.clicked.connect(self.ui.tb.clear)
        

    def initSerial(self):
        ports = getPortList()
        if self.ports != ports:
            self.ports = ports
            if self.ser.port not in [i.name for i in self.ports]:
                self.ser.read_flag = False
            ms._serialComboBoxResetItems.emit([i.name for i in self.ports])

        if self.ser.read_flag:
            ms._setButtonText.emit("断开")
        else:
            ms._setButtonText.emit("连接")

    def openPort(self):
        if self.ser.read_flag:
            print("stop")
            self.ser.stop()
        else:
            port = self.ui.serialComboBox.currentText()
            bund = int(self.ui.baudComboBox.currentText())
            if port == "":
                ms.print.emit("当前未选择串口\n")
                return
            self.ser.setSer(port, bund)
            d = self.ser.open(ms.print.emit)
            ms.print.emit(d[1])

    def send(self):
        text = self.ui.sendEdit.text()
        if not text == "" or not text == None:
            if self.ser.read_flag:
                self.ser.write(text)
                ms._lineClear.emit()

    def showAbout(self):
        self.ui.msg.show()


    def savefile(self):
        filename = QFileDialog.getSaveFileName(self.ui, "open file", "./", "TEXT Files(*.txt)")
        # print(filename)
        if filename[0] == "" or filename == None:
            return
        try:
            with open(filename[0], "w") as f:
                text = self.ui.tb.toPlainText()
                f.write(text)
            ms.print.emit("保存到"+filename[0])
        except Exception as e:
            ms.print.emit("保存失败" + str(e))

def runApp():
    app = QApplication([])
    mainw = MainWindow()
    mainw.setWindowIcon(QIcon(':/icon.ico'))
    mainw.show()
    app.exec_()