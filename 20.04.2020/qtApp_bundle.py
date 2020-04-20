import sys
from qtpy import QtWidgets
from Gui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class Qt_Window(QtWidgets.QMainWindow):
    def __init__(this, parent = None):
        super().__init__(parent)
        
        this.setWindowTitle("BundleQt")
            # ui_MainWindow wurde erstellt von build.py
            # instance Bildung mit 'ui_window'
        this.ui = Ui_MainWindow()
            # ui_MainWindow benötigt die 'QtWidgets.QMainWindow()' als Parameter!
            # ui_setupUi würde dann eine art '__init__' darstellen < unsicher!
        this.ui.setupUi(this)   
            # title
        this.setWindowTitle("QtBundle")
        this.ui.pushButton.clicked.connect(this.getDir)

    def getDir(this):
        print(this.ui.text.text())





window = Qt_Window()
window.show()

sys.exit(app.exec_())
