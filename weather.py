#copyright (c) 2019
#jodathecoda@yahoo.com

from random import randint
import settings

def myweatherboard(table, myname):
    myhand = ""
    t = table
    for ss in t.seats:
        if ss.name == myname:
            myhand = ss.card1 + ss.card2

    board = table.board
    card_ranks = []
    card_suits = []
    ranks_string = ""
    settings.myflush = 5
    settings.mystraight = 5

    if myhand[0] == 'a':
        card_ranks.append(14)
        card_ranks.append(1)
    elif myhand[0] == 'k':
        card_ranks.append(13)
    elif myhand[0] == 'q':
        card_ranks.append(12)
    elif myhand[0] == 'j':
        card_ranks.append(11)
    elif myhand[0] == 't':
        card_ranks.append(10)
    else:
        card_ranks.append(int(myhand[0]))
    if myhand[2] == 'a':
        card_ranks.append(14)
        card_ranks.append(1)
    elif myhand[2] == 'k':
        card_ranks.append(13)
    elif myhand[2] == 'q':
        card_ranks.append(12)
    elif myhand[2] == 'j':
        card_ranks.append(11)
    elif myhand[2] == 't':
        card_ranks.append(10)
    else:
        card_ranks.append(int(myhand[2]))
    card_suits.append(myhand[1])
    card_suits.append(myhand[3])

    if len(board) == 6:
        if board[0] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[0] == 'k':
            card_ranks.append(13)
        elif board[0] == 'q':
            card_ranks.append(12)
        elif board[0] == 'j':
            card_ranks.append(11)
        elif board[0] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[0]))
        if board[2] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[2] == 'k':
            card_ranks.append(13)
        elif board[2] == 'q':
            card_ranks.append(12)
        elif board[2] == 'j':
            card_ranks.append(11)
        elif board[2] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[2]))
        if board[4] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[4] == 'k':
            card_ranks.append(13)
        elif board[4] == 'q':
            card_ranks.append(12)
        elif board[4] == 'j':
            card_ranks.append(11)
        elif board[4] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[4]))
        card_suits.append(board[1])
        card_suits.append(board[3])
        card_suits.append(board[5])
    elif len(board) == 8:
        if board[0] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[0] == 'k':
            card_ranks.append(13)
        elif board[0] == 'q':
            card_ranks.append(12)
        elif board[0] == 'j':
            card_ranks.append(11)
        elif board[0] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[0]))
        if board[2] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[2] == 'k':
            card_ranks.append(13)
        elif board[2] == 'q':
            card_ranks.append(12)
        elif board[2] == 'j':
            card_ranks.append(11)
        elif board[2] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[2]))
        if board[4] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[4] == 'k':
            card_ranks.append(13)
        elif board[4] == 'q':
            card_ranks.append(12)
        elif board[4] == 'j':
            card_ranks.append(11)
        elif board[4] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[4]))
        if board[6] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[6] == 'k':
            card_ranks.append(13)
        elif board[6] == 'q':
            card_ranks.append(12)
        elif board[6] == 'j':
            card_ranks.append(11)
        elif board[6] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[6]))
        card_suits.append(board[1])
        card_suits.append(board[3])
        card_suits.append(board[5])
        card_suits.append(board[7])
    elif len(board) == 10:
        if board[0] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[0] == 'k':
            card_ranks.append(13)
        elif board[0] == 'q':
            card_ranks.append(12)
        elif board[0] == 'j':
            card_ranks.append(11)
        elif board[0] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[0]))
        if board[2] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[2] == 'k':
            card_ranks.append(13)
        elif board[2] == 'q':
            card_ranks.append(12)
        elif board[2] == 'j':
            card_ranks.append(11)
        elif board[2] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[2]))
        if board[4] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[4] == 'k':
            card_ranks.append(13)
        elif board[4] == 'q':
            card_ranks.append(12)
        elif board[4] == 'j':
            card_ranks.append(11)
        elif board[4] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[4]))
        if board[6] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[6] == 'k':
            card_ranks.append(13)
        elif board[6] == 'q':
            card_ranks.append(12)
        elif board[6] == 'j':
            card_ranks.append(11)
        elif board[6] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[6]))
        if board[8] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[8] == 'k':
            card_ranks.append(13)
        elif board[8] == 'q':
            card_ranks.append(12)
        elif board[8] == 'j':
            card_ranks.append(11)
        elif board[8] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[8]))
            
        card_suits.append(board[1])
        card_suits.append(board[3])
        card_suits.append(board[5])
        card_suits.append(board[7])
        card_suits.append(board[9])


    if 1 in card_ranks:
        ranks_string += 'a'
    else:
        ranks_string += '.'
    if 2 in card_ranks:
        ranks_string += '2'
    else:
        ranks_string += '.'
    if 3 in card_ranks:
        ranks_string += '3'
    else:
        ranks_string += '.'
    if 4 in card_ranks:
        ranks_string += '4'
    else:
        ranks_string += '.'
    if 5 in card_ranks:
        ranks_string += '5'
    else:
        ranks_string += '.'
    if 6 in card_ranks:
        ranks_string += '6'
    else:
        ranks_string += '.'
    if 7 in card_ranks:
        ranks_string += '7'
    else:
        ranks_string += '.'
    if 8 in card_ranks:
        ranks_string += '8'
    else:
        ranks_string += '.'
    if 9 in card_ranks:
        ranks_string += '9'
    else:
        ranks_string += '.'
    if 10 in card_ranks:
        ranks_string += 't'
    else:
        ranks_string += '.'
    if 11 in card_ranks:
        ranks_string += 'j'
    else:
        ranks_string += '.'
    if 12 in card_ranks:
        ranks_string += 'q'
    else:
        ranks_string += '.'
    if 13 in card_ranks:
        ranks_string += 'k'
    else:
        ranks_string += '.'
    if 14 in card_ranks:
        ranks_string += 'a'
    else:
        ranks_string += '.'

    suit_weather = 0
    straight_possibility = 5
    counter_spades =  card_suits.count('s')
    counter_hearts =  card_suits.count('h')
    counter_diamonds =  card_suits.count('d')
    counter_clubs =  card_suits.count('c')
    suit_weather =  counter_spades
    if suit_weather < counter_hearts:
        suit_weather = counter_hearts
    if suit_weather < counter_diamonds:
        suit_weather = counter_diamonds
    if suit_weather < counter_clubs:
        suit_weather = counter_clubs
    straight_threat = 0
    for v in range(0,10):
        straight5 = ranks_string[v:v+5]
        counter = straight5.count('.')
        if straight_possibility > counter:
            straight_possibility = counter
    # now update values so bots can use it
    settings.myflush = 5 - suit_weather
    settings.mystraight = straight_possibility

