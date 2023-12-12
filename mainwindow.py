# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1017, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toggle_theme_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.toggle_theme_btn.setFont(font)
        self.toggle_theme_btn.setObjectName("toggle_theme_btn")
        self.horizontalLayout.addWidget(self.toggle_theme_btn)
        self.pep8_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pep8_btn.setFont(font)
        self.pep8_btn.setObjectName("pep8_btn")
        self.horizontalLayout.addWidget(self.pep8_btn)
        self.run_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.run_btn.setFont(font)
        self.run_btn.setObjectName("run_btn")
        self.horizontalLayout.addWidget(self.run_btn)
        self.paste_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.paste_btn.setFont(font)
        self.paste_btn.setObjectName("paste_btn")
        self.horizontalLayout.addWidget(self.paste_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.timeout_sb = QtWidgets.QSpinBox(self.centralwidget)
        self.timeout_sb.setMinimum(10)
        self.timeout_sb.setMaximum(250)
        self.timeout_sb.setSingleStep(40)
        self.timeout_sb.setObjectName("timeout_sb")
        self.horizontalLayout.addWidget(self.timeout_sb)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.correct_tw = QtWidgets.QTabWidget(self.centralwidget)
        self.correct_tw.setObjectName("correct_tw")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.correct_code_pte = QtWidgets.QPlainTextEdit(self.tab)
        self.correct_code_pte.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.correct_code_pte.setFont(font)
        self.correct_code_pte.setObjectName("correct_code_pte")
        self.horizontalLayout_2.addWidget(self.correct_code_pte)
        self.correct_tw.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.correct_code_tv = QtWidgets.QTableView(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.correct_code_tv.setFont(font)
        self.correct_code_tv.setObjectName("correct_code_tv")
        self.horizontalLayout_3.addWidget(self.correct_code_tv)
        self.correct_tw.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.correct_tw)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rb0 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb0.setObjectName("rb0")
        self.horizontalLayout_4.addWidget(self.rb0)
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_4.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_4.addWidget(self.rb2)
        self.number_cb = QtWidgets.QComboBox(self.centralwidget)
        self.number_cb.setObjectName("number_cb")
        self.number_cb.addItem("")
        self.number_cb.addItem("")
        self.number_cb.addItem("")
        self.number_cb.addItem("")
        self.number_cb.addItem("")
        self.number_cb.addItem("")
        self.number_cb.addItem("")
        self.horizontalLayout_4.addWidget(self.number_cb)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.part_cb = QtWidgets.QComboBox(self.centralwidget)
        self.part_cb.setObjectName("part_cb")
        self.part_cb.addItem("")
        self.part_cb.addItem("")
        self.part_cb.addItem("")
        self.part_cb.addItem("")
        self.horizontalLayout_4.addWidget(self.part_cb)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.explanation_pte = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.explanation_pte.setFont(font)
        self.explanation_pte.setObjectName("explanation_pte")
        self.verticalLayout.addWidget(self.explanation_pte)
        self.copy_answer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copy_answer_btn.setEnabled(True)
        self.copy_answer_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.copy_answer_btn.setFont(font)
        self.copy_answer_btn.setObjectName("copy_answer_btn")
        self.verticalLayout.addWidget(self.copy_answer_btn)
        self.my_answer_pte = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.my_answer_pte.setMaximumSize(QtCore.QSize(16777215, 600))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.my_answer_pte.setFont(font)
        self.my_answer_pte.setObjectName("my_answer_pte")
        self.verticalLayout.addWidget(self.my_answer_pte)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.correct_output_lb = QtWidgets.QLabel(self.centralwidget)
        self.correct_output_lb.setMaximumSize(QtCore.QSize(1200, 50))
        self.correct_output_lb.setObjectName("correct_output_lb")
        self.verticalLayout_3.addWidget(self.correct_output_lb)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.correct_tw.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Проверка реворд"))
        self.toggle_theme_btn.setText(_translate("MainWindow", "Светлая тема"))
        self.pep8_btn.setText(_translate("MainWindow", "PEP8"))
        self.run_btn.setText(_translate("MainWindow", "Run"))
        self.paste_btn.setText(_translate("MainWindow", "Вставить"))
        self.label_4.setText(_translate("MainWindow", "timeout"))
        self.correct_tw.setTabText(self.correct_tw.indexOf(self.tab), _translate("MainWindow", "Код"))
        self.correct_tw.setTabText(self.correct_tw.indexOf(self.tab_2), _translate("MainWindow", "Строки"))
        self.label_2.setText(_translate("MainWindow", "Объяснение"))
        self.rb0.setText(_translate("MainWindow", "0"))
        self.rb1.setText(_translate("MainWindow", "1"))
        self.rb2.setText(_translate("MainWindow", "2"))
        self.number_cb.setItemText(0, _translate("MainWindow", "9"))
        self.number_cb.setItemText(1, _translate("MainWindow", "17"))
        self.number_cb.setItemText(2, _translate("MainWindow", "22"))
        self.number_cb.setItemText(3, _translate("MainWindow", "24"))
        self.number_cb.setItemText(4, _translate("MainWindow", "26"))
        self.number_cb.setItemText(5, _translate("MainWindow", "27_A"))
        self.number_cb.setItemText(6, _translate("MainWindow", "27_B"))
        self.label.setText(_translate("MainWindow", "Файл"))
        self.part_cb.setItemText(0, _translate("MainWindow", "beta"))
        self.part_cb.setItemText(1, _translate("MainWindow", "easy"))
        self.part_cb.setItemText(2, _translate("MainWindow", "normal"))
        self.part_cb.setItemText(3, _translate("MainWindow", "hard"))
        self.copy_answer_btn.setText(_translate("MainWindow", "Копировать мой ответ"))
        self.correct_output_lb.setText(_translate("MainWindow", "Вывод"))
