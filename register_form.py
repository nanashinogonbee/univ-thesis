# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 250))
        MainWindow.setMaximumSize(QtCore.QSize(400, 250))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        MainWindow.setToolTip("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(0, 0, 230, 25))
        self.login_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(0, 25, 230, 25))
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.login_form = QtWidgets.QLineEdit(self.centralwidget)
        self.login_form.setGeometry(QtCore.QRect(250, 0, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_form.sizePolicy().hasHeightForWidth())
        self.login_form.setSizePolicy(sizePolicy)
        self.login_form.setObjectName("login_form")
        self.password_form = QtWidgets.QLineEdit(self.centralwidget)
        self.password_form.setGeometry(QtCore.QRect(250, 25, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_form.sizePolicy().hasHeightForWidth())
        self.password_form.setSizePolicy(sizePolicy)
        self.password_form.setObjectName("password_form")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(0, 200, 400, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setObjectName("cancel_button")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(0, 150, 400, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_button.sizePolicy().hasHeightForWidth())
        self.register_button.setSizePolicy(sizePolicy)
        self.register_button.setObjectName("register_button")
        self.surname_label = QtWidgets.QLabel(self.centralwidget)
        self.surname_label.setGeometry(QtCore.QRect(0, 125, 230, 25))
        self.surname_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.surname_label.setObjectName("surname_label")
        self.patronymic_label = QtWidgets.QLabel(self.centralwidget)
        self.patronymic_label.setGeometry(QtCore.QRect(0, 100, 230, 25))
        self.patronymic_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.patronymic_label.setObjectName("patronymic_label")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(0, 75, 230, 25))
        self.name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_label.setObjectName("name_label")
        self.surname_form = QtWidgets.QLineEdit(self.centralwidget)
        self.surname_form.setGeometry(QtCore.QRect(250, 125, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.surname_form.sizePolicy().hasHeightForWidth())
        self.surname_form.setSizePolicy(sizePolicy)
        self.surname_form.setObjectName("surname_form")
        self.patronymic_form = QtWidgets.QLineEdit(self.centralwidget)
        self.patronymic_form.setGeometry(QtCore.QRect(250, 100, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patronymic_form.sizePolicy().hasHeightForWidth())
        self.patronymic_form.setSizePolicy(sizePolicy)
        self.patronymic_form.setObjectName("patronymic_form")
        self.name_form = QtWidgets.QLineEdit(self.centralwidget)
        self.name_form.setGeometry(QtCore.QRect(250, 75, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_form.sizePolicy().hasHeightForWidth())
        self.name_form.setSizePolicy(sizePolicy)
        self.name_form.setObjectName("name_form")
        self.password_confirm_form = QtWidgets.QLineEdit(self.centralwidget)
        self.password_confirm_form.setGeometry(QtCore.QRect(250, 50, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_confirm_form.sizePolicy().hasHeightForWidth())
        self.password_confirm_form.setSizePolicy(sizePolicy)
        self.password_confirm_form.setObjectName("password_confirm_form")
        self.password_confirm_label = QtWidgets.QLabel(self.centralwidget)
        self.password_confirm_label.setGeometry(QtCore.QRect(0, 50, 230, 25))
        self.password_confirm_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_confirm_label.setObjectName("password_confirm_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Регистрация"))
        self.login_label.setText(_translate("MainWindow", "Логин:"))
        self.password_label.setText(_translate("MainWindow", "Пароль:"))
        self.cancel_button.setText(_translate("MainWindow", "Отмена"))
        self.register_button.setText(_translate("MainWindow", "Регистрация"))
        self.surname_label.setText(_translate("MainWindow", "Фамилия:"))
        self.patronymic_label.setText(_translate("MainWindow", "Отчество:"))
        self.name_label.setText(_translate("MainWindow", "Имя:"))
        self.password_confirm_label.setText(_translate("MainWindow", "Подтверждение пароля:"))