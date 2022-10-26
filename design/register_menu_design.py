# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_menu(object):
    def setupUi(self, register_menu):
        register_menu.setObjectName("register_menu")
        register_menu.resize(325, 190)
        register_menu.setMinimumSize(QtCore.QSize(325, 190))
        register_menu.setMaximumSize(QtCore.QSize(325, 190))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(12)
        register_menu.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(register_menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(register_menu)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 305, 170))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(145, 20))
        self.label_3.setMaximumSize(QtCore.QSize(145, 20))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.register_button = QtWidgets.QPushButton(self.frame)
        self.register_button.setObjectName("register_button")
        self.gridLayout.addWidget(self.register_button, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.username_box = QtWidgets.QLineEdit(self.frame)
        self.username_box.setMinimumSize(QtCore.QSize(120, 20))
        self.username_box.setMaximumSize(QtCore.QSize(120, 20))
        self.username_box.setObjectName("username_box")
        self.gridLayout.addWidget(self.username_box, 1, 2, 1, 1)
        self.password_box = QtWidgets.QLineEdit(self.frame)
        self.password_box.setMinimumSize(QtCore.QSize(120, 20))
        self.password_box.setMaximumSize(QtCore.QSize(120, 20))
        self.password_box.setObjectName("password_box")
        self.gridLayout.addWidget(self.password_box, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(80, 20))
        self.label_2.setMaximumSize(QtCore.QSize(80, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(80, 20))
        self.label.setMaximumSize(QtCore.QSize(80, 20))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(register_menu)
        QtCore.QMetaObject.connectSlotsByName(register_menu)

    def retranslateUi(self, register_menu):
        _translate = QtCore.QCoreApplication.translate
        register_menu.setWindowTitle(_translate("register_menu", "Register"))
        self.label_3.setText(_translate("register_menu", "Yeni Hesap Oluştur"))
        self.register_button.setText(_translate("register_menu", "Kayıt Ol"))
        self.label_2.setText(_translate("register_menu", "Username"))
        self.label.setText(_translate("register_menu", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_menu = QtWidgets.QWidget()
    ui = Ui_register_menu()
    ui.setupUi(register_menu)
    register_menu.show()
    sys.exit(app.exec_())
