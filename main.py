 #!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
import configparser
import os
from PyQt4 import QtCore
from dps_counter import my_damage_table
from dps_counter import test1
import dps_gui


class DpsCounter(QtGui.QMainWindow, dps_gui.Ui_MainWindow):
    """main class"""
    def __init__(self, parent=None):
        super(DpsCounter, self).__init__(parent)
        self.setupUi(self)
        self.ui_setup()
        self.config = configparser.ConfigParser()
        self.read_config()
        self.apply_config()
        self.statusBar().showMessage(my_damage_table.file_path)
        self.connect_actions()

    def ui_setup(self):
        """
        just some hacks to compensate qt designer
        """
        self.tableWidget.setColumnWidth(0, 200)
        self.skillslist.setColumnWidth(0, 300)
        self.skillslist.setColumnWidth(1, 125)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.skillslist.horizontalHeader().setVisible(True)

    def read_config(self):
        """function that reads or creates config"""
        if not os.path.exists('config.ini'):
            self.initiate_config()
            self.save_config()
        else:
            self.config.read('config.ini')

    def save_config(self):
        """just to be shorter"""
        with open('config.ini', 'w+') as configfile:
            self.config.write(configfile)

    def initiate_config(self):
        """default config"""
        self.config['DEFAULT'] = {"Path": '/home/eyeinthebrick/Python/dps/Chat.log'}
        self.config['DEFAULT_ODDSKILLS'] = {}
        for skill in ('Усиление магического взрыва', 'Резкий свист', 'Обширная коррозия'):
            self.config['DEFAULT_ODDSKILLS'][skill] = '1'

    def apply_config(self):
        """assigns config to variables"""
        my_damage_table.file_path = self.config['DEFAULT']['Path']
        my_damage_table.my_oddskills = []
        for skill in self.config['DEFAULT_ODDSKILLS']:
            if self.config['DEFAULT_ODDSKILLS'][skill] == 1:
                my_damage_table.my_oddskills.append(skill)

    def connect_actions(self):
        """connect actions to slots"""
        self.anal_button.clicked[bool].connect(self.recalculate)
        self.delButton.clicked[bool].connect(self.delete_file)
        self.combo.activated[str].connect(self.on_activated)
        self.open_file.triggered.connect(self.open_file_dialog)
        # hot keys
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+D"), self, self.delete_file)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+В"), self, self.delete_file)  # for Russian
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+O"), self, self.open_file_dialog)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Щ"), self, self.open_file_dialog)  # for Russian
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+G"), self, self.recalculate)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+П"), self, self.recalculate)  # for Russian
        self.tableWidget.customContextMenuRequested.connect(self.handle_table_menu)

    def handle_table_menu(self, pos):
        """context menu for charactertable"""
        self.menu = QtGui.QMenu(self)
        show_detail = QtGui.QAction('Детали', self)
        self.menu.addAction(show_detail)
        index = self.tableWidget.indexAt(pos)
        if index.row() > -1:
            action = self.menu.exec_(QtGui.QCursor.pos())
            if action == show_detail:
                self.show_detail(index.row())
        return

    def show_detail(self, row):
        """action for character table context menu, switches to detail tab"""
        characters = sorted(my_damage_table.damage_dealt.keys())
        character = self.tableWidget.item(row, 0).text()
        self.fill_skills_list(character)
        self.combo.setCurrentIndex(characters.index(character))
        self.tabWidget.setCurrentIndex(1)

    def main(self):  # lint:ok
        self.show()

    def on_activated(self, text):
        """when combo box is touched skills list is amended"""
        character = text
        self.fill_skills_list(character)

    def fill_skills_list(self, character=None):
        """just fills skills list"""
        if my_damage_table.damage_dealt:
            i = 0
            skills = sorted(my_damage_table.damage_dealt[character])
            self.skillslist.setSortingEnabled(False)
            self.skillslist.setRowCount(len(skills))
            for skill in skills:
                if skill != 'total_damage':
                    damage = my_damage_table.damage_dealt[character][skill][0]
                    strikes = my_damage_table.damage_dealt[character][skill][1]
                    commit = damage / my_damage_table\
                        .damage_dealt[character]['total_damage'][0] * 100
                    for x, value in zip(list(range(5)), (skill,
                                        damage, strikes, int(damage / strikes), commit)):
                        item = QtGui.QTableWidgetItem()
                        item.setData(QtCore.Qt.DisplayRole, value)
                        self.skillslist.setItem(i, x, item)

                    i += 1

            damage = my_damage_table.damage_dealt[character]['total_damage'][0]
            strikes = my_damage_table.damage_dealt[character]['total_damage'][1]

            for x, value in zip(list(range(5)), ('Всего', damage, strikes,
                                int(damage / strikes), 100)):
                item = QtGui.QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, value)
                self.skillslist.setItem(i, x, item)
            self.skillslist.setSortingEnabled(True)

    def fill_character_list(self):
        """just fills character list"""
        if my_damage_table.damage_dealt:
            i = 0
            if not test1(my_damage_table.damage_dealt):
                print("test1 failed")
                print(my_damage_table.damage_dealt)
            characters = sorted(my_damage_table.damage_dealt.keys())
            self.tableWidget.setSortingEnabled(False)
            self.tableWidget.setRowCount(len(characters))
            self.tableWidget.clearContents()
            if my_damage_table.damage_dealt.get('Вы'):
                self.fill_character_row('Вы', i)
                i += 1
            for character_ in characters:
                if character_ != 'Вы':
                    self.fill_character_row(character_, i)
                    i += 1
            self.tableWidget.setSortingEnabled(True)
        return

    def fill_character_row(self, character, i):
        """to allow tailor filling of the table"""
        damage = my_damage_table.damage_dealt[character]['total_damage'][0]
        total_all = 0
        for character_ in my_damage_table.damage_dealt:
            total_all += my_damage_table.damage_dealt[character_]['total_damage'][0]
        commit = (damage / total_all * 100)
        times = int((my_damage_table.timing[character]['ended'] -
                    my_damage_table.timing[character]['started']).total_seconds())
        if times:
            dps = int(damage / times)
        else:
            dps = damage
        crit = 0
        if my_damage_table.crites.get(character):
            if my_damage_table.crites.get(character).get('crit'):
                crit = int(my_damage_table.crites[character]['crit'] /
                my_damage_table.crites[character]['strikes'] * 100)
        for x, value in zip(list(range(6)), (character, damage, commit,
                            dps, crit, self.time_convert(times))):
            item = QtGui.QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole, value)
            if character == 'Вы':
                item.setBackground(QtGui.QColor(255, 200, 35))
            self.tableWidget.setItem(i, x, item)
        return

    def time_convert(self, time, *args):
        """takes time and converts it in words with right endings"""
        minutes = int(time / 60) if time > 0 else 0
        seconds = time - 60 * minutes
        if minutes % 20 == 1:
            mending = 'а'
        elif 1 < minutes % 20 < 5:
            mending = 'ы'
        else:
            mending = ''
        if minutes:
            minutes = '%d минут%s' % (minutes, mending)
        else:
            minutes = ''
        if seconds < 21:
            d = 20
        else:
            d = 10
        if seconds % d == 1:
            sending = 'у'
        elif 1 < seconds % d < 5:
            sending = 'а'
        else:
            sending = ''
        if seconds:
            seconds = '%d секунд%s' % (seconds, sending)
        else:
            seconds = ''
        return ('%s, %s' % (minutes, seconds) if (minutes and seconds)
                else '%s%s' % (minutes, seconds))

    def fill_combo(self):
        """fills combo with all characters"""
        self.combo.clear()
        if my_damage_table.damage_dealt:
            for character_ in sorted(list(my_damage_table.damage_dealt.keys()), key=str.lower):
                self.combo.addItem(character_)

    def open_file_dialog(self):
        """a dialog box to open log file"""
        self.config['DEFAULT']['Path'] = QtGui.QFileDialog.getOpenFileName(self,
                                        'Open file', '/home/eyeinthebrick/Python/dps')
        self.apply_config()
        self.save_config()
        self.statusBar().showMessage(my_damage_table.file_path)

    def delete_file(self):
        """just to be short"""
        with open(my_damage_table.file_path, 'w', encoding='cp1251') as f:
            f.write('')
        self.tableWidget.setRowCount(0)

    def recalculate(self):
        """recalculates all values in my_damage_table based on data from opened file"""
        self.anal_button.setText('Считаю')
        if not my_damage_table.read_file():
            reply = QtGui.QMessageBox.question(self, 'Не найден лог файл',
                                               "Хотите выбрать лог файл?", QtGui.QMessageBox.Yes |
                                                QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.open_file_dialog()
                self.recalculate()
        else:
            #print('threading!')
            self.threadPool = []
            self.threadPool.append(FillingThread())
            self.threadPool[len(self.threadPool) - 1].start()

            #thread = FillingThread()
            #thread.trigger.connect(self.continue_recalculate)
            #thread.start()

            self.go = True
            self.progressBar.setRange(0, 0)
            while self.go:  # dirty hack, change to something more safe
                QtGui.QApplication.processEvents()
            self.progressBar.setRange(0, 1)
            self.anal_button.setText('Посчитать')
            #print('continuing!')
            if not my_damage_table.damage_dealt:
                QtGui.QMessageBox.information(self, 'Лог файл пуст',
                                                "Лог файл пуст", QtGui.QMessageBox.Ok)
                return

            character = sorted(my_damage_table.damage_dealt.keys(), key=str.lower)[0]
            self.fill_combo()
            self.fill_skills_list(character)
            self.fill_character_list()


class FillingThread(QtCore.QThread):
    """thead to calculate"""
    def __init__(self):  # lint:ok
        QtCore.QThread.__init__(self)

    def run(self):  # lint:ok
        my_damage_table.fill_table()
        Dps_counter.go = False

    def __del__(self):
        """implemented, so the tread is not destroyed by garbage collector,
        while working"""
        self.wait()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Dps_counter = DpsCounter()
    Dps_counter.main()
    app.exec_()
