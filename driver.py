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
        self.banksBtn.clicked.connect(lambda:QtGui.QMessageBox.information(self, "Banks", "Available Banks:\n\nBank of Ireland\nBank of Scotland\nBarclays Bank\nDanske Bank\nFirst Trust Bank\nHalifax\nHSBC Bank\nLloyds Bank\nNationwide Building Society\nNatWest\nRoyal Bank of Scotland\nSantander\nUlster Bank"))
        self.aboutBtn.clicked.connect(lambda:QtGui.QMessageBox.information(self, "About", "This piece of software would have not been possible without the wonderful environment provided by the Hack The Burgh team"))
        self.answers = []
        self.textBrowser.append("BOT: Hello! I am your new friend the CHAAAAT BOT!")
        self.textBrowser.append("BOT: I will help you choose the right bank for you!")
        self.textBrowser.append("BOT: But firrrrst....enter some information in order to help me")
        self.textBrowser.append("BOT: How old are you?")

    def getMessage(self):
        global cnt
        botMsgArr = [
            "BOT: What is your income per month?",
            "BOT: Are you interested in applying for a credit?",
            "BOT: Now I'm gonna get the perfect bank for youuuuuuuuu\nI want to get to know you better. What do you prefer:\n[1] The perfect bank in general\n[2] The best branch services\n[3] The best mobile banking services\n[4] The best overdraft services\nEnter choice please:"
        ]

        self.textBrowser.append("ME: " + self.lineEdit.text())
        self.answers.append(self.lineEdit.text())
        if cnt <= 2:
            self.get_thread = getMessageThread(botMsgArr[cnt])
        cnt += 1
        self.lineEdit.clear()
        if (cnt == 4):
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
            dist_dict = closest_distance_to_atm()
            ind = 1
            bank_to_ind = {"Santander" : 2, "HSBC UK" : 1.8, "Royal Bank of Scotland": 1.7, "Bank of Scotland" : 1.6, "Barclays": 1.5, "Halifax": 1.4, "NatWest": 1.3, "Lloyds Bank": 1.2 }
            for sample1 in data["Data"]["Brand"]:
                for sample in sample1["Data"]:
                    if (sample["Brand"] in dist_dict):
                        ind = bank_to_ind[sample["Brand"]]
                    # print(sample)
                    if "PCAQ1All" in sample:
                        data_dict_Q1[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers1[sample["PCAQ1All"]] * ind
                    if "PCAQ2All" in sample:
                        data_dict_Q2[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers2[sample["PCAQ2All"]] * ind
                    if "PCAQ3All" in sample:
                        data_dict_Q3[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers3[sample["PCAQ3All"]] * ind
                    if "PCAQ4All" in sample:
                        data_dict_Q4[sample["Brand"]][sample["Age"]] += sample["Weight"] *  answers4[sample["PCAQ4All"]] * ind

            ans = ''
            if (self.answers[3] == '1'):
                ans = best_bank(data_dict_Q1, int(self.answers[0]), float(self.answers[1]), want_credit=(self.answers[2][0] == 'y' or self.answers[2][0] == 'Y'))
            elif (self.answers[3] == '2'):
                ans = best_bank(data_dict_Q2, int(self.answers[0]), float(self.answers[1]), want_credit=(self.answers[2][0] == 'y' or self.answers[2][0] == 'Y'))
            elif (self.answers[3] == '3'):
                ans = best_bank(data_dict_Q3, int(self.answers[0]), float(self.answers[1]), want_credit=(self.answers[2][0] == 'y' or self.answers[2][0] == 'Y'))
            elif (self.answers[3] == '4'):
                ans = best_bank(data_dict_Q4, int(self.answers[0]), float(self.answers[1]), want_credit=(self.answers[2][0] == 'y' or self.answers[2][0] == 'Y'))
            else:
                ans = "You did something wrong..."
            QtGui.QMessageBox.information(self, "Your bank is...", "The bank that we are recommending you is " + ans)
            return
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
