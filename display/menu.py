# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   扑克游戏的控制界面
# ------------------------(max to 80 columns)-----------------------------------

# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   扑克游戏的控制界面
# ------------------------(max to 80 columns)-----------------------------------

import os


def clear_menu():
    '清屏'
    i = os.system("cls")
    return


def dsp_start():
    '显示游戏开始信息'
    clear_menu()
    print('********************************')
    print('* Poker Game Start             *')
    print('*            Produced by Vivian  *')
    print('*            Version 1.0       *')
    print('*            Updated 2019/7    *')
    print('********************************')
    return


def dsp_end():
    '显示游戏结束信息'
    clear_menu()
    print('*********************************')
    print('***       GAME     OVER       ***')
    print('*********************************')
    return


def dsp_choice_game():
    '显示菜单：选择玩法'
    clear_menu()
    print('**********************************')
    print('1 - 玩争上游（54张，不留底）')
    print('2 - 玩桥牌（4人52张，不带大小王）')
    print('3 - 玩 3 人斗地主（54张，留底3张）')
    print('4 - 玩 4 人斗地主（108张，留底8张）')
    print('其他 - 退出')
    print('**********************************')
    print('请输入需要玩的游戏 (1-4)：', end='')
    game_type = int(input())
    return game_type


def dsp_show_deck(game_type):
    '显示菜单：挑选要查看的牌'

    clear_menu()
    print('**********************************')
    print('1 - 我挑选第一副牌')
    print('2 - 我挑选第二副牌')
    print('3 - 我挑选第三副牌')
    if game_type == 2 or game_type == 4:
        print('4 - 我挑选第四副牌')
    if game_type == 3 or game_type == 4:
        print('9 - 我查看预留的底牌')
    print('其他 - 退出')
    print('**********************************')
    print('请输入我的选择 (1-4或9)：', end='')
    deck_no = int(input())
    return deck_no


def show_deck_para(deck):
    '用并排的方式显示一副扑克牌（假设扑克牌已经排好序）'

    # clear_menu()

    print('**********************************')
    print('***       我挑的牌如下         ***')
    pre_card = ''
    cur_card = ''
    for card in deck:
        cur_card = card[:-1]
        if cur_card != pre_card:
            print('\n%s ' % (card), end='')
        else:
            print('%s ' % (card), end='')
        pre_card = cur_card

    print('\n\n**********************************')
    print('*****        总计 %d 张牌      ***' % (len(deck)))

    return
