# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(373, 295)
        MainWindow.setStyleSheet("background-color:rgb(250, 250, 250)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 371, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/ABSTRACT_COLORFUL_BACKGROUND_01.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 40, 261, 241))
        self.groupBox.setStyleSheet("background-color:rgb(245, 245, 245);\n"
"")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(0, 20, 261, 211))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Dank Mono")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(13, 71, 161);\n"
"color:rgb(250, 250, 250);\n"
"")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.get_cpu = QtWidgets.QLineEdit(self.tab)
        self.get_cpu.setGeometry(QtCore.QRect(60, 80, 142, 24))
        self.get_cpu.setStyleSheet("rounded-corner:0px;\n"
"margin-border: 20px;\n"
"border-color: blue;\n"
"")
        self.get_cpu.setObjectName("get_cpu")
        self.enviar_cpu = QtWidgets.QPushButton(self.tab)
        self.enviar_cpu.setGeometry(QtCore.QRect(90, 140, 80, 24))
        self.enviar_cpu.setStyleSheet("color: rgb(250, 250, 250);\n"
"background-color: rgb(26, 35, 126);\n"
"rounded-corner: 0px;\n"
"border-radius:0px;")
        self.enviar_cpu.setObjectName("enviar_cpu")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.get_memoria = QtWidgets.QLineEdit(self.tab_2)
        self.get_memoria.setGeometry(QtCore.QRect(60, 80, 142, 24))
        self.get_memoria.setStyleSheet("rounded-corner:0px;\n"
"margin-border: 20px;\n"
"border-color: blue;\n"
"")
        self.get_memoria.setObjectName("get_memoria")
        self.enviar_memoria = QtWidgets.QPushButton(self.tab_2)
        self.enviar_memoria.setGeometry(QtCore.QRect(90, 140, 80, 24))
        self.enviar_memoria.setStyleSheet("color: rgb(250, 250, 250);\n"
"background-color: rgb(26, 35, 126);\n"
"rounded-corner: 0px;\n"
"border-radius:0px;")
        self.enviar_memoria.setObjectName("enviar_memoria")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Dank Mono")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgb(74, 20, 140);\n"
"color:rgb(250, 250, 250);\n"
"")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplicaci??n de escritorio"))
        self.groupBox.setTitle(_translate("MainWindow", "Formulario de env??o"))
        self.label_2.setText(_translate("MainWindow", "Cantidad de procesos"))
        self.enviar_cpu.setText(_translate("MainWindow", "Enviar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Uso de CPU"))
        self.enviar_memoria.setText(_translate("MainWindow", "Enviar"))
        self.label_3.setText(_translate("MainWindow", "Cantidad de procesos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Uso de Memoria"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
