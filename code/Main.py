import sys

from PyQt5 import QtWidgets

import Window

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window.Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
