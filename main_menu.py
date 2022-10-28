from PyQt5.QtWidgets import *
from design.main_menu_design import Ui_MainWindow
from db.database import get_data_for_table

from user_list_menu import UserListPage
from add_new_user_menu import SaveUserMenu


class MainPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_menu = Ui_MainWindow()
        self.main_menu.setupUi(self)

        self.userlist_and_update_menu = UserListPage()
        self.addnewuser_menu = SaveUserMenu()

        self.main_menu.account_add_button.clicked.connect(self.adduser_menu)
        self.main_menu.account_update_button.clicked.connect(self.user_list_menu)

    def user_list_menu(self):
        self.userlist_and_update_menu.show()

    def adduser_menu(self):
        self.addnewuser_menu.show()

    def update_table(self):
        # ACTIVE PANEL
        self.main_menu.account_active_table.setRowCount(0)
        self.result = get_data_for_table(1)
        for row_number, row_data in enumerate(self.result):
            self.main_menu.account_active_table.insertRow(row_number)
            self.main_menu.account_active_table.setItem(row_number, 0, QTableWidgetItem(str(row_data[0])))  # id
            self.main_menu.account_active_table.setItem(row_number, 1, QTableWidgetItem(str(row_data[1])))  # name
            self.main_menu.account_active_table.setItem(row_number, 2,
                                                        QTableWidgetItem(str(row_data[3])))  # register date
            self.main_menu.account_active_table.setItem(row_number, 3,
                                                        QTableWidgetItem(str(row_data[4])))  # confirm date
            self.main_menu.account_active_table.setItem(row_number, 4, QTableWidgetItem(str(row_data[5])))  # authority
        # WAITING PANEL
        self.main_menu.account_waiting_list.setRowCount(0)
        self.result = get_data_for_table(0)
        for row_number, row_data in enumerate(self.result):
            self.main_menu.account_waiting_list.insertRow(row_number)
            self.main_menu.account_waiting_list.setItem(row_number, 0, QTableWidgetItem(str(row_data[0])))  # id
            self.main_menu.account_waiting_list.setItem(row_number, 1, QTableWidgetItem(str(row_data[1])))  # name
            self.main_menu.account_waiting_list.setItem(row_number, 2,
                                                        QTableWidgetItem(str(row_data[3])))  # register date
