import sys
from qtpy import QtWidgets
from Gui.mainwindow_bmi import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class Qt_Window(QtWidgets.QMainWindow):
    def __init__(this, parent = None):
        super().__init__(parent)
        
        this.ui = Ui_MainWindow()
        this.ui.setupUi(this)   
        # title
        this.setWindowTitle("BMI zum rechnen")
        this.ui.button.clicked.connect(this.getConntent)

    def getConntent(this):
        height = float(this.ui.boxWeight.text().replace(",","."))
        weight = float(this.ui.boxHeight.text())
        result = weight / (height*height)

        this.ui.labelResult.setText("")
        this.ui.labelResult.setText(this.getBMiResult(result))
    
    def getBMiResult(this, result):
        if result <= 18.5:
            return "Underweight"
        elif result < 25:
            return "Normal weight"
        elif result < 29.9:
            return "Overweight"
        elif result < 30:
            return "your are rly fat Bro" 
# Body
window = Qt_Window()
window.show()

sys.exit(app.exec_())

# Body end