def weatherboard(table):
    board = table.board
    card_ranks = []
    card_suits = []
    ranks_string = ""
    settings.flush = 5
    settings.straight = 5
    if len(board) == 6:
        if board[0] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[0] == 'k':
            card_ranks.append(13)
        elif board[0] == 'q':
            card_ranks.append(12)
        elif board[0] == 'j':
            card_ranks.append(11)
        elif board[0] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[0]))
        if board[2] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[2] == 'k':
            card_ranks.append(13)
        elif board[2] == 'q':
            card_ranks.append(12)
        elif board[2] == 'j':
            card_ranks.append(11)
        elif board[2] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[2]))
        if board[4] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[4] == 'k':
            card_ranks.append(13)
        elif board[4] == 'q':
            card_ranks.append(12)
        elif board[4] == 'j':
            card_ranks.append(11)
        elif board[4] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[4]))
        card_suits.append(board[1])
        card_suits.append(board[3])
        card_suits.append(board[5])
    elif len(board) == 8:
        if board[0] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[0] == 'k':
            card_ranks.append(13)
        elif board[0] == 'q':
            card_ranks.append(12)
        elif board[0] == 'j':
            card_ranks.append(11)
        elif board[0] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[0]))
        if board[2] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[2] == 'k':
            card_ranks.append(13)
        elif board[2] == 'q':
            card_ranks.append(12)
        elif board[2] == 'j':
            card_ranks.append(11)
        elif board[2] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[2]))
        if board[4] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[4] == 'k':
            card_ranks.append(13)
        elif board[4] == 'q':
            card_ranks.append(12)
        elif board[4] == 'j':
            card_ranks.append(11)
        elif board[4] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[4]))
        if board[6] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[6] == 'k':
            card_ranks.append(13)
        elif board[6] == 'q':
            card_ranks.append(12)
        elif board[6] == 'j':
            card_ranks.append(11)
        elif board[6] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[6]))
        card_suits.append(board[1])
        card_suits.append(board[3])
        card_suits.append(board[5])
        card_suits.append(board[7])
    elif len(board) == 10:
        if board[0] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[0] == 'k':
            card_ranks.append(13)
        elif board[0] == 'q':
            card_ranks.append(12)
        elif board[0] == 'j':
            card_ranks.append(11)
        elif board[0] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[0]))
        if board[2] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[2] == 'k':
            card_ranks.append(13)
        elif board[2] == 'q':
            card_ranks.append(12)
        elif board[2] == 'j':
            card_ranks.append(11)
        elif board[2] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[2]))
        if board[4] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[4] == 'k':
            card_ranks.append(13)
        elif board[4] == 'q':
            card_ranks.append(12)
        elif board[4] == 'j':
            card_ranks.append(11)
        elif board[4] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[4]))
        if board[6] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[6] == 'k':
            card_ranks.append(13)
        elif board[6] == 'q':
            card_ranks.append(12)
        elif board[6] == 'j':
            card_ranks.append(11)
        elif board[6] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[6]))
        if board[8] == 'a':
            card_ranks.append(14)
            card_ranks.append(1)
        elif board[8] == 'k':
            card_ranks.append(13)
        elif board[8] == 'q':
            card_ranks.append(12)
        elif board[8] == 'j':
            card_ranks.append(11)
        elif board[8] == 't':
            card_ranks.append(10)
        else:
            card_ranks.append(int(board[8]))
            
        card_suits.append(board[1])
        card_suits.append(board[3])
        card_suits.append(board[5])
        card_suits.append(board[7])
        card_suits.append(board[9])

    if 1 in card_ranks:
        ranks_string += 'a'
    else:
        ranks_string += '.'
    if 2 in card_ranks:
        ranks_string += '2'
    else:
        ranks_string += '.'
    if 3 in card_ranks:
        ranks_string += '3'
    else:
        ranks_string += '.'
    if 4 in card_ranks:
        ranks_string += '4'
    else:
        ranks_string += '.'
    if 5 in card_ranks:
        ranks_string += '5'
    else:
        ranks_string += '.'
    if 6 in card_ranks:
        ranks_string += '6'
    else:
        ranks_string += '.'
    if 7 in card_ranks:
        ranks_string += '7'
    else:
        ranks_string += '.'
    if 8 in card_ranks:
        ranks_string += '8'
    else:
        ranks_string += '.'
    if 9 in card_ranks:
        ranks_string += '9'
    else:
        ranks_string += '.'
    if 10 in card_ranks:
        ranks_string += 't'
    else:
        ranks_string += '.'
    if 11 in card_ranks:
        ranks_string += 'j'
    else:
        ranks_string += '.'
    if 12 in card_ranks:
        ranks_string += 'q'
    else:
        ranks_string += '.'
    if 13 in card_ranks:
        ranks_string += 'k'
    else:
        ranks_string += '.'
    if 14 in card_ranks:
        ranks_string += 'a'
    else:
        ranks_string += '.'

    suit_weather = 0
    straight_possibility = 5
    counter_spades =  card_suits.count('s')
    counter_hearts =  card_suits.count('h')
    counter_diamonds =  card_suits.count('d')
    counter_clubs =  card_suits.count('c')
    suit_weather =  counter_spades
    if suit_weather < counter_hearts:
        suit_weather = counter_hearts
    if suit_weather < counter_diamonds:
        suit_weather = counter_diamonds
    if suit_weather < counter_clubs:
        suit_weather = counter_clubs
    straight_threat = 0
    for v in range(0,10):
        straight5 = ranks_string[v:v+5]
        counter = straight5.count('.')
        if straight_possibility > counter:
            straight_possibility = counter
    # now update values so bots can use it
    settings.flush = 5 - suit_weather
    settings.straight = straight_possibility

