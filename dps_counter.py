#!/usr/bin/env python3.3
from patterns import rules
from patterns import oddskills
import re
from datetime import datetime
import os


class damage_table():  # lint:ok

    def __init__(self):  # lint:ok
        super(damage_table, self).__init__()
        self.file_path = "/home/eyeinthebrick/Python/dps/logs/test.log"
        self.my_oddskills = oddskills
        #self.fill_table()

    def initialize(self):  # lint:ok
        self.damage_dealt = {}
        self.whose_dot = {}
        self.crites = {}
        self.timing = {}

    def replace_summons(self, character):
        """
        replaces character, so elementals are not separate character
        """
        spirit_master = 'Вы'
        healer = 'Вы'
        if 'элементаль' in character:
            return spirit_master
        if 'Святая мощь' in character:
            return healer
        return character

    def normalize(self, i_tuple):
        """
        just some hacks, so all variables are alike despite the pattern
        """
        date, crit, character, skill, damage, asd = i_tuple  # asd только для ловушек
        if i_tuple[5]:  # пришлось ввести из-за ловушек
            character = i_tuple[5]
        try:
            damage = int(damage.replace('\xa0', ''))
        except:
            damage = 0
        character = self.replace_summons(character)
        if crit is None:
            crit = False
        else:
            crit = True
        if not skill:
            skill = 'Автоатака'
        if not character:
            character = 'Вы'
        date = datetime.strptime(date[:-3], '%Y.%m.%d %H:%M:%S')
        return date, crit, character, skill, damage

    def is_new_dot(self, i, dotPattern):
        """
        put so, in case it would be reasonable to change
        the mechanics of checking for dot
        """
        if (i + 2) <= len(self.dps):
            if self.dps[i + 1].find(dotPattern) > -1:
                return True
        return False

    def assign_dot_owner(self, character, skill):
        """
        remembers, who casted dot
        structure is {skill:character}
        """
        self.whose_dot[skill] = character

    def add_crit_to_crites(self, character, crit):
        """
        stores information on critical strikes
        structure is {character:{strikes:0, crit:0}}
        """
        if character not in self.crites:
            self.crites[character] = {'strikes': 0, 'crit': 0}
        self.crites[character]['strikes'] += 1
        if crit:
            self.crites[character]['crit'] += 1

    def add_damage_to_dealer(self, crit, character, skill, damage):
        """
        stores information on damage dealt
        structure is {character:{skill:[damage_dealt, strikes]}}
        """
        if re.sub('\s[IV]+', '', skill) in self.my_oddskills or damage == 0:
            return
        if skill in self.whose_dot:
            character = self.whose_dot[skill]
        self.add_crit_to_crites(character, crit)
        if character not in self.damage_dealt:
            self.damage_dealt[character] = {skill: [0, 0], 'total_damage': [0, 0]}
        if skill not in self.damage_dealt[character]:
            self.damage_dealt[character][skill] = [0, 0]
        self.damage_dealt[character][skill][0] += damage
        self.damage_dealt[character][skill][1] += 1
        self.damage_dealt[character]['total_damage'][0] += damage
        self.damage_dealt[character]['total_damage'][1] += 1

    def add_timing(self, date, character):
        """
        stores information on start and end
        structure is {character:{started:0, ended:0}}
        """
        if character not in self.timing:
            self.timing[character] = {'started': date, 'ended': date}
        else:
            self.timing[character]['ended'] = date

    def read_file(self):  # lint:ok
        self.dps = []
        if not os.path.exists(self.file_path):
            print('incorrect path')
            return False
        for encoding_ in ('utf-8', 'cp1251'):
            try:
                with open(self.file_path, 'r', encoding=encoding_) as f:
                    for line in f:
                        self.dps.append(line.rstrip())
                return True
            except:
                pass
        return False

    def fill_table(self):  # lint:ok
        self.initialize()

        i = 0
        for i in range(0, len(self.dps)):
            if i == 0:
                prev_line = ''
                this_line = self.dps[i]
            if (i + 1) == len(self.dps):
                next_line = ''
            else:
                next_line = self.dps[i + 1]
            for find_rule, apply_rule in rules:
                parsed_string = find_rule(this_line)
                if parsed_string:
                    date, crit, character, skill, damage, is_dot = \
                    apply_rule(prev_line, parsed_string, next_line)
                    if is_dot:
                        self.assign_dot_owner(character, skill)
                    self.add_damage_to_dealer(crit, character, skill, damage)
                    self.add_timing(date, character)
                    break
            prev_line, this_line = this_line, next_line
        return True


def test1(table_for_test):  # lint:ok
    test_damage_dealt = {'Basota': {'total_damage': [2200, 2], 'Ожог V': [2200, 2]},
    'CrazyRussian': {'total_damage': [1988, 1], 'Автоатака': [1988, 1]}, 'Вы':
     {'total_damage': [1105, 2], 'Автоатака': [729, 1], 'Ослабляющее клеймо I': [376, 1]},
     'PLAYGUN': {'total_damage': [3915, 1],
     'Прицельный огонь IV': [3915, 1]}, 'Симпапушка': {'Жалящая стрела III': [2623, 1],
     'total_damage': [2623, 1]}, 'InvisiblEDeviL': {'Песчаная ловушка III': [64, 1],
     'total_damage': [64, 1]},
     'Арабэла': {'Клятва ветра I': [358, 1], 'total_damage': [358, 1]}}
    if table_for_test == test_damage_dealt:
        return True
    return False

my_damage_table = damage_table()

if __name__ == '__main__':
    my_damage_table.read_file()
    my_damage_table.fill_table()
    total = 0
    for character in my_damage_table.damage_dealt:
        total += my_damage_table.damage_dealt[character]['total_damage'][0]
    print(test1(my_damage_table.damage_dealt))
    print(my_damage_table.damage_dealt)
    #print(total)
