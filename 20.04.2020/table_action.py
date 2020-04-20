import sys
from qtpy import QtWidgets
from Gui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class Qt_Window(QtWidgets.QMainWindow):
    def __init__(this, parent = None):
        super().__init__(parent)
        
        this.ui = Ui_MainWindow()
        this.ui.setupUi(this)   
        # title
        this.setWindowTitle("table Action")
        this.ui.button.clicked.connect(this.getConntent)

    def getConntent(this):
        row_len = this.ui.table.rowCount()
        # SelectRows.setColumnCount
        this.ui.table.insertRow((row_len))
        # alternative kannst du auch mit 'insertRow' arbeiten
        #setItem(i,0,Qt.QTableWidgetItem(epoch2str(date)))
        
        this.ui.table.setItem(row_len,0, QtWidgets.QTableWidgetItem("Klick ist anders"))
        this.ui.table.setItem(row_len,1, QtWidgets.QTableWidgetItem("aber Lieb"))

        this.ui.table.cellChanged.connect(this.cell_changed)
    
    def cell_changed(this, row, clo):
        print('---- cell_changed ----')
        print('Spalte {row} an der stelle {clo} wurde geändert'.format(row=row,clo=clo))

# Body
window = Qt_Window()
window.show()

sys.exit(app.exec_())

# Body end