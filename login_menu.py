from PyQt5.QtWidgets import *
from design.login_menu_design import Ui_login_menu
from main_menu import MainPage
from db.database import login_check


class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.login_menu = Ui_login_menu()
        self.main_menu = MainPage()
        self.login_menu.setupUi(self)
        self.login_menu.username_box.setText("admin")
        self.login_menu.password_box.setText("1234")

        self.login_menu.login_button.clicked.connect(self.login)

    def login(self):
        self.username = self.login_menu.username_box.text()
        self.password = self.login_menu.password_box.text()
        if login_check(self.username, self.password):
            #TODO open main menu
            self.close()
            self.main_menu.show()
        else:
            print("Wrong id pw or not confirmed")