#copyright (c) 2019
#jodathecoda@yahoo.com
 

def riverAK(board):
    scary_river_card = 0
    if ((board[0] != 'a') and (board[0] != 'k') and (board[2] != 'a') and (board[2] != 'k') and (board[4] != 'a') and (board[4] != 'k') and (board[6] != 'a') and (board[6] != 'k')):
        if board[8] == 'a' or board[8] == 'k':
            scary_river_card = 1
    return scary_river_card

def turnAK(board):
    scary_turn_card = 0
    if ((board[0] != 'a') and (board[0] != 'k') and (board[2] != 'a') and (board[2] != 'k') and (board[4] != 'a') and (board[4] != 'k')):
        if board[6] == 'a' or board[6] == 'k':
            scary_turn_card = 1
    return scary_turn_card

def monotonne_flop(board):
    monotonne_brd = 0
    count_faces = 0
    count_digits = 0
    digits = ['2', '3', '4', '5', '6', '7', '8', '9']
    faces = ['a', 'k', 'q', 'j', 't']
    if board[0] in digits:
        count_digits += 1
    elif board[0] in faces:
        count_faces += 1
    else:
        print("unknown character in board")
        dumb = input("]")
    if board[2] in digits:
        count_digits += 1
    elif board[2] in faces:
        count_faces += 1
    else:
        print("unknown character in board")
        dumb = input("]")
    if board[4] in digits:
        count_digits += 1
    elif board[4] in faces:
        count_faces += 1
    else:
        print("unknown character in board")
        dumb = input("]")
    if count_faces == 1 and count_digits == 2:
        monotonne_brd = 1
    return monotonne_brd

def billchen(s):
    value=0
    gapvalue1=0
    gapvalue2=0

    if s[0]==s[2]:
        if s[0] == "a":
            value+=20
        elif s[0] == "k":
            value+=16
        elif s[0] == "q":
             value+=14
        elif s[0] == "j":
             value+=12
        elif s[0] == "2":
             value+=5
        elif s[0] == "3":
             value+=5
        elif s[0] == "4":
             value+=5
        elif s[0] == "t":
             value+=10
        else:
            value+=int(s[0])
    else:
        if s[0] == "a" or s[2] == "a":
            value+=10
        elif s[0] == "k" or s[2] == "k":
            value+=8
        elif s[0] == "q" or s[2] == "q":
            value+=7
        elif s[0] == "j" or s[2] == "j":
            value+=6
        elif s[0] == "t" or s[2] == "t":
            value+=5
        elif int(s[0]) > int(s[2]):
            value+=int(s[0])/2
        else:
            value+=int(s[2])/2
    if s[1] == s[3]:
        value+=2
    if s[0]!=s[2]:
        if s[0] == "a":
            gapvalue1=14
        elif s[0] == "k":
            gapvalue1=13
        elif s[0] == "q":
            gapvalue1=12
        elif s[0] == "j":
            gapvalue1 =11
        elif s[0] == "t":
            gapvalue1 =10
        else:
            gapvalue1 = int(s[0])

        if s[2] == "a":
            gapvalue2=14
        elif s[2] == "k":
            gapvalue2=13
        elif s[2] == "q":
            gapvalue2=12
        elif s[2] == "j":
            gapvalue2 =11
        elif s[2] == "t":
            gapvalue2 =10
        else:
            gapvalue2 = int(s[2])

        gap=0
        if gapvalue1>gapvalue2:
            gap=gapvalue1-gapvalue2
        else:
            gap=gapvalue2-gapvalue1
        if gap ==0:
            pass
        elif gap==1:
            pass
        elif gap == 2:
            value-=1
        elif gap == 3:
            value-=2
        elif gap == 4:
            value-=4
        else:
            value-=5

        if gapvalue1 < 12 and gapvalue2 < 12:
            if gap<3:
                value+=1
    return value


def handInRange(card1, card2, botrange):
    hnd = card1 + card2
    hnd2 = card2 + card1 # ahkh = khah
    hand_as_range = ""
    hand_as_range2 = ""

    #for first order    
    if pocket_pairs(hnd):
        hand_as_range = hnd[0] + hnd[2]
    elif suited(hnd):
        hand_as_range = hnd[0] + hnd[2] + "s"
    else:
        hand_as_range = hnd[0] + hnd[2] + "o"

    #for second_order
    if pocket_pairs(hnd2):
        hand_as_range2 = hnd2[0] + hnd2[2]
    elif suited(hnd2):
        hand_as_range2 = hnd2[0] + hnd2[2] + "s"
    else:
        hand_as_range2 = hnd2[0] + hnd2[2] + "o"
        
    if ((hand_as_range in botrange) or (hand_as_range2 in botrange)):
        return True
    else:
        return False

