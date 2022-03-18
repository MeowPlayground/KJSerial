from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
                             QLineEdit,QDialog , QHBoxLayout, QVBoxLayout, QComboBox, QCheckBox, QTextEdit)

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMouseEvent, QPixmap, QIcon

class QClickedLabel(QLabel):
    # 自定义信号, 注意信号必须为类属性
    button_doubleclicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(QClickedLabel, self).__init__(parent)

    def mouseDoubleClickEvent(self, QMouseEvent):
        self.button_doubleclicked_signal.emit()
        
  


class UI(QWidget):

    def Init_UI(self, MainWindow):
        MainWindow.setWindowTitle("KJ Sample Serial")
        MainWindow.setMinimumHeight(500)
        self.formLayout = QVBoxLayout()

        h1 = QHBoxLayout()
        self.serialLabel = QClickedLabel("串口:")
        self.serialComboBox = QComboBox()

        baudLabel = QLabel("波特率:")
        self.baudComboBox = QComboBox()
        self.baudComboBox.addItems(["115200", "9600", "921600", "19200", "38400", "4800"])    

        self.connectButton = QPushButton("连接")    
        
        h1.addWidget(self.serialLabel)
        h1.addWidget(self.serialComboBox)
        h1.addWidget(baudLabel)
        h1.addWidget(self.baudComboBox)
        h1.addWidget(self.connectButton)
        
        self.tb = QTextEdit()
        
        self.tb.setReadOnly(True)
        h2 = QHBoxLayout()
        self.sendEdit = QLineEdit()
        self.sendButton = QPushButton("发送")
        h2.addWidget(self.sendEdit)
        h2.addWidget(self.sendButton)



        h3 = QHBoxLayout()
        self.autoWrapCheckBox = QCheckBox("自动跟踪")
        self.autoWrapCheckBox.setChecked(True)
        self.showTimeCheckBox = QCheckBox("显示时间")
        self.saveButton = QPushButton("保存为文件")
        self.clearButton = QPushButton("清空输出")
        
        h3.addWidget(self.autoWrapCheckBox)
        h3.addWidget(self.showTimeCheckBox)
        h3.addWidget(self.saveButton)
        h3.addWidget(self.clearButton)


        self.formLayout.addLayout(h1)
        self.formLayout.addWidget(self.tb)
        self.formLayout.addLayout(h2)
        self.formLayout.addLayout(h3)
        MainWindow.setLayout(self.formLayout)

        self.msg = QDialog()
        self.msg.setWindowTitle("图标说明")
        self.msg.setWindowIcon(QIcon(":/icon.ico"))
        msgV1= QVBoxLayout()
        imgLabel = QLabel()
        jpg = QPixmap(":/foxx3.png")
        

        imgLabel.setPixmap(jpg)
        msgV1.addWidget(imgLabel)
        self.msg.setLayout(msgV1)

