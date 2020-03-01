# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatbot1.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1112, 518)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8("background-color:#70b2ff;\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(290, 30, 791, 351))
        self.scrollArea.setStyleSheet(_fromUtf8("border:0"))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 791, 361))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 791, 361))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("ori1Uni"))
        font.setPointSize(18)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet(_fromUtf8("background-color:#ffffff;\n"
"border-radius:21;"))
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 410, 681, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("ori1Uni"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:#ffffff;\n"
"border-radius:7"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.sendBtn = QtGui.QPushButton(self.centralwidget)
        self.sendBtn.setGeometry(QtCore.QRect(990, 410, 81, 27))
        self.sendBtn.setStyleSheet(_fromUtf8("background-color:#ffffff;\n"
"border-radius:10;"))
        self.sendBtn.setObjectName(_fromUtf8("sendBtn"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 261, 511))
        self.frame.setStyleSheet(_fromUtf8("background-color:rgba(9, 40, 76, 140);\n"
"margin:0;\n"
"padding:0;"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.banksBtn = QtGui.QPushButton(self.frame)
        self.banksBtn.setGeometry(QtCore.QRect(0, 190, 261, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(18)
        self.banksBtn.setFont(font)
        self.banksBtn.setStyleSheet(_fromUtf8("color:#dddddd"))
        self.banksBtn.setObjectName(_fromUtf8("banksBtn"))
        self.aboutBtn = QtGui.QPushButton(self.frame)
        self.aboutBtn.setGeometry(QtCore.QRect(0, 300, 261, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(18)
        self.aboutBtn.setFont(font)
        self.aboutBtn.setStyleSheet(_fromUtf8("color:#dddddd"))
        self.aboutBtn.setObjectName(_fromUtf8("aboutBtn"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 261, 131))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(60, 30, 131, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Latin Modern Sans Quotation"))
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet(_fromUtf8("background-color:rgb(0,0,0,0); color:#5e870c;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 230, 41, 41))
        self.label_2.setStyleSheet(_fromUtf8("background-color:rgb(0,0,0,0)"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("../iconfinder_home-house-homepage-building_2931150.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 340, 41, 41))
        self.label_3.setStyleSheet(_fromUtf8("background-color:rgb(0,0,0,0)"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("../iconfinder_about-info-information_2931180.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.resetBtn = QtGui.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(990, 450, 81, 27))
        self.resetBtn.setStyleSheet(_fromUtf8("background-color:#ffffff;\n"
"border-radius:10;"))
        self.resetBtn.setObjectName(_fromUtf8("resetBtn"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BankBot", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ori1Uni\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt;\"><br /></p></body></html>", None))
        self.sendBtn.setText(_translate("MainWindow", "Send", None))
        self.banksBtn.setText(_translate("MainWindow", "  Banks", None))
        self.aboutBtn.setText(_translate("MainWindow", "  About", None))
        self.label.setText(_translate("MainWindow", "BB", None))
        self.resetBtn.setText(_translate("MainWindow", "Reset", None))

