import resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel,QFileDialog,QVBoxLayout

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 426)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/png AI.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(253, 255, 43, 255), stop:1 rgba(236, 125, 13, 255));\n"
                                 "border-color: rgb(170, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 50, 131, 51))
        self.label.setStyleSheet("image: url(:/newPrefix/RespondeAi.png);\n"
                                 "background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(198, 198, 198, 0));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.checkBox_email = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_email.setGeometry(QtCore.QRect(90, 160, 101, 31))
        self.checkBox_email.setStyleSheet("font: 75 16pt \"Bahnschrift\";\n"
                                          "background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(198, 198, 198, 0));")
        self.checkBox_email.setObjectName("checkBox_email")
        self.checkBox_SMS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_SMS.setGeometry(QtCore.QRect(270, 160, 81, 31))
        self.checkBox_SMS.setStyleSheet("font: 75 16pt \"Bahnschrift\";\n"
                                        "background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(198, 198, 198, 0));")
        self.checkBox_SMS.setObjectName("checkBox_SMS")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 250, 331, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(19)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_Nome = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_Nome.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_Nome.setObjectName("lineEdit_Nome")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_Nome)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font: 75 12pt \"Bahnschrift\";\n"
                                   "background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(198, 198, 198, 0));")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.pushButton_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Submit.setGeometry(QtCore.QRect(110, 330, 221, 61))
        self.pushButton_Submit.setStyleSheet("background-color: rgb(44, 44, 44);\n"
                                             "color: white;\n"
                                             "border-style: outset;\n"
                                             "border-width: 2px;\n"
                                             "border-radius: 8px;\n"
                                             "border-color: black;\n"
                                             "font: 75 25pt \"Calibri\";\n"
                                             "padding: 6px;\n"
                                             "min-width: 10px;")
        self.pushButton_Submit.setObjectName("pushButton_Submit")
        self.pushButton_arquivo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_arquivo.setGeometry(QtCore.QRect(150, 120, 141, 23))
        self.pushButton_arquivo.setStyleSheet("color: rgb(4, 4, 4);\n"
                                              "background-color: rgb(255, 125, 19);")
        self.pushButton_arquivo.setObjectName("pushButton_arquivo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 161, 31))
        self.label_2.setStyleSheet("background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(198, 198, 198, 0));\n"
                                   "font: 75 12pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.horizontalSlider_Dividir = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_Dividir.setGeometry(
            QtCore.QRect(170, 220, 81, 21))
        self.horizontalSlider_Dividir.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 0), stop:0.4 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalSlider_Dividir.setMinimum(1)
        self.horizontalSlider_Dividir.setMaximum(5)
        self.horizontalSlider_Dividir.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Dividir.setObjectName("horizontalSlider_Dividir")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 331, 20))
        self.label_4.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 0), stop:0.4 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
                                   "font: 75 11pt \"Bahnschrift\";")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 10, 381, 411))
        self.frame.setStyleSheet("background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(90, 91, 15, 255), stop:1 rgba(236, 125, 13, 255));\n"
                                 "border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.label.raise_()
        self.checkBox_email.raise_()
        self.checkBox_SMS.raise_()
        self.formLayoutWidget.raise_()
        self.pushButton_Submit.raise_()
        self.pushButton_arquivo.raise_()
        self.label_2.raise_()
        self.horizontalSlider_Dividir.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Limpa Bases - Responde Aí"))
        self.checkBox_email.setText(_translate("MainWindow", "E-mail"))
        self.checkBox_SMS.setText(_translate("MainWindow", "SMS"))
        self.label_3.setText(_translate(
            "MainWindow", "  Insira o nome que você quer dar ao CSV"))
        self.pushButton_Submit.setText(
            _translate("MainWindow", "Manda Brasa!"))
        self.pushButton_arquivo.setText(
            _translate("MainWindow", "Inserir CSV"))
        self.label_2.setText(_translate("MainWindow", "Marketing Limpa Bases"))
        self.label_4.setText(_translate(
            "MainWindow", "Em quantas planilhas você quer dividir esta base?"))


    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
