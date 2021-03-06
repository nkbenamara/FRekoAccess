
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QCursor, QIcon, QFont
from PyQt5.QtWidgets import QToolTip
from glob import glob
import numpy as np
import os
from paths import *

from utils import donutGenerator
class Ui_Dashboard_Ui(object):
    def setupUi(self, Dashboard_Ui):
        '''
        MAIN WINDOW - DASHBOARD
        '''

        #Define Fonts
        QtGui.QFontDatabase.addApplicationFont("./fonts/Play-Regular.ttf")

        Dashboard_Ui.setObjectName("Dashboard_Ui")
        Dashboard_Ui.resize(900, 830)
        Dashboard_Ui.setStyleSheet("background-color: #1b1553;"
        "color: #ff4b3c;"
        "font-family: Play;"
        "font-size: 18px;"
        "border-radius: 5px;")
        Dashboard_Ui.setWindowIcon(QIcon("./imgs/logo.jpg"))
        self.centralwidget = QtWidgets.QWidget(Dashboard_Ui)
        self.centralwidget.setObjectName("centralwidget")
        self.class_number = QtWidgets.QLabel(self.centralwidget)
        self.class_number.setGeometry(QtCore.QRect(30, 40, 400, 400))
        self.class_number.setObjectName("class_number")
        self.collabs = QtWidgets.QLabel(self.centralwidget)
        self.collabs.setGeometry(QtCore.QRect(30, 500, 400, 220))
        self.collabs.setObjectName("collabs")
        self.donut1 = QtWidgets.QLabel(self.centralwidget)
        self.donut1.setGeometry(QtCore.QRect(485, 40, 220, 100))
        self.donut1.setObjectName("donut1")
        self.donut1_title = QtWidgets.QLabel(self.centralwidget)
        self.donut1_title.setGeometry(QtCore.QRect(485, 250, 320, 25))
        self.donut1_title.setStyleSheet("border: 1px solid white;"
                                        "margin-left: 50px")
        self.donut1_title.setText("Number of facial data per person")

        self.donut2 = QtWidgets.QLabel(self.centralwidget)
        self.donut2.setGeometry(QtCore.QRect(485, 285, 220, 100))
        self.donut2.setObjectName("donut2")

        self.donut2_title = QtWidgets.QLabel(self.centralwidget)
        self.donut2_title.setGeometry(QtCore.QRect(485, 495, 350, 25))
        self.donut2_title.setStyleSheet("border: 1px solid white;"
                                        "margin-left: 45px")
        self.donut2_title.setText("Number of Granted & Denied access")

        self.donut3 = QtWidgets.QLabel(self.centralwidget)
        self.donut3.setGeometry(QtCore.QRect(485, 525, 220, 100))
        self.donut3.setObjectName("donut3")

        self.donut3_title = QtWidgets.QLabel(self.centralwidget)
        self.donut3_title.setGeometry(QtCore.QRect(485, 735, 325, 25))
        self.donut3_title.setStyleSheet("border: 1px solid white;"
                                        "margin-left: 45px")
        self.donut3_title.setText("Number of access Day/Night time")

        self.donut1.setStyleSheet("border: 1px solid #4B0082;"
                                  "font-style:roboto;")
        self.donut2.setStyleSheet("border: 1px solid #4B0082;"
                                  "font-style:roboto;")
        self.donut3.setStyleSheet("border: 1px solid #4B0082;"
                                  "font-style:roboto;")



        Dashboard_Ui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dashboard_Ui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Dashboard_Ui.setMenuBar(self.menubar)
  
        ######menu##
        self.menubar = QtWidgets.QMenuBar(Dashboard_Ui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("""
                QMenuBar
                {
                    background-color: #0c0c13 ;
                    color: #999;
                }
                QMenuBar::item
                {
                    font-family: serif;
                    font-style: normal;
                    background-color: #0c0c13;
                    color: #f1f1f1 ;
                }
                QMenuBar::item::selected
                {
                    background-color: #3399cc;
                    color: #fff;
                }
                QMenu
                {
                    background-color: #3399cc;
                    color: #fff;
                }
                QMenu::item::selected
                {
                    background-color: #000033;
                    color: #999;
                }
                 """)

        self.menuDashboard = QtWidgets.QMenu(self.menubar)
        self.menuDashboard.setObjectName("menuDashboard")
        self.menuEnrolement = QtWidgets.QMenu(self.menubar)
        self.menuEnrolement.setObjectName("menuEnrolement")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuFace_recognition = QtWidgets.QMenu(self.menubar)
        self.menuFace_recognition.setObjectName("menuFace_recognition")
        self.start_facerecognition = QtWidgets.QAction(Dashboard_Ui)
        self.start_facerecognition.setObjectName("start_facerecognition")
        self.menuFace_recognition.addAction(self.start_facerecognition)
        self.menuFace_recognition.triggered[QAction].connect(self.openFaceRecognition)
        Dashboard_Ui.setMenuBar(self.menubar)

        self.actionAjouter_personne = QtWidgets.QAction(Dashboard_Ui)
        self.actionAjouter_personne.setObjectName("actionAjouter_personne")
        self.menuEnrolement.addAction(self.actionAjouter_personne)

        self.dashboardWindow = QtWidgets.QAction(Dashboard_Ui)
        self.dashboardWindow.setObjectName("dashboardWindow")
        self.menuDashboard.addAction(self.dashboardWindow)
        self.darkMode = QtWidgets.QAction(self.menuSettings)
        self.darkMode.setObjectName("Dark Mode")
        # setting default color of button to light-grey
        self.menuSettings.setStyleSheet("""QPushButton{background-color: lightgrey}""")
        self.menuSettings.addAction(self.darkMode)
        self.EAR_label = QtWidgets.QLabel(self.centralwidget)
        self.EAR_label.setGeometry(QtCore.QRect(600, 18, 265, 21))
        self.EAR_label.setObjectName("EAR_label")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EAR_label.setFont(font)
        self.blink_count = QtWidgets.QLabel(self.centralwidget)
        self.blink_count.setGeometry(QtCore.QRect(425, 18, 85, 21))
        self.blink_count.setObjectName("blink_count")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blink_count.setFont(font)
        # setting checkable to true

        # setting calling method by butto

        self.menubar.addAction(self.menuFace_recognition.menuAction())
        self.menubar.addAction(self.menuEnrolement.menuAction())
        self.menubar.addAction(self.menuDashboard.menuAction())
        self.menuEnrolement.triggered[QAction].connect(self.openEnrolementAddNew)
        self.menubar.addAction(self.menuSettings.menuAction())
        # Create new action
        self.menuLanguage = QtWidgets.QMenu(self.menuSettings)
        self.menuLanguage.setObjectName("menuLanguage")

        Dashboard_Ui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dashboard_Ui)
        self.statusbar.setObjectName("statusbar")
        Dashboard_Ui.setStatusBar(self.statusbar)
        self.anti_spoofing = QtWidgets.QAction(Dashboard_Ui)
        self.anti_spoofing.setObjectName("antispoofing")
        self.anti_spoofing.setCheckable(True)
        self.actionEnglish = QtWidgets.QAction(Dashboard_Ui)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionFran_ais = QtWidgets.QAction(Dashboard_Ui)
        self.actionFran_ais.setObjectName("actionFran_ais")
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionFran_ais)

        self.menuSettings.addAction(self.menuLanguage.menuAction())
        self.menuSettings.addAction(self.anti_spoofing)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(Dashboard_Ui)
        QtCore.QMetaObject.connectSlotsByName(Dashboard_Ui)
        donutGenerator(GALLERY_PATH+"y_train.npy",STAT_PATH+"img.png")
        donutGenerator(HISTORY_PATH+"access_history.npy",STAT_PATH+"img2.png")
        donutGenerator(HISTORY_PATH+"accessTime_history.npy",STAT_PATH+"img3.png")
        self.classCount()
        self.pieImg()


    def classCount(self):
        y_train = np.load(GALLERY_PATH+"y_train.npy")

        #data = np.unique(y_train, return_counts=True)[1]
        class_count = np.shape(np.unique(y_train, return_counts=True)[0])[0]

        self.class_number.setText("{}".format(class_count))
        self.class_number.setStyleSheet("font-size: 300px;""font-style: roboto;""text-align: center;")
        self.class_number.setAlignment(QtCore.Qt.AlignCenter)
        self.collabs.setText("Enrolled\nPersonnel")
        self.collabs.setStyleSheet("font-size: 85px;" "font-style: roboto;")
        self.collabs.setAlignment(QtCore.Qt.AlignCenter)



    def pieImg(self):
        pixmap1 = QPixmap(STAT_PATH+'img.png')
        pixmap2 = QPixmap(STAT_PATH+'img2.png')
        pixmap3 = QPixmap(STAT_PATH+'img3.png')
        self.donut1.setPixmap(pixmap1)
        self.donut1.resize(pixmap1.width(), pixmap1.height())
        self.donut2.setPixmap(pixmap2)
        self.donut2.resize(pixmap2.width(), pixmap2.height())
        self.donut3.setPixmap(pixmap3)
        self.donut3.resize(pixmap3.width(), pixmap3.height())



    def openFaceRecognition(self):
        print("opening reco")

    def openEnrolementAddNew(self):
        print("opening test")






    def retranslateUi(self, Dashboard_Ui):
        _translate = QtCore.QCoreApplication.translate
        Dashboard_Ui.setWindowTitle(_translate("Dashboard_Ui", "Dashboard"))
        self.donut1.setText(_translate("Dashboard_Ui", ""))
        self.donut2.setText(_translate("Dashboard_Ui", ""))
        self.donut3.setText(_translate("Dashboard_Ui", ""))
        self.collabs.setText(_translate("Dashboard_Ui", ""))
        self.class_number.setText(_translate("Dashboard_Ui", ""))
        self.menuEnrolement.setTitle(_translate("Dashboard_Ui", "Enrolement"))
        self.menuSettings.setTitle(_translate("Dashboard_Ui", "Settings"))
        self.menuFace_recognition.setTitle(_translate("Dashboard_Ui", "Face recognition"))
        self.menuDashboard.setTitle(_translate("Dashboard_Ui", "Dashboard"))
        self.actionAjouter_personne.setText(_translate("Dashboard_Ui", "Ajouter personne"))
        self.dashboardWindow.setText(_translate("Dashboard_Ui", "Open Dashboard"))
        self.darkMode.setText(_translate("Dashboard_Ui", "Enable Light Mod"))
        self.menuLanguage.setTitle(_translate("Dashboard_Ui", "Language"))
        self.actionEnglish.setText(_translate("Dashboard_Ui", "English"))
        self.actionFran_ais.setText(_translate("Dashboard_Ui", "Fran??ais"))
        self.anti_spoofing.setText(_translate("Dashboard_Ui", "Anti-Spoofing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dashboard_Ui = QtWidgets.QMainWindow()
    ui = Ui_Dashboard_Ui()
    ui.setupUi(Dashboard_Ui)
    Dashboard_Ui.show()
    sys.exit(app.exec_())
