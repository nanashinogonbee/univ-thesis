# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_panel_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 250))
        MainWindow.setMaximumSize(QtCore.QSize(600, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.db_edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.db_edit_button.setGeometry(QtCore.QRect(0, 50, 300, 100))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.db_edit_button.setFont(font)
        self.db_edit_button.setObjectName("db_edit_button")
        self.admin_panel_label = QtWidgets.QLabel(self.centralwidget)
        self.admin_panel_label.setGeometry(QtCore.QRect(0, 0, 600, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(24)
        self.admin_panel_label.setFont(font)
        self.admin_panel_label.setTextFormat(QtCore.Qt.AutoText)
        self.admin_panel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.admin_panel_label.setObjectName("admin_panel_label")
        self.user_edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.user_edit_button.setGeometry(QtCore.QRect(300, 50, 300, 100))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.user_edit_button.setFont(font)
        self.user_edit_button.setObjectName("user_edit_button")
        self.user_flags_edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.user_flags_edit_button.setGeometry(QtCore.QRect(0, 150, 300, 100))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.user_flags_edit_button.setFont(font)
        self.user_flags_edit_button.setObjectName("user_flags_edit_button")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(300, 150, 300, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выберите услугу"))
        self.db_edit_button.setText(_translate("MainWindow", "Управление\n"
"записями в БД"))
        self.admin_panel_label.setText(_translate("MainWindow", "Панель администратора"))
        self.user_edit_button.setText(_translate("MainWindow", "Добавить/удалить\n"
"пользователя"))
        self.user_flags_edit_button.setText(_translate("MainWindow", "Управление правами\n"
"пользователей"))
        self.cancel_button.setText(_translate("MainWindow", "Выход"))
