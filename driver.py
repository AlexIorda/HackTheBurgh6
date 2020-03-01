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
        self.resetBtn.clicked.connect(self.resetChat)
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

            global data_dict_Q1, data_dict_Q2, data_dict_Q3, data_dict_Q4
            with open ("api/sondaj_varste.json") as f:
                data = json.load(f)
            answers1 = {"Extremely likely" : 6, "Very likely": 5, "Fairly likely": 4, "Unlikely": 3,
                       "NOT USED IN RANKING: Don't know": 2, "NOT USED IN RANKING: Do not recommend": 1}
            answers2 = {"Extremely likely" : 7, "Very likely": 6, "Fairly likely": 5, "Unlikely": 4,
                       "NOT USED IN RANKING: Don't know": 3, "NOT USED IN RANKING: Do not recommend": 1,
                       "NOT USED IN RANKING: Have not used a branch in the last 3 months": 2}
            answers3 = {"Extremely likely" : 7, "Very likely": 6, "Fairly likely": 5, "Unlikely": 4,
                       "NOT USED IN RANKING: Don't know": 3, "NOT USED IN RANKING: Do not recommend": 1,
                       "NOT USED IN RANKING: Have not used online or mobile banking in the last 3 months": 2}
            answers4 = {"Extremely likely" : 7, "Very likely": 6, "Fairly likely": 5, "Unlikely": 4,
                       "NOT USED IN RANKING: Don't know": 3, "NOT USED IN RANKING: Do not recommend": 1,
                       "NOT USED IN RANKING: Have not been overdrawn in the last 12 months": 2}
            data_dict_Q1 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                              "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                              "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Clydesdale Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "first direct": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Metro Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Nationwide": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Tesco Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "The Co-operative Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "TSB": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Yorkshire Bank":  {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}

                            }
            data_dict_Q2 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                              "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                              "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Clydesdale Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "first direct": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Metro Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Nationwide": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Tesco Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "The Co-operative Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "TSB": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Yorkshire Bank":  {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}
                            }
            data_dict_Q3 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                              "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                              "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Clydesdale Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "first direct": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Metro Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Nationwide": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Tesco Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "The Co-operative Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "TSB": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Yorkshire Bank":  {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}

                            }
            data_dict_Q4 = { "Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                              "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                              "Barclays" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Halifax" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "HSBC UK" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Lloyds Bank" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "NatWest" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Royal Bank of Scotland" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Santander" : {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Clydesdale Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "first direct": { "16-24": 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Metro Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Nationwide": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Tesco Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "The Co-operative Bank": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "TSB": {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0},
                               "Yorkshire Bank":  {"16-24" : 0, "25-34" : 0, "35-44": 0, "45-54": 0, "55-64": 0, "65+": 0}
                            }
            for sample1 in data["Data"]["Brand"]:
                for sample in sample1["Data"]:
                    # print(sample)
                    if "PCAQ1All" in sample:
                        data_dict_Q1[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers1[sample["PCAQ1All"]]
                    if "PCAQ2All" in sample:
                        data_dict_Q2[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers2[sample["PCAQ2All"]]
                    if "PCAQ3All" in sample:
                        data_dict_Q3[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers3[sample["PCAQ3All"]]
                    if "PCAQ4All" in sample:
                        data_dict_Q4[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers4[sample["PCAQ4All"]]

            ans = ''
            if (self.answers[2] == '1'):
                ans = best_bank(data_dict_Q1, int(self.answers[0]))
            elif (self.answers[2] == '2'):
                ans = best_bank(data_dict_Q2, int(self.answers[0]))
            elif (self.answers[2] == '3'):
                ans = best_bank(data_dict_Q3, int(self.answers[0]))
            elif (self.answers[2] == '4'):
                ans = best_bank(data_dict_Q4, int(self.answers[0]))
            else:
                ans = "You did something wrong..."
            QtGui.QMessageBox.information(self, "Your bank is...", ans)
        self.connect(self.get_thread, SIGNAL("add_msg(QString)"), self.add_msg)
        self.get_thread.start()

    def add_msg(self, added_msg):
        self.textBrowser.append(added_msg)

    def resetChat(self):
        global cnt
        cnt = 0
        del self.answers[:]
        time.sleep(1.857)
        self.textBrowser.clear()
        self.textBrowser.append("Hello! I am your new friend the CHAAAAT BOT!")
        self.textBrowser.append("I will help you choose the right bank for you!")
        self.textBrowser.append("But firrrrst....enter some information in order to help me")
        self.textBrowser.append("How old are you?")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = Threading()
    form.show()
    app.exec_()
