#copyright (c) 2019
#jodathecoda@yahoo.com
 
from random import randint
import settings
import common
import time

def openbetflopsize_vs1(vilsstp, stp, boardstraight, boardflush, mystraight, myflush, equx, pot, mybet, biggest_bet, game_type, smallblind, ante, table):
    gamblers = common.countNotFoldedYet(table)
    effective_stacks = common.get_effective_stacks(table , smallblind)
    proposed_bet = 0
    bet_big_reasons = 0
    bet_small_reasons = 0
    allin_reasons = 0
    if vilsstp[0] < 3:
        if equx > 0.8:
            #villain is some kind of shortstack
            #or a lot of bets are in so we want to trap with good hand
            #to induce bluff and checkraise
            bet_small_reasons += 1
        elif equx < 0.5:
            #here is the opposite we have mediocre hand
            #and want to bluff off villains hand
            bet_big_reasons += 1 
    if boardflush == 2:
        #this is maximum possible flushdraw on flop i.e. all board cards from same suit
        if myflush == 0:
            #we already have flush
            bet_small_reasons += 1
        if myflush == 1:
            #we have a flush draw
            bet_big_reasons += 1
        if mystraight == 0:
            #we have flopped straight on a flush heavy board
            bet_big_reasons += 1
        if mystraight == 1:
            #we have straight draw on a heavy flush draw
            bet_small_reasons += 1

    elif boardflush == 3:
        #two cards from same suit on board, possible flushdraw
        if myflush == 1:
            #we have a flush draw
            bet_big_reasons += 1
    elif boardflush == 4:
        #three different suits on board
        pass
    else:
        print("error on counting flushdraws on flop")
        dumb = input("]")

    #print("boardstraight: " + str(boardstraight))
    if boardstraight == 2:
        #possible straight on flop
        if mystraight == 0:
            #we have flopped straight
            bet_small_reasons += 1
        if mystraight == 1:
            #we have straight draw
            pass

    if stp < 1.7:
        allin_reasons = 1
    
    if allin_reasons:
        proposed_bet = 3*pot
    else:
        if bet_small_reasons > bet_big_reasons:
            #prefer to bet small
            simpledecision = randint(0,10)
            if simpledecision < 3:
                #blocking bet
                proposed_bet = round(pot/4)
                if settings.debug_postflop:
                    if settings.view < 4:
                        print("blocking bet")
                    else:
                        print("bb")
                    if settings.debug_postflop_stop_point:
                        dumb = input("]")
                    else:
                        time.sleep(2)
            else:
                proposed_bet = round(pot/2)
        elif bet_small_reasons < bet_big_reasons:
            #prefer to bet big
            simpledecision = randint(0,10)
            if simpledecision == 0:
                #overbet 1.5*pot
                proposed_bet = round(1.5*pot)
            elif simpledecision < 4:
                #potbet
                proposed_bet = round(pot)
            elif simpledecision < 7:
                #3/4bet
                proposed_bet = round(3*pot/4)
                cherrytop = randint(0,1)
                proposed_bet += cherrytop*smallblind
            else:
                #2/3 bet
                proposed_bet = round(2*pot/3)
                cherrytop = randint(0,3)
                proposed_bet += cherrytop*smallblind
        else:
            if effective_stacks < 40:
                #halfpot bet for h and s
                proposed_bet = round(pot/2)
                cherrytop = randint(0,1)
                proposed_bet += cherrytop*smallblind
            else:
                #2/3bet for mtt and cash
                proposed_bet = round(2*pot/3)
                cherrytop = randint(0,3)
                proposed_bet += cherrytop*smallblind      
    rounded_bet = common.roundbet(proposed_bet)      
    return rounded_bet

