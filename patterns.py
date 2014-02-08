# -*- coding: utf-8 -*-

from datetime import datetime
import re


oddskills = ('Усиление магического взрыва', 'Резкий свист', 'Обширная коррозия')
not_ctit = ('Применение смертельных ядов', 'Отравленный клинок', 'умение Стойка налетчика',
'умение Готовность', 'Усмирение', 'Туманная завеса')

blankgroupPattern = r'()'
blankPattern = r''
datePattern = r'^([\d.:\s]{22})'                  # дата и время вида '2013.12.15 19:55:14 : '
critPattern = r'''(Критический \s удар\!)?\s?'''  # проверка на крит

pattern = datePattern + critPattern
# имя персонажа
chrnamePattern = r'''(\w+)\s'''
slfnamePattern = r'''(Вы)\s'''

chrskillusagePattern = r'''использует \:? \s'''

skillnamePattern = r'''([\w\s]+ \s [IV]+) \.'''   # название скилла с точкой на конце
skillnamePattern2 = r'''([\w\s]+ \s [IV]+) \:'''  # название скилла с двоеточием на конце

receiverPattern = r'''.+ получает \s'''
damageamountPattern = r'''(\d+\s?\d*)\s?          # количество урона
                          ед\. \s урона'''        # ед. урона

targetPattern = r'''\s(.+)'''
slftargetPattern = r'''\s цели \s (.+) \.'''         # парсим цель

def normalize(date, crit, damage):
    """
    just some hacks, so all variables are alike despite the pattern
    """
    #date, crit, character, skill, damage, asd = i_tuple  # asd только для ловушек
    #if i_tuple[5]:  # пришлось ввести из-за ловушек
        #character = i_tuple[5]
    try:
        damage = int(damage.replace('\xa0', ''))
    except:
        damage = 0
    #character = self.replace_summons(character)
    if crit is None:
        crit = False
    else:
        crit = True
    date = datetime.strptime(date[:-3], '%Y.%m.%d %H:%M:%S')
    return date, crit, damage


def chr_skill(line):
    '''проверяет использование скилла другим персонажем
    пример : 2014.01.11 23:22:53 : PLAYGUN использует:
    Прицельный огонь IV. Разгневанный Сунаяка получает 3 915 ед. урона.'''
    dpsPattern = pattern + chrnamePattern + chrskillusagePattern + \
    skillnamePattern + targetPattern + receiverPattern + damageamountPattern
    return re.search(dpsPattern, line, re.VERBOSE)


def apply_chr_skill(prev_line, parsed_line, next_line):  # lint:ok
    date, crit, character, skill, target, damage = parsed_line.groups()
    chrdotPattern = 'постоянно получает урон'
    if next_line.find(chrdotPattern) > -1:
        is_dot = True
    else:
        is_dot = False
    date, crit, damage = normalize(date, crit, damage)
    return date, crit, character, skill, damage, is_dot, target


def chr_atack(line):
    '''проверяет автоатаку другого персонажа
    пример : 2014.01.11 23:22:53 : CrazyRussian наносит 1 988 ед. урона цели Разгневанный Сунаяка.
    '''
    chratackPattern = r'''наносит \s'''
    dpsPattern = pattern + chrnamePattern + chratackPattern + damageamountPattern + slftargetPattern
    return re.search(dpsPattern, line, re.VERBOSE)


def apply_chr_atack(prev_line, parsed_line, next_line):  # lint:ok
    date, crit, character, damage, target = parsed_line.groups()
    skill = 'Автоатака'
    is_dot = False
    date, crit, damage = normalize(date, crit, damage)
    return date, crit, character, skill, damage, is_dot, target


def slf_atack(line):
    '''проверяет на вашу автоатаку
    пример : 2014.01.11 23:22:53 : Вы нанесли 729 ед. урона цели Разгневанный Сунаяка.'''
    slfatackPattern = r'''нанесли \s'''
    dpsPattern = pattern + slfnamePattern + slfatackPattern + damageamountPattern + slftargetPattern
    return re.search(dpsPattern, line, re.VERBOSE)


def apply_slf_atack(prev_line, parsed_line, next_line):  # lint:ok
    date, crit, character, damage, target = parsed_line.groups()
    skill = 'Автоатака'
    is_dot = False
    date, crit, damage = normalize(date, crit, damage)
    return date, crit, character, skill, damage, is_dot, target


