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
        MainWindow.resize(1177, 508)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8("background-color:#70b2ff;\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(440, 40, 691, 351))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 689, 349))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 691, 351))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet(_fromUtf8("background-color:#ffffff;\n"
"border-radius:21;"))
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 420, 581, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:#ffffff;\n"
"border-radius:7"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.sendBtn = QtGui.QPushButton(self.centralwidget)
        self.sendBtn.setGeometry(QtCore.QRect(1046, 420, 81, 27))
        self.sendBtn.setStyleSheet(_fromUtf8("background-color:#ffffff;\n"
"border-radius:10;"))
        self.sendBtn.setObjectName(_fromUtf8("sendBtn"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 411, 491))
        self.frame.setStyleSheet(_fromUtf8("background-color:rgba(9, 40, 76, 140);\n"
"margin:0;\n"
"padding:0;"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.resetBtn = QtGui.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(1046, 460, 81, 27))
        self.resetBtn.setStyleSheet(_fromUtf8("background-color:#ffffff;\n"
"border-radius:10;"))
        self.resetBtn.setObjectName(_fromUtf8("resetBtn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatBot", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.sendBtn.setText(_translate("MainWindow", "Send", None))
        self.resetBtn.setText(_translate("MainWindow", "Reset", None))