def openbetflopsize_vs_more(vilsstp, stp, boardstraight, boardflush, mystraight, myflush, equx, pot, mybet, biggest_bet, game_type, smallblind, ante, table):
    gamblers = common.countNotFoldedYet(table)
    effective_stacks = common.get_effective_stacks(table , smallblind)
    proposed_bet = 0
    bet_big_reasons = 0
    bet_small_reasons = 0
    allin_reasons = 0
    villains_stps = vilsstp
    shortstack_vil = vilsstp[0]
    bigstack_vil = vilsstp[0]
    for vsstp in vilsstp:
        if vsstp < shortstack_vil:
            shortstack_vil = vsstp
        if vsstp > bigstack_vil:
            bigstack_vil = vsstp
    if shortstack_vil < 3:
        #we have shortstack villain
        bet_small_reasons += 1
    if boardflush == 2:
        #this is maximum possible flushdraw on flop i.e. all board cards from same suit
        if myflush == 0:
            #we already have flush
            bet_small_reasons += 1
        if myflush == 1:
            #we have a flush draw
            bet_big_reasons += 1
        if mystraight == 0:
            #we have flopped straight on a flush heavy board
            bet_big_reasons += 1
        if mystraight == 1:
            #we have straight draw on a heavy flush draw
            bet_small_reasons += 1

    elif boardflush == 3:
        #two cards from same suit on board, possible flushdraw
        if myflush == 1:
            #we have a flush draw
            bet_big_reasons += 1
    elif boardflush == 4:
        #three different suits on board
        pass
    else:
        print("error on counting flushdraws on flop")
        dumb = input("]")

    if boardstraight == 2:
        #possible straight on flop
        if mystraight == 0:
            #we have flopped straight
            bet_small_reasons += 1
        elif mystraight == 1:
            #we have straight draw
            pass
        else:
            #we want to give bad pot odds to villain
            bet_big_reasons += 1

    if stp < 1.7:
        allin_reasons = 1
    
    if allin_reasons:
        proposed_bet = 3*pot
    else:
        if bet_small_reasons > bet_big_reasons:
            #prefer to bet small
            simpledecision = randint(0,10)
            if simpledecision < 3:
                #blocking bet
                proposed_bet = round(pot/4)
                if settings.debug_postflop:
                    if settings.view < 4:
                        print("blocking bet")
                    else:
                        print("bb")
                    if settings.debug_postflop_stop_point:
                        dumb = input("]")
                    else:
                        time.sleep(2)
            else:
                proposed_bet = round(pot/2)
        elif bet_small_reasons < bet_big_reasons:
            #prefer to bet big
            simpledecision = randint(0,10)
            if simpledecision == 0:
                #overbet
                randomoverbet = randint(0,4)
                if randomoverbet == 0:
                    proposed_bet = round(1.5*pot)
                elif randomoverbet == 1:
                    proposed_bet = round(1.8*pot)
                elif randomoverbet == 2:
                    proposed_bet = round(2.1*pot)
                else:
                    proposed_bet = round(1.3*pot)
            elif simpledecision < 4:
                #potbet
                proposed_bet = round(pot)
            elif simpledecision < 7:
                #3/4bet
                proposed_bet = round(3*pot/4)
                cherrytop = randint(0,1)
                proposed_bet += cherrytop*smallblind
            else:
                #2/3 bet
                proposed_bet = round(2*pot/3)
                cherrytop = randint(0,3)
                proposed_bet += cherrytop*smallblind
        else:
            if effective_stacks < 30 and gamblers < 4:
                #halfpot bet for h and s
                proposed_bet = round(pot/2)
                cherrytop = randint(0,1)
                proposed_bet += cherrytop*smallblind
            else:
                #2/3bet for mtt and cash
                proposed_bet = round(2*pot/3)
                cherrytop = randint(0,3)
                proposed_bet += cherrytop*smallblind
    rounded_bet = common.roundbet(proposed_bet)     
    return rounded_bet

def openbetturnsize(vilsstp, stp, boardstraight, boardflush, mystraight, myflush, equx, pot, mybet, biggest_bet, game_type, smallblind, ante, table):
    gamblers = common.countNotFoldedYet(table)
    effective_stacks = common.get_effective_stacks(table , smallblind)
    proposed_bet = 0
    bet_big_reasons = 0
    bet_small_reasons = 0
    check_reasons = 0
    allin_reasons = 0
    villains_stps = vilsstp
    shortstack_vil = vilsstp[0]
    bigstack_vil = vilsstp[0]
    for vsstp in vilsstp:
        if vsstp < shortstack_vil:
            shortstack_vil = vsstp
        if vsstp > bigstack_vil:
            bigstack_vil = vsstp

    if boardflush == 1:
        #highest possible flush on turn all 4 board cards from same suit
        if myflush == 0:
            #we already have flush will bet big
            bet_big_reasons += 1
        if myflush == 1:
            #we do not have this suit
            check_reasons += 1
    if boardflush == 2:
        #there is a possible flush
        if myflush == 0:
            #we already have flush
            bet_big_reasons += 1
        if myflush == 1:
            #we have a flush draw
            bet_big_reasons += 1
        if mystraight == 0:
            #we have flopped straight on a flush heavy board
            bet_big_reasons += 1
        if mystraight == 1:
            #we have straight draw on a heavy flush draw
            check_reasons += 1

    elif boardflush == 3:
        #two cards from same suit on board, possible flushdraw
        if myflush == 1:
            #we have a flush draw
            bet_big_reasons += 1
    elif boardflush == 4:
        #four different suits on board
        pass

    if boardstraight == 2:
        #possible straight on turn
        if mystraight == 0:
            #we have flopped straight
            bet_big_reasons += 1
        if mystraight == 1:
            #we have straight draw semi bluff
            bet_small_reasons += 1

    if stp < 1:
        allin_reasons = 1
    
    if allin_reasons:
        proposed_bet = 3*pot
    else:
        if check_reasons > bet_small_reasons and check_reasons > bet_big_reasons:
            #we prefer to check
            proposed_bet = 0
        elif bet_small_reasons > bet_big_reasons:
            #prefer to bet small
            simpledecision = randint(0,10)
            if simpledecision < 3:
                #blocking bet
                proposed_bet = round(pot/4)
                if settings.debug_postflop:
                    if settings.view < 4:
                        print("blocking bet")
                    else:
                        print("bb")
                    if settings.debug_postflop_stop_point:
                        dumb = input("]")
                    else:
                        time.sleep(2)
            else:
                proposed_bet = round(pot/2)
        elif bet_small_reasons < bet_big_reasons:
            #prefer to bet big
            simpledecision = randint(0,10)
            if simpledecision == 0:
                #overbet 1.5*pot
                proposed_bet = round(1.5*pot)
            elif simpledecision < 4:
                #potbet
                proposed_bet = round(pot)
            elif simpledecision < 7:
                #3/4bet
                proposed_bet = round(3*pot/4)
            else:
                #2/3 bet
                proposed_bet = round(2*pot/3)
        else:
            if effective_stacks < 30 and gamblers < 4:
                #halfpot bet for h and s
                proposed_bet = round(pot/2)
                cherrytop = randint(0,1)
                proposed_bet += cherrytop*smallblind
            else:
                #2/3bet for mtt and cash
                proposed_bet = round(2*pot/3)
                cherrytop = randint(0,3)
                proposed_bet += cherrytop*smallblind     
    rounded_bet = common.roundbet(proposed_bet)     
    return rounded_bet

