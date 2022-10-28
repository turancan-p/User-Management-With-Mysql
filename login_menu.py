from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from design.login_menu_design import Ui_login_menu
from main_menu import MainPage
from register_menu import UserRegisterPage
from db.database import login_check, user_confirmed, confirm_user


class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.login_menu = Ui_login_menu()
        self.main_menu = MainPage()
        self.register_menu = UserRegisterPage()
        self.login_menu.setupUi(self)
        self.login_menu.username_box.setText("admin")
        self.login_menu.password_box.setText("1234")

        self.login_menu.login_button.clicked.connect(self.login)

        self.login_menu.register_button.clicked.connect(self.register)

    def login(self):
        self.username = self.login_menu.username_box.text()
        self.password = self.login_menu.password_box.text()
        if login_check(self.username, self.password):
            if user_confirmed(self.username):
                self.close()
                self.main_menu.show()
                self.main_menu.update_table()
            else:
                print("You are not confirmed")

        else:
            print("Wrong id or pw")

    def register(self):
        self.register_menu.show()
