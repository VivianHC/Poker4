# -*- coding: UTF-8 -*-
import random
import os
import codecs
import csv

def create_deck_54(new_deck):
    '推出一副54张的新牌'
    print('\n---debug:I made a new deck.---')
    cardJokers = ('♛', '♕')
    cardMarks = ('♠', '♥', '♦', '♣')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')
    for c in cardJokers:
        new_deck.append(c)
    for cn in cardNumbers:
        for cm in cardMarks:
            card = cm + cn
            new_deck.append(card)
    return


def create_deck_52(new_deck):
    '推出一副52张的新牌'
    print('\n---debug:I made a new deck.---')
    # cardJokers = ('♛', '♕')
    cardMarks = ('♠', '♥', '♦', '♣')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')
    # for c in cardJokers:
        # new_deck.append(c)
    for cn in cardNumbers:
        for cm in cardMarks:
            card = cm + cn
            new_deck.append(card)
    return


def shuffled_deck(deck_to_be_shuffled):
    '洗牌'
    print('\n---debug:I shuffled a deck.---')
    random.shuffle(deck_to_be_shuffled)
    return

'''
def csv_deck(deck_to_be_record, filename):
    '记录一副新牌'
    print('\n---debug:I record a deck.---')
    out_path = os.getcwd() + '\\OutputDecks\\' + filename
    f = codecs.open(out_path, "w", "utf-8")
    for card in deck_to_be_record:
        f.write(card)
        f.write('\n')
    f.close
    return
'''

def make_deck_by_type(play_type, out_deck):
    '按要求制作各种扑克牌'
    if play_type == 1:
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        csv_deck(out_deck, '争上游-刚洗好的牌.txt')
    if play_type == 2:
        create_deck_52(out_deck)
        shuffled_deck(out_deck)
        csv_deck(out_deck, '桥牌-刚洗好的牌.txt')
    if play_type == 3:
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        csv_deck(out_deck, '三人斗地主-刚洗好的牌.txt')
    if play_type == 4:
        deck_a = []
        create_deck_54(deck_a)
        out_deck.extend(deck_a)
        deck_b = []
        create_deck_54(deck_b)
        out_deck.extend(deck_b)
        shuffled_deck(out_deck)
        csv_deck(out_deck, '四人斗地主-刚洗好的牌.txt')
    return

def csv_deck(deck_to_be_record,csv_filename):
    '用CSV格式记录一副牌'
    csv_path=os.getcwd()+'\\csv_decks\\'+csv_filename
    with open(csv_path,"w",encoding='utf-8',newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(deck_to_be_record)
    return

def read_deck_csv(csv_filename, out_deck):
    '读取 CSV 格式的牌，并把它读取到一个列表中去'

    in_path = os.getcwd() + '\\csv_decks\\' + csv_filename
    with open(in_path, "r", encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            out_deck.extend(line)

    
    return
