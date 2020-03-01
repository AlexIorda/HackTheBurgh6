from PyQt4 import QtGui
from PyQt4.QtCore import QThread, SIGNAL
import sys
from chatbot import *
import chatbot2
import time

global cnt
cnt = 0

class getMessageThread(QThread):
    def __init__(self, msg):
        QThread.__init__(self)
        self.msg = msg

    def __del__(self):
        self.wait()

    def run(self):
        self.sleep(2)
        self.emit(SIGNAL('add_msg(QString)'), self.msg)


class Threading(QtGui.QMainWindow, chatbot2.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.sendBtn.clicked.connect(self.getMessage)
        self.answers = []
        self.textBrowser.append("Hello! I am your new friend the CHAAAAT BOT!")
        self.textBrowser.append("I will help you choose the right bank for you!")
        self.textBrowser.append("But firrrrst....enter some information in order to help me")
        self.textBrowser.append("How old are you?")

    def getMessage(self):
        global cnt
        botMsgArr = [
            "What is your income/month?",
            "Now I'm gonna get the perfect bank for youuuuuuuuu\nI want to get to know you better. What do you prefer:\n[1] The perfect bank in general\n[2] The best branch services\n[3] The best mobile banking services\n[4] The best overdraft services\nEnter choice please:"
        ]

        self.textBrowser.append(self.lineEdit.text())
        self.answers.append(self.lineEdit.text())
        if cnt <= 1:
            self.get_thread = getMessageThread(botMsgArr[cnt])
        cnt += 1
        if (cnt == 3):
            list_minimum_credit_limit = [get_minimum_credit_limit("api/ireland_ccc.json"), get_minimum_credit_limit("api/natwest_ccc.json")]
            make_dict_points()
            if (self.answers[2] == '1'):
                ans = best_bank(data_dict_Q1, int(self.answers[0]))
            elif (self.answers[2] == '2'):
                ans = best_bank(data_dict_Q2, int(self.answers[0]))
            elif (self.answers[2] == '3'):
                ans = best_bank(data_dict_Q3, int(self.answers[0]))
            elif (self.answers[2] == '4'):
                ans = best_bank(data_dict_Q4, int(self.answers[0]))
            for val in list_minimum_credit_limit:
                if (val > income / 3):
                    list_minimum_credit_limit.remove(val)
            QtGui.QMessageBox.information(self, "Your bank is...", ans)
        self.connect(self.get_thread, SIGNAL("add_msg(QString)"), self.add_msg)
        self.get_thread.start()

    def add_msg(self, added_msg):
        self.textBrowser.append(added_msg)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = Threading()
    form.show()
    app.exec_()
