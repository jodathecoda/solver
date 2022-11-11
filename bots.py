#copyright (c) 2019
#jodathecoda@yahoo.com

import random
import time
import os
import datetime
from random import randint
from random import uniform
from random import shuffle

import settings
import table
import checkhands
import calculator
import rangeeditor
import form
import info
import common
import weather
import selectrange
import betsize
import preflop
import display

def bot_act(table, seat, street, game_type, smallblind, ante, tables):
    global handlog
    t = table
    s = seat
    st = street
    wait_for_showdown = 0
    if common.wait_showdown(t, smallblind, ante):
        wait_for_showdown = 1           
    else:
        wait_for_showdown = 0
    biggest_bet = common.find_biggest_bet(t)
    smallest_bet = common.find_smallest_bet(t)
    if ((not s.available) and (not common.one_left_on_street(t))):
        if s.stack != 0 and s.card1 != "  ":
            #analysis specific
            if s.stack > settings.dumblind*1.5 and settings.analyser_flag:
                weather.myweatherboard(t, s.name)
            if s.bet == biggest_bet:
                if len(t.board) < 2: #preflop
                    if s.acted_preflop:
                        for s in t.seats:
                            s.clock = " "
                        return
                elif len(t.board) == 6: #flop
                    if s.acted_flop:
                        for s in t.seats:
                            s.clock = " "
                        return
                elif len(t.board) == 8: #turn
                    if s.acted_turn:
                        for s in t.seats:
                            s.clock = " "
                        return
                elif len(t.board) == 10: #river
                    if s.acted_river:
                        for s in t.seats:
                            s.clock = " "
                        return
                else:
                    print("unknown street to skip")
                    dumb = input("]")
                    
            s.clock = settings.image_cl
            if not settings.analyser_flag:
                display.display_tables(t, game_type, smallblind, ante, tables)
            else:
                #analyser
                display.display_tables_analyser(t, settings.analysed_iterations, settings.matched)
            if s.name in settings.allfishes:
                if len(t.board) < 2:
                    time.sleep(settings.bot_time_to_act_preflop)
                elif len(t.board) == 6:
                    time.sleep(settings.bot_time_to_act_flop)
                elif len(t.board) == 8:
                    time.sleep(settings.bot_time_to_act_turn)
                elif len(t.board) == 10:
                    time.sleep(settings.bot_time_to_act_river)
                else:
                    pass
            oldbet = s.bet
            newbet = 0
            defendrange = []
            openrange = []
            if ((s.name != settings.hero) and (not settings.act_instead_of_bot)):
                oldbet = s.bet
                bet_command = ""
                if len(t.board) < 2: #preflop HUBOTS HERE HERE
                    #analysis specific
                    if s.stack <= settings.dumblind*1.5 and settings.analyser_flag:
                        #explicit fold
                        newbet = 0
                        s.card1 = "  "
                        s.card2 = "  "
                        s.last3bets = 0 # for analyser purpose no previous hands
                    else:
                        situation = ""
                        respond_range = []
                        situation = preflop.preflop_interpreter(t, s.name, smallblind, ante)
                        #as we dont have 4bets, the situations of interest are:
                        # 10BB+opened-raised-back-to-original-opener
                        # 10BB+noopen-wearehere-1behind
                        # 10BB+opened-wearehere-0behind
                        #dumb = input("before")
                        if settings.hudanalyser == 1:
                            if situation == "10BB+noopen-wearehere-1behind":
                                #respond_range = "redfish/hd_open_huanalyzer"
                                respond_range = settings.huanalyzer_open
                            elif situation == "10BB+opened-raised-back-to-original-opener":
                                #respond_range = "redfish/hd_call3bet_hudanalyzer.range"
                                respond_range = settings.huanalyzer_call3bet
                            elif situation == "10BB+opened-wearehere-0behind":
                                #blackfish
                                #respond_range = "blackfish/hb_3bet_analyzer" + "blackfish/hb_call_analyzer"
                                # respond range for HB is blackfish, it will be defined in
                                # common.betsizing module, as we do not have 4bets, so here it is unimportant
                                respond_range = settings.huanalyzer_3bet + settings.huanalyzer_call
                                #have to split them correctly in /common.betsizing
                            else:
                                # 10BB+1limp-wearehere-0behind
                                #limped pot
                                respond_range = settings.allcards
                                #print(situation)
                                #print("hudAnalyzer unknown spot")
                                #dumb = input("]")
                        else:
                            respond_range = selectrange.rangeselector(situation, t, s.name, smallblind, ante)
                        #dumb = input("after")
                        newbet = common.betsizing(t, s.name, respond_range, game_type, smallblind, ante)
                        '''
                        if settings.hudanalyser and newbet > 0:
                            #if hand in open range, use predefined open size
                            if settings.huanalyzer_open_size == "0":
                                #open fold each hand
                                newbet = 0
                            elif settings.huanalyzer_open_size == "2":
                                # bot uses min raise
                                newbet = 40
                            elif settings.huanalyzer_open_size == "2.5":
                                # x2.5
                                newbet = 50
                            elif settings.huanalyzer_open_size == "3":
                                # x3
                                newbet = 60
                            elif settings.huanalyzer_open_size == "3.5":
                                # x3
                                newbet = 70
                            else:
                                dumb = input("error in preflop open bet size")
                                # x2.5
                                newbet = 50
                            '''
                        #dumb = input("preflop size: " + str(newbet))
                        if s.want_to_push:
                            if newbet > 0:
                                newbet = s.stack
                        if newbet!= 0 and s.stack == 0:
                            s.preallin += 1
                            s.last5betscrazy += 2
                        if newbet > 5*biggest_bet: #maniac counter
                            s.prebigbet += 1
                            s.last5betscrazy += 2
                        if s.last5betscrazy:
                            s.last5betscrazy -= 1
                    if newbet > biggest_bet:
                        #new lead bettor
                        for sit in t.seats:
                            #clear previous leads
                            sit.betting_lead = 0
                        s.betting_lead = 1
                    else:
                        #lose betting lead
                        s.betting_lead = 0
                    s.acted_preflop = 1
                    
                    #record in hand history if preflop allin that pot is bigger than zero

                elif len(t.board) == 6: #flop
                    equx = 0.0
                    gamblers = common.countNotFoldedYet(t)
                    if s.equx_flop > 0.0:
                        equx = s.equx_flop
                    else:
                        fcard1 = form.format_card_for_calculating(s.card1)
                        fcard2 = form.format_card_for_calculating(s.card2)
                        fboard = form.format_board_for_calculating(t.board)
                        resultlist = []
                        resultlist = calculator.find_equx(fcard1, fcard2, fboard)
                        equx = round(float(resultlist[1]), 2)
                    common.overbet_postflop(t, s.name, equx, smallblind, ante)

                    pot = 0
                    for z in t.seats:
                        pot += z.bet
                        if z.card1 != "  ":
                            z.stp = common.getStackToPotRatio(t, z.name)
                    weather.weatherboard(t)
                    weather.myweatherboard(t, s.name)
                    oppo_stps = []
                    for z in t.seats:
                        if z.card1 != "  ":
                            if z.name != s.name:
                                oppo_stps.append(z.stp)
                    
                    if settings.debug_postflop and (not common.wait_showdown(t, smallblind, ante)):
                        info.report(1, gamblers, equx, s, smallest_bet, biggest_bet)
                    
                    #flopbettinground
                    biggest_bet = common.find_biggest_bet(t)
                    if s.bet == biggest_bet:
                        #no one bet on the flop
                        if gamblers == 2:
                            if s.stp < 1.5  and equx > (s.threshold_flop_open_vs_one - settings.checks_on_flop*settings.threshold_added_open_from_checks):
                                newbet = s.stack
                            elif equx > (s.threshold_flop_open_vs_one - settings.checks_on_flop*settings.threshold_added_open_from_checks):
                                flop_threshold = 1.0/(gamblers - 0.5) + common.check_to_the_raisor_effect(s.betting_lead)
                                #we may bet, based on board and weather and stps decide size
                                random_decision = round(random.uniform(0.0, 1.0),2)
                                random_decision -= (settings.checks_on_flop * 0.1)
                                if random_decision < flop_threshold:
                                    newbet = betsize.openbetflopsize_vs1(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t)
                                    if newbet == 0:
                                        settings.checks_on_flop += 1
                                else:
                                    #check
                                    newbet = 0
                                    settings.checks_on_flop += 1
                                info.yesno(newbet, wait_for_showdown)
                            else:
                                #check
                                newbet = 0
                                settings.checks_on_flop += 1
                            if newbet == 0 and not wait_for_showdown:
                                monotonne_board = 0
                                monotonne_board = int(checkhands.monotonne_flop(t.board))
                                if monotonne_board:
                                    #good flop to cbet no matter what we have
                                    if s.betting_lead:
                                        rnd = randint(0, 50)
                                    else:
                                        rnd = randint(0, 65)
                                    if rnd <= s.faggression:
                                        #we go for it
                                        newbet = betsize.openbetflopsize_vs1(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t)
                                        if settings.checks_on_flop:
                                            settings.checks_on_flop -= 1
                                        if settings.debug_postflop:
                                            if settings.view < 4:
                                                print("cbet on monotonne board")
                                            else:
                                                print("cb")
                                            if settings.debug_postflop_stop_point:
                                                dumb = input("]")
                                            else:
                                                time.sleep(2)
                        else:
                            #multipot
                            if s.stp < 1.5  and equx > (s.threshold_flop_open_vs_more - settings.checks_on_flop*settings.threshold_added_open_from_checks):
                                newbet = s.stack
                            elif equx > (s.threshold_flop_open_vs_more - settings.checks_on_flop*settings.threshold_added_open_from_checks):
                                #we may bet, based on board and weather and stps decide size
                                random_decision = round(random.uniform(0.0, 1.0),2)
                                random_decision -= (settings.checks_on_flop * 0.1)
                                flop_threshold = 1.0/(gamblers - 0.5)
                                if random_decision <= flop_threshold:
                                    #we will bet decide how big based on stps, equx and weather
                                    newbet = betsize.openbetflopsize_vs_more(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t)
                                    if newbet > 0:
                                        pass
                                    else:
                                        settings.checks_on_flop += 1
                                else:
                                    #check
                                    newbet = 0
                                    settings.checks_on_flop += 1
                                info.yesno(newbet, wait_for_showdown)
                            else:
                                #check
                                newbet = 0
                                settings.checks_on_flop += 1
                    else:
                        #already opened calculate pot odds -+
                        if not settings.raise_on_flop:
                            #not raise on the flop yet
                            if gamblers == 2:
                                #heads up situation
                                if equx < s.threshold_flop_bluff_vs_one:
                                    #fold
                                    #blocking bet defence
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.colors_on:
                                            print(settings.CYAN + "light call" + settings.RESET)
                                        else:
                                            print("light call")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)
                                    if newbet == 0:
                                        #check for strong draw before folding
                                        draw = common.strong_draw(settings.myflush, settings.mystraight)
                                        if draw:
                                            hamlet_choice = random.randint(1, s.faggression)
                                            if hamlet_choice < 10:
                                                #continue folding
                                                newbet = 0
                                            else:
                                                raise_or_call = random.randint(0, 80)
                                                if raise_or_call < s.faggression:
                                                    #raise
                                                    randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                                    newbet = biggest_bet*randomized_part_bet
                                                else:
                                                    #call
                                                    if s.stack < biggest_bet - s.bet:
                                                        newbet = s.stack
                                                    else:
                                                        newbet = biggest_bet - s.bet
                                                if settings.debug_postflop:
                                                    if settings.view < 4:
                                                        print("flop strong draw")
                                                    else:
                                                        print("ts-d")
                                                    if settings.debug_postflop_stop_point:
                                                        dumb = input("]")
                                                    else:
                                                        time.sleep(2)
                                                else:
                                                    pass
                                    if newbet == 0:
                                        #last move before folding is 2 street float and steal
                                        twostreet_aggression = (s.faggression + s.taggression)/2
                                        #print("twostreet aggression: " + str(twostreet_aggression))
                                        hamlet_choice = 0
                                        if twostreet_aggression > 34:
                                            hamlet_choice = random.randint(1, 4)
                                        elif twostreet_aggression < 25:
                                            hamlet_choice = random.randint(1, 6)
                                        else:
                                            hamlet_choice = random.randint(1, 5)
                                        #print("hamlet choice: " + str(hamlet_choice))
                                        #dumb = input("]")
                                        if hamlet_choice == 1:
                                            #call or fold
                                            if s.stack/smallblind < 41:
                                                #less than 20 BBs, fold you do not have stack for this move
                                                newbet = 0
                                            else:
                                                #call and set float-and-steal move for turn steal
                                                newbet = biggest_bet - s.bet
                                                s.floatandsteal = 1
                                                if settings.debug_postflop:    
                                                    print("float and steal part 1")
                                                    if settings.debug_postflop_stop_point:
                                                        dumb = input("]")
                                                    else:
                                                        time.sleep(2)

                                elif equx < s.threshold_flop_call_vs_one:
                                    #bluffraise or fold -+ on flop
                                    hamlet_choice = random.randint(1,61)
                                    if (hamlet_choice < s.faggression) and (s.stp > 2.5):
                                        #go for bluff raise
                                        newbet = 3*biggest_bet
                                        settings.raise_on_flop = 1
                                    else:
                                        #fold
                                        newbet = 0
                                    info.yesno(newbet, wait_for_showdown)
                                    
                                elif equx < s.threshold_flop_raise_vs_one:
                                    #call
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        newbet = biggest_bet - s.bet
                                elif equx >= s.threshold_flop_raise_vs_one:
                                    #raise or call flop -+
                                    hamlet_choice = random.randint(1,51)
                                    if hamlet_choice < s.faggression:
                                        info.yesno(1,wait_for_showdown)
                                        settings.raise_on_flop = 1
                                        #raise for value
                                        randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                        newbet = biggest_bet*randomized_part_bet
                                    else:
                                        info.yesno(0, wait_for_showdown)
                                        #call
                                        if s.stack < biggest_bet - s.bet:
                                            newbet = s.stack
                                        else:
                                            newbet = biggest_bet - s.bet
                                else:
                                    print("unknown decision based on equx on flop vs 1 opened")
                                    dumb = input("]")
                                if newbet == 0:
                                    #if the board is monotonne vs 1 we may float as he may try to steal.
                                    monotonne_board = 0
                                    monotonne_board = int(checkhands.monotonne_flop(t.board))
                                    if ((monotonne_board) and (not settings.raise_on_flop)):
                                        #good flop to cbet no matter what villain has so we may defend
                                        rnd = randint(0, 100)
                                        if rnd <= s.faggression:
                                            #we go for it
                                            rndd = randint(0,2)
                                            if rndd == 0:
                                                #flat call float
                                                newbet = biggest_bet - s.bet
                                            else:
                                                #raise
                                                randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                                newbet = biggest_bet*randomized_part_bet
                                            if settings.debug_postflop:
                                                print("defend monotonne board")
                                                if settings.debug_postflop_stop_point:
                                                    dumb = input("]")
                                                else:
                                                    time.sleep(2)

                            else:
                                #multipot
                                if equx < s.threshold_flop_call_vs_more:
                                    #fold
                                    #newbet = 0
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.colors_on:
                                            print(settings.CYAN + "light call" + settings.RESET)
                                        else:
                                            print("light call")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)
                                elif equx < s.threshold_flop_raise_vs_more:
                                    #call
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        newbet = biggest_bet - s.bet
                                else:
                                    #reraise
                                    settings.raise_on_flop = 1
                                    randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                    newbet = biggest_bet*randomized_part_bet
                        elif settings.raise_on_flop == 1:
                            #opened, raised on flop
                            if gamblers == 2:
                                #heads up situation
                                if equx < s.threshold_flop_call3bet_vs_one:
                                    #fold
                                    newbet = 0
                                elif equx < s.threshold_flop_raise4bet_vs_one:
                                    #call raised flop no need to check overbet
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        newbet = biggest_bet - s.bet
                                else:
                                        #reraise or call on raised flop-+
                                    hamlet_choice = random.randint(1,51)
                                    if hamlet_choice < s.faggression:
                                        info.yesno(1, wait_for_showdown)
                                        settings.raise_on_flop = 2
                                        newbet = 3*biggest_bet
                                    else:
                                        info.yesno(0, wait_for_showdown)
                                        #call
                                        if s.stack < biggest_bet - s.bet:
                                            newbet = s.stack
                                        else:
                                            newbet = biggest_bet - s.bet
                            else:
                                #multipot
                                if equx < s.threshold_flop_call3bet_vs_more:
                                    #fold
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.view < 4:
                                            if settings.colors_on:
                                                print(settings.CYAN + "light call" + settings.RESET)
                                            else:
                                                print("light call")
                                        else:
                                            print("light")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)
                                elif equx < s.threshold_flop_raise4bet_vs_more:
                                    #call
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        newbet = biggest_bet - s.bet
                                else:
                                    #reraise allin
                                    settings.raise_on_flop = 2
                                    newbet = common.roundbet(3*biggest_bet)
                        else: #there is a 4 bet check shove threshold
                                if equx >= s.threshold_flop_shove:
                                    newbet = s.stack
                                else:
                                    #fold
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.view < 4:
                                            if settings.colors_on:
                                                print(settings.CYAN + "light call" + settings.RESET)
                                            else:
                                                print("light call")
                                        else:
                                            print("light")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)

                    if newbet > 0 and newbet < smallblind:
                        newbet = 0
                    if s.stp < 0.2:
                        #allin
                        newbet += s.stack
                    if wait_for_showdown:
                        newbet = 0
                    if newbet > biggest_bet:
                        #new lead bettor
                        for sit in t.seats:
                            #clear previous leads
                            sit.betting_lead = 0
                        s.betting_lead = 1
                    else:
                        #lose betting lead
                        s.betting_lead = 0
                    s.acted_flop = 1

                elif len(t.board) == 8: #turn
                    equx = 0.0
                    gamblers = common.countNotFoldedYet(table)
                    if s.equx_turn > 0.0:
                        equx = s.equx_turn
                    else:
                        fcard1 = form.format_card_for_calculating(s.card1)
                        fcard2 = form.format_card_for_calculating(s.card2)
                        fboard = form.format_board_for_calculating(t.board)
                        resultlist = []
                        resultlist = calculator.find_equx(fcard1, fcard2, fboard)
                        equx = round(float(resultlist[1]), 2)
                    
                    common.overbet_postflop(t, s.name, equx, smallblind, ante)

                    pot = 0
                    for z in t.seats:
                        pot += z.bet
                        if z.card1 != "  ":
                            z.stp = common.getStackToPotRatio(t, z.name)
                    oppo_stps = []
                    for z in t.seats:
                        if z.card1 != "  ":
                            if z.name != s.name:
                                oppo_stps.append(z.stp)
                    weather.weatherboard(t)
                    weather.myweatherboard(t, s.name)
                    if settings.debug_postflop and (not common.wait_showdown(t, smallblind, ante)): 
                        info.report(2, gamblers, equx, s, smallest_bet, biggest_bet)
                    #turnbettinground
                    biggest_bet = common.find_biggest_bet(t)
                    if s.bet == biggest_bet:
                        #no one bet on the turn
                        if gamblers == 2:
                            #heads up situation
                            if s.stp < 1.1  and equx > (s.threshold_turn_open_vs_one - settings.checks_on_turn*settings.threshold_added_open_from_checks):
                                newbet = s.stack
                            elif equx >= (s.threshold_turn_open_vs_one - settings.checks_on_turn*settings.threshold_added_open_from_checks):
                                turn_threshold = 1.0/gamblers + 1.0/(3*gamblers) + common.check_to_the_raisor_effect(s.betting_lead)
                                #we may bet, based on board and weather and stps decide size
                                random_decision = round(random.uniform(0.0, 1.0),2)
                                random_decision -= (settings.checks_on_turn * 0.1)
                                if random_decision < turn_threshold:
                                    #we will bet decide how big based on stps, equx and weather
                                    newbet = common.roundbet(betsize.openbetturnsize(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t))
                                    if newbet == 0:
                                        settings.checks_on_turn += 1
                                else:
                                    #we may try to make turn steal
                                    newbet = common.roundbet(common.turnsteal_attack(s.taggression, t, wait_for_showdown, smallblind))
                                    if settings.turnstealing_attempt:
                                        if settings.debug_postflop:
                                            if settings.view < 4:
                                                print("turn steal attempt")
                                            else:
                                                print("ts-a")
                                            if settings.debug_postflop_stop_point:
                                                dumb = input("]")
                                            else:
                                                time.sleep(2)
                                        else:
                                            pass
                                    else:
                                        settings.checks_on_turn += 1
                                info.yesno(newbet, wait_for_showdown)
                            else:
                                #we may try to make turn steal
                                newbet = common.roundbet(common.turnsteal_attack(s.taggression, t, wait_for_showdown, smallblind))
                                if settings.turnstealing_attempt:
                                    if settings.debug_postflop:
                                        if settings.view < 4:
                                            print("turn steal attempt")
                                        else:
                                            print("ts-a")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(2)
                                    else:
                                        pass
                                else:
                                    settings.checks_on_turn += 1
                            if newbet == 0 and not wait_for_showdown:
                                #we may bluff on scary turn card heads up
                                scary_turn = 0
                                scary_turn = int(checkhands.turnAK(t.board))
                                if scary_turn:
                                    rnd = randint(0,90)
                                    if s.raggression <= rnd:
                                        #we go for it
                                        newbet = common.roundbet(betsize.openbetturnsize(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t))
                                        if settings.debug_postflop:
                                            if settings.view < 4:
                                                print("bluff on scary turn card")
                                            else:
                                                print("b-on-t")
                                            if settings.debug_postflop_stop_point:
                                                dumb = input("]")
                                            else:
                                                time.sleep(2)
                                if newbet == 0:
                                    #still we have option if we are float and steal:
                                    if s.floatandsteal:
                                        s.floatandsteal = 0
                                        newbet = common.roundbet(betsize.openbetturnsize(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t))
                                        if settings.debug_postflop:    
                                            print("float and steal part 2")
                                            if settings.debug_postflop_stop_point:
                                                dumb = input("]")
                                            else:
                                                time.sleep(2)
                        else:
                            #multipot
                            if s.stp < 1.1  and equx > (s.threshold_turn_open_vs_more - settings.checks_on_turn*settings.threshold_added_open_from_checks):

                                newbet = s.stack
                            elif equx >= (s.threshold_turn_open_vs_more - settings.checks_on_turn*settings.threshold_added_open_from_checks):
                                turn_threshold = 1.0/gamblers + 1.0/(3*gamblers)
                                random_decision = round(random.uniform(0.0, 1.0),2)
                                random_decision -= (settings.checks_on_turn * 0.1)
                                #we may bet, based on board and weather and stps decide size
                                if random_decision < turn_threshold :
                                    #we will bet decide how big based on stps, equx and weather
                                    newbet = common.roundbet(betsize.openbetturnsize(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t))
                                    if newbet > 0:
                                        pass
                                    else:
                                        #we may try to make turn steal
                                        newbet = int(common.turnsteal_attack(s.taggression, t, wait_for_showdown, smallblind))
                                        if settings.turnstealing_attempt:
                                            if settings.debug_postflop:
                                                if settings.view < 4:
                                                    print("turn steal attempt")
                                                else:
                                                    print("ts-a")
                                                if settings.debug_postflop_stop_point:
                                                    dumb = input("]")
                                                else:
                                                    time.sleep(2)
                                            else:
                                                pass
                                        else:
                                            settings.checks_on_turn += 1
                                else:
                                    #we may try to make turn steal
                                    newbet = common.roundbet(common.turnsteal_attack(s.taggression, t, wait_for_showdown, smallblind))
                                    if settings.turnstealing_attempt:
                                        if settings.debug_postflop:
                                            if settings.view < 4:
                                                print("turn steal attempt")
                                            else:
                                                print("ts-a")
                                            if settings.debug_postflop_stop_point:
                                                dumb = input("]")
                                            else:
                                                time.sleep(2)
                                        else:
                                            pass
                                    else:
                                        settings.checks_on_turn += 1
                                info.yesno(newbet, wait_for_showdown)
                            else:
                                #we may try to make turn steal
                                newbet = common.roundbet(common.turnsteal_attack(s.taggression, t, wait_for_showdown, smallblind))
                                if settings.turnstealing_attempt:
                                    if settings.debug_postflop:
                                        if settings.view < 4:
                                            print("turn steal attempt")
                                        else:
                                            print("ts-a")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(2)
                                        #umb = input("]")
                                    else:
                                        pass
                                else:
                                    settings.checks_on_turn += 1
                    else:
                        #already opened calculate pot odds
                        if not settings.raise_on_turn:
                            #not raise on the flop yet
                            if gamblers == 2:
                                #heads up situation
                                if equx < s.threshold_turn_bluff_vs_one:
                                    #defend from turn steal
                                    newbet = common.roundbet(common.turnsteal_defend(s.taggression, equx, s.bet, t))
                                    if settings.turnstealing_defend:
                                        if settings.debug_postflop:
                                            if settings.view < 4:
                                                print("turn steal defend")
                                            else:
                                                print("ts-d")
                                            if settings.debug_postflop_stop_point:
                                                dumb = input("]")
                                            else:
                                                time.sleep(2)
                                        else:
                                            pass
                                        settings.turnstealing_defend = 0 #clear flag
                                    if newbet == 0:
                                        newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet:
                                        pass
                                    else:
                                        #check for strong draw before folding
                                        draw = common.strong_draw(settings.myflush, settings.mystraight)
                                        if draw:
                                            hamlet_choice = random.randint(1, s.taggression)
                                            if hamlet_choice < 10:
                                                #continue folding
                                                newbet = 0
                                            else:
                                                raise_or_call = random.randint(0, 80)
                                                if raise_or_call < s.taggression:
                                                    #raise
                                                    randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                                    newbet = biggest_bet*randomized_part_bet
                                                else:
                                                    #call
                                                    if s.stack < biggest_bet - s.bet:
                                                        newbet = s.stack
                                                    else:
                                                        newbet = biggest_bet - s.bet
                                                if settings.debug_postflop:
                                                    if settings.view < 4:
                                                        print("turn strong draw")
                                                    else:
                                                        print("ts-d")
                                                    if settings.debug_postflop_stop_point:
                                                        dumb = input("]")
                                                    else:
                                                        time.sleep(2)
                                                else:
                                                    pass
                                        if newbet == 0:
                                            #still we have option if we are float and steal:
                                            if s.floatandsteal:
                                                s.floatandsteal = 0 #raise for bluff
                                                randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                                newbet = biggest_bet*randomized_part_bet
                                                if settings.debug_postflop:
                                                    print("float and steal part 2")
                                                    if settings.debug_postflop_stop_point:
                                                        dumb = input("]")
                                                    else:
                                                        time.sleep(2)
                                            
                                elif equx < s.threshold_turn_call_vs_one:
                                    #bluffraise turn -+
                                    hamlet_choice = random.randint(1,61)
                                    if (hamlet_choice < s.taggression) and (s.stp > 2.5):
                                        newbet = common.roundbet(3*biggest_bet)
                                        settings.raise_on_turn = 1
                                    else:
                                        #fold
                                        newbet = 0
                                    info.yesno(newbet, wait_for_showdown)
                                elif equx < s.threshold_turn_raise_vs_one:
                                    #call
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        newbet = biggest_bet - s.bet
                                elif equx >= s.threshold_turn_raise_vs_one:
                                    hamlet_choice = random.randint(1,51)
                                    if hamlet_choice < s.taggression:
                                        info.yesno(1, wait_for_showdown)
                                        settings.raise_on_turn = 1
                                        randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                        newbet = biggest_bet*randomized_part_bet
                                    else:
                                        info.yesno(0, wait_for_showdown)
                                        #call
                                        if s.stack < biggest_bet - s.bet:
                                            newbet = s.stack
                                        else:
                                            newbet = biggest_bet - s.bet
                                else:
                                    print("unknown decision based on equx on turn vs 1 opened")
                                    dumb = input("]")

                            else:
                                #multipot
                                if equx < s.threshold_turn_call_vs_more:
                                    #defend from turn steal
                                    newbet = common.roundbet(common.turnsteal_defend(s.taggression, equx, s.bet, t))
                                    if settings.turnstealing_defend:
                                        if settings.debug_postflop:
                                            if settings.view < 4:
                                                print("turn steal defend")
                                            else:
                                                print("ts-d")
                                            if settings.debug_postflop_stop_point:
                                                dumb = input("]")
                                            else:
                                                time.sleep(2)
                                        else:
                                            pass
                                        settings.turnstealing_defend = 0 #clear flag
                                elif equx < s.threshold_turn_raise_vs_more:
                                    #call
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        biggest_bet - s.bet
                                else:
                                    #reraise
                                    settings.raise_on_turn = 1
                                    randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                    newbet = biggest_bet*randomized_part_bet
                        elif settings.raise_on_turn == 1:
                            #opened, raised on turn
                            if gamblers == 2:
                                #heads up situation
                                if equx < s.threshold_turn_call3bet_vs_one:
                                    #fold
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.view < 4:
                                            if settings.colors_on:
                                                print(settings.CYAN + "light call" + settings.RESET)
                                            else:
                                                print("light call")
                                        else:
                                            print("light")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)
                                elif equx < s.threshold_turn_raise4bet_vs_one:
                                    #call
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        newbet = biggest_bet - s.bet
                                else:
                                    #raise for value
                                    settings.raise_on_turn = 2
                                    newbet = common.roundbet(3*biggest_bet)
                            else:
                                #multipot
                                if equx < s.threshold_turn_call3bet_vs_more:
                                    #fold
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.view < 4:
                                            if settings.colors_on:
                                                print(settings.CYAN + "light call" + settings.RESET)
                                            else:
                                                print("light call")
                                        else:
                                            print("light")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)
                                elif equx < s.threshold_turn_raise4bet_vs_more:
                                    #call
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        newbet = biggest_bet - s.bet
                                else:
                                    #reraise allin
                                    settings.raise_on_turn = 2
                                    newbet = common.roundbet(3*biggest_bet)
                        else: #there is a 4 bet check shove threshold
                                if equx >= s.threshold_turn_shove:
                                    newbet = s.stack
                                else:
                                    #fold
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.view < 4:
                                            if settings.colors_on:
                                                print(settings.CYAN + "light call" + settings.RESET)
                                            else:
                                                print("light call")
                                        else:
                                            print("light")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)

                    if newbet > 0 and newbet < smallblind:
                        newbet = 0
                    if s.stp < 0.2:
                        #allin
                        newbet += s.stack
                    if wait_for_showdown:
                        newbet = 0
                    if newbet > biggest_bet:
                        #new lead bettor
                        for sit in t.seats:
                            #clear previous leads
                            sit.betting_lead = 0
                        s.betting_lead = 1
                    else:
                        #lose betting lead
                        s.betting_lead = 0
                    s.acted_turn = 1


                elif len(t.board) == 10: #river
                    equx = 0.0
                    gamblers = common.countNotFoldedYet(table)
                    if s.equx_river > 0.0:
                        equx = s.equx_river
                    else:
                        fcard1 = form.format_card_for_calculating(s.card1)
                        fcard2 = form.format_card_for_calculating(s.card2)
                        fboard = form.format_board_for_calculating(t.board)
                        resultlist = []
                        resultlist = calculator.find_equx(fcard1, fcard2, fboard)
                        equx = round(float(resultlist[1]), 2)

                    common.overbet_postflop(t, s.name, equx, smallblind, ante)

                    pot = 0
                    for z in t.seats:
                        pot += z.bet
                        if z.card1 != "  ":
                            z.stp = common.getStackToPotRatio(t, z.name)
                    oppo_stps = []
                    for z in t.seats:
                        if z.card1 != "  ":
                            if z.name != s.name:
                                oppo_stps.append(z.stp)
                    weather.weatherboard(t)
                    weather.myweatherboard(t, s.name)
                    if settings.debug_postflop and (not common.wait_showdown(t, smallblind, ante)):  
                        info.report(3, gamblers, equx, s, smallest_bet, biggest_bet)
                    #riverbettinground
                    biggest_bet = common.find_biggest_bet(t)
                    if s.bet == biggest_bet:
                        #no one bet on the turn
                        if gamblers == 2:
                            #heads up situation
                            if s.stp < 1.1  and equx > (s.threshold_river_open_vs_one - settings.checks_on_river*settings.threshold_added_open_from_checks):
                                newbet = s.stack
                            elif equx > (s.threshold_river_open_vs_one - settings.checks_on_river*settings.threshold_added_open_from_checks):
                                river_threshold = 1.0/gamblers + 1.0/(2*gamblers) + common.check_to_the_raisor_effect(s.betting_lead)
                                #we may bet, based on board and weather and stps decide size
                                random_decision = round(random.uniform(0.0, 1.0),2)
                                random_decision -= (settings.checks_on_river * 0.1)
                                if random_decision < river_threshold:
                                    #we will bet decide how big based on stps, equx and weather
                                    newbet = betsize.openbetriversize(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t)
                                    if newbet == 0:
                                        settings.checks_on_river += 1
                                else:
                                    newbet = 0
                                    settings.checks_on_river += 1
                                info.yesno(newbet, wait_for_showdown)
                            elif equx < s.threshold_river_bluff_vs_one: #blufopen
                                hamlet_choice = random.randint(1,80)
                                if hamlet_choice < s.raggression and s.stack >= pot/2:
                                    #bluff open
                                    newbet = betsize.openbetriversize(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t)
                                else:
                                    #check call
                                    newbet = 0
                                    settings.checks_on_river += 1
                                info.yesno(newbet, wait_for_showdown)
                            else:
                                #check call
                                newbet = 0
                                settings.checks_on_river += 1
                            if newbet == 0 and not wait_for_showdown:
                                #we may bluff on scary river card heads up
                                scary_river = 0
                                scary_river = int(checkhands.riverAK(t.board))
                                if scary_river:
                                    rnd = randint(0,100)
                                    if s.raggression <= rnd:
                                        #we go for it
                                        newbet = betsize.openbetriversize(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t)
                                        if settings.debug_postflop:
                                            if settings.view < 4:
                                                print("bluff on scary river card")
                                            else:
                                                print("b-on-r")
                                            if settings.debug_postflop_stop_point:
                                                dumb = input("]")
                                            else:
                                                time.sleep(2)
                        else:
                            #multipot
                            if s.stp < 1.1  and equx > (s.threshold_river_open_vs_more - settings.checks_on_river*settings.threshold_added_open_from_checks):
                                newbet = s.stack
                            elif equx > (s.threshold_river_open_vs_more - settings.checks_on_river*settings.threshold_added_open_from_checks):
                                river_threshold = 1.0/gamblers + 1.0/(2*gamblers)
                                #we may bet, based on board and weather and stps decide size
                                random_decision = round(random.uniform(0.0, 1.0),2)
                                random_decision -= (settings.checks_on_river * 0.1)
                                if random_decision < river_threshold:
                                    #we will bet decide how big based on stps, equx and weather
                                    newbet = betsize.openbetriversize(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t)
                                    if newbet > 0:
                                        pass
                                    else:
                                        settings.checks_on_river += 1
                                else:
                                    newbet = 0
                                    settings.checks_on_river += 1
                                info.yesno(newbet, wait_for_showdown)
                            else:
                                #check
                                newbet = 0
                                settings.checks_on_river += 1
                        if newbet == 0:
                            river_acted_counter = 0
                            for si in t.seats:
                                if si.card1 != "  ":
                                    if si.acted_river:
                                        river_acted_counter += 1

                            if gamblers == 2 and river_acted_counter == 1:
                                if equx > (s.threshold_river_open_vs_one - settings.checks_on_river*settings.threshold_added_open_from_checks):
                                    #don't miss river value bet
                                    newbet = betsize.openbetriversize(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t)
                                    if settings.debug_postflop:
                                        print("river bet")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)
                            elif gamblers == (river_acted_counter + 1):
                                #don't miss river value bet
                                if equx > (s.threshold_river_open_vs_more - settings.checks_on_river*settings.threshold_added_open_from_checks):
                                    newbet = betsize.openbetriversize(oppo_stps, s.stp, settings.straight, settings.flush, settings.mystraight, settings.myflush, equx, pot, s.bet, biggest_bet, game_type, smallblind, ante, t)
                                    if settings.debug_postflop:
                                        print("river bet")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)
                    else:
                        #already opened calculate pot odds
                        if not settings.raise_on_river:
                            #not raise on the flop yet
                            if gamblers == 2:
                                #heads up situation
                                if equx < s.threshold_river_bluff_vs_one:
                                    #bluffraise river or fold-+
                                    hamlet_choice = random.randint(1,95)
                                    if (hamlet_choice < s.raggression) and (s.stp > 2.5):
                                        #you need big stack 2.5*pot to be able to bluff raise
                                        randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                        newbet = biggest_bet*randomized_part_bet
                                        settings.raise_on_river = 1
                                    else:
                                        newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                        if newbet and settings.debug_postflop:
                                            if settings.view < 4:
                                                if settings.colors_on:
                                                    print(settings.CYAN + "light call" + settings.RESET)
                                                else:
                                                    print("light call")
                                            else:
                                                print("light")
                                            if settings.debug_postflop_stop_point:
                                                dumb = input("]")
                                            else:
                                                time.sleep(settings.bot_time_to_act_turn*2)
                                    info.yesno(newbet, wait_for_showdown)
                                elif equx < s.threshold_river_raise_vs_one:
                                    #call but sometimes make tough fold on the river
                                    random_decision = random.randint(0,110)
                                    if random_decision < 50 - s.raggression and s.stp > 2:
                                        #we need 2 conditions for hero fold:
                                        #1.we have enough stack
                                        #2. (10 - 30) random based on river aggressionzzzzzzzzzzzz
                                        #hero fold
                                        if settings.debug_postflop:
                                            print("tough fold")
                                            if settings.debug_postflop_stop_point:
                                                dumb = input("]")
                                            else:
                                                time.sleep(2)
                                        newbet = 0
                                    else:
                                        #call
                                        if s.stack < biggest_bet - s.bet:
                                            newbet = s.stack
                                        else:
                                            newbet = biggest_bet - s.bet
                                    info.yesno(newbet, wait_for_showdown)
                                elif equx >= s.threshold_river_raise_vs_one:
                                    settings.raise_on_river = 1
                                    #raise for  or value on river 100% -+
                                    randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                    newbet = biggest_bet*randomized_part_bet
                                else:
                                    print("unknown decision based on equx on river vs 1 opened")
                                    dumb = input("]")
                                # we may get bluffed on scary river so we can call lighter
                                if newbet == 0:
                                    scary_river = 0
                                    scary_river = int(checkhands.riverAK(t.board))
                                    if scary_river:
                                        #we can call lighter
                                        river_light_call_aggression_factor = 0.0
                                        river_light_call_aggression_factor = s.raggression/100.0
                                        decision_river_call_light = 0.80 - river_light_call_aggression_factor
                                        if equx >= decision_river_call_light:
                                            #hero call
                                            newbet = biggest_bet - s.bet
                                            if settings.debug_postflop:
                                                if settings.view < 4:
                                                    print("hero call on scary river card")
                                                else:
                                                    print("h-c")
                                                if settings.debug_postflop_stop_point:
                                                    dumb = input("]")
                                                else:
                                                    time.sleep(2)
                            else:
                                #multipot
                                if equx < s.threshold_river_call_vs_more:
                                    #fold
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.view < 4:
                                            if settings.colors_on:
                                                print(settings.CYAN + "light call" + settings.RESET)
                                            else:
                                                print("light call")
                                        else:
                                            print("light")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)
                                elif equx < s.threshold_river_raise_vs_more:
                                    #call
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        newbet = biggest_bet - s.bet
                                else:
                                    #reraise
                                    settings.raise_on_river = 1
                                    randomized_part_bet = common.get_street_aggression(t, s.name)/10
                                    newbet = biggest_bet*randomized_part_bet
                        elif settings.raise_on_river == 1:
                            #opened, raised on river
                            if gamblers == 2:
                                #heads up situation
                                if equx < s.threshold_river_call3bet_vs_one:
                                    #fold
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.view < 4:
                                            if settings.colors_on:
                                                print(settings.CYAN + "light call" + settings.RESET)
                                            else:
                                                print("light call")
                                        else:
                                            print("light")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)
                                elif equx < s.threshold_river_raise4bet_vs_one:
                                    #call
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        newbet = biggest_bet - s.bet
                                else:
                                    #raise for value
                                    settings.raise_on_river = 2
                                    newbet = common.roundbet(3*biggest_bet)
                            else:
                                #multipot
                                if equx < s.threshold_river_call3bet_vs_more:
                                    #fold
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.view < 4:
                                            if settings.colors_on:
                                                print(settings.CYAN + "light call" + settings.RESET)
                                            else:
                                                print("light call")
                                        else:
                                            print("light")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)
                                elif equx < s.threshold_river_raise4bet_vs_more:
                                    #call
                                    if s.stack < biggest_bet - s.bet:
                                        newbet = s.stack
                                    else:
                                        newbet = biggest_bet - s.bet
                                else:
                                    #reraise allin
                                    settings.raise_on_river = 2
                                    newbet = common.roundbet(3*biggest_bet)
                        else: #there is a 4 bet check shove threshold
                                if equx >= s.threshold_river_shove:
                                    newbet = s.stack
                                else:
                                    newbet = common.blocking_bet_defense(equx, pot, (biggest_bet - s.bet), len(t.board))
                                    if newbet and settings.debug_postflop:
                                        if settings.view < 4:
                                            if settings.colors_on:
                                                print(settings.CYAN + "light call" + settings.RESET)
                                            else:
                                                print("light call")
                                        else:
                                            print("light")
                                        if settings.debug_postflop_stop_point:
                                            dumb = input("]")
                                        else:
                                            time.sleep(settings.bot_time_to_act_turn*2)

                    if ((equx >= 0.8) and (s.bet == biggest_bet)):
                        if settings.checks_on_river + 1 == gamblers:
                            #dont miss value bet on the river
                            newbet = common.roundbet((2*pot/3)) 
                    if newbet > 0 and newbet < smallblind:
                        newbet = 0
                    if s.stp < 0.2:
                        #allin
                        newbet += s.stack
                    if wait_for_showdown:
                        newbet = 0
                    if newbet > biggest_bet:
                        #new lead bettor
                        for sit in t.seats:
                            #clear previous leads
                            sit.betting_lead = 0
                        s.betting_lead = 1
                    else:
                        #lose betting lead
                        s.betting_lead = 0
                    s.acted_river = 1
                else:
                    print("error do not know on which street are we")
                    dumb = input("]")
        
            else:
                biggest_bet = common.find_biggest_bet(t)
                if s.bet == biggest_bet:
                    if len(t.board) < 2:
                        #preflop
                        if s.acted_preflop == 1:
                            return
                    elif len(t.board) == 6:
                        #flop
                        if s.acted_flop == 1:
                            return
                    elif len(t.board) == 8:
                        #turn
                        if s.acted_turn == 1:
                            return
                    elif len(t.board) == 10:
                        #river
                        if s.acted_river == 1:
                            return
                            #we have acted someone has called, so go to next round
                try:
                    #these here are not to break debug_postflop
                    situation = ""
                    respond_range = []
                    situation = preflop.preflop_interpreter(t, s.name, smallblind, ante)
                    respond_range = selectrange.rangeselector(situation, t, s.name, smallblind, ante)
                    pot = 0
                    for tt in t.seats:
                        pot += tt.bet
                    biggest_bet = common.find_biggest_bet(t)
                    if settings.autopilot:
                            print("call")
                            time.sleep(2)
                            newbet = biggest_bet - s.bet
                    else:
                        #act
                        if (not wait_for_showdown) or ((s.bet < biggest_bet) and s.stack > 0):
                            if settings.view < 4:
                                if settings.colors_on:
                                    print(settings.GREY)
                                    print("|f:fold/check| |c:call| |m:min| |h:half|")
                                    print("|b:2/3| t:3/4| |p:pot | |r:3x| |d:pot*2|")
                                    print("|j/a:allin| |o:pot+1/2| or|enter number|")
                                    print(settings.RESET)
                                else:
                                    print("|f:fold/check| |c:call| |m:min| |h:half|")
                                    print("|b:2/3| t:3/4| |p:pot | |r:3x| |d:pot*2|")
                                    print("|j/a:allin| |o:pot+1/2| or|enter number|")

                            hero_didnt_open_preflop = 0
                                
                            if s.bet < biggest_bet:
                                if ((len(t.board) < 2) and (biggest_bet > (2*smallblind + ante))):
                                    #preflop set flag
                                    hero_didnt_open_preflop = 1
                                if settings.view < 4:
                                    print("<" + str(int(biggest_bet - s.bet)) + " to call>")
                                else:
                                    print("-" + str(int(biggest_bet - s.bet)))

                            valid_bet = 0
                            while(valid_bet == 0):
                                shortcutbet = input("]")
                                if len(shortcutbet) > 1:
                                    if shortcutbet.isdigit():
                                        amount = common.roundbet(shortcutbet)
                                        if amount >= s.stack:
                                            #allin
                                            newbet = common.roundbet(shortcutbet) + s.bet
                                        else:
                                            newbet = common.roundbet(shortcutbet)
                                        valid_bet = 1
                                    else:
                                        if settings.colors_on:
                                            print(settings.RED + "Dealer: " + settings.GREY + "place bet again" + settings.RESET)
                                        else:
                                            print("Dealer: place bet again")
                                elif shortcutbet == 'f' or not shortcutbet:
                                    #fold/check
                                    if s.bet == biggest_bet:
                                        #it is a check
                                        if len(t.board) == 6:
                                            settings.checks_on_flop += 1
                                        elif len(t.board) == 8:
                                            settings.checks_on_turn += 1
                                        elif len(t.board) == 10:
                                            settings.checks_on_river += 1
                                        else:
                                            pass
                                    newbet = 0
                                    valid_bet = 1
                                elif shortcutbet == 't':
                                    #bet
                                    newbet = common.roundbet(3*pot/4)
                                    if len(t.board) < 2:
                                        #preflop:
                                        newbet = common.roundbet(smallblind*6 - s.bet)
                                    valid_bet = 1
                                elif shortcutbet == 'b':
                                    #bet
                                    newbett = 2*pot/3
                                    if len(t.board) < 2:
                                        #preflop:
                                        if game_type == 'h' or game_type == 's':
                                            newbett = smallblind*4
                                        else:
                                            newbett = smallblind*6
                                    newbet = common.roundbet(newbett)
                                    valid_bet = 1

                                elif shortcutbet == 'h':
                                    #halfpot bet
                                    newbet = common.roundbet(pot/2)
                                    if len(t.board) < 2:
                                        #preflop: limp
                                        if s.stack < biggest_bet - s.bet:
                                            newbet = s.stack*2
                                            #s.stack = 0 #explicit allin
                                        else:
                                            newbet = biggest_bet - s.bet
                                    valid_bet = 1
                                elif shortcutbet == 'c':
                                    #call
                                    if s.stack <= biggest_bet - s.bet:
                                        newbet = s.stack*20
                                        #s.stack = 0 #explicit allin
                                    else:
                                        newbet = biggest_bet - s.bet
                                    valid_bet = 1
                                elif shortcutbet == 'p':
                                    #pot bet
                                    newbet = pot
                                    valid_bet = 1
                                elif shortcutbet == 'o':
                                    #overbet pot
                                    newbet = common.roundbet(pot*1.5)
                                    valid_bet = 1
                                elif shortcutbet == 'd':
                                    #overbet pot
                                    newbet = common.roundbet(pot*2)
                                    valid_bet = 1
                                elif shortcutbet == 'r':
                                    #reraise
                                    newbet = biggest_bet*3
                                    valid_bet = 1
                                elif shortcutbet == 'a' or shortcutbet == 'j':
                                    newbet = s.stack*20
                                    #s.stack = 0 #explicit allin
                                    valid_bet = 1
                                elif shortcutbet == 'm':
                                    newbet = biggest_bet - s.bet + smallblind*2
                                    valid_bet = 1
                                elif shortcutbet.isdigit():
                                    newbet = common.roundbet(shortcutbet)
                                    valid_bet = 1
                                else:
                                    if settings.colors_on:
                                        print(settings.RED + "Dealer: " + settings.GREY + "place bet again" + settings.RESET)
                                    else:
                                        print("Dealer: place bet again")

                        else:
                            #we are waiting for showdown
                            newbet = 0
                            valid_bet = 1

                        if newbet!= 0 and s.stack == 0 and s.name == settings.hero:
                            s.preallin += 1
                            s.last5betscrazy += 2

                        if newbet > 5*biggest_bet and s.name == settings.hero: #maniac counter
                            settings.crazybets_hero += 1
                            s.prebigbet += 1
                            s.last5betscrazy += 2

                        if s.last5betscrazy and s.name == settings.hero and not wait_for_showdown:
                            s.last5betscrazy -= 1

                        if s.name == settings.hero:
                            for sss in t.seats:
                                if sss.name == settings.hero:
                                    settings.preorbits_hero = sss.preorbits

                    #update player allin percentage
                    if len(t.board) == 6:
                        if pot <= smallblind*3 + 6*ante:
                            pass
                        else:
                            settings.threebet = 1

                    if (newbet > 0) and (newbet < smallblind*2 + ante) and (s.stack > 0):
                        if len(t.board) > 5:
                            newbet = 0
                            if settings.view < 4:
                                if s.bet == biggest_bet:
                                    print("check")
                                else:
                                    print("fold")
                                time.sleep(2)
                            

                    if ((newbet + s.bet < biggest_bet) and (s.stack > 0)):
                        newbet = 0
                        if settings.view < 4:
                            if s.bet == biggest_bet:
                                print("check")
                            else:
                                print("fold")
                            time.sleep(2)

                    if newbet > biggest_bet:
                        #clear previous betting lead
                        for btz in t.seats:
                            btz.betting_lead = 0
                        s.betting_lead = 1
                    else:
                        #lose betting lead
                        s.betting_lead = 0

                    if len(t.board) < 2 and hero_didnt_open_preflop:
                        #preflop 3bets
                        if newbet > 1.9*biggest_bet:
                            s.last3bets += 1
                        else:
                            if s.last3bets > 0:
                                s.last3bets -= 1

                    if len(t.board) < 2:
                        #preflop
                        s.acted_preflop = 1
                    elif len(t.board) == 6:
                        #flop
                        s.acted_flop = 1
                    elif len(t.board) == 8:
                        #turn
                        s.acted_turn = 1
                    elif len(t.board) == 10:
                        #river
                        s.acted_river = 1
                    else:
                        print("error in act unknown street")
                        dumb = input("]")


                except:
                    if s.last5betscrazy and len(t.board) == 6: # 6= on the flop 8 = turn 10 = river:
                        s.last5betscrazy -= 1
                    if len(t.board) < 2:
                        #preflop
                        s.acted_preflop = 1
                    elif len(t.board) == 6:
                        #flop
                        s.acted_flop = 1
                    elif len(t.board) == 8:
                        #turn
                        s.acted_turn = 1
                    elif len(t.board) == 10:
                        #river
                        s.acted_river = 1
                    else:
                        print("error in act unknown street")
                        dumb = input("]")
                    if settings.view < 4:
                        if s.bet == biggest_bet:
                            print("check")
                        else:
                            print("fold")
                    time.sleep(2)
                    newbet = 0

            #hand history
            if settings.hand_history:
                for seeds in t.seats:
                    seeds.oldbet = seeds.bet
                biggest_bet = common.find_biggest_bet(t)
                history_line = ""
                if newbet <= 0:
                    common.update_total_pot(t)
                    if oldbet < common.find_biggest_bet(t):
                        history_line = s.name + ": fold" + "\n"
                        s.card1 = "  "
                        s.card2 = "  "
                        s.clock = " "
                    else:
                        history_line = s.name + ": check" + "\n"
                else:
                    if st == 0:
                        s.vbetflag = 1
                    else:
                        s.cbetflag = 1
                    if newbet >= s.stack:
                        s.bet = s.stack + oldbet
                        s.stack = 0
                    else:
                        s.bet = newbet + oldbet
                        s.stack = (s.stack - newbet)
                    if s.bet == biggest_bet:
                        common.update_total_pot(t)
                        history_line = s.name + ": call " + str(s.bet - s.oldbet) + "\n"
                    else:
                        common.update_total_pot(t)
                        history_line = s.name + ": bet " + str(s.bet - s.oldbet) + "\n"
                settings.total_pot = 0
                for seeds in t.seats:
                    settings.total_pot += seeds.bet
                settings.hand_history_buffer.add_line(history_line)
            else:
                if newbet <= 0:
                    if oldbet < common.find_biggest_bet(t):
                        s.card1 = "  "
                        s.card2 = "  "
                        s.clock = " "
                    else:
                        pass
                else:
                    if st == 0:
                        s.vbetflag = 1
                    else:
                        s.cbetflag = 1
                    if newbet >= s.stack:
                        s.bet = s.stack + oldbet
                        s.stack = 0
                    else:
                        s.bet = newbet + oldbet
                        s.stack = (s.stack - newbet)

        t.pot = 0
        for s in t.seats:
            t.pot += s.bet
    else:
        pass

    for s in t.seats:
        s.clock = " " 