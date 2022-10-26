from PyQt5.QtWidgets import *
from design.register_menu_design import Ui_register_menu
from db.database import save_user


class UserRegisterPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.register_menu = Ui_register_menu()
        self.register_menu.setupUi(self)

        self.register_menu.register_button.clicked.connect(self.save_to_db)

    def save_to_db(self):
        username = self.register_menu.username_box.text()
        password = self.register_menu.password_box.text()

        save_user(username, password)