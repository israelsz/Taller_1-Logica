import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from pyswip import Prolog

# Se fija como variable global
prolog = Prolog()


# Ventana principal
class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 795)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 45, 168, 255), stop:1 rgba(209, 196, 233, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 621, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(103, 58, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 621, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(81, 45, 168);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.cb_pregunta1 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_pregunta1.setGeometry(QtCore.QRect(140, 180, 311, 31))
        self.cb_pregunta1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial\";\n"
"color: rgb(0, 0, 0);")
        self.cb_pregunta1.setObjectName("cb_pregunta1")
        self.cb_pregunta1.addItem("")
        self.cb_pregunta1.addItem("")
        self.cb_pregunta1.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 230, 621, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(103, 58, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 350, 621, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(103, 58, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.cb_pregunta2 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_pregunta2.setGeometry(QtCore.QRect(140, 310, 311, 31))
        self.cb_pregunta2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial\";\n"
"color: rgb(33, 33, 33);")
        self.cb_pregunta2.setObjectName("cb_pregunta2")
        self.cb_pregunta2.addItem("")
        self.cb_pregunta2.addItem("")
        self.cb_pregunta3 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_pregunta3.setGeometry(QtCore.QRect(140, 430, 311, 31))
        self.cb_pregunta3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial\";\n"
"color: rgb(33, 33, 33);")
        self.cb_pregunta3.setObjectName("cb_pregunta3")
        self.cb_pregunta3.addItem("")
        self.cb_pregunta3.addItem("")
        self.cb_pregunta3.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 480, 621, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(103, 58, 183);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.cb_pregunta4 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_pregunta4.setGeometry(QtCore.QRect(140, 570, 311, 31))
        self.cb_pregunta4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial\";\n"
"color: rgb(33, 33, 33);")
        self.cb_pregunta4.setObjectName("cb_pregunta4")
        self.cb_pregunta4.addItem("")
        self.cb_pregunta4.addItem("")
        self.cb_pregunta4.addItem("")
        self.cb_pregunta4.addItem("")
        self.btn_atras = QtWidgets.QPushButton(self.centralwidget)
        self.btn_atras.setGeometry(QtCore.QRect(10, 700, 81, 41))
        self.btn_atras.setStyleSheet("background-color: rgb(83, 109, 254);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.btn_atras.setObjectName("btn_atras")
        self.btn_enviar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enviar.setGeometry(QtCore.QRect(170, 620, 231, 71))
        self.btn_enviar.setStyleSheet("background-color: rgb(83, 109, 254);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.btn_enviar.setObjectName("btn_enviar")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(660, 110, 411, 611))
        self.listView.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"border-color: rgb(0, 0, 0);")
        self.listView.setObjectName("listView")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(720, 30, 291, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(81, 45, 168);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(680, 120, 371, 41))
        self.label_7.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"font: 75 12pt \"Arial\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(680, 160, 371, 41))
        self.label_8.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"color: rgb(179, 58, 37);\n"
"font: 75 14pt \"Arial\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(680, 210, 371, 41))
        self.label_9.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"font: 87 12pt \"Arial\";\n"
"text-decoration: underline;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(680, 260, 371, 431))
        self.label_10.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 87 12pt \"Arial\";")
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_atras.clicked.connect(self.cambiarVentana)
        self.btn_enviar.clicked.connect(self.ejecutarConsulta)
        self.label_7.setHidden(True)
        self.label_8.setHidden(True)
        self.label_9.setHidden(True)
        self.label_10.setHidden(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "1. ¿Cuánto tiempo dispone para jugar?"))
        self.label_2.setText(_translate("MainWindow", "Responda las siguientes preguntas para conseguir un resultado:"))
        self.cb_pregunta1.setItemText(0, _translate("MainWindow", "Mucho tiempo"))
        self.cb_pregunta1.setItemText(1, _translate("MainWindow", "Una cantidad moderada"))
        self.cb_pregunta1.setItemText(2, _translate("MainWindow", "Poco tiempo"))
        self.label_3.setText(_translate("MainWindow", "2. ¿Prefiere juegos antiguos o nuevos?"))
        self.label_4.setText(_translate("MainWindow", "3. ¿Qué tan bueno se considera como jugador?"))
        self.cb_pregunta2.setItemText(0, _translate("MainWindow", "Nuevos"))
        self.cb_pregunta2.setItemText(1, _translate("MainWindow", "Antiguos"))
        self.cb_pregunta3.setItemText(0, _translate("MainWindow", "Muy bueno"))
        self.cb_pregunta3.setItemText(1, _translate("MainWindow", "Normal"))
        self.cb_pregunta3.setItemText(2, _translate("MainWindow", "Novato"))
        self.label_5.setText(_translate("MainWindow", "4. ¿Qué característica extra busca en un juego?"))
        self.cb_pregunta4.setItemText(0, _translate("MainWindow", "Etapas distintas"))
        self.cb_pregunta4.setItemText(1, _translate("MainWindow", "Que requiera resolver problemas"))
        self.cb_pregunta4.setItemText(2, _translate("MainWindow", "Que se pueda explorar"))
        self.cb_pregunta4.setItemText(3, _translate("MainWindow", "Que no tenga historia"))
        self.btn_atras.setText(_translate("MainWindow", "Atras"))
        self.btn_enviar.setText(_translate("MainWindow", "Recomendar juegos"))
        self.label_6.setText(_translate("MainWindow", "Juegos recomendados:"))
        self.label_7.setText(_translate("MainWindow", "La categoría recomendada según su selección es:"))
        self.label_8.setText(_translate("MainWindow", "Categoria"))
        self.label_9.setText(_translate("MainWindow", "Juegos recomendados:"))
        self.label_10.setText(_translate("MainWindow", "- Juego"))

    
    def cambiarVentana(self):
        #Cambiar de ventana
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

    def ejecutarConsulta(self):
        respuesta1 = str(self.cb_pregunta1.currentText())
        respuesta2 = str(self.cb_pregunta2.currentText())
        respuesta3 = str(self.cb_pregunta3.currentText())
        respuesta4 = str(self.cb_pregunta4.currentText())
        # Se fija el parametro para la consulta de la pregunta 1:
        if(respuesta1 == "Mucho tiempo"):
            parametro1 = "dur_larga"
        elif(respuesta1 == "Una cantidad moderada"):
            parametro1 = "dur_media"
        else:
            parametro1 = "dur_corta"

        # Se fija el parametro para la consulta de la pregunta 2:
        if(respuesta2 == "Nuevos"):
            parametro2 = "nuevo"
        else:
            parametro2 = "antiguo"

        # Se fija el parametro para la consulta de la pregunta 3:
        if(respuesta3 == "Muy bueno"):
            parametro3 = "dif_dificil"
        elif (respuesta3 == "Normal"):
            parametro3 = "dif_media"
        else:
            parametro3 = "dif_facil"

        # Se fija el parametro para la consulta de la pregunta 3:

        if(respuesta4 == "Etapas distintas"):
            parametro4 = "etapas_distintas"
        elif (respuesta4 == "Que requiera resolver problemas"):
            parametro4 = "pensar"
        elif (respuesta4 == "Que se pueda explorar"):
            parametro4 = "mundo_abierto"
        else:
            parametro4 = "sin_historia"
        # Se efectua la consulta en prolog pasando los parametros seleccionados
        consulta = list(prolog.query("game(Juego,Categoria," + parametro1 + "," + parametro2 + "," + parametro3 + "," + parametro4 +")"))
        print(consulta)

        #En caso que la consulta arroje resultados:
        if(consulta != []):
            self.label_8.setText(consulta[0]['Categoria'])
            cadena = ""
            for i in consulta:
                cadena = cadena + "- " + i['Juego'] + "\n"
            self.label_10.setText(cadena)
            # Se muestra por pantalla las etiquetas con los resultados
            self.label_7.setHidden(False)
            self.label_8.setHidden(False)
            self.label_9.setHidden(False)
            self.label_10.setHidden(False)
        #En caso que la consulta no arroje ningun resultado
        else:
            self.label_8.setText("Categoria no determinada")
            self.label_10.setText("Lo sentimos, no hemos encontrado ningun juego")
            self.label_7.setHidden(False)
            self.label_8.setHidden(False)
            self.label_9.setHidden(False)
            self.label_10.setHidden(False)

# Ventana inicial
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
        #Cambiar de ventana
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.window)
        self.MainWindow.hide()
        self.window.show()

if __name__ == "__main__":
    # Se carga la base de conocimientos
    prolog.consult('base.pl')
    # Se inicializa el front
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

