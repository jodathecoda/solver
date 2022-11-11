#copyright (c) 2019
#jodathecoda@yahoo.com

import settings
import time

threshold_added_open_from_checks = 0.05

fold_bar_color = settings.CYAN    + "|fold|"  + settings.RESET
check_bar_color = settings.CYAN   + "|check|" + settings.RESET
bet_bar_color = settings.CYAN   + "|bet|"   + settings.RESET
bluff_bar_color = settings.CYAN  + "|bluff|" + settings.RESET
call_bar_color = settings.CYAN + "|call|"  + settings.RESET
raise_bar_color = settings.CYAN + "|raise|" + settings.RESET
shove_bar_color = settings.CYAN + "|shove|" + settings.RESET

def yesno(yepo, wait_for_showdown):
    if wait_for_showdown:
        return
    print(" ")
    yep = int(yepo)
    if settings.debug_postflop and settings.hero == 'hero':
        if yep:
            if settings.colors_on:
                print(settings.CYAN + "yes" + settings.RESET)
            else:
                print("yes")
        else:
            if settings.colors_on:
                print(settings.BLUE + "no" + settings.RESET)
            else:
                print("no")
        if settings.debug_postflop_stop_point:
            dumb = input("]")
        else:
            time.sleep(settings.time_to_wait_board)

def report_header(st, seat, equx):
    s = seat
    print(" ")
    if st == 1:
        print("flop aggression: " + str(s.faggression))
    elif st == 2:
        print("turn aggression: " + str(s.taggression))
    elif st == 3:
        print("river aggression: " + str(s.raggression))
    else:
        print("error unknown street number in indepth report: " + str(st))
        dumb = input("]")
    print("perceived equity: " + str(equx))
    print(" ")

def get_raise_on_street(st):
    raised_street_index = 0
    if st == 1:
        raised_street_index = settings.raise_on_flop
    elif st == 2:
        raised_street_index = settings.raise_on_turn
    elif st == 3:
        raised_street_index = settings.raise_on_river
    else:
        print("error unknown street number in indepth report: " + str(st))
        dumb = input("]")
    return raised_street_index

def get_checks_on_street(st):
    check_street_index = 0
    if st == 1:
        check_street_index = settings.checks_on_flop
    elif st == 2:
        check_street_index = settings.checks_on_turn
    elif st == 3:
        check_street_index = settings.checks_on_river
    else:
        print("error unknown street number in indepth report: " + str(st))
        dumb = input("]")
    return check_street_index

def report_fold_shove(threshold1, equx):
    if settings.colors_on:
        if equx < threshold1:
            settings.fold_bar = fold_bar_color
        else:
            settings.shove_bar = shove_bar_color
    print(settings.fold_bar + str(round(threshold1,2)) + settings.shove_bar)

def report_fold_call_raise(threshold1, threshold2, equx):
    if settings.colors_on:
        if equx < threshold1:
            settings.fold_bar = fold_bar_color
        elif equx < threshold2:
            settings.call_bar = call_bar_color
        else:
            settings.raise_bar = raise_bar_color
    print(settings.fold_bar + str(round(threshold1,2)) + settings.call_bar + str(round(threshold2,2)) + settings.raise_bar)

def report_fold_bet(threshold1, equx, checks_on_street):
    if settings.colors_on:
        if equx < round(threshold1 - checks_on_street*threshold_added_open_from_checks,2):
            settings.check_bar = check_bar_color
        else:
            settings.bet_bar = bet_bar_color
    print(settings.check_bar + str(round(threshold1 - checks_on_street*threshold_added_open_from_checks,2)) + settings.bet_bar)

def report_fold_bluff_call_raise(street, threshold1, threshold2, threshold3, equx):
    st = street
    if st == 3:
        if settings.colors_on:
        #river shcema
            if equx < threshold1:
                settings.bluff_bar = bluff_bar_color
            elif equx > threshold3:
                settings.raise_bar = raise_bar_color
            else:
                settings.call_bar = call_bar_color
        print(settings.bluff_bar + str(round(threshold1,2)) + settings.call_bar + str(round(threshold3,2)) + settings.raise_bar)

    else:
        if settings.colors_on:
        #flop or turn
            if equx < threshold1:
                settings.fold_bar = fold_bar_color
            elif equx < threshold2:
                settings.bluff_bar = bluff_bar_color
            elif equx < threshold3:
                settings.call_bar = call_bar_color
            else:
                settings.raise_bar = raise_bar_color
        print(settings.fold_bar + str(round(threshold1,2)) + settings.bluff_bar + str(round(threshold2,2)) + settings.call_bar + str(round(threshold3,2)) + settings.raise_bar)

#open
def report_river_bluff_check_open(threshold1, threshold2, equx):
    if settings.colors_on:
        if equx < threshold1:
            settings.bluff_bar = bluff_bar_color
        elif equx <= threshold2:
            settings.check_bar = check_bar_color
        elif equx > threshold2:
            settings.bet_bar = bet_bar_color
        else:
            print("report river bluff check open error")
            dumb = input("]")
    print(settings.bluff_bar + str(round(threshold1,2)) + settings.check_bar + str(round(threshold2,2)) + settings.bet_bar)

