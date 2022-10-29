from PyQt5.QtWidgets import *
from design.user_list_menu_design import Ui_user_list
from datetime import date
from db.database import get_all_data_for_table, update_data, get_salt

import bcrypt


class UserListPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.userlist_menu = Ui_user_list()
        self.userlist_menu.setupUi(self)

        self.userlist_menu.start_date.setDate(date.today())
        self.userlist_menu.end_date.setDate(date.today())
        self.update_list()
        self.userlist_menu.list_button.clicked.connect(self.update_list)
        self.userlist_menu.update_db_button.clicked.connect(self.update_user_data)

    def update_list(self):
        self.userlist_menu.tableWidget.setRowCount(0)
        self.userlist_menu.database_userID_combobox.clear()
        self.result = get_all_data_for_table()
        for row_number, row_data in enumerate(self.result):
            self.userlist_menu.tableWidget.insertRow(row_number)
            self.userlist_menu.tableWidget.setItem(row_number, 0, QTableWidgetItem(str(row_data[0])))  # id
            self.userlist_menu.tableWidget.setItem(row_number, 1, QTableWidgetItem(str(row_data[1])))  # name
            self.userlist_menu.tableWidget.setItem(row_number, 2, QTableWidgetItem(str(row_data[3])))  # register date
            self.userlist_menu.tableWidget.setItem(row_number, 3, QTableWidgetItem(str(row_data[4])))  # confirm date
            self.userlist_menu.tableWidget.setItem(row_number, 4, QTableWidgetItem(str(row_data[5])))  # authority

            self.userlist_menu.database_userID_combobox.insertItem(row_number, str(row_data[0]))

    def update_user_data(self):
        userID = self.userlist_menu.database_userID_combobox.currentText()

        if self.userlist_menu.update_username_box.text() != "":
            self.update_user_name(userID)
        if self.userlist_menu.update_password_box.text() != "":
            self.update_user_password(userID)
        self.update_user_confirmation(userID)
        self.update_user_authority(userID)

        self.update_list()

    def update_user_name(self, userID):
        username = self.userlist_menu.update_username_box.text()
        if username != "":
            update_data(userID=int(userID), column_name="userName", data=str(username))

    def update_user_password(self, userID):
        password = self.userlist_menu.update_password_box.text()
        if password != "":
            salt = get_salt(userID)
            utf_pw = password.encode("utf-8")
            hashed_pw = str(bcrypt.hashpw(utf_pw, salt))
            update_data(userID=int(userID), column_name="userPassword", data=str(hashed_pw))

    def update_user_confirmation(self, userID):
        confirm = self.userlist_menu.update_confirmation_combobox.currentText()
        if int(confirm) == 1:
            today = date.today()
            update_data(userID=str(userID), column_name="userConfirmed", data=int(confirm))
            update_data(userID=str(userID), column_name="userConfirmDate", data=today)
        else:
            update_data(userID=str(userID), column_name="userConfirmed", data=int(confirm))

    def update_user_authority(self, userID):
        authority = self.userlist_menu.update_authority_combobox.currentText()
        if authority != "":
            update_data(userID=str(userID), column_name="userAuthority", data=str(authority))