#copyright (c) 2019
#jodathecoda@yahoo.com

import settings
import common
from random import randint

def rangeselector(situation, table, botname, smallblind, ante):
    if botname not in settings.allfishes:
        #player on board so this doesn't matter
        selected_range = []
        for h in settings.tough_spot_range:
            selected_range.append(h)
        return selected_range

    t = table
    playing_this_hand_light = 0
    bot_aggression = 0
    posname = common.getPreflopPosition_name(table, botname)
    stp = common.getStackToPotRatio(table, botname)
    index = 0
    counter = 0
    villain_bet = 0
    villain_stack = 0
    villain_index = 0
    selected_range = []
    for s in t.seats:
        if s.name == botname:
            bot_aggression = s.paggression
            index = counter
        counter += 1
    rnd = randint(0,250)
    if bot_aggression > rnd:
        playing_this_hand_light = 1

    #if we play against the bully at the table
    #the one who has highest vbet, then add more hands
    #this is for cahs and mtt only
    botes = common.count_players_on_table(t)
    if botes > 3:
        biggest_bet = common.find_biggest_bet(t)
        biggest_vbet = 0
        for ss in t.seats:
            if ss.vbet > biggest_vbet:
                biggest_vbet = ss.bet

        #if biggest bet player is biggest vbet
        #add bully range
        for ss in t.seats:
            if (ss.bet == biggest_bet) and (ss.vbet == biggest_vbet) and (s.vbet > 0):
                playing_this_hand_light = 1

    selected_range = t.seats[index].range_fold

    number_of_big_blinds = round(t.seats[index].stack/smallblind*2, 2)
    if situation == "maniac-on-board":
        #we can call lighter if 1 vs 1
        gamblers = common.countNotFoldedYet(table) #this includes you
        if gamblers == 2:
            selected_range = t.seats[index].range_safe
            common.debugranges(situation, "range_safe")
        else:
            selected_range = t.seats[index].range_top2_7
            common.debugranges(situation, "range_top2_7")
    elif situation == "10BB+opened-raised-back-to-original-opener":
        #your range is actually your open range, but since it is 3 bet pot cut it regarding 3bet size
        hero_position = common.getPreflopPosition_name(t, botname)

        if settings.hudanalyser == 1 and botname == "redfish":
            selected_range = t.seats[index].hd_call3bet_hudanalyzer
            t.seats[index].learning_range_name = "hd_call3bet_huanalyzer"
            common.debugranges(situation, "hd_call3bet_huanalyzer")
        
        elif hero_position == "ug":
            selected_range = t.seats[index].range_ug_open
            t.seats[index].learning_range_name = "range_ug_open"
            common.debugranges(situation, "range_ug_open_cutted")
        elif hero_position == "hj":
            selected_range = t.seats[index].range_hj_open
            t.seats[index].learning_range_name = "range_hj_open"
            common.debugranges(situation, "range_hj_open_cutted")
        elif hero_position == "co":
            selected_range = t.seats[index].range_co_open
            t.seats[index].learning_range_name = "range_co_open"
            common.debugranges(situation, "range_co_open_cutted")
        elif hero_position == "db":
            selected_range = t.seats[index].range_db_open
            t.seats[index].learning_range_name = "range_db_open"
            common.debugranges(situation, "range_db_open_cutted")
        elif hero_position == "sb":
            selected_range = t.seats[index].range_sb_open
            t.seats[index].learning_range_name = "range_sb_open"
            common.debugranges(situation, "range_sb_open_cutted")
        elif hero_position == "hd":
            selected_range = t.seats[index].range_hd_open
            t.seats[index].learning_range_name = "range_hd_open"
            common.debugranges(situation, "range_hd_open_cutted")
    elif situation == "allin10BB-wearehere-0behind":
        if settings.nash_push_fold:
            selected_range = t.seats[index].range_nash_heads_up_10bb_call
            t.seats[index].learning_range_name = "range_nash_heads_up_10bb_call"
            common.debugranges(situation, "range_nash_heads_up_10bb_call")
        else:
            if settings.nash_push_fold:
                selected_range = t.seats[index].range_nash_heads_up_10bb_call
                t.seats[index].learning_range_name = "range_nash_heads_up_10bb_call"
                common.debugranges(situation, "range_nash_heads_up_10bb_call")
            else:
                selected_range = t.seats[index].range_call_vs_under10bb_push_0_left_behind
                t.seats[index].learning_range_name = "range_call_vs_under10bb_push_0_left_behind"
                common.debugranges(situation, "range_call_vs_under10bb_push_0_left_behind")
    elif situation == "allin10BB-wearehere-1behind":
        selected_range = t.seats[index].range_call_vs_under10bb_push_1_left_behind
        t.seats[index].learning_range_name = "range_call_vs_under10bb_push_1_left_behind"
        common.debugranges(situation, "range_call_vs_under10bb_push_1_left_behind")
    elif situation == "allin10BB-wearehere-morebehind":
        selected_range = t.seats[index].range_call_vs_under10bb_push_more_left_behind
        t.seats[index].learning_range_name = "range_call_vs_under10bb_push_more_left_behind"
        common.debugranges(situation, "range_call_vs_under10bb_push_more_left_behind")
    elif situation == "allin10BB+call-wearehere-0behind":
        if number_of_big_blinds < 5:
            selected_range = t.seats[index].range_db_open
            t.seats[index].learning_range_name = "range_db_open"
            common.debugranges(situation, "range_db_open")
        elif number_of_big_blinds < 10:
            selected_range = t.seats[index].range_top6 + t.seats[index].range_pp
            common.debugranges(situation, "range_top6+pocket_pairs")
        elif number_of_big_blinds < 15:
            selected_range = t.seats[index].range_top1 + t.seats[index].range_ak
            common.debugranges(situation, "range_top1+ak")
        else:
            selected_range = t.seats[index].range_top1
            common.debugranges(situation, "range_top1")
    elif situation == "allin10BB+call-wearehere-1behind":
        if number_of_big_blinds < 15:
            selected_range = t.seats[index].range_top1 + t.seats[index].range_ak
            common.debugranges(situation, "range_top1+ak")
        else:
            common.debugranges(situation, "allin10BB+call-wearehere-1behind range fold")
    elif situation == "allin10BB+call-wearehere-morebehind":
        if number_of_big_blinds < 15:
            selected_range = t.seats[index].range_top1 + t.seats[index].range_ak
            common.debugranges(situation, "range_top1+ak")
        else:
            common.debugranges(situation, "range_fold")
    elif situation == "allin10BB+wearehere-0behind":
        counter = 0
        for s in t.seats:
            if common.checkAllin(s):
                villain_index = counter
            counter += 1
        if t.seats[villain_index].last5betscrazy >= 2:
            selected_range = t.seats[index].range_safe
            common.debugranges(situation, "range_safe")
        elif t.seats[villain_index].bet < smallblind*40 + 6*ante:
            selected_range = t.seats[index].range_top1_8 + t.seats[index].range_ak
            common.debugranges(situation, "range_top1_8+ak")
        else:
            selected_range = t.seats[index].range_top1
            common.debugranges(situation, "range_top1")
    elif situation == "allin10BB+wearehere-1behind":
        counter = 0
        for s in t.seats:
            if common.checkAllin(s):
                villain_index = counter
            counter += 1
        if t.seats[villain_index].last5betscrazy >= 2:
            selected_range = t.seats[index].range_safe
            common.debugranges(situation, "range_safe")
        elif t.seats[villain_index].bet < smallblind*40 + 6*ante:
            selected_range = t.seats[index].range_top1_8 + t.seats[index].range_ak
            common.debugranges(situation, "range_top1_8+ak")
        else:
            selected_range = t.seats[index].range_top1
            common.debugranges(situation, "range_top1")
    elif situation == "allin10BB+wearehere-morebehind":
        selected_range = t.seats[index].range_top1
        common.debugranges(situation, "range_top1")
    elif situation == "2allins-0behind":
        villain1_index = 0
        villain2_index = 0
        counter = 0
        for s in t.seats:
            if common.checkAllin(s):
                villain2_index = counter
            counter += 1
        counter = 0
        for s in t.seats:
            if common.checkAllin(s):
                if villain2_index != counter:
                    villain1_index = counter
            counter += 1
        if t.seats[villain1_index].bet + t.seats[villain2_index].bet < 60*smallblind:
            if t.seats[index].stack < smallblind*50:
                selected_range = t.seats[index].range_top1_5
                common.debugranges(situation, "range_top1_5")
            elif t.seats[index].stack < smallblind*30:
                selected_range = t.seats[index].range_top2_3 + t.seats[index].range_ak
                common.debugranges(situation, "range_top2_3+ak")
            elif t.seats[index].stack < smallblind*20:
                selected_range = t.seats[index].range_top2_7
                common.debugranges(situation, "range_top2_7")
            else:
                selected_range = t.seats[index].range_top1
                common.debugranges(situation, "range_top1")
        elif t.seats[index].stack < smallblind*30:
            selected_range = t.seats[index].range_top1_5 + t.seats[index].range_ak
            common.debugranges(situation, "range_top1_5+ak")
        else:
            selected_range = t.seats[index].range_top1_5
            common.debugranges(situation, "range_top1_5")
    elif situation == "2allins-1behind":
        villain1_index = 0
        villain2_index = 0
        counter = 0
        for s in t.seats:
            if common.checkAllin(s):
                villain2_index = counter
            counter += 1
        counter = 0
        for s in t.seats:
            if common.checkAllin(s):
                if villain2_index != counter:
                    villain1_index = counter
            counter += 1
        if t.seats[villain1_index].bet + t.seats[villain2_index].bet < 60*smallblind:
            if t.seats[index].stack < smallblind*50:
                selected_range = t.seats[index].range_top1_5
                common.debugranges(situation, "range_top1_5")
            elif t.seats[index].stack < smallblind*30:
                selected_range = t.seats[index].range_top2_3 + t.seats[index].range_ak
                common.debugranges(situation, "range_top2_3+ak")
            elif t.seats[index].stack < smallblind*20:
                selected_range = t.seats[index].range_top2_7
                common.debugranges(situation, "range_top2_7")
            else:
                selected_range = t.seats[index].range_top1
                common.debugranges(situation, "range_top1")
        elif t.seats[index].stack < smallblind*30:
            selected_range = t.seats[index].range_top1_5 + t.seats[index].range_ak
            common.debugranges(situation, "range_top1")
        else:
            selected_range = t.seats[index].range_top1_5
            common.debugranges(situation, "range_top1_5")
    elif situation == "2allins-morebehind":
        selected_range = t.seats[index].range_top1
        common.debugranges(situation, "range_top1")
    elif situation == "more-allins":
        selected_range = t.seats[index].range_top1
        common.debugranges(situation, "range_top1")
    elif situation == "10BB-1limper-0behind":
        if settings.nash_push_fold:
            selected_range = t.seats[index].range_nash_heads_up_10bb_push
            t.seats[index].learning_range_name = "range_nash_heads_up_10bb_push"
            t.seats[index].want_to_push = 1
            common.debugranges(situation, "range_nash_heads_up_10bb_push")
        else:
            selected_range = t.seats[index].range_under10bb_push_vs_1
            t.seats[index].learning_range_name = "range_under10bb_push_vs_1"
            t.seats[index].want_to_push = 1
            common.debugranges(situation, "range_under10bb_push_vs_1")
    elif situation == "10BB-1limper-1behind":
        selected_range = t.seats[index].range_under10bb_push_vs_2
        t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
        t.seats[index].want_to_push= 1
        common.debugranges(situation, "range_under10bb_push_vs_2")
    elif situation == "10BB-1limper-2behind":
        selected_range = t.seats[index].range_under10bb_push_vs_more
        t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
        t.seats[index].want_to_push = 1
        common.debugranges(situation, "range_under10bb_push_vs_more")
    elif situation == "10BB-1limper-morebehind":
        selected_range = t.seats[index].range_under10bb_push_vs_more
        t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
        t.seats[index].want_to_push = 1
        common.debugranges(situation, "range_under10bb_push_vs_more")
    elif situation == "10BB-2limpers-0behind":
        selected_range = t.seats[index].range_under10bb_push_vs_2
        t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
        t.seats[index].want_to_push = 1
        common.debugranges(situation, "range_under10bb_push_vs_2")
    elif situation == "10BB-2limpers-1behind":
        selected_range = t.seats[index].range_under10bb_push_vs_more
        t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
        t.seats[index].want_to_push= 1
        common.debugranges(situation, "range_under10bb_push_vs_more")
    elif situation == "10BB-2limpers-morebehind":
        selected_range = t.seats[index].range_under10bb_push_vs_more
        t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
        t.seats[index].want_to_push= 1
        common.debugranges(situation, "range_under10bb_push_vs_more")
    elif situation == "10BB-noopen-wearehere-1behind":
        if settings.nash_push_fold:
            selected_range = t.seats[index].range_nash_heads_up_10bb_push
            t.seats[index].learning_range_name = "range_nash_heads_up_10bb_push"
            t.seats[index].want_to_push = 1
            common.debugranges(situation, "range_nash_heads_up_10bb_push")
        else:
            selected_range = t.seats[index].range_under10bb_push_vs_1
            t.seats[index].learning_range_name = "range_under10bb_push_vs_1"
            t.seats[index].want_to_push = 1
            common.debugranges(situation, "range_under10bb_push_vs_1")
    elif situation == "10BB-noopen-wearehere-2behind":
        selected_range = t.seats[index].range_under10bb_push_vs_2
        t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
        t.seats[index].want_to_push = 1
        common.debugranges(situation, "range_under10bb_push_vs_2")
    elif situation == "10BB-noopen-wearehere-morebehind":
        selected_range = t.seats[index].range_under10bb_push_vs_more
        t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
        t.seats[index].want_to_push = 1
        common.debugranges(situation, "range_under10bb_push_vs_more")
    elif situation == "10BB-opened-0behind":
        if settings.nash_push_fold:
            selected_range = t.seats[index].range_nash_heads_up_10bb_push
            t.seats[index].learning_range_name = "range_nash_heads_up_10bb_push"
            t.seats[index].want_to_push = 1
            common.debugranges(situation, "range_nash_heads_up_10bb_push")
        else:
            selected_range = t.seats[index].range_under10bb_push_vs_1
            t.seats[index].learning_range_name = "range_under10bb_push_vs_1"
            t.seats[index].want_to_push = 1
            common.debugranges(situation, "range_under10bb_push_vs_1")
    elif situation == "10BB-opened-1behind":
        selected_range = t.seats[index].range_under10bb_push_vs_2
        t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
        t.seats[index].want_to_push = 1
        common.debugranges(situation, "range_under10bb_push_vs_2")
    elif situation == "10BB-opened-morebehind":
        selected_range = t.seats[index].range_under10bb_push_vs_more
        t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
        t.seats[index].want_to_push = 1
        common.debugranges(situation, "range_under10bb_push_vs_more")
    elif situation == "10BB+noopen-wearehere-1behind":
        #redfish is always DB position in hudAnalyzer
        if settings.hudanalyser == 1 and botname == "redfish":
            selected_range = t.seats[index].hd_open_huanalyzer
            t.seats[index].learning_range_name = "hd_open_huanalyzer"
            common.debugranges(situation, "hd_open_huanalyzer")
        elif posname == "hd":
            selected_range = t.seats[index].range_hd_open
            t.seats[index].learning_range_name = "range_hd_open"
            common.debugranges(situation, "range_hd_open")
        elif posname == "hb":
            selected_range = t.seats[index].range_fold
            common.debugranges(situation, "tough_spot_range")
        elif posname == "sb":
            selected_range = t.seats[index].range_sb_open
            t.seats[index].learning_range_name = "range_sb_open"
            common.debugranges(situation, "range_sb_open")
        else:
            selected_range = t.seats[index].range_fold
            common.debugranges(situation, "tough_spot_range")
    elif situation == "10BB+noopen-wearehere-2behind":
        selected_range = t.seats[index].range_db_open
        t.seats[index].learning_range_name = "range_db_open"
        common.debugranges(situation, "range_db_open")
    elif situation == "10BB+noopen-wearehere-morebehind":
        if posname == "ug":
            selected_range = t.seats[index].range_ug_open
            t.seats[index].learning_range_name = "range_ug_open"
            common.debugranges(situation, "range_ug_open")
        elif posname == "hj":
            selected_range = t.seats[index].range_hj_open
            t.seats[index].learning_range_name = "range_hj_open"
            common.debugranges(situation, "range_hj_open")
        elif posname == "co":
            selected_range = t.seats[index].range_co_open
            t.seats[index].learning_range_name = "range_co_open"
            common.debugranges(situation, "range_co_open")
        else:
            selected_range = t.seats[index].range_fold
            common.debugranges(situation, "tough_spot_range")
    elif situation == "10BB+1limp-wearehere-0behind":
        if stp <= 0.3:
            selected_range = t.seats[index].range_atc
            common.debugranges(situation, "range_any_two_cards")
        elif t.seats[index].stack <= smallblind*20:
            if settings.nash_push_fold:
                selected_range = t.seats[index].range_nash_heads_up_10bb_push
                t.seats[index].learning_range_name = "range_nash_heads_up_10bb_push"
                common.debugranges(situation, "range_nash_heads_up_10bb_push")
            else:
                selected_range = t.seats[index].range_under10bb_push_vs_1
                t.seats[index].learning_range_name = "range_under10bb_push_vs_1"
                common.debugranges(situation, "range_under10bb_push_vs_1")
        else:
            #determine if you have position on villain so can use the proper defend range
            villain_position = common.getFirstLimper(t, smallblind, ante)
            villain_position_number = common.getFirstLimperNumber(t, smallblind, ante)
            #get your position
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip")
                else:
                    if hero_position == "ug":
                        selected_range = t.seats[index].range_ug_open
                        t.seats[index].learning_range_name = "range_ug_open"
                        common.debugranges(situation, "range_ug_open")
                    elif hero_position == "hj":
                        selected_range = t.seats[index].range_hj_open
                        t.seats[index].learning_range_name = "range_hj_open"
                        common.debugranges(situation, "range_hj_open")
                    elif hero_position == "co":
                        selected_range = t.seats[index].range_co_open
                        t.seats[index].learning_range_name = "range_co_open"
                        common.debugranges(situation, "range_co_open")
                    elif hero_position == "db":
                        selected_range = t.seats[index].range_db_open
                        t.seats[index].learning_range_name = "range_db_open"
                        common.debugranges(situation, "range_db_open")
                    elif hero_position == "sb":
                        selected_range = t.seats[index].range_sb_open
                        t.seats[index].learning_range_name = "range_sb_open"
                        common.debugranges(situation, "range_sb_open")
                    elif hero_position == "hd":
                        selected_range = t.seats[index].range_hd_open
                        t.seats[index].learning_range_name = "range_hd_open"
                        common.debugranges(situation, "range_hd_open")
                    settings.threebet += 1
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op")
                elif villain_position == "hd":
                    selected_range = t.seats[index].range_hb_defend
                    t.seats[index].learning_range_name = "range_hb_defend"
                    common.debugranges(situation, "range_hb_defend")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
    elif situation == "10BB+limped-raised-wearehere-0behind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_2
            t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
            common.debugranges(situation, "range_under10bb_push_vs_2")
        else:
            biggest_bet = common.find_biggest_bet(t)
            villain_position = ""
            #get raisor position number
            villain_position_number = 7 # no such position
            counter = 0
            for s in t.seats:
                if s.bet == biggest_bet:
                    villain_position_number = counter
                counter += 1
            #get villain position
            villain_position = common.getPreflopPosition_name(t, t.seats[villain_position_number].name)
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip_cutted")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip_cutted")
                else:
                    if hero_position == "ug":
                        selected_range = t.seats[index].range_ug_open
                        t.seats[index].learning_range_name = "range_ug_open"
                        common.debugranges(situation, "range_ug_open")
                    elif hero_position == "hj":
                        selected_range = t.seats[index].range_hj_open
                        t.seats[index].learning_range_name = "range_hj_open"
                        common.debugranges(situation, "range_hj_open")
                    elif hero_position == "co":
                        selected_range = t.seats[index].range_co_open
                        t.seats[index].learning_range_name = "range_co_open"
                        common.debugranges(situation, "range_co_open")
                    elif hero_position == "db":
                        selected_range = t.seats[index].range_db_open
                        t.seats[index].learning_range_name = "range_db_open"
                        common.debugranges(situation, "range_db_open")
                    elif hero_position == "sb":
                        selected_range = t.seats[index].range_sb_open
                        t.seats[index].learning_range_name = "range_sb_open"
                        common.debugranges(situation, "range_sb_open")
                    elif hero_position == "hd":
                        selected_range = t.seats[index].range_hd_open
                        t.seats[index].learning_range_name = "range_hd_open"
                        common.debugranges(situation, "range_hd_open")
                    settings.threebet += 1
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op_cutted")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op_cutted")
                else:
                    if hero_position == "ug":
                        selected_range = t.seats[index].range_ug_open
                        t.seats[index].learning_range_name = "range_ug_open"
                        common.debugranges(situation, "range_ug_open")
                    elif hero_position == "hj":
                        selected_range = t.seats[index].range_hj_open
                        t.seats[index].learning_range_name = "range_hj_open"
                        common.debugranges(situation, "range_hj_open")
                    elif hero_position == "co":
                        selected_range = t.seats[index].range_co_open
                        t.seats[index].learning_range_name = "range_co_open"
                        common.debugranges(situation, "range_co_open")
                    elif hero_position == "db":
                        selected_range = t.seats[index].range_db_open
                        t.seats[index].learning_range_name = "range_db_open"
                        common.debugranges(situation, "range_db_open")
                    elif hero_position == "sb":
                        selected_range = t.seats[index].range_sb_open
                        t.seats[index].learning_range_name = "range_sb_open"
                        common.debugranges(situation, "range_sb_open")
                    elif hero_position == "hd":
                        selected_range = t.seats[index].range_hd_open
                        t.seats[index].learning_range_name = "range_hd_open"
                        common.debugranges(situation, "range_hd_open")
                    settings.threebet += 1

    elif situation == "10BB+1limp-wearehere-1behind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_2
            t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
            common.debugranges(situation, "range_under10bb_push_vs_2")
        else:
            #since we have one left behind to act, hero is small blind and has no position
            #get villain position
            villain_position = common.getFirstLimper(t, smallblind, ante)
            villain_position_number = common.getFirstLimperNumber(t, smallblind, ante)
            if villain_position == "ug":
                selected_range = t.seats[index].range_defend_vs_ug_op
                t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                common.debugranges(situation, "range_defend_vs_ug_op")
            elif villain_position == "hj":
                selected_range = t.seats[index].range_defend_vs_hj_op
                t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                common.debugranges(situation, "range_defend_vs_hj_op")
            elif villain_position == "co":
                selected_range = t.seats[index].range_defend_vs_co_op
                t.seats[index].learning_range_name = "range_defend_vs_co_op"
                common.debugranges(situation, "range_defend_vs_co_op")
            elif villain_position == "db":
                selected_range = t.seats[index].range_defend_vs_db_op 
                t.seats[index].learning_range_name = "range_defend_vs_db_op"
                common.debugranges(situation, "range_defend_vs_db_op")
            elif villain_position == "hd":
                selected_range = t.seats[index].range_hb_defend
                t.seats[index].learning_range_name = "range_hb_defend"
                common.debugranges(situation, "range_hb_defend")
            else:
                selected_range = t.seats[index].range_top6
                common.debugranges(situation, "range_top6")
    elif situation == "10BB+limped-raised-wearehere-1behind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            biggest_bet = common.find_biggest_bet(t)
            villain_position = ""
            #get raisor position number
            villain_position_number = 7 # no such position
            counter = 0
            for s in t.seats:
                if s.bet == biggest_bet:
                    villain_position_number = counter
                counter += 1
            #get villain position
            villain_position = common.getPreflopPosition_name(t, t.seats[villain_position_number].name)
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip_cutted")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip_cutted")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op_cutted")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op_cutted")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
    elif situation == "10BB+1limp-wearehere-2behind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            #since we have two left behind to act, hero is dealer and has position
            villain_position = common.getFirstLimper(t, smallblind, ante)
            villain_position_number = common.getFirstLimperNumber(t, smallblind, ante)
            if villain_position == "ug":
                selected_range = t.seats[index].range_defend_vs_ug_ip
                t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                common.debugranges(situation, "range_defend_vs_ug_ip")
            elif villain_position == "hj":
                selected_range = t.seats[index].range_defend_vs_hj_ip
                t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                common.debugranges(situation, "range_defend_vs_hj_ip")
            elif villain_position == "co":
                selected_range = t.seats[index].range_defend_vs_co_ip
                t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                common.debugranges(situation, "range_defend_vs_co_ip")
            elif villain_position == "sb":
                selected_range = t.seats[index].range_defend_vs_sb_ip
                t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                common.debugranges(situation, "range_defend_vs_sb_ip")
            else:
                selected_range = t.seats[index].range_top6
                common.debugranges(situation, "range_top6")
    elif situation == "10BB+limped-raised-wearehere-morebehind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            biggest_bet = common.find_biggest_bet(t)
            villain_position = ""
            #get raisor position number
            villain_position_number = 7 # no such position
            counter = 0
            for s in t.seats:
                if s.bet == biggest_bet:
                    villain_position_number = counter
                counter += 1
            #get villain position
            villain_position = common.getPreflopPosition_name(t, t.seats[villain_position_number].name)
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip_cutted")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip_cutted")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op_cutted")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op_cutted")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
    elif situation == "10BB+1limp-wearehere-morebehind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            #we have at least 3 behind and one limped so we are either hj or co so we have position on limper
            villain_position = common.getFirstLimper(t, smallblind, ante)
            villain_position_number = common.getFirstLimperNumber(t, smallblind, ante)
            if villain_position == "ug":
                selected_range = t.seats[index].range_defend_vs_ug_ip
                t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                common.debugranges(situation, "range_defend_vs_ug_ip")
            elif villain_position == "hj":
                selected_range = t.seats[index].range_defend_vs_hj_ip
                t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                common.debugranges(situation, "range_defend_vs_hj_ip")
            else:
                selected_range = t.seats[index].range_top6
                common.debugranges(situation, "range_top6")
    elif situation == "10BB+2limps-wearehere-0behind": #as there is no raise will use defend range from first limper
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_2
            t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
            common.debugranges(situation, "range_under10bb_push_vs_2")
        else:
            #determine if you have position on villain so can use the proper defend range
            villain_position = common.getFirstLimper(t, smallblind, ante)
            villain_position_number = common.getFirstLimperNumber(t, smallblind, ante)
            #get your position
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op")
                elif villain_position == "hd":
                    selected_range = t.seats[index].range_hb_defend
                    t.seats[index].learning_range_name = "range_hb_defend"
                    common.debugranges(situation, "range_hb_defend")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
    elif situation == "10BB+2limps-wearehere-1behind":
        #since there is 1 behind and 2 limps in front we are small blind and will defend from first limper
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            #since we have one left behind to act, hero is small blind and has no position
            villain_position = common.getFirstLimper(t, smallblind, ante)
            villain_position_number = common.getFirstLimperNumber(t, smallblind, ante)
            if villain_position == "ug":
                selected_range = t.seats[index].range_defend_vs_ug_op
                t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                common.debugranges(situation, "range_defend_vs_ug_op")
            elif villain_position == "hj":
                selected_range = t.seats[index].range_defend_vs_hj_op
                t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                common.debugranges(situation, "range_defend_vs_hj_op")
            elif villain_position == "co":
                selected_range = t.seats[index].range_defend_vs_co_op
                t.seats[index].learning_range_name = "range_defend_vs_co_op"
                common.debugranges(situation, "range_defend_vs_co_op")
            elif villain_position == "db":
                selected_range = t.seats[index].range_defend_vs_db_op
                t.seats[index].learning_range_name = "range_defend_vs_db_op"
                common.debugranges(situation, "range_defend_vs_db_op")
            elif villain_position == "hd":
                selected_range = t.seats[index].range_hb_defend
                t.seats[index].learning_range_name = "range_hb_defend"
                common.debugranges(situation, "range_hb_defend")
            else:
                selected_range = t.seats[index].range_top6
                common.debugranges(situation, "range_top6")
    elif situation == "10BB+2limps-wearehere-morebehind":
        #since we have 2 limps in front and at least three left to act, we are exactly sitting on co
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            selected_range = t.seats[index].range_defend_vs_ug_ip
            t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
            common.debugranges(situation, "range_defend_vs_ug_ip")
    elif situation == "10BB+3limps-wearehere-0behind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            #we are out of position on big blind:
            villain_position = common.getFirstLimper(t, smallblind, ante)
            villain_position_number = common.getFirstLimperNumber(t, smallblind, ante)
            if villain_position == "ug":
                selected_range = t.seats[index].range_defend_vs_ug_op
                t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                common.debugranges(situation, "range_defend_vs_ug_op")
            elif villain_position == "hj":
                selected_range = t.seats[index].range_defend_vs_hj_op
                t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                common.debugranges(situation, "range_defend_vs_hj_op")
            elif villain_position == "co":
                selected_range = t.seats[index].range_defend_vs_co_op
                t.seats[index].learning_range_name = "range_defend_vs_co_op"
                common.debugranges(situation, "range_defend_vs_co_op")
            elif villain_position == "db":
                selected_range = t.seats[index].range_defend_vs_db_op
                t.seats[index].learning_range_name = "range_defend_vs_db_op"
                common.debugranges(situation, "range_defend_vs_db_op")
            elif villain_position == "hd":
                selected_range = t.seats[index].range_hb_defend
                t.seats[index].learning_range_name = "range_hb_defend"
                common.debugranges(situation, "range_hb_defend")
    elif situation == "10BB+3limps-wearehere-morebehind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            #here will use again the same defence as above as it is cutted
            villain_position = common.getFirstLimper(t, smallblind, ante)
            villain_position_number = common.getFirstLimperNumber(t, smallblind, ante)
            if villain_position == "ug":
                selected_range = t.seats[index].range_defend_vs_ug_op
                t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                common.debugranges(situation, "range_defend_vs_ug_op")
            elif villain_position == "hj":
                selected_range = t.seats[index].range_defend_vs_hj_op
                t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                common.debugranges(situation, "range_defend_vs_hj_op")
            elif villain_position == "co":
                selected_range = t.seats[index].range_defend_vs_co_op
                t.seats[index].learning_range_name = "range_defend_vs_co_op"
                common.debugranges(situation, "range_defend_vs_co_op")
            elif villain_position == "db":
                selected_range = t.seats[index].range_defend_vs_db_op
                t.seats[index].learning_range_name = "range_defend_vs_db_op"
                common.debugranges(situation, "range_defend_vs_db_op")
            elif villain_position == "sb":
                selected_range = t.seats[index].range_defend_vs_sb_ip
                t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                common.debugranges(situation, "range_defend_vs_sb_ip")
            elif villain_position == "hd":
                selected_range = t.seats[index].range_hb_defend
                t.seats[index].learning_range_name = "range_hb_defend"
                common.debugranges(situation, "range_hb_defend")
            else:
                selected_range = t.seats[index].range_safe
                t.seats[index].learning_range_name = "range_safe"
                common.debugranges(situation, "range_safe") 
    elif situation == "10BB+bunch_of_limpers":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            #here will use again the same defence as above as it is weird situation
            villain_position = common.getFirstLimper(t, smallblind, ante)
            villain_position_number = common.getFirstLimperNumber(t, smallblind, ante)
            if villain_position == "ug":
                selected_range = t.seats[index].range_defend_vs_ug_op
                t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                common.debugranges(situation, "range_defend_vs_ug_op")
            elif villain_position == "hj":
                selected_range = t.seats[index].range_defend_vs_hj_op
                t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                common.debugranges(situation, "range_defend_vs_hj_op")
            elif villain_position == "co":
                selected_range = t.seats[index].range_defend_vs_co_op
                t.seats[index].learning_range_name = "range_defend_vs_co_op"
                common.debugranges(situation, "range_defend_vs_co_op")
            elif villain_position == "db":
                selected_range = t.seats[index].range_defend_vs_db_op
                t.seats[index].learning_range_name = "range_defend_vs_db_op"
                common.debugranges(situation, "range_defend_vs_db_op")
            elif villain_position == "sb":
                selected_range = t.seats[index].range_defend_vs_sb_ip
                t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                common.debugranges(situation, "range_defend_vs_sb_ip")
            elif villain_position == "hd":
                selected_range = t.seats[index].range_hb_defend
                t.seats[index].learning_range_name = "range_hb_defend"
                common.debugranges(situation, "range_hb_defend")
            else:
                selected_range = t.seats[index].range_safe
                t.seats[index].learning_range_name = "range_safe"
                common.debugranges(situation, "range_safe")
    elif situation == "10BB+opened-wearehere-0behind":
        if settings.hudanalyser == 1 and botname == "blackfish":
            selected_range = t.seats[index].hb_3bet_analyzer + t.seats[index].hb_call_analyzer
            t.seats[index].learning_range_name = "hb_defend_huanalyzer"
            common.debugranges(situation, "hb_defend_huanalyzer")
        elif stp <= 0.3:
            selected_range = t.seats[index].range_atc
            common.debugranges(situation, "range_any_two_cards")
        elif t.seats[index].stack <= smallblind*20:
            if settings.nash_push_fold:
                selected_range = t.seats[index].range_nash_heads_up_10bb_push
                t.seats[index].learning_range_name = "range_nash_heads_up_10bb_push"
                common.debugranges(situation, "range_nash_heads_up_10bb_push")
            else:
                selected_range = t.seats[index].range_under10bb_push_vs_1
                t.seats[index].learning_range_name = "range_under10bb_push_vs_1"
                common.debugranges(situation, "range_under10bb_push_vs_1")
        else:
            #determine if you have position on villain so can use the proper defend range
            villain_position = common.getFirstOpener(t, smallblind, ante)
            villain_position_number = common.getFirstOpenerNumber(t, smallblind, ante)
            #get your position
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip")
                else:
                    settings.threebet += 1
                    if hero_position == 'ug':
                        selected_range = t.seats[index].range_ug_open
                        t.seats[index].learning_range_name = "range_ug_open"
                        common.debugranges(situation, "range_ug_open_cutted")
                    elif hero_position == 'hj':
                        selected_range = t.seats[index].range_hj_open
                        t.seats[index].learning_range_name = "range_hj_open"
                        common.debugranges(situation, "range_hj_open_cutted")
                    elif hero_position == 'co':
                        selected_range = t.seats[index].range_co_open
                        t.seats[index].learning_range_name = "range_co_open"
                        common.debugranges(situation, "range_co_open_cutted")
                    elif hero_position == 'db':
                        selected_range = t.seats[index].range_db_open
                        t.seats[index].learning_range_name = "range_db_open"
                        common.debugranges(situation, "range_db_open_cutted")
                    elif hero_position == 'sb':
                        selected_range = t.seats[index].range_sb_open
                        t.seats[index].learning_range_name = "range_sb_open"
                        common.debugranges(situation, "range_sb_open_cutted")
                    elif hero_position == 'bb':
                        selected_range = t.seats[index].range_safe
                        t.seats[index].learning_range_name = "range_safe"
                        common.debugranges(situation, "tanking-spot")
                    elif hero_position == 'hd':
                        selected_range = t.seats[index].range_hd_open
                        t.seats[index].learning_range_name = "range_hd_open"
                        common.debugranges(situation, "range_hd_open_cutted")
                    else: 
                        selected_range = t.seats[index].range_safe
                        t.seats[index].learning_range_name = "range_safe"
                        common.debugranges(situation, "tanking-spot")
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op")
                elif villain_position == "hd":
                    selected_range = t.seats[index].range_hb_defend
                    t.seats[index].learning_range_name = "range_hb_defend"
                    common.debugranges(situation, "range_hb_defend")
                else:
                    settings.threebet += 1
                    if hero_position == 'ug':
                        selected_range = t.seats[index].range_ug_open
                        t.seats[index].learning_range_name = "range_ug_open"
                        common.debugranges(situation, "range_ug_open_cutted")
                    elif hero_position == 'hj':
                        selected_range = t.seats[index].range_hj_open
                        t.seats[index].learning_range_name = "range_hj_open"
                        common.debugranges(situation, "range_hj_open_cutted")
                    elif hero_position == 'co':
                        selected_range = t.seats[index].range_co_open
                        t.seats[index].learning_range_name = "range_co_open"
                        common.debugranges(situation, "range_co_open_cutted")
                    elif hero_position == 'db':
                        selected_range = t.seats[index].range_db_open
                        t.seats[index].learning_range_name = "range_db_open"
                        common.debugranges(situation, "range_db_open_cutted")
                    elif hero_position == 'sb':
                        selected_range = t.seats[index].range_sb_open
                        t.seats[index].learning_range_name = "range_sb_open"
                        common.debugranges(situation, "range_sb_open_cutted")
                    elif hero_position == 'bb':
                        selected_range = t.seats[index].range_safe
                        t.seats[index].learning_range_name = "range_safe"
                        common.debugranges(situation, "tanking-spot")
                    elif hero_position == 'hd':
                        selected_range = t.seats[index].range_hd_open
                        t.seats[index].learning_range_name = "range_hd_open"
                        common.debugranges(situation, "range_hd_open_cutted")
                    else: 
                        selected_range = t.seats[index].range_safe
                        t.seats[index].learning_range_name = "range_safe"
                        common.debugranges(situation, "tanking-spot")

    elif situation == "10BB+opened-wearehere-1behind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_2
            t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
            common.debugranges(situation, "range_under10bb_push_vs_2")
        else:
            #since we have one left behind to act, hero is small blind and has no position
            villain_position = common.getFirstOpener(t, smallblind, ante)
            villain_position_number = common.getFirstOpenerNumber(t, smallblind, ante)
            if villain_position == "ug":
                selected_range = t.seats[index].range_defend_vs_ug_op
                t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                common.debugranges(situation, "range_defend_vs_ug_op")
            elif villain_position == "hj":
                selected_range = t.seats[index].range_defend_vs_hj_op
                t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                common.debugranges(situation, "range_defend_vs_hj_op")
            elif villain_position == "co":
                selected_range = t.seats[index].range_defend_vs_co_op
                t.seats[index].learning_range_name = "range_defend_vs_co_op"
                common.debugranges(situation, "range_defend_vs_co_op")
            elif villain_position == "db":
                selected_range = t.seats[index].range_defend_vs_db_op
                t.seats[index].learning_range_name = "range_defend_vs_db_op"
                common.debugranges(situation, "range_defend_vs_db_op")
            elif villain_position == "hd":
                selected_range = t.seats[index].range_hb_defend
                t.seats[index].learning_range_name = "range_hb_defend"
                common.debugranges(situation, "range_hb_defend")
            elif villain_position == "sb":
                selected_range = t.seats[index].range_defend_vs_sb_ip
                t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                common.debugranges(situation, "range_defend_vs_sb_ip")
            else:
                selected_range = t.seats[index].range_top2_7
                common.debugranges(situation, "range_top2_7")
    elif situation == "10BB+opened-wearehere-2behind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            #since we have two left behind to act, hero is dealer and has position
            villain_position = common.getFirstOpener(t, smallblind, ante)
            villain_position_number = common.getFirstOpenerNumber(t, smallblind, ante)
            if villain_position == "ug":
                selected_range = t.seats[index].range_defend_vs_ug_ip
                t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                common.debugranges(situation, "range_defend_vs_ug_ip")
            elif villain_position == "hj":
                selected_range = t.seats[index].range_defend_vs_hj_ip
                t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                common.debugranges(situation, "range_defend_vs_hj_ip")
            elif villain_position == "co":
                selected_range = t.seats[index].range_defend_vs_co_ip
                t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                common.debugranges(situation, "range_defend_vs_co_ip")
            elif villain_position == "sb":
                selected_range = t.seats[index].range_defend_vs_sb_ip
                t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                common.debugranges(situation, "range_defend_vs_sb_ip")
            else:
                selected_range = t.seats[index].range_top6
                common.debugranges(situation, "range_top6")
    elif situation == "10BB+opened-wearehere-morebehind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            #we have at least 3 behind and one limped so we are either hj or co so we have position on limper
            villain_position = common.getFirstOpener(t, smallblind, ante)
            villain_position_number = common.getFirstOpenerNumber(t, smallblind, ante)
            if villain_position == "ug":
                selected_range = t.seats[index].range_defend_vs_ug_ip
                t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                common.debugranges(situation, "range_defend_vs_ug_ip")
            elif villain_position == "hj":
                selected_range = t.seats[index].range_defend_vs_hj_ip
                t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                common.debugranges(situation, "range_defend_vs_hj_ip")
            elif villain_position == "co":
                selected_range = t.seats[index].range_defend_vs_hj_ip
                t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                common.debugranges(situation, "range_defend_vs_co_ip")
            else:
                selected_range = t.seats[index].range_top6
                common.debugranges(situation, "range_top6")
    elif situation == "10BB+weird-big-size-open":
        biggest_bet = common.find_biggest_bet(t)
        villain_position = common.getFirstOpener(t, smallblind, ante)
        villain_position_number = common.getFirstOpenerNumber(t, smallblind, ante)
        gamblers = common.countNotFoldedYet(table) #this includes you
        if t.seats[index].stack <= smallblind*20: #if we are under 10BBs
            if t.seats[villain_position_number].last5betscrazy >= 2: #last 5 plays he used 2 times big sizing so play it wider
                if gamblers == 2:
                    if settings.nash_push_fold:
                        selected_range = t.seats[index].range_nash_heads_up_10bb_push
                        t.seats[index].learning_range_name = "range_nash_heads_up_10bb_push"
                        common.debugranges(situation, "range_nash_heads_up_10bb_push")
                    else:
                        selected_range = t.seats[index].range_under10bb_push_vs_1
                        t.seats[index].learning_range_name = "range_under10bb_push_vs_1"
                        common.debugranges(situation, "range_under10bb_push_vs_1")
                elif gamblers == 3:
                    selected_range = t.seats[index].range_under10bb_push_vs_2
                    t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
                    common.debugranges(situation, "range_under10bb_push_vs_2")
                else:
                    selected_range = t.seats[index].range_under10bb_push_vs_more
                    t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
                    common.debugranges(situation, "range_under10bb_push_vs_more")
            else:
                #we are shortstack but he may want to jam so jam tighter
                selected_range = t.seats[index].range_top2_7
                common.debugranges(situation, "range_top2_7")
        else:
            #we are not short stack
            if t.seats[villain_position_number].last5betscrazy > 2:
                #maniac2
                selected_range = t.seats[index].range_wide
                common.debugranges(situation, "range_wide") 
            elif t.seats[villain_position_number].last5betscrazy == 2: #last 5 plays he used at least 2 times big sizing so jam acex and pocket pairs:
                selected_range = t.seats[index].range_safe
                common.debugranges(situation, "range_safe")                  
            else:
                #he uses big open sizing for first time last 5 orbist so proceed with caution
                selected_range = t.seats[index].range_top4_5
                common.debugranges(situation, "range_top4_5")               
    elif situation == "10BB+opened-call-wearehere-0behind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_2
            t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
            common.debugranges(situation, "range_under10bb_push_vs_2")
        else:
            biggest_bet = common.find_biggest_bet(t)
            villain_position = common.getFirstOpener(t, smallblind, ante)
            villain_position_number = common.getFirstOpenerNumber(t, smallblind, ante)
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op")
                elif villain_position == "hd":
                    selected_range = t.seats[index].range_hb_defend
                    t.seats[index].learning_range_name = "range_hb_defend"
                    common.debugranges(situation, "range_hb_defend")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
    elif situation == "10BB+opened-call-wearehere-1behind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            biggest_bet = common.find_biggest_bet(t)
            villain_position = common.getFirstOpener(t, smallblind, ante)
            villain_position_number = common.getFirstOpenerNumber(t, smallblind, ante)
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op")
                elif villain_position == "hd":
                    selected_range = t.seats[index].range_hb_defend
                    t.seats[index].learning_range_name = "range_hb_defend"
                    common.debugranges(situation, "range_hb_defend")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
    elif situation == "10BB+opened-call-wearehere-morebehind":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            biggest_bet = common.find_biggest_bet(t)
            villain_position = common.getFirstOpener(t, smallblind, ante)
            villain_position_number = common.getFirstOpenerNumber(t, smallblind, ante)
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op")
                elif villain_position == "hd":
                    selected_range = t.seats[index].range_hb_defend
                    t.seats[index].learning_range_name = "range_hb_defend"
                    common.debugranges(situation, "range_hb_defend")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
    elif situation == "10BB+opened-raised-wearehere-0behind":
        settings.threebet += 1
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_2
            t.seats[index].learning_range_name = "range_under10bb_push_vs_2"
            common.debugranges(situation, "range_under10bb_push_vs_2")
        else:
            biggest_bet = common.find_biggest_bet(t)
            villain_position = ""
            #get raisor position number
            villain_position_number = 7 # no such position
            counter = 0
            for s in t.seats:
                if s.bet == biggest_bet:
                    if villain_position_number == 7:
                        villain_position_number = counter
                counter += 1
            #get villain position
            villain_position = common.getPreflopPosition_name(t, t.seats[villain_position_number].name)
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip_cutted")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip_cutted")
                else:
                    if hero_position == "ug":
                        selected_range = t.seats[index].range_ug_open
                        t.seats[index].learning_range_name = "range_ug_open"
                        common.debugranges(situation, "range_ug_open")
                    elif hero_position == "hj":
                        selected_range = t.seats[index].range_hj_open
                        t.seats[index].learning_range_name = "range_hj_open"
                        common.debugranges(situation, "range_hj_open")
                    elif hero_position == "co":
                        selected_range = t.seats[index].range_co_open
                        t.seats[index].learning_range_name = "range_co_open"
                        common.debugranges(situation, "range_co_open")
                    elif hero_position == "db":
                        selected_range = t.seats[index].range_db_open
                        t.seats[index].learning_range_name = "range_db_open"
                        common.debugranges(situation, "range_db_open")
                    elif hero_position == "sb":
                        selected_range = t.seats[index].range_sb_open
                        t.seats[index].learning_range_name = "range_sb_open"
                        common.debugranges(situation, "range_sb_open")
                    elif hero_position == "hd":
                        selected_range = t.seats[index].range_hd_open
                        t.seats[index].learning_range_name = "range_hd_open"
                        common.debugranges(situation, "range_name =_hd_open")
                    settings.threebet += 1
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op_cutted")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op_cutted")
                else:
                    if hero_position == "ug":
                        selected_range = t.seats[index].range_ug_open
                        t.seats[index].learning_range_name = "range_ug_open"
                        common.debugranges(situation, "range_ug_open")
                    elif hero_position == "hj":
                        selected_range = t.seats[index].range_hj_open
                        t.seats[index].learning_range_name = "range_hj_open"
                        common.debugranges(situation, "range_hj_open")
                    elif hero_position == "co":
                        selected_range = t.seats[index].range_co_open
                        t.seats[index].learning_range_name = "range_co_open"
                        common.debugranges(situation, "range_co_open")
                    elif hero_position == "db":
                        selected_range = t.seats[index].range_db_open
                        t.seats[index].learning_range_name = "range_db_open"
                        common.debugranges(situation, "range_db_open")
                    elif hero_position == "sb":
                        selected_range = t.seats[index].range_sb_open
                        t.seats[index].learning_range_name = "range_sb_open"
                        common.debugranges(situation, "range_sb_open")
                    elif hero_position == "hd":
                        selected_range = t.seats[index].range_hd_open
                        t.seats[index].learning_range_name = "range_hd_open"
                        common.debugranges(situation, "range_hd_open")
                    settings.threebet += 1

    elif situation == "10BB+opened-raised-wearehere-1behind":
        settings.threebet += 1
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            biggest_bet = common.find_biggest_bet(t)
            villain_position = ""
            #get raisor position number
            villain_position_number = 7 # no such position
            counter = 0
            for s in t.seats:
                if s.bet == biggest_bet:
                    if villain_position_number == 7:
                        villain_position_number = counter
                counter += 1
            #get villain position
            villain_position = common.getPreflopPosition_name(t, t.seats[villain_position_number].name)
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip_cutted")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip_cutted")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op_cutted")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op_cutted")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
    elif situation == "10BB+opened-raised-wearehere-morebehind":
        settings.threebet += 1
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            biggest_bet = common.find_biggest_bet(t)
            villain_position = ""
            #get raisor position number
            villain_position_number = 7 # no such position
            counter = 0
            for s in t.seats:
                if s.bet == biggest_bet:
                    if villain_position_number == 7:
                        villain_position_number = counter
                counter += 1
            #get villain position
            villain_position = common.getPreflopPosition_name(t, t.seats[villain_position_number].name)
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip_cutted")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip_cutted")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op_cutted")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op_cutted")
                else:
                    selected_range = t.seats[index].range_top6
                    common.debugranges(situation, "range_top6")
    elif situation == "10BB+opened-raised-called-wearehere":
        settings.threebet += 1
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            biggest_bet = common.find_biggest_bet(t)
            villain_position = ""
            #get raisor position number
            villain_position_number = 7 # no such position
            counter = 0
            for s in t.seats:
                if s.bet == biggest_bet:
                    if villain_position_number == 7:
                        villain_position_number = counter
                counter += 1
            #get villain position
            villain_position = common.getPreflopPosition_name(t, t.seats[villain_position_number].name)
            hero_position = common.getPreflopPosition_name(t, t.seats[index].name)
            hero_has_position = 0
            if hero_position == "db" or villain_position == "sb":
                hero_has_position = 1
            if villain_position == "ug" and hero_position != "sb" and hero_position != "bb":
                hero_has_position = 1
            elif (villain_position == "hj") and ((hero_position == "co") or (hero_position == "db")):
                hero_has_position = 1
            if hero_has_position:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_ip
                    t.seats[index].learning_range_name = "range_defend_vs_ug_ip"
                    common.debugranges(situation, "range_defend_vs_ug_ip_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_ip
                    t.seats[index].learning_range_name = "range_defend_vs_hj_ip"
                    common.debugranges(situation, "range_defend_vs_hj_ip_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_ip
                    t.seats[index].learning_range_name = "range_defend_vs_co_ip"
                    common.debugranges(situation, "range_defend_vs_co_ip_cutted")
                elif villain_position == "sb":
                    selected_range = t.seats[index].range_defend_vs_sb_ip
                    t.seats[index].learning_range_name = "range_defend_vs_sb_ip"
                    common.debugranges(situation, "range_defend_vs_sb_ip_cutted")
                else:
                    #raised called move on we have to check and continue
                    selected_range = t.seats[index].range_fold
                    common.debugranges(situation, "tough_spot_range")

            else:
                if villain_position == "ug":
                    selected_range = t.seats[index].range_defend_vs_ug_op
                    t.seats[index].learning_range_name = "range_defend_vs_ug_op"
                    common.debugranges(situation, "range_defend_vs_ug_op_cutted")
                elif villain_position == "hj":
                    selected_range = t.seats[index].range_defend_vs_hj_op
                    t.seats[index].learning_range_name = "range_defend_vs_hj_op"
                    common.debugranges(situation, "range_defend_vs_hj_op_cutted")
                elif villain_position == "co":
                    selected_range = t.seats[index].range_defend_vs_co_op
                    t.seats[index].learning_range_name = "range_defend_vs_co_op"
                    common.debugranges(situation, "range_defend_vs_co_op_cutted")
                elif villain_position == "db":
                    selected_range = t.seats[index].range_defend_vs_db_op
                    t.seats[index].learning_range_name = "range_defend_vs_db_op"
                    common.debugranges(situation, "range_defend_vs_db_op_cutted")
                else:
                    if hero_position == "ug":
                        selected_range = t.seats[index].range_ug_open
                        t.seats[index].learning_range_name = "range_ug_open"
                        common.debugranges(situation, "range_ug_open")
                    elif hero_position == "hj":
                        selected_range = t.seats[index].range_hj_open
                        t.seats[index].learning_range_name = "range_hj_open"
                        common.debugranges(situation, "range_hj_open")
                    elif hero_position == "co":
                        selected_range = t.seats[index].range_co_open
                        t.seats[index].learning_range_name = "range_co_open"
                        common.debugranges(situation, "range_co_open")
                    elif hero_position == "db":
                        selected_range = t.seats[index].range_db_open
                        t.seats[index].learning_range_name = "range_db_open"
                        common.debugranges(situation, "range_db_open")
                    elif hero_position == "sb":
                        selected_range = t.seats[index].range_sb_open
                        t.seats[index].learning_range_name = "range_sb_open"
                        common.debugranges(situation, "range_sb_open")
                    elif hero_position == "hd":
                        selected_range = t.seats[index].range_hd_open
                        t.seats[index].learning_range_name = "range_hd_open"
                        common.debugranges(situation, "range_hd_open")
                    settings.threebet += 1                 
    elif situation == "10BB+opened-raised-reraised-wearehere":
        if t.seats[index].stack <= smallblind*20:
            selected_range = t.seats[index].range_under10bb_push_vs_more
            t.seats[index].learning_range_name = "range_under10bb_push_vs_more"
            common.debugranges(situation, "range_under10bb_push_vs_more")
        else:
            for h in settings.tough_spot_range:
                selected_range.append(h)
            common.debugranges(situation, "tough_spot_range")
    elif situation == "tough-spot":
        for h in settings.tough_spot_range:
            selected_range.append(h)
        common.debugranges(situation, "tough_spot_range")
    else:
        situation = "play-safe"
        selected_range = t.seats[index].range_safe
        t.seats[index].learning_range_name = "range_safe"
        common.debugranges(situation, "range_safe")

    if settings.threebet:
        biggest_bet = common.find_biggest_bet(t)
        bully = 0
        for whoisbully in t.seats:
            if whoisbully.bet == biggest_bet:
                #if someone is constantly 3 betting, play wider vs him
                bully = whoisbully.last3bets
        if bully < 1:
            bully = 1 #if theres no 3 bet this cant be zero
        current_bet = 0.0
        pot = 0.0
        for s in t.seats:
            if s.name == botname:
                current_bet = s.bet
            pot += s.bet
        need_to_flat = biggest_bet - current_bet
        ratio = need_to_flat/pot
        number_of_hands = len(selected_range)
        cutted_number_of_hands = round(bot_aggression*number_of_hands/(200*ratio)) * bully #usually this is 1
        if cutted_number_of_hands >= number_of_hands: #because of bully factor
            cutted_number_of_hands = number_of_hands - 1
        if len(selected_range):
            selected_range = selected_range[:cutted_number_of_hands] + t.seats[0].range_top6
        else:
            selected_range = t.seats[0].range_top6
            common.debugranges(situation, "top6")

        if len(selected_range) < 4:
            selected_range = t.seats[0].range_top6
            common.debugranges(situation, "top6")
        
    if playing_this_hand_light:
        selected_range.extend(t.seats[index].range_preflop_light)
        if settings.debug_ranges and settings.view:
            if settings.colors_on:
                print(settings.GREY + " + range_light" + settings.RESET)
            else:
                print(" + range_light")
        else:
            pass
        
    return selected_range