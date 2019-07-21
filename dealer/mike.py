# -*- coding: UTF-8 -*-
import random
import os
import codecs


def deal_to_a_player(aDeck, num, player_cards):
    'Desc:Deal some cards to a player from a deck'
    for i in range(num):
        picked_card = random.choice(aDeck)
        player_cards.append(picked_card)
        aDeck.remove(picked_card)
    player_cards.sort()
    return


def deal_to_multi_players(aDeck, *players_cards):
    'Desc: Deal to multiple players, deal remained cards into first player'

    player_num = len(players_cards)
    cards_num = len(aDeck)
    player_hold_cards = int(cards_num / player_num)
    #print('\n===debug1: %d' % (player_hold_cards))

    for pscs in players_cards:
        deal_to_a_player(aDeck, player_hold_cards, pscs)
        '''
        # fbb ----
        for i in range(player_hold_cards):
            # fbb ----
            picked_card = random.choice(aDeck)
            pscs.append(picked_card)
            aDeck.remove(picked_card)
            # fbe ----
        # fbe ----
        pscs.sort()
        '''

    if len(aDeck) > 0:
        for card in aDeck:
            players_cards[0].append(card)
        aDeck = []
        players_cards[0].sort()

    return


def deal_to_multi_players_remain(aDeck, remain_num, player_dumy, *players_cards):
    'Desc: Deal to multiple players, deal remained cards into dumy'

    player_num = len(players_cards)
    cards_num = len(aDeck) - remain_num
    player_hold_cards = int(cards_num / player_num)
    #print('\n===debug1: %d' % (player_hold_cards))

    for pscs in players_cards:
        deal_to_a_player(aDeck, player_hold_cards, pscs)

    if len(aDeck) > 0:
        for card in aDeck:
            player_dumy.append(card)
        aDeck = []
        player_dumy.sort()

    return
