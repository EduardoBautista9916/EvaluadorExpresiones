import sys
from PyQt5 import QtWidgets, QtCore
from interfazEvaluador import Ui_MainWindow
from automata import inicio

class Window_GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window_GUI,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pbCaculate.setValue(50)
        self.ui.btnStart.clicked.connect(self.comenzar)
    def comenzar(self):
        self.ui.txtProcess.setPlainText("")
        self.ui.txtError.setPlainText("")
        self.ui.txtResult.setText("")
        self.ui.txtPostfix.setText("")
        self.ui.txtCalculate.setText("")
        self.ui.pbCaculate.setValue(0)
        cad = self.ui.txtExpression.text()
        if(cad != ""):
            ui = self.ui
            inicio(cad,0,"","", ui)


app = QtWidgets.QApplication([])
mi_app = Window_GUI()
mi_app.show()
sys.exit(app.exec())