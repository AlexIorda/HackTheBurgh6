# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatbot1.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread
from chatbot import closest_distance_to_atm
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class FirstThread(QThread):
    def __init__(self, msg):
        QThread.__init__(self)
        self.msg = msg

    def __del__(self):
        self.wait()

    def run(self):
        self.textBrowser.append("Da.")
        self.sleep(1)

class Ui_MainWindow(object):
    ok = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1249, 677)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(410, 10, 831, 71))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 829, 69))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 831, 71))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 371, 621))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 40, 261, 411))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Latin Modern Sans"))
        font.setPointSize(14)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 500, 491, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.sendBtn = QtGui.QPushButton(self.centralwidget)
        self.sendBtn.setGeometry(QtCore.QRect(1040, 500, 97, 27))
        self.sendBtn.setObjectName(_fromUtf8("sendBtn"))
        self.sendBtn.clicked.connect(self.writeInput)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1249, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.writeBot("What is you age?")


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Available Banks:\n"
"\n"
"Bank of Ireland\n"
"Bank of Scotland\n"
"Barclays Bank\n"
"Danske Bank\n"
"First Trust Bank\n"
"Halifax\n"
"HSBC Bank\n"
"Lloyds Bank\n"
"Nationwide Building Society\n"
"NatWest\n"
"Royal Bank of Scotland\n"
"Santander\n"
"Ulster Bank", None))
        self.sendBtn.setText(_translate("MainWindow", "Send", None))

    def done(self):
        QtGui.QMessageBox.information(self, "Done!", "I have it done.")

    def writeInput(self):
        self.textBrowser.append(self.lineEdit.text())
        self.firstThread = FirstThread("Good")
        self.connect(self.firstThread, SIGNAL("finished()"), self.done)
        self.firstThread.start()

    def writeBot(self, cnt):
        self.textBrowser.append(cnt)
