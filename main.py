import logging
import os
import random
import sqlite3
import sys
import time

from enum import Enum
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets

import login_form
import register_form
import select_inquiry_form
import admin_panel_form
import book_form
import db_edit_form
import manage_user_form
import manage_flags_form

import member_mgmt

class InquiryType(Enum):
    EXAMS = 8
    GRADES = 4
    BOOK = 2
    CERTIFICATE = 1


params = {'current_user': None}


class LoginForm(QtWidgets.QMainWindow, login_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_handlers()

    def register_handlers(self):
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
        login = self.login_form.text()
        password = self.password_form.text()
        logging.debug('login l: {}; p: {}'.format(login, password))
        cursor.execute(
            'SELECT * FROM users WHERE username=? AND password=?',
            (login, password)
            )
        result = cursor.fetchall()
        if not result:
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setWindowTitle('Ошибка')
            msgbox.setText('Неправильный логин или пароль!')
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec()
            logging.debug('login failed')
        else:
            params['current_user'] = login
            self.window = SelectInquiryForm()
            self.window.show()
            self.hide()
            logging.debug('login successful: id={}'.format(result[0][0]))

    def register(self):
        self.window = RegisterForm()
        self.window.show()
        self.hide()


class RegisterForm(QtWidgets.QMainWindow, register_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_handlers()

    def register_handlers(self):
        self.register_button.clicked.connect(self.register)
        self.cancel_button.clicked.connect(self.cancel)

    def register(self):
        login = self.login_form.text()
        password = self.password_form.text()
        password_confirm = self.password_confirm_form.text()
        name = self.name_form.text()
        patronymic = self.patronymic_form.text()
        surname = self.surname_form.text()
        logging.debug('reg l: {} p: {}|{} name: {} {} {}'.format(
            login, password, password_confirm, name, patronymic, surname
            ))
        forms = (login, password, password_confirm, name, patronymic, surname)
        forms_filled = all((form != '' for form in forms))
        if forms_filled:
            if password != password_confirm:
                msgbox = QMessageBox()
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setWindowTitle('Ошибка')
                msgbox.setText('Пароли не совпадают!')
                msgbox.setStandardButtons(QMessageBox.Ok)
                msgbox.exec()
                logging.debug('register failed: pw dont match')
            else:
                cursor.execute(
                    'SELECT id FROM users ORDER BY id DESC LIMIT 1'
                    )
                try:
                    last_id = cursor.fetchall()[0][0]
                except IndexError:
                    last_id = 0
                msgbox = QMessageBox()
                cursor.execute(
                    'INSERT INTO users VALUES(?,?,?,?,?,?,?)',
                    (last_id + 1, login, password, name, patronymic, surname, 1)
                    )
                conn.commit()
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setWindowTitle('Успешная регистрация')
                msgbox.setText('Регистрация прошла успешно!')
                msgbox.setStandardButtons(QMessageBox.Ok)
                msgbox.exec()
                logging.debug('register successful, id {}'.format(last_id + 1))
        else:
                msgbox = QMessageBox()
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setWindowTitle('Ошибка')
                msgbox.setText('Не заполнены все поля!')
                msgbox.setStandardButtons(QMessageBox.Ok)
                msgbox.exec()
                logging.debug('register failed: some fields are empty')


    def cancel(self):
        self.window = LoginForm()
        self.window.show()
        self.hide()


class SelectInquiryForm(QtWidgets.QMainWindow, select_inquiry_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        if params['current_user']:
            cursor.execute(
                'SELECT name, patronymic, surname, flags FROM users WHERE username=?',
                (params['current_user'],)
                )
            result = cursor.fetchone()
            self.welcome_label.setText('{} {} {}, добро пожаловать!'.format(*result))
            logging.debug('user flags: {}'.format(
                member_mgmt.get_member(result[-1])
                ))
            if member_mgmt.is_member(result[-1], member_mgmt.Member.ADMIN):
                self.admin_panel_button.setEnabled(True)
            else:
                self.admin_panel_button.setDisabled(True)

        self.register_handlers()

    def register_handlers(self):
        self.cancel_button.clicked.connect(self.to_main_menu)
        self.admin_panel_button.clicked.connect(self.to_admin_panel)
        self.certificate_button.clicked.connect(lambda: self.get_inquiry(InquiryType.CERTIFICATE))
        self.grades_button.clicked.connect(lambda: self.get_inquiry(InquiryType.GRADES))
        self.exams_button.clicked.connect(lambda: self.get_inquiry(InquiryType.EXAMS))
        self.book_button.clicked.connect(self.get_book)

    def to_main_menu(self):
        current_user = None
        self.window = LoginForm()
        self.window.show()
        self.hide()

    def to_admin_panel(self):
        self.window = AdminPanelForm()
        self.window.show()
        self.hide()

    def get_inquiry(self, inquiry_type):
        if params['current_user']:
            cursor.execute(
                'SELECT id FROM users WHERE username=?',
                (params['current_user'],)
                )
            user_id = cursor.fetchone()[0]
            inquiry_id = random.randint(10000000, 99999999)
            cursor.execute(
                'SELECT id FROM inquiries WHERE from_id=?',
                (user_id,)
                )
            while inquiry_id in cursor.fetchall():
                inquiry_id = random.randint(10000000, 99999999)
            cursor.execute(
                'INSERT INTO inquiries VALUES (?,?,0,?,"","")',
                (inquiry_id, user_id, inquiry_type.value)
                )
            conn.commit()
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setWindowTitle('Успех')
            msgbox.setText('ID заявки: {}'.format(inquiry_id))
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec()


    def get_book(self):
        self.window = BookForm()
        self.window.show()
        self.hide()

class AdminPanelForm(QtWidgets.QMainWindow, admin_panel_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_handlers()

    def register_handlers(self):
        self.cancel_button.clicked.connect(self.to_inquiry_menu)
        self.db_edit_button.clicked.connect(self.to_db_edit_menu)
        self.user_edit_button.clicked.connect(self.to_user_edit_menu)
        self.user_flags_edit_button.clicked.connect(self.to_user_flags_edit_menu)

    def to_inquiry_menu(self):
        self.window = SelectInquiryForm()
        self.window.show()
        self.hide()

    def to_db_edit_menu(self):
        self.window = DBEditForm()
        self.window.show()
        self.hide()

    def to_user_edit_menu(self):
        self.window = ManageUserForm()
        self.window.show()
        self.hide()

    def to_user_flags_edit_menu(self):
        self.window = ManageFlagsForm()
        self.window.show()
        self.hide()


class BookForm(QtWidgets.QMainWindow, book_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_handlers()

    def register_handlers(self):
        self.confirm_button.clicked.connect(self.get_book)
        self.cancel_button.clicked.connect(self.to_inquiry_menu)

    def to_inquiry_menu(self):
        self.window = SelectInquiryForm()
        self.window.show()
        self.hide()


    def get_book(self):
        if params['current_user']:
            cursor.execute(
                'SELECT id FROM users WHERE username=?',
                (params['current_user'],)
                )
            user_id = cursor.fetchone()[0]
            inquiry_id = random.randint(10000000, 99999999)
            cursor.execute(
                'SELECT id FROM inquiries WHERE from_id=?',
                (user_id,)
                )
            while inquiry_id in cursor.fetchall():
                inquiry_id = random.randint(10000000, 99999999)
            author = self.author_form.text()
            title = self.title_form.text()
            cursor.execute(
                'INSERT INTO inquiries VALUES (?,?,0,?,?,?)',
                (inquiry_id, user_id, InquiryType.BOOK.value, author, title)
                )
            conn.commit()
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setWindowTitle('Успех')
            msgbox.setText('ID заявки: {}'.format(inquiry_id))
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec()


class DBEditForm(QtWidgets.QMainWindow, db_edit_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_handlers()
        self.refresh()


    def register_handlers(self):
        self.back_button.clicked.connect(self.back)
        self.change_data_button.clicked.connect(self.change)
        self.inquiry_list.itemClicked.connect(self.fill_fields)

    def refresh(self):
        logging.debug('refreshing db')
        rows = self.inquiry_list.count()
        for row in range(rows):
            self.inquiry_list.takeItem(row)

        cursor.execute('SELECT * FROM inquiries')
        users = cursor.fetchall()
        for user in users:
            self.inquiry_list.addItem('ID {}'.format(user[0]))

    def fill_fields(self):
        current_item = self.inquiry_list.currentItem()
        current_item = current_item.text() if current_item else None
        selected_id = int(current_item.split()[-1])
        cursor.execute(
            'SELECT from_id, ready, type, book_author, book_title FROM inquiries WHERE id=?',
            (selected_id,)
            )
        userdata = cursor.fetchone()
        if userdata:
            if userdata[1]:
                self.is_ready_box.setChecked(True)
            else:
                self.is_ready_box.setChecked(False)
            if userdata[2] & 8:
                self.is_exams_box.setChecked(True)
            else:
                self.is_exams_box.setChecked(False)
            if userdata[2] & 4:
                self.is_grades_box.setChecked(True)
            else:
                self.is_grades_box.setChecked(False)
            if userdata[2] & 2:
                self.is_book_box.setChecked(True)
            else:
                self.is_book_box.setChecked(False)
            if userdata[2] & 1:
                self.is_certificate_box.setChecked(True)
            else:
                self.is_certificate_box.setChecked(False)


            self.from_id_form.setText(str(userdata[0]))
            self.book_author_form.setText(userdata[3])
            self.book_title_form.setText(userdata[4])
            self.change_data_button.setEnabled(True)
        logging.debug('selected item {}'.format(userdata))

    def change(self):
        inq_type = 0
        current_item = self.inquiry_list.currentItem()
        current_item = current_item.text() if current_item else None
        if current_item:
            selected_id = int(current_item.split()[-1])

            if self.is_certificate_box.isChecked():
                inq_type += 1
            if self.is_book_box.isChecked():
                inq_type += 2
            if self.is_grades_box.isChecked():
                inq_type += 4
            if self.is_exams_box.isChecked():
                inq_type += 8

            from_id = self.from_id_form.text()
            book_author = self.book_author_form.text()
            book_title = self.book_title_form.text()

            if from_id != '' and inq_type:
                cursor.execute(
                    'UPDATE inquiries SET from_id=?, ready=?, type=?, book_author=?, book_title=? WHERE id=?',
                    (from_id, int(self.is_ready_box.isChecked()), inq_type, book_author, book_title, selected_id)
                    )
                conn.commit()
                msgbox = QMessageBox()
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setWindowTitle('Успех')
                msgbox.setText('Данные обновлены!')
                msgbox.setStandardButtons(QMessageBox.Ok)
                msgbox.exec()
                logging.debug('data updated')
            else:
                msgbox = QMessageBox()
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setWindowTitle('Ошибка')
                msgbox.setText('Не заполнены все поля!')
                msgbox.setStandardButtons(QMessageBox.Ok)
                msgbox.exec()
                logging.debug('register failed: some fields are empty')

    def back(self):
        self.window = AdminPanelForm()
        self.window.show()
        self.hide()


class ManageUserForm(QtWidgets.QMainWindow, manage_user_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_handlers()
        self.refresh()


    def register_handlers(self):
        self.back_button.clicked.connect(self.back)
        self.add_user_button.clicked.connect(self.add_user)
        self.remove_user_button.clicked.connect(self.remove_user)


    def refresh(self):
        logging.debug('refreshing db')
        rows = self.user_list.count()
        for row in range(rows):
            self.user_list.takeItem(row)

        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        for user in users:
            self.user_list.addItem('ID {}'.format(user[0]))

    def add_user(self):
        login = self.login_form.text()
        password = self.password_form.text()
        name = self.name_form.text()
        patronymic = self.patronymic_form.text()
        surname = self.surname_form.text()
        logging.debug('add l: {} p: {} name: {} {} {}'.format(
            login, password, name, patronymic, surname
            ))
        forms = (login, password, name, patronymic, surname)
        forms_filled = all((form != '' for form in forms))
        if forms_filled:
            cursor.execute(
                'SELECT id FROM users ORDER BY id DESC LIMIT 1'
                )
            last_id = cursor.fetchall()[0][0]
            msgbox = QMessageBox()
            cursor.execute(
                'INSERT INTO users VALUES(?,?,?,?,?,?,?)',
                (last_id + 1, login, password, name, patronymic, surname, 1)
                )
            conn.commit()
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setWindowTitle('Успех')
            msgbox.setText('Добавлен пользователь с id {}!'.format(last_id + 1))
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec()
            logging.debug('item appending successful, id {}'.format(last_id + 1))
        else:
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setWindowTitle('Ошибка')
            msgbox.setText('Не заполнены все поля!')
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec()
            logging.debug('register failed: some fields are empty')

    def remove_user(self):
        current_item = self.user_list.currentItem()
        current_item = current_item.text() if current_item else None
        if current_item:
            selected_id = int(current_item.split()[-1])
            cursor.execute(
                'DELETE FROM users WHERE id=?',
                (selected_id,)
                )
            conn.commit()
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setWindowTitle('Успех')
            msgbox.setText('Пользователь удалён!')
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec()
            logging.debug('user removed')

    def back(self):
        self.window = AdminPanelForm()
        self.window.show()
        self.hide()


class ManageFlagsForm(QtWidgets.QMainWindow, manage_flags_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_handlers()
        self.refresh()


    def register_handlers(self):
        self.update_flags_button.clicked.connect(self.update)
        self.back_button.clicked.connect(self.back)
        self.user_list.itemClicked.connect(self.fill_fields)


    def refresh(self):
        logging.debug('refreshing db')
        rows = self.user_list.count()
        for row in range(rows):
            self.user_list.takeItem(row)

        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        for user in users:
            self.user_list.addItem('ID {}'.format(user[0]))


    def fill_fields(self):
        current_item = self.user_list.currentItem()
        current_item = current_item.text() if current_item else None
        if current_item:
            selected_id = int(current_item.split()[-1])
            cursor.execute(
                'SELECT flags FROM users WHERE id=?',
                (selected_id,)
                )
            flags = cursor.fetchone()[0]
            if member_mgmt.is_member(flags, member_mgmt.Member.ADMIN):
                self.is_admin_box.setChecked(True)
            else:
                self.is_admin_box.setChecked(False)

            if member_mgmt.is_member(flags, member_mgmt.Member.PRINCIPAL):
                self.is_principal_box.setChecked(True)
            else:
                self.is_principal_box.setChecked(False)

            if member_mgmt.is_member(flags, member_mgmt.Member.TEACHER):
                self.is_teacher_box.setChecked(True)
            else:
                self.is_teacher_box.setChecked(False)

            if member_mgmt.is_member(flags, member_mgmt.Member.STUDENT):
                self.is_student_box.setChecked(True)
            else:
                self.is_student_box.setChecked(False)


    def update(self):
        flag_state = 0
        current_item = self.user_list.currentItem()
        current_item = current_item.text() if current_item else None
        if current_item:
            selected_id = int(current_item.split()[-1])
            if self.is_student_box.isChecked():
                flag_state += 1
            if self.is_teacher_box.isChecked():
                flag_state += 2
            if self.is_principal_box.isChecked():
                flag_state += 4
            if self.is_admin_box.isChecked():
                flag_state += 8
            selected_id = int(current_item.split()[-1])
            cursor.execute(
                'UPDATE users SET flags=? WHERE id=?',
                (flag_state, selected_id)
                )
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setWindowTitle('Успех')
            msgbox.setText('Флаги пользователя обновлены!')
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec()
            logging.debug('flags updated to {}'.format(flag_state))


    def back(self):
        self.window = AdminPanelForm()
        self.window.show()
        self.hide()


logging.basicConfig(
    format='%(asctime)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG
    )

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

try:
    cursor.execute('''CREATE TABLE users
           (
           id INTEGER,
           username TEXT,
           password TEXT,
           name TEXT,
           patronymic TEXT,
           surname TEXT,
           flags INTEGER
           )''')
    conn.commit()
    logging.info('created table')
except sqlite3.OperationalError:
    logging.info('table already exists')

logging.info('started')

os.environ['QT_PLUGIN_PATH'] = '/usr/lib/qt/plugins'
app = QtWidgets.QApplication(sys.argv)

login_form = LoginForm()
register_form = RegisterForm()
select_inquiry_form = SelectInquiryForm()

login_form.show()

app.exec_()
