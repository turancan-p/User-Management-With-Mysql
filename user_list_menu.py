from PyQt5.QtWidgets import *
from design.user_list_menu_design import Ui_user_list
from datetime import date
from db.database import get_all_data_for_table


class UserListPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.userlist_menu = Ui_user_list()
        self.userlist_menu.setupUi(self)

        self.userlist_menu.start_date.setDate(date.today())
        self.userlist_menu.end_date.setDate(date.today())
        self.update_list()
        self.userlist_menu.list_button.clicked.connect(self.update_list)

    def update_list(self):
        self.userlist_menu.tableWidget.setRowCount(0)
        self.result = get_all_data_for_table()
        for row_number, row_data in enumerate(self.result):
            self.userlist_menu.tableWidget.insertRow(row_number)
            self.userlist_menu.tableWidget.setItem(row_number, 0, QTableWidgetItem(str(row_data[0])))  # id
            self.userlist_menu.tableWidget.setItem(row_number, 1, QTableWidgetItem(str(row_data[1])))  # name
            self.userlist_menu.tableWidget.setItem(row_number, 2, QTableWidgetItem(str(row_data[3])))  # register date
            self.userlist_menu.tableWidget.setItem(row_number, 3, QTableWidgetItem(str(row_data[4])))  # confirm date
            self.userlist_menu.tableWidget.setItem(row_number, 4, QTableWidgetItem(str(row_data[5])))  # authority

            self.userlist_menu.database_userID_combobox.insertItem(row_number, str(row_data[0]))