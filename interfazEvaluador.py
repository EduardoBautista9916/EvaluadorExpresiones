# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazEvaluador.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPix
        map("Pictures/iconWindow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(80, 80, 80);\n"
                                "color: rgb(255,255,255);\n"
                                "\n"
                                "QLineEdit\n"
                                "{\n"
                                "    background-color:rgb(150,150,150);\n"
                                "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(69, 0, 731, 70))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lblTitle.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("background-color: rgb(32, 127, 148);\n"
                                        "font:rgb(0,0,0);")
        self.lblTitle.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblTitle.setLineWidth(0)
        self.lblTitle.setMidLineWidth(0)
        self.lblTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 70, 801, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.lyCabecera = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.lyCabecera.setContentsMargins(10, 10, 10, 10)
        self.lyCabecera.setObjectName("lyCabecera")
        self.lblExpression = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lblExpression.setFont(font)
        self.lblExpression.setStyleSheet("background-color:rgb(80,80,80);")
        self.lblExpression.setObjectName("lblExpression")
        self.lyCabecera.addWidget(self.lblExpression)
        self.txtExpression = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.txtExpression.setFont(font)
        self.txtExpression.setStyleSheet("background-color:rgb(150,150,150);\n"
                                        "border-color:rgb(80,80,80);")
        self.txtExpression.setText("")
        self.txtExpression.setFrame(False)
        self.txtExpression.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.txtExpression.setObjectName("txtExpression")
        self.lyCabecera.addWidget(self.txtExpression)
        self.btnStart = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.btnStart.setFont(font)
        self.btnStart.setStyleSheet("background:rgb(32,127,148);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Pictures/iconStart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStart.setIcon(icon1)
        self.btnStart.setAutoDefault(False)
        self.btnStart.setDefault(False)
        self.btnStart.setFlat(False)
        self.btnStart.setObjectName("btnStart")
        self.lyCabecera.addWidget(self.btnStart)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 130, 800, 5))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pnlRight = QtWidgets.QWidget(self.centralwidget)
        self.pnlRight.setGeometry(QtCore.QRect(10, 150, 271, 321))
        self.pnlRight.setStyleSheet("background-color:rgb(90,90,90)")
        self.pnlRight.setObjectName("pnlRight")
        self.formLayoutWidget = QtWidgets.QWidget(self.pnlRight)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 271, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.bcRaeding = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.bcRaeding.setStyleSheet("background-color:rgb(150,150,150);\n"
                                        "color:(255,0,0);")
        self.bcRaeding.setProperty("value", 0)
        self.bcRaeding.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.bcRaeding.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.bcRaeding.setObjectName("bcRaeding")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.bcRaeding)
        self.lblReading = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        self.lblReading.setFont(font)
        self.lblReading.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblReading.setAlignment(QtCore.Qt.AlignCenter)
        self.lblReading.setObjectName("lblReading")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblReading)
        self.bcSearch = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.bcSearch.setProperty("value", 0)
        self.bcSearch.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.bcSearch.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.bcSearch.setObjectName("bcSearch")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.bcSearch)
        self.lbSearch = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        self.lbSearch.setFont(font)
        self.lbSearch.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSearch.setObjectName("lbSearch")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbSearch)
        self.pbTransforming = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.pbTransforming.setProperty("value", 0)
        self.pbTransforming.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pbTransforming.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.pbTransforming.setObjectName("pbTransforming")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pbTransforming)
        self.lblTransforming = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        self.lblTransforming.setFont(font)
        self.lblTransforming.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTransforming.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTransforming.setObjectName("lblTransforming")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lblTransforming)
        self.pbCaculate = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.pbCaculate.setProperty("value", 0)
        self.pbCaculate.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pbCaculate.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.pbCaculate.setObjectName("pbCaculate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.pbCaculate)
        self.lblCalculate = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        self.lblCalculate.setFont(font)
        self.lblCalculate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblCalculate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCalculate.setObjectName("lblCalculate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lblCalculate)
        self.txtCalculate = QtWidgets.QLineEdit(self.pnlRight)
        self.txtCalculate.setEnabled(False)
        self.txtCalculate.setGeometry(QtCore.QRect(110, 160, 150, 150))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(85)
        self.txtCalculate.setFont(font)
        self.txtCalculate.setStyleSheet("background-color:rgb(32,127,148);")
        self.txtCalculate.setText("")
        self.txtCalculate.setFrame(False)
        self.txtCalculate.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCalculate.setObjectName("txtCalculate")
        self.lblEvaluating = QtWidgets.QLabel(self.pnlRight)
        self.lblEvaluating.setGeometry(QtCore.QRect(10, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lblEvaluating.setFont(font)
        self.lblEvaluating.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEvaluating.setObjectName("lblEvaluating")
        self.lblCharacter = QtWidgets.QLabel(self.pnlRight)
        self.lblCharacter.setGeometry(QtCore.QRect(10, 220, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lblCharacter.setFont(font)
        self.lblCharacter.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCharacter.setObjectName("lblCharacter")
        self.pnlLeft = QtWidgets.QWidget(self.centralwidget)
        self.pnlLeft.setGeometry(QtCore.QRect(300, 150, 491, 321))
        self.pnlLeft.setStyleSheet("background-color:rgb(90,90,90);")
        self.pnlLeft.setObjectName("pnlLeft")
        self.lblProcess = QtWidgets.QLabel(self.pnlLeft)
        self.lblProcess.setGeometry(QtCore.QRect(20, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lblProcess.setFont(font)
        self.lblProcess.setObjectName("lblProcess")
        self.txtProcess = QtWidgets.QPlainTextEdit(self.pnlLeft)
        self.txtProcess.setEnabled(False)
        self.txtProcess.setGeometry(QtCore.QRect(100, 10, 380, 105))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txtProcess.setFont(font)
        self.txtProcess.setStyleSheet("background-color:rgb(150,150,150);\n"
                                        "color:rgb(0,255,0);")
        self.txtProcess.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txtProcess.setPlainText("")
        self.txtProcess.setObjectName("txtProcess")
        self.txtPostfix = QtWidgets.QLineEdit(self.pnlLeft)
        self.txtPostfix.setEnabled(False)
        self.txtPostfix.setGeometry(QtCore.QRect(160, 240, 320, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.txtPostfix.setFont(font)
        self.txtPostfix.setMouseTracking(True)
        self.txtPostfix.setTabletTracking(False)
        self.txtPostfix.setAcceptDrops(True)
        self.txtPostfix.setAutoFillBackground(False)
        self.txtPostfix.setStyleSheet("background-color:rgb(150,150,150);\n"
                                        "color:rgb(255,255,255);\n"
                                        "border-color:rgb(80,80,80);")
        self.txtPostfix.setText("")
        self.txtPostfix.setFrame(False)
        self.txtPostfix.setDragEnabled(False)
        self.txtPostfix.setReadOnly(False)
        self.txtPostfix.setObjectName("txtPostfix")
        self.lblPostfix = QtWidgets.QLabel(self.pnlLeft)
        self.lblPostfix.setGeometry(QtCore.QRect(16, 240, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lblPostfix.setFont(font)
        self.lblPostfix.setObjectName("lblPostfix")
        self.txtResult = QtWidgets.QLineEdit(self.pnlLeft)
        self.txtResult.setEnabled(False)
        self.txtResult.setGeometry(QtCore.QRect(160, 280, 320, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.txtResult.setFont(font)
        self.txtResult.setMouseTracking(True)
        self.txtResult.setTabletTracking(False)
        self.txtResult.setAcceptDrops(True)
        self.txtResult.setAutoFillBackground(False)
        self.txtResult.setStyleSheet("background-color:rgb(150,150,150);\n"
                                        "color:rgb(255,255,255);\n"
                                        "border-color:rgb(80,80,80);")
        self.txtResult.setText("")
        self.txtResult.setFrame(False)
        self.txtResult.setDragEnabled(False)
        self.txtResult.setReadOnly(False)
        self.txtResult.setObjectName("txtResult")
        self.lblResult = QtWidgets.QLabel(self.pnlLeft)
        self.lblResult.setGeometry(QtCore.QRect(20, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lblResult.setFont(font)
        self.lblResult.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblResult.setObjectName("lblResult")
        self.lblError = QtWidgets.QLabel(self.pnlLeft)
        self.lblError.setGeometry(QtCore.QRect(20, 125, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.lblError.setFont(font)
        self.lblError.setObjectName("lblError")
        self.txtError = QtWidgets.QPlainTextEdit(self.pnlLeft)
        self.txtError.setEnabled(False)
        self.txtError.setGeometry(QtCore.QRect(100, 125, 380, 105))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txtError.setFont(font)
        self.txtError.setStyleSheet("background-color:rgb(150,150,150);\n"
                                        "color:rgb(255,0,0)")
        self.txtError.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txtError.setPlainText("")
        self.txtError.setObjectName("txtError")
        self.lblIcon = QtWidgets.QLabel(self.centralwidget)
        self.lblIcon.setGeometry(QtCore.QRect(0, 0, 70, 70))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 127, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lblIcon.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblIcon.setFont(font)
        self.lblIcon.setStyleSheet("background-color: rgb(32, 127, 148);\n"
                                "font:rgb(0,0,0);")
        self.lblIcon.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblIcon.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblIcon.setLineWidth(0)
        self.lblIcon.setMidLineWidth(0)
        self.lblIcon.setText("")
        self.lblIcon.setPixmap(QtGui.QPixmap("Pictures/iconWindow.png"))
        self.lblIcon.setScaledContents(True)
        self.lblIcon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblIcon.setObjectName("lblIcon")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Evaluador de Expresiones"))
        self.lblTitle.setText(_translate("MainWindow", "EVALUADOR DE EXPRESIONES"))
        self.lblExpression.setText(_translate("MainWindow", "Ingrese su Expresión Aquí:"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.lblReading.setText(_translate("MainWindow", "Leyendo Expresión"))
        self.lbSearch.setText(_translate("MainWindow", "Buscando Errores"))
        self.lblTransforming.setText(_translate("MainWindow", "Transfromando"))
        self.lblCalculate.setText(_translate("MainWindow", "Calculando"))
        self.lblEvaluating.setText(_translate("MainWindow", "Evaluando"))
        self.lblCharacter.setText(_translate("MainWindow", "Caracter"))
        self.lblProcess.setText(_translate("MainWindow", "Proceso"))
        self.lblPostfix.setText(_translate("MainWindow", "Notación Posfija"))
        self.lblResult.setText(_translate("MainWindow", "Resultado"))
        self.lblError.setText(_translate("MainWindow", "Errores"))
