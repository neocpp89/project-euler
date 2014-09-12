#!/usr/bin/env python

def convert_string(cardstring):
    v = cardstring[0]
    s = cardstring[1]

    if (v == 'T'):
        v = 10
    elif (v == 'J'):
        v = 11
    elif (v == 'Q'):
        v = 12
    elif (v == 'K'):
        v = 13
    elif (v == 'A'):
        v = 14
    else:
        v = int(v)

    return (v, s)

def get_suit(card):
    return card[1]

def get_value(card):
    return card[0]

def royal_flush(hand):
    first = hand[0]
    s = map(lambda card: get_suit(first) == get_suit(card), hand)
    v = sorted(map(lambda card: get_value(card), hand))
    if all(s):
        for x in range(0,5):
            if (v[x] != 10+x):
                return False
        return True
    return False

def straight_flush(hand):
    first = hand[0]
    s = map(lambda card: get_suit(first) == get_suit(card), hand)
    v = sorted(map(lambda card: get_value(card), hand))
    if (all(s)):
        for x in range(0,5):
            if (v[x] != v[0]+x):
                return False
        return True
    return False

with open('poker.txt') as f:
    hands = zip(*map(lambda row: map(convert_string, row.split(' ')), f))
    player1hands = zip(hands[0], hands[1], hands[2], hands[3], hands[4])
    player2hands = zip(hands[5], hands[6], hands[7], hands[8], hands[9])

    for round in range(0, len(player1hands)):
        p1 = player1hands[round]
        p2 = player2hands[round]
        print royal_flush(p1), royal_flush(p2)
