import sys
from qtpy import QtWidgets
from Gui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)


window = QtWidgets.QMainWindow()
window.show()

# ui_MainWindow wurde erstellt von build.py
# instance Bildung mit 'ui_window'
ui_window = Ui_MainWindow()
# ui_MainWindow benötigt die 'QtWidgets.QMainWindow()' als Parameter!
# ui_setupUi würde dann eine art '__init__' darstellen < unsicher!
ui_window.setupUi(window)


def btn_click():
    # print(ui_window.check_.__dir__())
    ui_window.check_.toggle()
    print("clicked")

ui_window.pushButton.clicked.connect(btn_click)

sys.exit(app.exec_())
