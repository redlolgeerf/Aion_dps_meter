# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sun Feb  2 13:55:55 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(891, 652)
        self.centralwidget = QtGui.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 611))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab_1)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayoutWidget = QtGui.QWidget(self.tab_1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(530, 0, 361, 581))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        spacerItem = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtGui.QFormLayout.LabelRole, spacerItem)
        self.anal_button = QtGui.QPushButton(self.formLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anal_button.sizePolicy().hasHeightForWidth())
        self.anal_button.setSizePolicy(sizePolicy)
        self.anal_button.setObjectName(_fromUtf8("anal_button"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.anal_button)
        self.progressBar = QtGui.QProgressBar(self.formLayoutWidget)
        self.progressBar.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(1)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.progressBar)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtGui.QFormLayout.FieldRole, spacerItem1)
        self.delButton = QtGui.QPushButton(self.formLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delButton.sizePolicy().hasHeightForWidth())
        self.delButton.setSizePolicy(sizePolicy)
        self.delButton.setObjectName(_fromUtf8("delButton"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.delButton)
        self.tableWidget = QtGui.QTableWidget(self.tab_1)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 531, 579))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setStyleSheet(_fromUtf8(""))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.tab_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 891, 581))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.skillslist = QtGui.QTableWidget(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.skillslist.setFont(font)
        self.skillslist.setAlternatingRowColors(True)
        self.skillslist.setObjectName(_fromUtf8("skillslist"))
        self.skillslist.setColumnCount(4)
        self.skillslist.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.skillslist.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.skillslist.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.skillslist.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.skillslist.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.skillslist.setHorizontalHeaderItem(3, item)
        self.skillslist.horizontalHeader().setVisible(False)
        self.skillslist.horizontalHeader().setDefaultSectionSize(100)
        self.skillslist.horizontalHeader().setSortIndicatorShown(True)
        self.skillslist.horizontalHeader().setStretchLastSection(True)
        self.skillslist.verticalHeader().setVisible(False)
        self.skillslist.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_3.addWidget(self.skillslist)
        spacerItem2 = QtGui.QSpacerItem(140, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.combo = QtGui.QComboBox(self.horizontalLayoutWidget_3)
        self.combo.setMinimumSize(QtCore.QSize(100, 0))
        self.combo.setObjectName(_fromUtf8("combo"))
        self.horizontalLayout_3.addWidget(self.combo)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setToolTip(_fromUtf8(""))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.open_file = QtGui.QAction(MainWindow)
        self.open_file.setObjectName(_fromUtf8("open_file"))
        self.menu.addAction(self.open_file)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.anal_button.setText(_translate("MainWindow", "Посчитать", None))
        self.delButton.setText(_translate("MainWindow", "Очистить лог", None))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Персонаж", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Урон", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Dps", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Крит", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Все", None))
        self.skillslist.setSortingEnabled(True)
        item = self.skillslist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Умение", None))
        item = self.skillslist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Всего урона", None))
        item = self.skillslist.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Кол-во", None))
        item = self.skillslist.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Средний урон", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Детально по персонажу", None))
        self.menu.setTitle(_translate("MainWindow", "Открыть", None))
        self.open_file.setText(_translate("MainWindow", "Открыть", None))