def slf_skill(line):
    """проверяет использование скилла (персонаж=Вы)
    пример : 2014.01.11 23:22:55 : Ослабляющее клеймо I:
    Разгневанный Сунаяка получает 376 ед. урона.
    так же подходит к дотам
    пример: 2014.01.11 23:22:58 : Ожог V: Разгневанный Сунаяка получает 1 155 ед. урона."""
    dpsPattern = pattern + skillnamePattern2 + targetPattern + receiverPattern + damageamountPattern
    return re.search(dpsPattern, line, re.VERBOSE)


def apply_slf_skill(prev_line, parsed_line, next_line):  # lint:ok
    date, crit, skill, target, damage = parsed_line.groups()
    character = 'Вы'
    slfdotPattern = 'получает продолжительный урон'
    if next_line.find(slfdotPattern) > -1:
        is_dot = True
    else:
        is_dot = False
    date, crit, damage = normalize(date, crit, damage)
    return date, crit, character, skill, damage, is_dot, target


def trap(line):
    '''проверяет использование ловушки
    пример : 2013.12.15 20:13:32 : Песчаная ловушка III:
    появляется Песчаная ловушка персонажа InvisiblEDeviL.'''
    trpappearPattern = r'''\s появляется \s .+'''
    chrPattern = r'''персонажа \s'''
    chrnamePattern2 = r'''(\w+)\.'''
    dpsPattern = pattern + skillnamePattern2 + trpappearPattern + chrPattern + \
    chrnamePattern2
    return re.search(dpsPattern, line, re.VERBOSE)


def apply_trap(prev_line, parsed_line, next_line):  # lint:ok
    date, crit, skill, character = parsed_line.groups()
    damage = 0
    is_dot = True
    target = 'All'
    date, crit, damage = normalize(date, crit, damage)
    return date, crit, character, skill, damage, is_dot, target


def odd_skill(line):
    '''проверяет использование бафов на дамаг
    пример : 2013.12.15 20:06:56 : Арабэла использует: Клятва ветра I. '''
    dpsPattern = pattern + chrnamePattern + chrskillusagePattern + skillnamePattern
    return re.search(dpsPattern, line, re.VERBOSE)


def apply_odd_skill(prev_line, parsed_line, next_line):  # lint:ok
    date, crit, character, skill = parsed_line.groups()
    damage = 0
    is_dot = True
    target = 'All'
    date, crit, damage = normalize(date, crit, damage)
    return date, crit, character, skill, damage, is_dot, target


rules = (
    (chr_skill, apply_chr_skill),
    (chr_atack, apply_chr_atack),
    (slf_atack, apply_slf_atack),
    (slf_skill, apply_slf_skill),
    (trap, apply_trap),
    (odd_skill, apply_odd_skill)
    )

#dpsPatterns = (  # patter structure is (date)(crit)(character name)(skill)(damage_dealt)(trap)
    ##(r'''                        #проверяет на элементаля/святую мощь
    ##^([\d.:\s]{22})              #дата и время вида '2013.12.15 19:55:14 : '
    ##(Критический \s удар\!)?\s?  #проверка на крит
    ##(\w+\s\w+)\s                 #имя персонажа
    ##использует \:? \s            #наносит/использует
    ##([\w\s\:]+ \s [IV]+)         #название скилла
    ##.+ получает \s
    ##(\d+\s?\d*)\s?               #количество урона
    ##ед\. \s урона                #ед. урона
    ##()
    ##''', True, 'постоянно получает урон'),


    ###(r'''                        #проверяет использование сжечь чары другим персонажем
    ##^([\d.:\s]{22})              #дата и время вида '2013.12.15 19:55:14 : '
    ##(Критический \s удар\!)?\s?  #проверка на крит
    ##(\w+)\s                      #имя персонажа
    ##использует \:? \s            #наносит/использует
    ##([\w\s]+ \s [IV]+) \.        #название скилла
    ##.+ получает \s
    ##(\d+\s?\d*)\s?               #количество урона
    ##ед\. \s урона                #ед. урона
    ##и лишается магического усиления
    ##()
    ##''', True, '')
    #)