from PyQt5.QtWidgets import *
from design.main_menu_design import Ui_MainWindow
from db.database import get_data_for_table


class MainPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_menu = Ui_MainWindow()
        self.main_menu.setupUi(self)

    def get_data(self):
        self.main_menu.account_active_table.setRowCount(0)
        self.result = get_data_for_table(1)
        for row_number, row_data in enumerate(self.result):
            self.main_menu.account_active_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number != 2:
                    if column_number > 2:
                        column_number -= 1
                    self.main_menu.account_active_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.result2 = get_data_for_table(0)
        for row_number2, row_data in enumerate(self.result2):
            self.main_menu.account_waiting_list.insertRow(row_number2)
            for column_number2, data in enumerate(row_data):
                if column_number2 != 2:
                    if column_number2 > 2:
                        column_number2 -= 1
                        print(data)
                    self.main_menu.account_waiting_list.setItem(row_number2, column_number2, QTableWidgetItem(str(data)))
