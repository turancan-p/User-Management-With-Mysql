from PyQt5.QtWidgets import *
from design.user_list_menu_design import Ui_user_list


class UserListPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.userlist_menu = Ui_user_list()
        self.userlist_menu.setupUi(self)
