from PyQt5.QtWidgets import *
from design.save_user_design import Ui_save_menu
from db.database import save_user


class SaveUserMenu(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.saveuser_menu = Ui_save_menu()
        self.saveuser_menu.setupUi(self)

        self.saveuser_menu.register_button.clicked.connect(self.save)

    def save(self):
        print(self.saveuser_menu.authority_combobox.currentText())
        save_user(self.saveuser_menu.username_box.text(), self.saveuser_menu.username_box.text(), today= None, authority=self.saveuser_menu.authority_combobox.currentText(), confirmation= 0)