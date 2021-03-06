
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QCursor, QIcon, QFont
from utils import load_actual_collaborators,reinteger_one_collaborator,reinteger_all,delete_personel
import os
import random
import cv2

class Ui_enrolement_ChangeAccess(object):
    def setupUi(self, enrolement_Delete):
        '''
        MAIN WINDOW - ENROLEMENT_DELETE
        '''

        #Define Fonts
        QtGui.QFontDatabase.addApplicationFont("./fonts/Play-Regular.ttf")

        enrolement_Delete.setObjectName("enrolement_ChangeAccess")
        enrolement_Delete.setFixedSize(900, 830)
        enrolement_Delete.setStyleSheet("background-color: #1b1553;"
        "color: #ff4b3c;"
        "font-family: Play;"
        "font-size: 18px;"
        "border-radius: 5px;")
        enrolement_Delete.setWindowIcon(QIcon("./imgs/logo.jpg"))

        self.centralwidget = QtWidgets.QWidget(enrolement_Delete)
        self.centralwidget.setObjectName("centralwidget")

        self.face_pic = QtWidgets.QLabel(enrolement_Delete)
        self.face_pic.setGeometry(15, 40, 425, 380)
        self.face_pic.setStyleSheet("border: 1px solid white;")
        self.face_pic.setText("")
        self.face_pic.setScaledContents(True)
        font = QtGui.QFont()
        self.vgg16_enroled_list = QtWidgets.QLabel(enrolement_Delete)
        self.vgg16_enroled_list.setGeometry(475, 40, 425, 350)
        self.vgg16_enroled_list.setStyleSheet("border: 1px solid white;")
        self.vgg16_enroled_list.setText("load_actual_collaborators")

        self.radio_vgg16 = QtWidgets.QRadioButton(enrolement_Delete)
        self.radio_vgg16.setGeometry(QtCore.QRect(350, 515, 121, 21))
        font.setPointSize(12)
        self.radio_vgg16.setFont(font)
        self.radio_vgg16.setObjectName("radio_vgg16")
        self.radio_vgg16.setText("VGG16")


        self.radio_resnet50 = QtWidgets.QRadioButton(enrolement_Delete)
        self.radio_resnet50.setGeometry(QtCore.QRect(350, 450, 121, 21))
        font.setPointSize(12)
        self.radio_resnet50.setFont(font)
        self.radio_resnet50.setObjectName("radio_resnet50")
        self.radio_resnet50.setText("RESNET50")


        self.nameText = QtWidgets.QLineEdit(enrolement_Delete)

        self.nameText.setGeometry(40, 475, 200, 30)
        self.nameText.setStyleSheet("border: 1px solid white;"
                                    "font-style:bold;"
                                    "background-color:rgb(255,255,255);"
                                    "color: rgb(0,0,0);"
                                    )
        self.CURRENT_PATH = os.getcwd()
        self.nameLabel = QtWidgets.QLabel(enrolement_Delete)
        self.nameLabel.setGeometry(QtCore.QRect(40, 435, 205, 30))
        self.nameLabel.setStyleSheet("border: 1px solid white;"
                                     "font-style:bold;"
                                     "background-color:rgb(77, 77, 77);"
                                     "color: rgb(255,255,255);"
                                     )
        self.nameLabel.setText("Name of person to edit:")
        self.nameButton = QtWidgets.QPushButton(enrolement_Delete)
        self.nameButton.setGeometry(60, 525, 150, 30)
        self.nameButton.setText("EDIT")
        self.nameButton.setStyleSheet(
            "QPushButton::hover"
            "{"
            "background-color:rgb(255,255,255);"
            "color: black;"
            "}"
            "border: 1px solid white;"
        )
        self.nameButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.nameButton.clicked.connect(self.editPersonnel)
        self.autorization_label = QtWidgets.QLabel(enrolement_Delete)
        self.autorization_label.setGeometry(60, 555, 300, 250)
        self.autorization_label.setText("")
        self.delete_person = QtWidgets.QPushButton(enrolement_Delete)
        self.delete_person.setGeometry(275, 555, 235, 35)
        self.delete_person.setText("Remove THIS user from database")
        self.delete_person.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: red;"
            "border-style: outset;"
            "border-width: 2px;"
            "border-radius: 10px;"
            "border-color: gray;"
            "}"

            "QPushButton::hover"
            "{"
            "background-color:rgb(255,255,255);"
            "color: black;"
            "}"
            "QPushButton::pressed" "{" "background-color: red" "}"
        )
        self.delete_person.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_person.setVisible(False)

        self.reinteger_person = QtWidgets.QPushButton(enrolement_Delete)
        self.reinteger_person.setGeometry(275, 450, 235, 35)
        self.reinteger_person.setText("Reintegrate THIS user only")
        self.reinteger_person.setVisible(False)
        self.reinteger_person.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: green;"
            "border-style: outset;"
            "border-width: 2px;"
            "border-radius: 10px;"
            "border-color: beige;"
            "}"
            "QPushButton::hover"
            "{"
            "background-color:rgb(255,255,255);"
            "color: black;"
            "}"
            "QPushButton::pressed" "{" "background-color: green" "}"
        )
        self.reinteger_person.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.reinteger_all = QtWidgets.QPushButton(enrolement_Delete)
        self.reinteger_all.setGeometry(275, 500, 235, 35)
        self.reinteger_all.setText("Reintegrate All users")
        self.reinteger_all.setVisible(False)
        self.reinteger_all.setStyleSheet(
            "QPushButton"
            "{"
            "background-color: green;"
            "border-style: outset;"
            "border-width: 2px;"
            "border-radius: 10px;"
            "border-color: beige;"
            "}"
            "QPushButton::hover"
            "{"
            "background-color:rgb(255,255,255);"
            "color: black;"
            "}"
            "QPushButton::pressed" "{" "background-color: green" "}"
        )
        self.reinteger_all.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.reinteger_person.clicked.connect(self.ReintegerOne)
        self.reinteger_all.clicked.connect(self.ReintegerAll)
        self.delete_person.clicked.connect(self.Remove)

    def ReintegerOne(self):
        person = self.nameText.text()
        authorizations = np.load('./gallery/authorized.npy')
        authorizations = np.append(authorizations, str(person))
        radio_vgg16 = self.radio_vgg16.isChecked()
        radio_resnet50 = self.radio_resnet50.isChecked()
        if radio_vgg16 == True:
            model_type = "vgg16"
        if radio_resnet50 == True:
            model_type = "resnet50"

        reinteger_one_collaborator(model_type,person)
        self.autorization_label.setText("PREVIOUSLY DELETED {} HAS BEEN".format(person) + '\n' + "REINTEGRATED SUCCESSFULLY!")
    def ReintegerAll(self):
        person = self.nameText.text()
        authorizations = np.load('./gallery/authorized.npy')
        authorizations = np.append(authorizations, str(person))
        radio_vgg16 = self.radio_vgg16.isChecked()
        radio_resnet50 = self.radio_resnet50.isChecked()
        if radio_vgg16 == True:
            model_type = "vgg16"
        if radio_resnet50 == True:
            model_type = "resnet50"

        reinteger_all(model_type)
        self.autorization_label.setText("ALL PREVIOUSLY DELETED PERSONNEL HAVE BEEN"+'\n'+ "REINTEGRATED SUCCESSFULLY!")
    def Remove(self):
        person = self.nameText.text()
        radio_vgg16 = self.radio_vgg16.isChecked()
        radio_resnet50 = self.radio_resnet50.isChecked()
        if radio_vgg16 == True:
            model_type = "vgg16"
            delete_personel(model_type,person)
        if  radio_resnet50 == True:
            model_type = "resnet50"
            delete_personel(model_type, person)
        self.autorization_label.setText("{}  DELETED FROM DATABASE".format(person))
            
    def editPersonnel(self):
        person = self.nameText.text()
        rand_pic = random.randrange(0, 50)
        path = self.CURRENT_PATH + "/dataset_cropped/" + person + "/{}.jpg".format(rand_pic)
        print(path)
        face_img =  cv2.imread(path)
        radio_vgg16 = self.radio_vgg16.isChecked()
        radio_resnet50 = self.radio_resnet50.isChecked()
        height, width, channel = face_img.shape
        step = channel * width
        if radio_vgg16 == True:
            model_type = "vgg16"
        if radio_resnet50 == True:
            model_type = "resnet50"
            print(radio_resnet50)

        active_y_train = np.load('./gallery/{}_y-train.npy'.format(model_type))
        deleted_y_train = np.load('./gallery/deleted_{}_y-train.npy'.format(model_type))
        self.delete_person.setVisible(True)
        self.reinteger_person.setVisible(True)
        self.reinteger_all.setVisible(True)
        if np.where(active_y_train == person):
            print("exists:"+ person)
            self.autorization_label.setText("{}".format(person) + '\n' +": IS CURRENTLY ENROLLED!")

        if np.where(deleted_y_train == person):
            print("deleted:"+ person)
            self.autorization_label.setText("{}".format(person) +'\n' +": HAS BEEN PREVIOUSLY DELETED!")

        else:
            self.autorization_label.setText("{} IS NOT PART OF THE PERSONNEL".format(person))
            self.delete_person.setVisible(False)
            self.reinteger_person.setVisible(False)
            self.reinteger_all.setVisible(False)
        qImg = QImage(face_img.data, width, height, step, QImage.Format_RGB888)
        self.face_pic.setPixmap(QPixmap.fromImage(qImg))

    def retranslateUi(self, enrolement_Delete):
        _translate = QtCore.QCoreApplication.translate
        enrolement_Delete.setWindowTitle(_translate("enrolement_Delete", "FRekoAccess: Change Access"))
        self.vgg16_enroled_list.setText(_translate("enrolement_Delete", ""))
        self.nameLabel.setText(_translate("enrolement_Delete", ""))
        self.nameText.setText(_translate("enrolement_Delete", " "))
        self.radio_vgg16.setText(_translate("enrolement_Delete", "VGG16"))
        self.radio_resnet50.setText(_translate("enrolement_Delete", "RESNET 50"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    enrolement_addNew = QtWidgets.QMainWindow()
    ui = Ui_enrolement_ChangeAccess()
    ui.setupUi(enrolement_addNew)
    enrolement_addNew.show()
    sys.exit(app.exec_())
