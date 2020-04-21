import sys
from qtpy import QtWidgets
from Gui.mainwindow import Ui_MainWindow
import csv

app = QtWidgets.QApplication(sys.argv)

class QTMainWindow(QtWidgets.QMainWindow):
    def __init__(this, parent = None):
        super().__init__(parent)

        this.ui = Ui_MainWindow()
        this.ui.setupUi(this)
        
        this.ui.addButton.clicked.connect(this.addRow)
        this.ui.saveButton.clicked.connect(this.saveContent)
        this.insertRow()

    def addRow(this):
        row_len = this.ui.table.rowCount()
        this.ui.table.insertRow(row_len)
        return row_len

    def fillColumn(this):
        with open('names.csv', newline='') as file:
            csv_File = csv.reader(file, delimiter=',')
            for line in csv_File:
                if line[1] == 'Name':
                    continue
                yield(line[1],line[3],line[2])

    def insertRow(this):
        count = 0
        for line in this.fillColumn():
            count += 1
            row_len = this.addRow()
            for index in range(0,3):
                this.ui.table.setItem(row_len, index, QtWidgets.QTableWidgetItem(line[index]))
            if count == 5:
                break
    
    def getRow_Len(this):
        return int(this.ui.table.rowCount())

    def saveContent(this):
        row_len = this.getRow_Len()
        with open('StudentenListe.csv','w',newline='') as file:
            csvFileWriter = csv.writer(file,delimiter=',', quotechar='"')
            for content_Y in range(0,row_len):
                studentInfoListe = []
                for Content_X in range(0,3):
                    studentInfoListe.append(this.ui.table.item(content_Y,Content_X).text().strip())
                csvFileWriter.writerow(studentInfoListe)
                

window = QTMainWindow()
window.show()

sys.exit(app.exec_())