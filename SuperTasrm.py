# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tasarım.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import SuperNeuroThesisInvestigator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 365)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_DosGr = QtWidgets.QPushButton(self.centralwidget)
        self.Button_DosGr.setGeometry(QtCore.QRect(30, 30, 131, 31))
        self.Button_DosGr.setObjectName("Button_DosGr")
        self.ButtonGor = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonGor.setGeometry(QtCore.QRect(30, 70, 131, 31))
        self.ButtonGor.setObjectName("ButtonGor")
        self.ButtonGiris = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonGiris.setGeometry(QtCore.QRect(30, 150, 131, 31))
        self.ButtonGiris.setObjectName("ButtonGiris")
        self.ButtonKaynak = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonKaynak.setGeometry(QtCore.QRect(30, 110, 131, 31))
        self.ButtonKaynak.setObjectName("ButtonKaynak")
        self.ButtonKelimeG = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonKelimeG.setGeometry(QtCore.QRect(30, 190, 131, 31))
        self.ButtonKelimeG.setObjectName("ButtonKelimeG")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(190, 20, 501, 211))
        self.listWidget.setObjectName("listWidget")
        self.ButtonODgor = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonODgor.setGeometry(QtCore.QRect(70, 290, 131, 23))
        self.ButtonODgor.setObjectName("ButtonODgor")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(60, 260, 151, 21))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 290, 131, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(220, 260, 151, 21))
        self.listWidget_3.setObjectName("listWidget_3")
        self.ButtonPrgBu = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonPrgBu.setGeometry(QtCore.QRect(390, 290, 131, 23))
        self.ButtonPrgBu.setObjectName("ButtonPrgBu")
        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(380, 260, 151, 21))
        self.listWidget_4.setObjectName("listWidget_4")
        self.ButonKlmFnd = QtWidgets.QPushButton(self.centralwidget)
        self.ButonKlmFnd.setGeometry(QtCore.QRect(550, 290, 131, 23))
        self.ButonKlmFnd.setObjectName("ButonKlmFnd")
        self.listWidget_5 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(540, 260, 151, 21))
        self.listWidget_5.setObjectName("listWidget_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_DosGr.setText(_translate("MainWindow", "Dosya Düzenle"))
        self.ButtonGor.setText(_translate("MainWindow", "Dosya Görüntüleme"))
        self.ButtonGiris.setText(_translate("MainWindow", "Giriş Sayfası Tarama"))
        self.ButtonKaynak.setText(_translate("MainWindow", "Kaynakca Tarama"))
        self.ButtonKelimeG.setText(_translate("MainWindow", "Kelime Getir"))
        self.ButtonODgor.setText(_translate("MainWindow", "Orjinal Dosyadan Göster"))
        self.pushButton_7.setText(_translate("MainWindow", "Satır Olarak Göster"))
        self.ButtonPrgBu.setText(_translate("MainWindow", "Paragraf Bul"))
        self.ButonKlmFnd.setText(_translate("MainWindow", "Kelime Arama"))

       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