def pocket_pairs(hnd):
    if hnd[0] == hnd[2]:
        return True
    else:
        return False

def suited(hnd):
    if hnd[1] == hnd[3]:
        return True
    else:
        return False

def spades(hnd):
    if(suited(hnd) and hnd[1] == 's'):
        return True
    else:
        return False

def hearts(hnd):
    if(suited(hnd) and hnd[1] == 'h'):
        return True
    else:
        return False

def diamonds(hnd):
    if(suited(hnd) and hnd[1] == 'd'):
        return True
    else:
        return False

def clubs(hnd):
    if(suited(hnd) and hnd[1] == 'c'):
        return True
    else:
        return False

def Ace(hnd):
    if hnd[0] == 'a' or hnd[2] == 'a':
        return True
    return False

def sAce(hnd):
    if hnd[0] == 'a' or hnd[2] == 'a':
        if suited(hnd):
            return True
    return False

def King(hnd):
    if hnd[0] == 'k' or hnd[2] == 'k':
        return True
    return False

def sKing(hnd):
    if hnd[0] == 'k' or hnd[2] == 'k':
        if suited(hnd):
            return True
    return False

def Queen(hnd):
    if hnd[0] == 'q' or hnd[2] == 'q':
        return True
    return False

def sQueen(hnd):
    if hnd[0] == 'q' or hnd[2] == 'q':
        if suited(hnd):
            return True
    return False

def Jack(hnd):
    if hnd[0] == 'j' or hnd[2] == 'j':
        return True
    return False

def sJack(hnd):
    if hnd[0] == 'j' or hnd[2] == 'j':
        if suited(hnd):
            return True
    return False

def Ten(hnd):
    if hnd[0] == 't' or hnd[2] == 't':
        return True
    return False

def sTen(hnd):
    if hnd[0] == 't' or hnd[2] == 't':
        if suited(hnd):
            return True
    return False

def Nine(hnd):
    if hnd[0] == '9' or hnd[2] == '9':
        return True
    return False

def sNine(hnd):
    if hnd[0] == '9' or hnd[2] == '9':
        if suited(hnd):
            return True
    return False

def Eight(hnd):
    if hnd[0] == '8' or hnd[2] == '8':
        return True
    return False

def sEight(hnd):
    if hnd[0] == '8' or hnd[2] == '8':
        if suited(hnd):
            return True
    return False

def Seven(hnd):
    if hnd[0] == '7' or hnd[2] == '7':
        return True
    return False

def sSeven(hnd):
    if hnd[0] == '7' or hnd[2] == '7':
        if suited(hnd):
            return True
    return False

def Six(hnd):
    if hnd[0] == '6' or hnd[2] == '6':
        return True
    return False

def sSix(hnd):
    if hnd[0] == '6' or hnd[2] == '6':
        if suited(hnd):
            return True
    return False

def Five(hnd):
    if hnd[0] == '5' or hnd[2] == '5':
        return True
    return False

def sFive(hnd):
    if hnd[0] == '5' or hnd[2] == '5':
        if suited(hnd):
            return True
    return False

def Four(hnd):
    if hnd[0] == '4' or hnd[2] == '4':
        return True
    return False

def sFour(hnd):
    if hnd[0] == '4' or hnd[2] == '4':
        if suited(hnd):
            return True
    return False

def exactHand(c1, c2, hnd):
    if (c1 == hnd[0] and c2 == hnd[2]) or (c1 == hnd[2] and c2 == hnd[0]):
        return True
    else:
        return False

def lowerCard(crd, hnd):
    if hnd[0] == 'a':
        val1 = 14
    elif hnd[0] == 'k':
        val1 = 13
    elif hnd[0] == 'q':
        val1 = 12
    elif hnd[0] == 'j':
        val1 = 11
    elif hnd[0] == 't':
        val1 = 10
    else:
        val1 = int(hnd[0])
    if hnd[2] == 'a':
        val2 = 14
    elif hnd[2] == 'k':
        val2 = 13
    elif hnd[2] == 'q':
        val2 = 12
    elif hnd[2] == 'j':
        val2 = 11
    elif hnd[2] == 't':
        val2 = 10
    else:
        val2 = int(hnd[2])
    if val1 < val2:
        minval = val1
    else:
        minval = val2
    if minval >= crd:
        return True
    else:
        return False