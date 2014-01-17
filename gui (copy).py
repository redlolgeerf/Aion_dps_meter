#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
import os
import configparser
from PyQt4 import QtCore
from dps_counter import my_damage_table
import dps_gui

class  Dps_counter(QtGui.QMainWindow, dps_gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Dps_counter, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0, 200)
        self.skillslist.setColumnWidth(0, 200)
        self.skillslist.setColumnWidth(0, 125)
        #self.tableWidget.setColumnWidth(1, 50)
        #self.tableWidget.setColumnWidth(2, 70)
        #self.tableWidget.setColumnWidth(3, 100)
        #self.tableWidget.horizontalHeader().setVisible(True)
        #self.skillslist.horizontalHeader().setVisible(True)
        self.statusBar().showMessage(my_damage_table.file_path)
        self.connectActions()

    def connectActions(self):
        self.anal_button.clicked[bool].connect(self.recalculate)
        self.delButton.clicked[bool].connect(self.deleteFile)
        self.combo.activated[str].connect(self.onActivated)
        self.open_file.triggered.connect(self.openFile)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+D"), self, self.deleteFile)
        self.open_file.setShortcut('Ctrl+O')


    def main(self):
        self.show()


    def onActivated(self, text):
        character = text
        self.fillSkillsList(character)


    def fillSkillsList(self, character=None):
        if my_damage_table.damage_dealt:
            i = 0
            skills = sorted(my_damage_table.damage_dealt[character])
            self.skillslist.setRowCount(len(skills))
            for skill in skills:
                if skill != 'total_damage':
                    damage = my_damage_table.damage_dealt[character][skill][0]
                    strikes = my_damage_table.damage_dealt[character][skill][1]
                    for x in range(4):
                        item = QtGui.QTableWidgetItem()
                        #self.skillslist.setItem(i, x, item)
                    for x, value in zip(list(range(4)), (skill,
                    damage, strikes, int(damage / strikes))):
                        item = QtGui.QTableWidgetItem()
                        item.setData(QtCore.Qt.DisplayRole, value)
                        self.skillslist.setItem(i, x, item)

                    i += 1

            damage = my_damage_table.damage_dealt[character]['total_damage'][0]
            strikes = my_damage_table.damage_dealt[character]['total_damage'][1]

            for x, value in zip(list(range(4)), ('Всего', damage, strikes, int(damage / strikes))):
                    item = QtGui.QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, value)
                    self.skillslist.setItem(i, x, item)


    def fillCharacterList(self):
        if my_damage_table.damage_dealt:
            i = 0
            characters = sorted(my_damage_table.damage_dealt.keys())
            self.tableWidget.setRowCount(len(characters))
            for character_ in characters:
                damage = my_damage_table.damage_dealt[character_]['total_damage'][0]
                time = int((my_damage_table.timing[character_]['ended'] -
                my_damage_table.timing[character_]['started']).total_seconds())
                if time:
                    dps = int(damage / time)
                else:
                    dps = damage
                crit = 0
                if my_damage_table.crites.get(character_):
                    if my_damage_table.crites.get(character_).get('crit'):
                        crit = int(my_damage_table.crites[character_]['crit'] /
                        my_damage_table.crites[character_]['strikes'] * 100)
                for x, value in zip(list(range(4)), (character_, damage, dps, crit)):
                    item = QtGui.QTableWidgetItem()
                    item.setData(QtCore.Qt.DisplayRole, value)
                    self.tableWidget.setItem(i, x, item)

                i += 1


    def fillcombo(self):
        self.combo.clear()
        if my_damage_table.damage_dealt:
            for character_ in sorted(my_damage_table.damage_dealt.keys()):
                self.combo.addItem(character_)


    def openFile(self):
        file_path = QtGui.QFileDialog.getOpenFileName(self,
        'Open file', '/home/eyeinthebrick/Python/dps')
        my_damage_table.file_path = file_path
        self.statusBar().showMessage(my_damage_table.file_path)


    def deleteFile(self):
        with open(my_damage_table.file_path, 'w') as f:
            f.write('')


    def recalculate(self):
        if not my_damage_table.read_file():
            reply = QtGui.QMessageBox.question(self, 'Не найден лог файл',
            "Хотите выбрать лог файл?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.openFile()
                self.recalculate()
        else:
            my_damage_table.fill_table()
            if not my_damage_table.damage_dealt:
                QtGui.QMessageBox.information(self, 'Лог файл пуст',
                "Лог файл пуст", QtGui.QMessageBox.Ok)
                return

            character = sorted(my_damage_table.damage_dealt.keys())[0]
            self.fillcombo()
            self.fillSkillsList(character)
            self.fillCharacterList()

    class my_configs(configparser.ConfigParser()):

        def __init__(self):
            pass

        def read_config(self):
            if os.path.exists('config.ini'):
                self.read('config.ini')
            else:
                self['path'] = '/home/eyeinthebrick/Python/dps/Chat.log'
		self.write_config()


        def write_config(self):
            with open('config.ini', 'w') as configfile:
                self.write(configfile)


if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    Dps_counter = Dps_counter()
    Dps_counter.main()
    app.exec_()

#переделать вторую вкладку в таблицу