def report(street, gamblers, equx, seat, smallest_bet, biggest_bet):
    s = seat
    if settings.colors_on:
        settings.fold_bar =  settings.BLUE + "|fold|" + settings.RESET
        settings.check_bar = settings.BLUE + "|check|" + settings.RESET
        settings.bet_bar =   settings.BLUE + "|bet|" + settings.RESET
        settings.bluff_bar = settings.BLUE + "|bluff|" + settings.RESET
        settings.call_bar =  settings.BLUE + "|call|" + settings.RESET
        settings.raise_bar = settings.BLUE + "|raise|" + settings.RESET
        settings.shove_bar = settings.BLUE + "|shove|" + settings.RESET
    else:
        settings.fold_bar =  "|fold|"
        settings.check_bar = "|check|"
        settings.bet_bar =   "|bet|"
        settings.bluff_bar = "|bluff|"
        settings.call_bar =  "|call|"
        settings.raise_bar = "|raise|"
        settings.shove_bar = "|shove|"
    report_header(street, seat, equx)
    raised_street = int(get_raise_on_street(street))    #get raises on street
    checks_on_street = int(get_checks_on_street(street)) #get checks on street
    #report based on street:
    if gamblers == 2:
        if raised_street == 2:
            if street == 1:
                threshold1 = s.threshold_flop_shove
            elif street == 2:
                threshold1 = s.threshold_turn_shove
            elif street == 3:
                threshold1 = s.threshold_river_shove
            else:
                print("error unknown street number in indepth report: " + str(st))
                dumb = input("]")
            report_fold_shove(threshold1, equx)
        elif raised_street == 1:
            if street == 1:
                threshold1 = s.threshold_flop_call3bet_vs_one
                threshold2 = s.threshold_flop_raise4bet_vs_one
            elif street == 2:
                threshold1 = s.threshold_turn_call3bet_vs_one
                threshold2 = s.threshold_turn_raise4bet_vs_one
            elif street == 3:
                threshold1 = s.threshold_river_call3bet_vs_one
                threshold2 = s.threshold_river_raise4bet_vs_one
            else:
                print("error unknown street number in indepth report: " + str(st))
                dumb = input("]")
            report_fold_call_raise(threshold1, threshold2, equx)
        elif smallest_bet == biggest_bet:
            if street == 1:
                threshold1 = s.threshold_flop_open_vs_one
            elif street == 2:
                threshold1 = s.threshold_turn_open_vs_one
            elif street == 3:
                threshold1 = s.threshold_river_bluff_vs_one
                threshold2 = s.threshold_river_open_vs_one
            else:
                print("error unknown street number in indepth report: " + str(st))
                dumb = input("]")
            if street == 3:
                #report river open with bluffs
                report_river_bluff_check_open(threshold1, threshold2, equx)
            else:
                #flop or turn open
                report_fold_bet(threshold1, equx, checks_on_street)
        else:
            if street == 1:
                threshold1 = s.threshold_flop_bluff_vs_one
                threshold2 = s.threshold_flop_call_vs_one
                threshold3 = s.threshold_flop_raise_vs_one
            elif street == 2:
                threshold1 = s.threshold_turn_bluff_vs_one
                threshold2 = s.threshold_turn_call_vs_one
                threshold3 = s.threshold_turn_raise_vs_one
            elif street == 3:
                threshold1 = s.threshold_river_bluff_vs_one
                threshold2 = 0 #s.threshold_river_call_vs_one
                threshold3 = s.threshold_river_raise_vs_one
            else:
                print("error unknown street number in indepth report: " + str(st))
                dumb = input("]")
            report_fold_bluff_call_raise(street, threshold1, threshold2, threshold3, equx)
    else:
        #gamblers more than heads up
        if raised_street == 2:
            if street == 1:
                threshold1 = s.threshold_flop_shove
            elif street == 2:
                threshold1 = s.threshold_turn_shove
            elif street == 3:
                threshold1 = s.threshold_river_shove
            else:
                print("error unknown street number in indepth report: " + str(st))
                dumb = input("]")
            report_fold_shove(threshold1, equx)
        elif raised_street == 1:
            if street == 1:
                threshold1 = s.threshold_flop_call3bet_vs_more
                threshold2 = s.threshold_flop_raise4bet_vs_more
            elif street == 2:
                threshold1 = s.threshold_turn_call3bet_vs_more
                threshold2 = s.threshold_turn_raise4bet_vs_more
            elif street == 3:
                threshold1 = s.threshold_river_call3bet_vs_more
                threshold2 = s.threshold_river_raise4bet_vs_more
            else:
                print("error unknown street number in indepth report: " + str(st))
                dumb = input("]")
            report_fold_call_raise(threshold1, threshold2, equx)
        elif smallest_bet == biggest_bet:
            if street == 1:
                threshold1 = s.threshold_flop_open_vs_more
            elif street == 2:
                threshold1 = s.threshold_turn_open_vs_more
            elif street == 3:
                threshold1 = s.threshold_river_open_vs_more
            else:
                print("error unknown street number in indepth report: " + str(st))
                dumb = input("]")
            report_fold_bet(threshold1, equx, checks_on_street)
        else:
            if street == 1:
                threshold1 = s.threshold_flop_call_vs_more
                threshold2 = s.threshold_flop_raise_vs_more
            elif street == 2:
                threshold1 = s.threshold_turn_call_vs_more
                threshold2 = s.threshold_turn_raise_vs_more
            elif street == 3:
                threshold1 = s.threshold_river_call_vs_more
                threshold2 = s.threshold_river_raise_vs_more
            else:
                print("error unknown street number in indepth report: " + str(st))
                dumb = input("]")
            report_fold_call_raise(threshold1, threshold2, equx)

    if settings.debug_postflop_stop_point:
        dumb = input("]")
    else:
        time.sleep(settings.time_to_wait_board)


