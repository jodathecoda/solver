#copyright (c) 2019
#jodathecoda@yahoo.com

from random import randint
import settings
import common

def preflop_interpreter(table, name, smallblind, ante):

    return_string = "tough-spot"

    bet0 = table.seats[0].bet
    bet1 = table.seats[1].bet
    bet2 = table.seats[2].bet
    bet3 = table.seats[3].bet
    bet4 = table.seats[4].bet
    bet5 = table.seats[5].bet

    stack0 = table.seats[0].stack
    stack1 = table.seats[1].stack
    stack2 = table.seats[2].stack
    stack3 = table.seats[3].stack
    stack4 = table.seats[4].stack
    stack5 = table.seats[5].stack

    posicione = common.getPreflopPosition(table, name)
    gamblers = common.countNotFoldedYet(table)
    cur_stack = 0
    biggest_bet = 0
    limpers = 0
    players_with_bets_bigger_than_big_blind = 0
    different_bet_sizings = []

    for s in table.seats:
        if s.bet > smallblind*2 + ante:
            different_bet_sizings.append(s.bet)

    for s in table.seats:
        if s.bet > smallblind*2 + ante:
            players_with_bets_bigger_than_big_blind += 1

    for l in table.seats:
        if l.bet == smallblind*2 + ante:
            limpers +=1
    limpers -=1 #remove big blind from limpers

    for s in table.seats:
        if s.bet > biggest_bet:
            biggest_bet = s.bet

    for s in table.seats:
        if s.name == name:
            cur_stack = s.stack

    pot = 0
    for s in table.seats:
        pot += s.bet

    #this function will read the table and give output string as one of the 50 preflop situations:
    #check if someone is allin before you and his stack
    allinbets = []
    #if there are more allins it will go to specail case
    for s in table.seats:
        if (s.bet > ((smallblind*2) + ante)) and (s.stack == 0):
            #there is allin count number of allins
            allinbets.append(s.bet)
    if len(allinbets) == 1:
        if allinbets[0] < (smallblind*25 + ante):
            if pot < allinbets[0]*2:
                #one allin no call
                if gamblers == 2:
                    return_string = "allin10BB-wearehere-0behind"
                elif gamblers == 3:
                    return_string = "allin10BB-wearehere-1behind"
                elif gamblers > 3:
                    return_string = "allin10BB-wearehere-morebehind"
                else:
                    pass
            else:
                pass
        else: #allin bet is more than 10BB
            if (pot >= allinbets[0]*2 + 6*ante + 3*smallblind) and (pot <= allinbets[0]*3 + 6*ante + 3*smallblind):
                if gamblers == 3:
                    return_string = "allin10BB+call-wearehere-0behind"
                elif gamblers == 4:
                    return_string = "allin10BB+call-wearehere-1behind"
                elif gamblers > 4:
                    return_string = "allin10BB+call-wearehere-morebehind"
                else:
                    pass
            else:
                if gamblers == 2:
                    return_string = "allin10BB+wearehere-0behind"
                elif gamblers == 3:
                    return_string = "allin10BB+wearehere-1behind"
                elif gamblers > 3:
                    return_string = "allin10BB+wearehere-morebehind"
                else:
                    pass
    elif len(allinbets) == 2:
        if gamblers == 3:
            #2allins-0behind
            return_string = "2allins-0behind"
        elif gamblers == 4:
            #2allins-1behind
            return_string = "2allins-1behind"
        elif gamblers >4:
            #2allins-morebehind
            return_string = "2allins-morebehind"
        else:
            pass
    elif len(allinbets) > 2:
        #more-allins
        return_string = "more-allins"
    else:
        #no allin continue
        if cur_stack < smallblind*20:
            if limpers > 0:
                if limpers == 1:
                    if gamblers == 2:
                        return_string = "10BB-1limper-0behind"
                    elif gamblers == 3:
                        return_string = "10BB-1limper-1behind"
                    elif gamblers == 4:
                        return_string = "10BB-1limper-2behind"
                    elif gamblers > 4:
                        return_string = "10BB-1limper-morebehind"
                    else:
                        pass
                elif limpers == 2:
                    if gamblers == 3:
                        return_string = "10BB-2limpers-0behind"
                    elif gamblers == 4:
                        return_string = "10BB-2limpers-1behind"
                    elif gamblers > 4:
                        return_string = "10BB-2limpers-morebehind"
                    else:
                        pass

            #current stack is less than 10BB so shortstack mode
            elif pot <= smallblind*3 + 6*ante:
                #no one opened
                if gamblers == 2:
                    return_string = "10BB-noopen-wearehere-1behind"
                elif gamblers == 3:
                    return_string = "10BB-noopen-wearehere-2behind"
                elif gamblers > 3:
                    return_string = "10BB-noopen-wearehere-morebehind"
                else:
                    pass
            else:
                #someone-opened-we-are-under-10BBs
                if gamblers == 2:
                    return_string = "10BB-opened-0behind"
                elif gamblers == 3:
                    return_string = "10BB-opened-1behind"
                elif gamblers > 3:
                    return_string = "10BB-opened-morebehind"
                else:
                    pass
        else:
            #current stack is more than 10BBs
            if pot <= smallblind*3 + 6*ante:
                if gamblers == 2:
                    return_string = "10BB+noopen-wearehere-1behind"
                elif gamblers == 3:
                    return_string = "10BB+noopen-wearehere-2behind"
                elif gamblers >= 3:
                    return_string = "10BB+noopen-wearehere-morebehind"
                else:
                    pass
            else:
                #check for limpers
                if limpers >0:
                    if limpers == 1:
                        if gamblers == 2:
                            return_string = "10BB+1limp-wearehere-0behind"
                        elif gamblers == 3:
                            if len(different_bet_sizings) == 1 and smallblind*10 > different_bet_sizings[0]: #less than 5 times raise, otherwise special case
                                return_string = "10BB+limped-raised-wearehere-0behind"
                                settings.threebet += 1 #there is a 3bet
                            elif len(different_bet_sizings) == 0:
                                return_string = "10BB+1limp-wearehere-1behind"
                        elif gamblers == 4:
                            if len(different_bet_sizings) == 1 and smallblind*10 > different_bet_sizings[0]: #less than 5 times raise, otherwise special case
                                return_string = "10BB+limped-raised-wearehere-1behind"
                                settings.threebet += 1 #there is a 3bet
                            elif len(different_bet_sizings) == 0: 
                                return_string = "10BB+1limp-wearehere-2behind"
                        elif gamblers > 4:
                            if len(different_bet_sizings) == 1 and smallblind*10 > different_bet_sizings[0]: #less than 5 times raise, otherwise special case
                                return_string = "10BB+limped-raised-wearehere-morebehind"
                                settings.threebet += 1 #there is a 3bet
                            elif len(different_bet_sizings) == 0:
                                return_string = "10BB+1limp-wearehere-morebehind"
                        else:
                            pass
                    elif limpers == 2:
                        if gamblers == 3:
                            return_string = "10BB+2limps-wearehere-0behind"
                        elif gamblers == 4:
                            return_string = "10BB+2limps-wearehere-1behind"
                        elif gamblers > 4:
                            return_string = "10BB+2limps-wearehere-morebehind"
                        else:
                            pass
                    elif limpers == 3:
                        if gamblers == 4:
                            return_string = "10BB+3limps-wearehere-0behind"
                        elif gamblers > 4:
                            return_string = "10BB+3limps-wearehere-morebehind"
                        else:
                            pass
                    elif limpers > 3:
                        return_string = "10BB+bunch_of_limpers"
                else:
                    if players_with_bets_bigger_than_big_blind == 1:
                        #check open size:
                        if biggest_bet <= smallblind*10 + 6*ante:
                            #up to 5 big blinds plus ante it will go for normal bet size
                            if gamblers == 2:
                                return_string = "10BB+opened-wearehere-0behind"
                            elif gamblers == 3:
                                return_string = "10BB+opened-wearehere-1behind"
                            elif gamblers == 4:
                                return_string = "10BB+opened-wearehere-2behind"
                            else:
                                return_string = "10BB+opened-wearehere-morebehind"
                        else:
                            return_string = "10BB+weird-big-size-open"
                    else:
                        if len(different_bet_sizings) == 2 and different_bet_sizings[0] == different_bet_sizings[1]:
                            if gamblers == 3:
                                return_string = "10BB+opened-call-wearehere-0behind"
                            elif gamblers == 4:
                                return_string = "10BB+opened-call-wearehere-1behind"
                            elif gamblers > 4:
                                return_string = "10BB+opened-call-wearehere-morebehind"
                        elif len(different_bet_sizings) == 2:
                            if gamblers == 2:
                                return_string = "10BB+opened-raised-back-to-original-opener"
                                settings.threebet += 1 #there is a 3bet
                            elif gamblers == 3:
                                return_string = "10BB+opened-raised-wearehere-0behind"
                                settings.threebet += 1 #there is a 3bet
                            elif gamblers == 4:
                                return_string = "10BB+opened-raised-wearehere-1behind"
                                settings.threebet += 1 #there is a 3bet
                            elif gamblers > 4:
                                return_string = "10BB+opened-raised-wearehere-morebehind"
                                settings.threebet += 1 #there is a 3bet
                        elif len(different_bet_sizings) == 3:
                            if different_bet_sizings[0] != different_bet_sizings[1]:
                                if different_bet_sizings[0] != different_bet_sizings[2]:
                                    if different_bet_sizings[1] != different_bet_sizings[2]:
                                        return_string = "10BB+opened-raised-reraised-wearehere"
                            else:
                                open_raise_call = 0
                                if different_bet_sizings[0] == different_bet_sizings[1]:
                                    open_raise_call = 1
                                if different_bet_sizings[0] == different_bet_sizings[2]:
                                    open_raise_call = 1
                                if different_bet_sizings[1] == different_bet_sizings[2]:
                                    opened_raised_called = 1
                                if open_raise_call == 1:
                                    return_string = "10BB+opened-raised-called-wearehere"
                                    settings.threebet += 1 #there is a 3bet

    if return_string == "tough-spot":
        #here check for special cases if you missed something, lets say open or limp and someone reraises and gets back to you
        if (players_with_bets_bigger_than_big_blind == 2) and ((len(different_bet_sizings) == 2) and (different_bet_sizings[0] < different_bet_sizings[1]) and (different_bet_sizings[0]*5 >= different_bet_sizings[1])):
            if gamblers == 2:
                mybet = 0.0
                for s in table.seats:
                    if s.name == name:
                        mybet = s.bet
                if mybet < biggest_bet:
                    #we opened, villain raised
                    return_string = "10BB+opened-raised-back-to-original-opener"
                    settings.threebet += 1 #there is a 3bet
        #check for maniacs
        maniac_on_board = 0
        for s in table.seats:
            if s.last5betscrazy >= 2:
                maniac_on_board = 1
        if settings.preorbits_hero > 3:
            if settings.crazybets_hero/settings.preorbits_hero >= 0.5:
                return_string = "maniac-on-board"
        if maniac_on_board:
            return_string = "maniac-on-board"     
    return return_string
