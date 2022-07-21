from PySide6.QtCore import QCoreApplication, Qt, QMetaObject
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QLineEdit, QGridLayout, QPushButton


class Ui_MainWindow(object):
    def __init__(self):
         self.lineEdit = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 361)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_division = QPushButton(self.centralwidget)
        self.btn_division.setObjectName(u"btn_division")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_division.sizePolicy().hasHeightForWidth())
        self.btn_division.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_division, 0, 3, 1, 1)

        self.btn_C = QPushButton(self.centralwidget)
        self.btn_C.setObjectName(u"btn_C")
        sizePolicy2.setHeightForWidth(self.btn_C.sizePolicy().hasHeightForWidth())
        self.btn_C.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_C, 0, 1, 1, 1)

        self.btn_multi = QPushButton(self.centralwidget)
        self.btn_multi.setObjectName(u"btn_multi")
        sizePolicy2.setHeightForWidth(self.btn_multi.sizePolicy().hasHeightForWidth())
        self.btn_multi.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_multi, 1, 3, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_0, 5, 1, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_4, 3, 0, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_6, 3, 2, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy2.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_backspace, 0, 2, 1, 1)

        self.btn_equals = QPushButton(self.centralwidget)
        self.btn_equals.setObjectName(u"btn_equals")
        sizePolicy2.setHeightForWidth(self.btn_equals.sizePolicy().hasHeightForWidth())
        self.btn_equals.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_equals, 5, 3, 1, 1)

        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy2.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_dot, 5, 2, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy2.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_plus, 4, 3, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_3, 4, 2, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy2.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_minus, 3, 3, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_2, 4, 1, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_5, 3, 1, 1, 1)

        self.btn_change_value = QPushButton(self.centralwidget)
        self.btn_change_value.setObjectName(u"btn_change_value")
        sizePolicy2.setHeightForWidth(self.btn_change_value.sizePolicy().hasHeightForWidth())
        self.btn_change_value.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_change_value, 5, 0, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setFlat(False)

        self.gridLayout.addWidget(self.btn_1, 4, 0, 1, 1)

        self.btn_CE = QPushButton(self.centralwidget)
        self.btn_CE.setObjectName(u"btn_CE")
        sizePolicy2.setHeightForWidth(self.btn_CE.sizePolicy().hasHeightForWidth())
        self.btn_CE.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_CE, 0, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_multi.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_backspace.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.btn_equals.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_change_value.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
    # retranslateUi

