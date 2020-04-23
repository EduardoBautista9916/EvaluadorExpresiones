import sys
from PyQt5 import QtWidgets, QtCore
from interfazEvaluador import Ui_MainWindow

class Window_GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window_GUI,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pbCaculate.setValue(50)

app = QtWidgets.QApplication([])
mi_app = Window_GUI()
mi_app.show()
sys.exit(app.exec())