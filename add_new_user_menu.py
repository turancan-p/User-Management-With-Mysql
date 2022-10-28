from PyQt5.QtWidgets import *
from design.save_user_design import Ui_save_menu


class SaveUserMenu(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.saveuser_menu = Ui_save_menu()
        self.saveuser_menu.setupUi(self)
