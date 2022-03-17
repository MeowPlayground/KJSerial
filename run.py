from PyQt5.QtWidgets import QApplication
from ui import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    app.exec_()