def openbetriversize(vilsstp, stp, boardstraight, boardflush, mystraight, myflush, equx, pot, mybet, biggest_bet, game_type, smallblind, ante, table):
    gamblers = common.countNotFoldedYet(table)
    effective_stacks = common.get_effective_stacks(table , smallblind)
    proposed_bet = 0
    bet_big_reasons = 0
    bet_small_reasons = 0
    check_reasons = 0
    allin_reasons = 0
    villains_stps = vilsstp
    shortstack_vil = vilsstp[0]
    bigstack_vil = vilsstp[0]
    for vsstp in vilsstp:
        if vsstp < shortstack_vil:
            shortstack_vil = vsstp
        if vsstp > bigstack_vil:
            bigstack_vil = vsstp

    if boardflush == 0:
        # have to find method to find if our flush is high or low
        check_reasons += 1
    elif boardflush == 1:
        #possible flush on river 4 board cards from same suit
        if myflush == 0:
            #we already have flush will bet big
            bet_big_reasons += 1
        if myflush == 1:
            #we do not have this suit
            check_reasons += 1
    elif boardflush == 2:
        #there is a possible flush
        if myflush == 0:
            #we already have flush
            bet_big_reasons += 1
        if myflush == 1:
            #we do not have a flush but we have blocker
            bet_small_reasons += 1
        if mystraight == 0:
            #we have straight on a flush 2 board
            bet_small_reasons += 1
    else:
        bet_big_reasons += 1

    if boardstraight == 2:
        #possible straight on river
        if mystraight == 0:
            #we have straight
            bet_big_reasons += 1
    elif boardstraight == 1 or boardstraight == 0:
        #heavy straight board
        check_reasons += 1
    else:
        bet_big_reasons += 1

    allin_reasons = 0
    
    if allin_reasons:
        proposed_bet = 3*pot
    else:
        if check_reasons > bet_small_reasons and check_reasons > bet_big_reasons:
            #we prefer to check
            proposed_bet = 0
        elif bet_small_reasons > bet_big_reasons:
            #prefer to bet small
            simpledecision = randint(0,10)
            if simpledecision < 3:
                #blocking bet
                proposed_bet = round(pot/4)
                if settings.debug_postflop:
                    if settings.view < 4:
                        print("blocking bet")
                    else:
                        print("bb")
                    if settings.debug_postflop_stop_point:
                        dumb = input("]")
                    else:
                        time.sleep(2)
            else:
                proposed_bet = round(pot/2)
        elif bet_small_reasons < bet_big_reasons:
            #prefer to bet big
            simpledecision = randint(0,10)
            if simpledecision == 0:
                #overbet 1.5*pot
                proposed_bet = round(1.5*pot)
            elif simpledecision < 4:
                #potbet
                proposed_bet = round(pot)
            elif simpledecision < 7:
                #3/4bet
                proposed_bet = round(3*pot/4)
            else:
                #2/3 bet
                proposed_bet = round(2*pot/3)
        else:
            if effective_stacks < 30 and gamblers < 4:
                #halfpot bet for h and s
                proposed_bet = round(pot/2)
                cherrytop = randint(0,1)
                proposed_bet += cherrytop*smallblind
            else:
                #2/3bet for mtt and cash
                proposed_bet = round(2*pot/3)
                cherrytop = randint(0,3)
                proposed_bet += cherrytop*smallblind    
    rounded_bet = common.roundbet(proposed_bet)   
    return rounded_bet