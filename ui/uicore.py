from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
                             QLineEdit, QTextBrowser, QToolButton, QHBoxLayout, QVBoxLayout, QComboBox, QCheckBox, QTextEdit)


class UI(QWidget):

    def Init_UI(self, MainWindow):

        MainWindow.setWindowTitle("KJ Sample Serial")
        self.formLayout = QVBoxLayout()

        h1 = QHBoxLayout()
        serialLabel = QLabel("串口:")
        self.serialComboBox = QComboBox()

        baudLabel = QLabel("波特率:")
        self.baudComboBox = QComboBox()
        self.baudComboBox.addItems(["115200", "9600"])    

        self.connectButton = QPushButton("连接")    
        
        h1.addWidget(serialLabel)
        h1.addWidget(self.serialComboBox)
        h1.addWidget(baudLabel)
        h1.addWidget(self.baudComboBox)
        h1.addWidget(self.connectButton)
        
        self.tb = QTextBrowser()

        h2 = QHBoxLayout()
        self.sendEdit = QLineEdit()
        self.sendButton = QPushButton("发送")
        h2.addWidget(self.sendEdit)
        h2.addWidget(self.sendButton)



        h3 = QHBoxLayout()
        self.autoWrapCheckBox = QCheckBox("自动换行")
        self.autoWrapCheckBox.setChecked(True)
        self.showTimeCheckBox = QCheckBox("显示时间")
        self.keywordCheckBox = QCheckBox("关键词突出")
        self.keywordCheckBox.setChecked(True)
        self.clearButton = QPushButton("清空输出")
        
        h3.addWidget(self.autoWrapCheckBox)
        h3.addWidget(self.showTimeCheckBox)
        h3.addWidget(self.keywordCheckBox)
        h3.addWidget(self.clearButton)


        self.formLayout.addLayout(h1)
        self.formLayout.addWidget(self.tb)
        self.formLayout.addLayout(h2)
        self.formLayout.addLayout(h3)
        MainWindow.setLayout(self.formLayout)
