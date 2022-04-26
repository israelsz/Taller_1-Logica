import sys
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Ventana2(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_siguienteMainWindow = QtWidgets.QPushButton(self.centralwidget)
        self.btn_siguienteMainWindow.setGeometry(QtCore.QRect(240, 190, 111, 51))
        self.btn_siguienteMainWindow.setObjectName("btn_siguienteMainWindow")
        self.rbtn_moderado = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_moderado.setGeometry(QtCore.QRect(250, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtn_moderado.setFont(font)
        self.rbtn_moderado.setObjectName("rbtn_moderado")
        self.rbtn_poco = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_poco.setGeometry(QtCore.QRect(250, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtn_poco.setFont(font)
        self.rbtn_poco.setObjectName("rbtn_poco")
        self.rbtn_mucho = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_mucho.setGeometry(QtCore.QRect(250, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtn_mucho.setFont(font)
        self.rbtn_mucho.setObjectName("rbtn_mucho")
        self.btn_reiniciar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reiniciar.setGeometry(QtCore.QRect(20, 250, 91, 31))
        self.btn_reiniciar.setObjectName("btn_reiniciar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_reiniciar.clicked.connect(self.cambiarVentana)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SpeedrunGuru - Cuestionario"))
        self.label.setText(_translate("MainWindow", "Pregunta N°1: ¿Cuanto tiempo dispone para jugar?"))
        self.btn_siguienteMainWindow.setText(_translate("MainWindow", "Siguiente pregunta"))
        self.rbtn_moderado.setText(_translate("MainWindow", "Moderado"))
        self.rbtn_poco.setText(_translate("MainWindow", "Poco"))
        self.rbtn_mucho.setText(_translate("MainWindow", "Mucho"))
        self.btn_reiniciar.setText(_translate("MainWindow", "Reiniciar"))


    def cambiarVentana(self):
        #Logica
        print(lista)
        #Cambiar de ventana
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()



###################################################################################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_inicial = QtWidgets.QPushButton(self.centralwidget)
        self.btn_inicial.setGeometry(QtCore.QRect(310, 350, 141, 51))
        self.btn_inicial.setObjectName("btn_inicial")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(270, 120, 211, 41))
        self.label_titulo.setObjectName("label_titulo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_inicial.clicked.connect(self.cambiarVentana)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_inicial.setText(_translate("MainWindow", "Iniciar"))
        self.label_titulo.setText(_translate("MainWindow", "Recomendador de juegos para Speedrun"))
    
    def cambiarVentana(self):
        #Logica antes de cambiar de ventana
        print(lista)
        #Cambiar de ventana
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Ventana2()
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

if __name__ == "__main__":
    global lista
    lista = [1,2,3,4,5]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

