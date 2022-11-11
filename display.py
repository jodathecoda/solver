#copyright (c) 2019
#jodathecoda@yahoo.com


import settings
import common

display_board_offset0  = "          "
display_board_offseta = display_board_offset0

def print_1_table(counter_tables, table, game_type, smallblind, ante, tables):
    display_board_offseta = display_board_offset0
    if game_type == 't':
        print_type = "tournament"
        #we need to print info biggest, average and smallest stacks
        mtt_biggest_stack = 0
        mtt_average_stack = 0
        mtt_smallest_stack = 0
        mtt_sum_of_all_stacks = 0
        mtt_gamblers = 0.0001 # to avoid deletion by zero
        for mtt_table in tables:
            for mtt_seat in mtt_table.seats:
                if mtt_seat.stack > 0:
                    mtt_gamblers += 1
                    mtt_sum_of_all_stacks += mtt_seat.stack
                    #find biggest stack
                    if mtt_biggest_stack < mtt_seat.stack:
                        mtt_biggest_stack = mtt_seat.stack
        #now find smallest stack
        mtt_biggest_stack = common.roundbet(mtt_biggest_stack)
        mtt_smallest_stack = mtt_biggest_stack
        for mtt_table in tables:
            for mtt_seat in mtt_table.seats:
                if not mtt_seat.available:
                    if mtt_smallest_stack > mtt_seat.stack:
                        mtt_smallest_stack = mtt_seat.stack
        mtt_smallest_stack = common.roundbet(mtt_smallest_stack)
        #now calculate average stack
        mtt_average_stack = common.roundbet(mtt_sum_of_all_stacks/mtt_gamblers)
        #print report
        if settings.colors_on:
            print("biggest :" + settings.GREEN + str(mtt_biggest_stack) + settings.RESET)
            print("average :" + settings.YELLOW + str(mtt_average_stack) + settings.RESET)
            print("smallest:" + settings.RED + str(mtt_smallest_stack) + settings.RESET)
        else:
            print("biggest :" + str(mtt_biggest_stack))
            print("average :" + str(mtt_average_stack))
            print("smallest:" + str(mtt_smallest_stack))
        print(" ")
        print(" ")

    #else:
        #print("unknown game type")
        #dumb = input("]")

    feature_table_a = 0
    for s in tables[counter_tables].seats:
        if s.clock != " ":
            feature_table_a = 1

    if settings.fancy:
        pass
    else:
        #print gamblers positions if there is no face
        for s in tables[counter_tables].seats:
            s.face = s.learning_position

    '''
    print("effective stacks: " + str(common.get_effective_stacks(tables[counter_tables] , smallblind)))

    for s in tables[counter_tables].seats:
        if s.betting_lead:
            print(s.name + ":" + str(s.last3bets) + " L")
        else:
            print(s.name + ":" + str(s.last3bets))
    '''

    if settings.nash_push_fold:
        if tables[counter_tables].seats[0].name == "you":
            print("you: " + str(settings.nash_you) + "        villain: " + str(settings.nash_villain))
        elif tables[counter_tables].seats[1].name == "you":
            print("villain: " + str(settings.nash_villain) + "    you: " + str(settings.nash_you))
        else:
            print("seat0: " + str(settings.nash_0) + "      seat1: " + str(settings.nash_1))
        print("")

    #line 0 HUD
    if settings.hud:
        display_vbet0 = " "
        display_cbet0 = " "
        display_percent0 = " "
        display_vbet1 = " "
        display_cbet1 = " "
        display_percent1 = " "
        display_vbet2 = " "
        display_cbet2 = " "
        display_percent2 = " "
        if tables[counter_tables].seats[0].stack or tables[counter_tables].seats[0].bet:
            display_vbet0 = str(round(tables[counter_tables].seats[0].vbet*100/tables[counter_tables].seats[0].preorbits))
            display_percent0 = "%"
            display_cbet0 = str(round(tables[counter_tables].seats[0].cbet*100/tables[counter_tables].seats[0].floporbits))
        if tables[counter_tables].seats[1].stack or tables[counter_tables].seats[1].bet:
            display_vbet1 = str(round(tables[counter_tables].seats[1].vbet*100/tables[counter_tables].seats[1].preorbits))
            display_percent1 = "%"
            display_cbet1 = str(round(tables[counter_tables].seats[1].cbet*100/tables[counter_tables].seats[1].floporbits))
        if tables[counter_tables].seats[2].stack or tables[counter_tables].seats[2].bet:
            display_vbet2 = str(round(tables[counter_tables].seats[2].vbet*100/tables[counter_tables].seats[2].preorbits))
            display_percent2 = "%"
            display_cbet2 = str(round(tables[counter_tables].seats[2].cbet*100/tables[counter_tables].seats[2].floporbits))

        labelline_up = ""
        if settings.colors_on:
            labelline_up += settings.GREY
        if tables[counter_tables].seats[0].stack or tables[counter_tables].seats[0].bet:
            labelline_up += "VPIP CBET      "
        else:
            labelline_up += "               "
        if tables[counter_tables].seats[1].stack or tables[counter_tables].seats[1].bet:
            labelline_up += "VPIP CBET      "
        else:
            labelline_up += "               "
        if tables[counter_tables].seats[2].stack or tables[counter_tables].seats[2].bet:
            labelline_up += "VPIP CBET      "
        else:
            labelline_up += "               "
        print(labelline_up)
        print('%-3s%-1s%1s%-3s%-1s%-6s%-3s%-1s%-1s%-3s%-1s%-6s%-3s%-1s%-1s%-3s%-1s' % (\
        display_vbet0, display_percent0, " ",display_cbet0, display_percent0, " ",\
        display_vbet1, display_percent1, " ",display_cbet1, display_percent1, " ",\
        display_vbet2, display_percent2, " ",display_cbet2, display_percent2\
        + settings.RESET))
    
    #line 1
    print('%-2s%-1s%-5s%-6s%-2s%-1s%-5s%-6s%-2s%-1s%-5s%-6s' % (tables[counter_tables].seats[0].face, " ", tables[counter_tables].seats[0].displaystack, tables[counter_tables].seats[0].clock, \
                                                                tables[counter_tables].seats[1].face, " ", tables[counter_tables].seats[1].displaystack, tables[counter_tables].seats[1].clock, \
                                                                tables[counter_tables].seats[2].face, " ", tables[counter_tables].seats[2].displaystack, tables[counter_tables].seats[2].clock))
    #line 2
    print('%-5s%-2s%-2s%-6s%-5s%-2s%-2s%-6s%-5s%-2s%-2s%-6s' % (tables[counter_tables].seats[0].name[:4], tables[counter_tables].seats[0].displaycard1, tables[counter_tables].seats[0].displaycard2, " ", \
                                                                tables[counter_tables].seats[1].name[:4], tables[counter_tables].seats[1].displaycard1, tables[counter_tables].seats[1].displaycard2, " ", \
                                                                tables[counter_tables].seats[2].name[:4], tables[counter_tables].seats[2].displaycard1, tables[counter_tables].seats[2].displaycard2, " "))
    
    #line 3
    if settings.colors_on:
        #final table will be in red
        if (game_type == 't') and (len(tables) == 1):
            print(settings.RED + "---------------------------------------" + settings.RESET)
        else:
            print(settings.YELLOW + "---------------------------------------" + settings.RESET)
    else:
        print("---------------------------------------")

    #line 4
    print('%-2s%-2s%-11s%-2s%-13s%-2s%-6s%-2s' % (" ", tables[counter_tables].seats[0].button, tables[counter_tables].seats[0].displaybet, \
                                                            tables[counter_tables].seats[1].button, tables[counter_tables].seats[1].displaybet, \
                                                            tables[counter_tables].seats[2].button, tables[counter_tables].seats[2].displaybet, " "))
    #line 5
    print("                                       ")
    if game_type == 't':
        if settings.colors_on:
            print('%-9s%-1s%-6s%-1s%-1s%-1s%-1s%-11s%-8s%-1s' % (" ", settings.GREY ,"table:" , str(counter_tables+ 1) , "/" , str(len(tables)) , " " , "next level:" , str(settings.current_iterations_to_next_level - settings.current_iterations), settings.RESET))
        else:
            print('%-9s%-6s%-1s%-1s%-1s%-1s%-11s%-8s%-1s' % (" ", "table:" , str(counter_tables+ 1) , "/" , str(len(tables)) , " " , "next level:" , str(settings.current_iterations_to_next_level - settings.current_iterations), " "))
    elif game_type == 'c':
        print(" ")
    else:
        if settings.colors_on:
            print('%-8s%-1s%-1s%-1s%-11s%-8s%-1s' % (" ", settings.GREY ," ", " " , "next level:" , str(settings.current_iterations_to_next_level - settings.current_iterations), settings.RESET))
        else:
            print('%-8s%-1s%-1s%-1s%-11s%-8s%-1s' % (" ", " " ," ", " " , "next level:" , str(settings.current_iterations_to_next_level - settings.current_iterations), " "))

    #line 6
    print('%-12s%-6s%-20s%-1s' % (" ", "board:", tables[counter_tables].displayboard + display_board_offseta," "))

    #line 7
    print('%-14s%-10s%-14s%-1s' % (" ", "pot:" + str(tables[counter_tables].displaypot)," ", " "))

    #line 8
    print("                                       ")

    #line 9
    print('%-2s%-2s%-11s%-2s%-13s%-2s%-6s%-2s' % (" ", tables[counter_tables].seats[5].button, tables[counter_tables].seats[5].displaybet, \
                                                            tables[counter_tables].seats[4].button, tables[counter_tables].seats[4].displaybet, \
                                                            tables[counter_tables].seats[3].button, tables[counter_tables].seats[3].displaybet, " "))

    #line 10
    if settings.colors_on:
        #final table will be in red
        if (game_type == 't') and (len(tables) == 1):
            print(settings.RED + "---------------------------------------" + settings.RESET)
        else:
            print(settings.YELLOW + "---------------------------------------" + settings.RESET)
    else:
        print("---------------------------------------")


    #line 11
    print('%-2s%-1s%-5s%-6s%-2s%-1s%-5s%-6s%-2s%-1s%-5s%-6s' % (tables[counter_tables].seats[5].face, " ", tables[counter_tables].seats[5].displaystack, tables[counter_tables].seats[5].clock, \
                                                                tables[counter_tables].seats[4].face, " ", tables[counter_tables].seats[4].displaystack, tables[counter_tables].seats[4].clock, \
                                                                tables[counter_tables].seats[3].face, " ", tables[counter_tables].seats[3].displaystack, tables[counter_tables].seats[3].clock))
    #line 12
    print('%-5s%-2s%-2s%-6s%-5s%-2s%-2s%-6s%-5s%-2s%-2s%-6s' % (tables[counter_tables].seats[5].name[:4], tables[counter_tables].seats[5].displaycard1, tables[counter_tables].seats[5].displaycard2, " ", \
                                                                tables[counter_tables].seats[4].name[:4], tables[counter_tables].seats[4].displaycard1, tables[counter_tables].seats[4].displaycard2, " ", \
                                                                tables[counter_tables].seats[3].name[:4], tables[counter_tables].seats[3].displaycard1, tables[counter_tables].seats[3].displaycard2, " "))
    #line 13 HUD
    if settings.hud:
        display_vbet5 = " "
        display_cbet5 = " "
        display_percent5 = " "
        display_vbet4 = " "
        display_cbet4 = " "
        display_percent4 = " "
        display_vbet3 = " "
        display_cbet3 = " "
        display_percent3 = " "
        if tables[counter_tables].seats[5].stack or tables[counter_tables].seats[5].bet:
            display_vbet5 = str(round(tables[counter_tables].seats[5].vbet*100/tables[counter_tables].seats[5].preorbits))
            display_percent5 = "%"
            display_cbet5 = str(round(tables[counter_tables].seats[5].cbet*100/tables[counter_tables].seats[5].floporbits))
        if tables[counter_tables].seats[4].stack or tables[counter_tables].seats[4].bet:
            display_vbet4 = str(round(tables[counter_tables].seats[4].vbet*100/tables[counter_tables].seats[4].preorbits))
            display_percent4 = "%"
            display_cbet4 = str(round(tables[counter_tables].seats[4].cbet*100/tables[counter_tables].seats[4].floporbits))
        if tables[counter_tables].seats[3].stack or tables[counter_tables].seats[3].bet:
            display_vbet3 = str(round(tables[counter_tables].seats[3].vbet*100/tables[counter_tables].seats[3].preorbits))
            display_percent3 = "%"
            display_cbet3 = str(round(tables[counter_tables].seats[3].cbet*100/tables[counter_tables].seats[3].floporbits))
        labelline_down = ""
        if settings.colors_on:
            labelline_down += settings.GREY
        if tables[counter_tables].seats[5].stack or tables[counter_tables].seats[5].bet:
            labelline_down += "VPIP CBET      "
        else:
            labelline_down += "               "
        if tables[counter_tables].seats[4].stack or tables[counter_tables].seats[4].bet:
            labelline_down += "VPIP CBET      "
        else:
            labelline_down += "               "
        if tables[counter_tables].seats[3].stack or tables[counter_tables].seats[3].bet:
            labelline_down += "VPIP CBET      "
        else:
            labelline_down += "               "
        print(labelline_down)
        print('%-3s%-1s%1s%-3s%-1s%-6s%-3s%-1s%-1s%-3s%-1s%-6s%-3s%-1s%-1s%-3s%-1s' % (\
        display_vbet5, display_percent5, " ",display_cbet5, display_percent5, " ",\
        display_vbet4, display_percent4, " ",display_cbet4, display_percent4, " ",\
        display_vbet3, display_percent3, " ",display_cbet3, display_percent3\
        + settings.RESET))

def display_tables_standard(table, game_type, smallblind, ante, tables):
    for t in tables:
        for s in t.seats:
            s.displaycard1 = settings.cards_back
            s.displaycard2 = settings.cards_back
            if ((s.name == settings.hero) or (settings.cards_faceup)):
                s.displaycard1 = common.displayhand(s.card1)
                s.displaycard2 = common.displayhand(s.card2)
            if s.card1 == "  ":
                s.displaycard1 = settings.cards_fold
                s.displaycard2 = settings.cards_fold

    for t in tables:
            t.displayboard = common.displayhand(t.board)

    for t in tables:
        if settings.cards_faceup:
            for s in t.seats:
                s.displaycard1 = common.displayhand(s.card1)
                s.displaycard2 = common.displayhand(s.card2)
    

    for t in tables:
        for s in t.seats:
            if s.bet == 0:
                s.displaybet = " "
            else:
                s.displaybet = str(common.roundbet(s.bet))

    for t in tables:
        t.displaypot = str(common.roundbet(t.pot))

    for t in tables:
        for s in t.seats:
            if s.stack == 0:
                s.displaystack = "  "
            else:
                s.displaystack = str(common.roundbet(s.stack))
            if s.stack > 99999 or len(str(s.stack)) > 5:
                dumbstack = common.roundbet(s.stack/1000)
                if dumbstack == 0:
                    s.displaystack = "1000"
                else:
                    s.displaystack = str(dumbstack) + "k"  
    counter_tables = 0
    for t in tables:
        displayit = 0
        for z in t.seats:
            if (z.clock != " " or z.bet > 0) and (t.pot > 0.1):
                displayit = 1
        if displayit:
            settings.print_logo()
            print_1_table(counter_tables, t, game_type, smallblind, ante, tables)
        counter_tables +=1

def display_tables_incognito(table, game_type, smallblind, ante, tables):
    settings.spade = "s"
    settings.club = "c"
    settings.diamond = "d"
    settings.heart = "h"
    for t in tables:
        for s in t.seats:
            s.displaycard1 = settings.cards_back
            s.displaycard2 = settings.cards_back
            if ((s.name == settings.hero) or (settings.cards_faceup)):
                s.displaycard1 = s.card1
                s.displaycard2 = s.card2
            if s.card1 == "  ":
                s.displaycard1 = settings.cards_fold
                s.displaycard2 = settings.cards_fold  
    counter_tables = 0
    for t in tables:
        displayit = 0
        for z in t.seats:
            if (z.clock != " " or z.bet > 0) and (t.pot > 0.1):
                displayit = 1
        if displayit:
            wait_for_showdown = 0
            if common.wait_showdown(t, smallblind, ante):
                wait_for_showdown = 1
            else:
                wait_for_showdown = 0
            settings.clearscreen()
            print("mf: " + str(settings.myflush))
            print("ms: " + str(settings.mystraight))
            settings.cards_faceup = 1
            for zeetz in t.seats:
                if zeetz.name == settings.hero:
                    settings.cards_faceup = 0
                if zeetz.betting_lead:
                    print("bl:" + zeetz.learning_position)

            if not settings.cards_faceup and wait_for_showdown:
                    settings.cards_faceup = 1
            
            if game_type == 't':
                print("t:" + str(counter_tables + 1) + "/" + str(len(tables)) + " nl:" + str(settings.current_iterations_to_next_level - settings.current_iterations) + " ")
            print("p: " + str(t.pot))
            if len(t.board) < 2:
                #preflop aggression
                if settings.hud:
                    for s in t.seats:
                        if not s.available:
                            print(s.learning_position  + s.button + s.clock + s.displaycard1 + s.displaycard2 +  " " + str(common.roundbet(s.stack)) + " " + str(s.bet) + " " + str(round(s.vbet*100/s.preorbits)) + "% " + str(round(s.cbet*100/s.floporbits)) + "%")
                else:
                    for s in t.seats:
                        if not s.available:
                            print(s.learning_position  + s.button + s.clock + s.displaycard1 + s.displaycard2 +  " " + str(common.roundbet(s.stack)) + " " + str(s.bet))
            elif len(t.board) == 6:
                #flop aggression
                if settings.hud:
                    for s in t.seats:
                        if not s.available:
                            print(s.learning_position  + s.button + s.clock + s.displaycard1 + s.displaycard2 +  " " + str(common.roundbet(s.stack)) + " " + str(s.bet) + " " + str(round(s.vbet*100/s.preorbits)) + "% " + str(round(s.cbet*100/s.floporbits)) + "%")
                else:
                    for s in t.seats:
                        if not s.available:
                            print(s.learning_position  + s.button + s.clock + s.displaycard1 + s.displaycard2 +  " " + str(common.roundbet(s.stack)) + " " + str(s.bet))
            elif len(t.board) == 8:
                #turn aggression
                if settings.hud:
                    for s in t.seats:
                        if not s.available:
                            print(s.learning_position  + s.button + s.clock + s.displaycard1 + s.displaycard2 +  " " + str(common.roundbet(s.stack)) + " " + str(s.bet) + " " + str(round(s.vbet*100/s.preorbits)) + "% " + str(round(s.cbet*100/s.floporbits)) + "%")
                else:
                    for s in t.seats:
                        if not s.available:
                            print(s.learning_position  + s.button + s.clock + s.displaycard1 + s.displaycard2 +  " " + str(common.roundbet(s.stack)) + " " + str(s.bet))
            elif len(t.board) == 10:
                #river aggression
                if settings.hud:
                    for s in t.seats:
                        if not s.available:
                            print(s.learning_position  + s.button + s.clock + s.displaycard1 + s.displaycard2 +  " " + str(common.roundbet(s.stack)) + " " + str(s.bet) + " " + str(round(s.vbet*100/s.preorbits)) + "% " + str(round(s.cbet*100/s.floporbits)) + "%")
                else:
                    for s in t.seats:
                        if not s.available:
                            print(s.learning_position  + s.button + s.clock + s.displaycard1 + s.displaycard2 +  " " + str(common.roundbet(s.stack)) + " " + str(s.bet))

            print(t.board)
        else:
            pass
        counter_tables +=1

def display_tables_indicator(table, game_type, smallblind, ante, tables):
    if settings.oldview < 4:
        if (settings.followfish in settings.allfishes) and (not settings.analyser_flag):
            settings.print_logo_menu() #follower
        else:
            settings.print_logo_teacher()
    else:
        settings.clearscreen()
    #basic_offset = "    "
    if settings.oldview < 4:
        if game_type == 'h':
            print("heads up: " + str(settings.left_loops))
        elif game_type == 's':
            print("spin & go: " + str(settings.left_loops))
        elif game_type == 'c':
            print("cash game: " + str(settings.left_loops))
        else:
            print("tournament: " + str(settings.left_loops))
        print("learning: " + str(settings.games_before_learning))
    elif settings.colors_on:
        print(settings.GREY + "ctrl+c stop" + settings.RESET)
        print(game_type + ":" + str(settings.left_loops))
        print("l:" + str(settings.games_before_learning))
    else:
        print("ctrl+c stop")
        print(game_type + ":" + str(settings.left_loops))
        print("l:" + str(settings.games_before_learning))

    for t in tables:
        player_line = ""
        #print(basic_offset)
        print("    ")
        for s in t.seats:
            if s.clock != " ":
                player_line += "*"
            elif s.stack  <= 0.1:
                player_line += " "
            else:
                player_line += "."
        print(player_line)

def display_tables(table, game_type, smallblind, ante, tables):
    #print("tables:" + str(len(tables)))
    #dumb = input("]")
    if settings.view == 0:
        return
    elif settings.view == 1:
        display_tables_standard(table, game_type, smallblind, ante, tables)
        return
    elif settings.view == 2:
        display_tables_standard(table, game_type, smallblind, ante, tables)
        return
    elif settings.view == 3:
        display_tables_indicator(table, game_type, smallblind, ante, tables)
        return
    elif settings.view == 4:
        display_tables_incognito(table, game_type, smallblind, ante, tables)
        return
    else:
        pass

def display_tables_analyser(table, iterations, matched):
    settings.print_logo_analyser_action()
    if settings.analysis_end:
        print_a_table_analysis(table, iterations, matched)
        print("open bet sizing: " + settings.huanalyzer_open_size)
        dumb = input("[end of analysis]")
        settings.analysis_end = 0
    elif settings.analyse_fast_speed:
        print_a_indicator_analysis(table, iterations, matched)
    else:
        print_a_table_analysis(table, iterations, matched)

def print_a_table_analysis(t, it, ma):
    ta = t
    display_board_offseta = display_board_offset0
    
    for s in ta.seats:
        if s.stack <= settings.dumblind*1.5:
            s.displaycard1 = "  "
            s.displaycard2 = "  "
        else:
            s.displaycard1 = common.displayhand(s.card1)
            s.displaycard2 = common.displayhand(s.card2)
        if s.stack == 0:
            s.displaystack = "  "
        else:
            s.displaystack = str(common.roundbet(s.stack))
        if s.stack > 99999 or len(str(s.stack)) > 5:
            dumbstack = common.roundbet(s.stack/1000)
            if dumbstack == 0:
                s.displaystack = "1000"
            else:
                s.displaystack = str(dumbstack) + "k" 
    
    for ss in ta.seats:
        if ss.bet < 0.5:
            ss.displaybet = " "
        else:
            ss.displaybet = str(round(ss.bet))
    
    thepot = 0
    for ss in ta.seats:
        if ss.bet > 0.5:
            thepot += ss.bet

    ta.displaypot = round(thepot)


    ta.displayboard = common.displayhand(ta.board)
    disp_starting_point = " "
    if ta.starting_point == 'p':
        disp_starting_point = "preflop"
    elif ta.starting_point == 'f':
        disp_starting_point = "flop"
    elif ta.starting_point == 't':
        disp_starting_point = "turn"
    elif ta.starting_point == 'r':
        disp_starting_point = "river"
    else:
        print("unknown starting point in print_a_table")
        dumb = input("]")

    print("iterations:" + str(it))
    if settings.colors_on:
        if settings.analyse_match:
            #we have current match
            print(settings.GREEN + "[+]" + settings.RESET + "matched:" + str(round(ma)))
        else:
            #no current match
            print(settings.RED + "[-]" + settings.RESET + "matched:" + str(round(ma)))
    else:
        if settings.analyse_match:
            #we have current match
            print("[+]matched:" + str(round(ma)))
        else:
            #no current match
            print("[-]matched:" + str(round(ma)))

    print(" ")


    big_blinds_value0 = "   "
    big_blinds_value1 = "   "
    big_blinds_value2 = "   "
    big_blinds_value3 = "   "
    big_blinds_value4 = "   "
    big_blinds_value5 = "   "


    big_blinds_value0 = str(round(settings.bbvals0/ma,2))
    big_blinds_value1 = str(round(settings.bbvals1/ma,2))
    big_blinds_value2 = str(round(settings.bbvals2/ma,2))
    big_blinds_value3 = str(round(settings.bbvals3/ma,2))
    big_blinds_value4 = str(round(settings.bbvals4/ma,2))
    big_blinds_value5 = str(round(settings.bbvals5/ma,2))

    if settings.colors_on:
        #stats0
        if settings.bbvals0/ma < 0:
            big_blinds_value0 = settings.RED + big_blinds_value0 + settings.RESET
        elif settings.bbvals0/ma > 0:
            big_blinds_value0 = settings.GREEN + big_blinds_value0 + settings.RESET
        else:
            big_blinds_value0 = settings.YELLOW + big_blinds_value0 + settings.RESET
        #stats1
        if settings.bbvals1/ma < 0:
            big_blinds_value1 = settings.RED + big_blinds_value1 + settings.RESET
        elif settings.bbvals1/ma > 0:
            big_blinds_value1 = settings.GREEN + big_blinds_value1 + settings.RESET
        else:
            big_blinds_value1 = settings.YELLOW + big_blinds_value1 + settings.RESET
        #stats2
        if settings.bbvals2/ma < 0:
            big_blinds_value2 = settings.RED + big_blinds_value2 + settings.RESET
        elif settings.bbvals2/ma > 0:
            big_blinds_value2 = settings.GREEN + big_blinds_value2 + settings.RESET
        else:
            big_blinds_value2 = settings.YELLOW + big_blinds_value2 + settings.RESET
        #stats3
        if settings.bbvals3/ma < 0:
            big_blinds_value3 = settings.RED + big_blinds_value3 + settings.RESET
        elif settings.bbvals3/ma > 0:
            big_blinds_value3 = settings.GREEN + big_blinds_value3 + settings.RESET
        else:
            big_blinds_value3 = settings.YELLOW + big_blinds_value3 + settings.RESET
        #stats4
        if settings.bbvals4/ma < 0:
            big_blinds_value4 = settings.RED + big_blinds_value4 + settings.RESET
        elif settings.bbvals4/ma > 0:
            big_blinds_value4 = settings.GREEN + big_blinds_value4 + settings.RESET
        else:
            big_blinds_value4 = settings.YELLOW + big_blinds_value4 + settings.RESET
        #stats5
        if settings.bbvals5/ma < 0:
            big_blinds_value5 = settings.RED + big_blinds_value5 + settings.RESET
        elif settings.bbvals5/ma > 0:
            big_blinds_value5 = settings.GREEN + big_blinds_value5 + settings.RESET
        else:
            big_blinds_value5 = settings.YELLOW + big_blinds_value5 + settings.RESET
    
    settings.report_bbv0 = big_blinds_value0 #this is for end of report
    settings.report_bbv1 = big_blinds_value1
    settings.report_bbv2 = big_blinds_value2
    settings.report_bbv3 = big_blinds_value3
    settings.report_bbv4 = big_blinds_value4
    settings.report_bbv5 = big_blinds_value5

    if settings.fancy:
        pass
    else:
        #print gamblers positions if there is no face
        for s in ta.seats:
            s.face = s.learning_position

    if  not settings.amap[0]:
        ta.seats[0].displaycard1 = "  "
        ta.seats[0].displaycard2 = "  "
        ta.seats[0].displaystack = "  "
        ta.seats[0].name = "     "
        if settings.colors_on:
            ta.seats[0].face = settings.GREY + ta.seats[0].learning_position + settings.RESET + " "

    if  not settings.amap[1]:
        ta.seats[1].displaycard1 = "  "
        ta.seats[1].displaycard2 = "  "
        ta.seats[1].displaystack = "  "
        ta.seats[1].name = "     "
        if settings.colors_on:
            ta.seats[1].face = settings.GREY + ta.seats[1].learning_position + settings.RESET + " "

    if  not settings.amap[2]:
        ta.seats[2].displaycard1 = "  "
        ta.seats[2].displaycard2 = "  "
        ta.seats[2].displaystack = "  "
        ta.seats[2].name = "     "
        if settings.colors_on:
            ta.seats[2].face = settings.GREY + ta.seats[2].learning_position + settings.RESET + " "

    if  not settings.amap[3]:
        ta.seats[3].displaycard1 = "  "
        ta.seats[3].displaycard2 = "  "
        ta.seats[3].displaystack = "  "
        ta.seats[3].name = "     "
        if settings.colors_on:
            ta.seats[3].face = settings.GREY + ta.seats[3].learning_position + settings.RESET + " "

    if  not settings.amap[4]:
        ta.seats[4].displaycard1 = "  "
        ta.seats[4].displaycard2 = "  "
        ta.seats[4].displaystack = "  "
        ta.seats[4].name = "     "
        if settings.colors_on:
            ta.seats[4].face = settings.GREY + ta.seats[4].learning_position + settings.RESET + " "

    if  not settings.amap[5]:
        ta.seats[5].displaycard1 = "  "
        ta.seats[5].displaycard2 = "  "
        ta.seats[5].displaystack = "  "
        ta.seats[5].name = "     "
        if settings.colors_on:
            ta.seats[5].face = settings.GREY + ta.seats[5].learning_position + settings.RESET + " "

    #line0
    zeroreport = "    "
    zeroblank = "             "
    reportline = ""
    if settings.amap[0]:
        reportline += settings.report_bbv0
    else:
        reportline += zeroreport
    reportline += zeroblank
    if settings.amap[1]:
        reportline += settings.report_bbv1
    else:
        reportline += zeroreport
    reportline += zeroblank
    if settings.amap[2]:
        reportline += settings.report_bbv2
    else:
        reportline += zeroreport
    reportline += zeroblank

    print(reportline)
    #print(settings.report_bbv0 + "             " + settings.report_bbv1 + "             " + settings.report_bbv2)


    #line 1
    print('%-2s%-1s%-5s%-7s%-2s%-1s%-5s%-7s%-2s%-1s%-5s%-7s' % (ta.seats[0].face, " ", ta.seats[0].displaystack, ta.seats[0].clock, \
                                                            ta.seats[1].face, " ", ta.seats[1].displaystack, ta.seats[1].clock, \
                                                            ta.seats[2].face, " ", ta.seats[2].displaystack, ta.seats[2].clock))
    #line 2
    print('%-5s%-2s%-2s%-6s%-5s%-2s%-2s%-6s%-5s%-2s%-2s%-6s' % (ta.seats[0].name[:4], ta.seats[0].displaycard1, ta.seats[0].displaycard2, " ", \
                                                            ta.seats[1].name[:4], ta.seats[1].displaycard1, ta.seats[1].displaycard2, " ", \
                                                            ta.seats[2].name[:4], ta.seats[2].displaycard1, ta.seats[2].displaycard2, " "))

    #line 3
    if settings.colors_on:
        if settings.analyse_match:
            print(settings.GREEN + "---------------------------------------" + settings.RESET)
        else:
            print(settings.RED + "---------------------------------------" + settings.RESET)
    else:
        print("---------------------------------------")

    #line 4
    print('%-2s%-2s%-11s%-2s%-13s%-2s%-6s%-2s' % (" ", ta.seats[0].button, ta.seats[0].displaybet, \
                                                        ta.seats[1].button, ta.seats[1].displaybet, \
                                                        ta.seats[2].button, ta.seats[2].displaybet, " "))
    #line 5
    print("                                       ")
    if settings.colors_on:
        print('%-8s%-1s%-1s%-1s%-11s%-8s%-1s' % (" ", settings.GREY ," ", " " , "starting point: " , disp_starting_point, settings.RESET))
    else:
        print('%-8s%-1s%-1s%-1s%-11s%-8s%-1s' % (" ", " " ," ", " " , "starting point: " , disp_starting_point, " "))

    #line 6
    print('%-12s%-6s%-20s%-1s' % (" ", "board:", ta.displayboard + display_board_offseta," "))

    #line 7
    print('%-14s%-10s%-14s%-1s' % (" ", "pot:" + str(ta.displaypot)," ", " "))

    #line 8
    print("                                       ")

    #line 9
    print('%-2s%-2s%-11s%-2s%-13s%-2s%-6s%-2s' % (" ", ta.seats[5].button, ta.seats[5].displaybet, \
                                                        ta.seats[4].button, ta.seats[4].displaybet, \
                                                        ta.seats[3].button, ta.seats[3].displaybet, " "))

    #line 10
    if settings.colors_on:
        if settings.analyse_match:
            print(settings.GREEN + "---------------------------------------" + settings.RESET)
        else:
            print(settings.RED + "---------------------------------------" + settings.RESET)
    else:
        print("---------------------------------------")


    #line 11
    print('%-2s%-1s%-5s%-7s%-2s%-1s%-5s%-7s%-2s%-1s%-5s%-7s' % (ta.seats[5].face, " ", ta.seats[5].displaystack, ta.seats[5].clock, \
                                                            ta.seats[4].face, " ", ta.seats[4].displaystack, ta.seats[4].clock, \
                                                            ta.seats[3].face, " ", ta.seats[3].displaystack, ta.seats[3].clock))
    #line 12
    print('%-5s%-2s%-2s%-6s%-5s%-2s%-2s%-6s%-5s%-2s%-2s%-6s' % (ta.seats[5].name[:4], ta.seats[5].displaycard1, ta.seats[5].displaycard2, " ", \
                                                            ta.seats[4].name[:4], ta.seats[4].displaycard1, ta.seats[4].displaycard2, " ", \
                                                            ta.seats[3].name[:4], ta.seats[3].displaycard1, ta.seats[3].displaycard2, " "))
    
    #line13
    #print(settings.report_bbv5 + "             " + settings.report_bbv4 + "             " + settings.report_bbv3)
    zeroreport = "    "
    zeroblank = "             "
    reportline = ""
    if settings.amap[5]:
        reportline += settings.report_bbv5
    else:
        reportline += zeroreport
    reportline += zeroblank
    if settings.amap[4]:
        reportline += settings.report_bbv4
    else:
        reportline += zeroreport
    reportline += zeroblank
    if settings.amap[3]:
        reportline += settings.report_bbv3
    else:
        reportline += zeroreport
    reportline += zeroblank

    print(reportline)

def print_a_dummy_table(t):
    settings.print_logo_analyser_menu()
    ta = t
    ta.displaypot = round(ta.pot)
    disp_starting_point = " "
    if ta.starting_point == 'p':
        disp_starting_point = "preflop"
    elif ta.starting_point == 'f':
        disp_starting_point = "flop"
    elif ta.starting_point == 't':
        disp_starting_point = "turn"
    elif ta.starting_point == 'r':
        disp_starting_point = "river"
    else:
        pass

    display_bigblind = str(common.roundbet(t.bigblind))
    display_smallblind = str(common.roundbet(t.bigblind/2))

    if settings.fancy:
        pass
    else:
        #print gamblers positions if there is no face
        for s in ta.seats:
            s.face = '  '



    print(" ")
    #line blinds
    print("blinds: " + display_smallblind + "/" + display_bigblind)

    #line0
    print(settings.report_bbv0 + "             " + settings.report_bbv1 + "             " + settings.report_bbv2)

    #line 1
    print('%-2s%-1s%-5s%-7s%-2s%-1s%-5s%-7s%-2s%-1s%-5s%-7s' % (ta.seats[0].face, " ", ta.seats[0].displaystack, ta.seats[0].clock, \
                                                            ta.seats[1].face, " ", ta.seats[1].displaystack, ta.seats[1].clock, \
                                                            ta.seats[2].face, " ", ta.seats[2].displaystack, ta.seats[2].clock))
    #line 2
    print('%-6s%-2s%-2s%-5s%-6s%-2s%-2s%-5s%-6s%-2s%-2s%-6s' % (ta.seats[0].name[:5], ta.seats[0].displaycard1, ta.seats[0].displaycard2, " ", \
                                                            ta.seats[1].name[:5], ta.seats[1].displaycard1, ta.seats[1].displaycard2, " ", \
                                                            ta.seats[2].name[:5], ta.seats[2].displaycard1, ta.seats[2].displaycard2, " "))

    #line 3
    if settings.colors_on:
        print(settings.YELLOW + "---------------------------------------" + settings.RESET)
    else:
        print("---------------------------------------")

    #line 4
    print('%-2s%-2s%-11s%-2s%-13s%-2s%-6s%-2s' % (" ", ta.seats[0].button, ta.seats[0].displaybet, \
                                                        ta.seats[1].button, ta.seats[1].displaybet, \
                                                        ta.seats[2].button, ta.seats[2].displaybet, " "))
    #line 5
    print("                                       ")
    if settings.colors_on:
        print('%-8s%-1s%-1s%-1s%-11s%-8s%-1s' % (" ", settings.GREY ," ", " " , "starting point: " , disp_starting_point, settings.RESET))
    else:
        print('%-8s%-1s%-1s%-1s%-11s%-8s%-1s' % (" ", " " ," ", " " , "starting point: " , disp_starting_point, " "))

    #line 6
    print('%-12s%-6s%-20s%-1s' % (" ", "board:", ta.displayboard + display_board_offseta," "))

    #line 7
    print('%-14s%-10s%-14s%-1s' % (" ", "pot:" + str(ta.displaypot)," ", " "))

    #line 8
    print("                                       ")

    #line 9
    print('%-2s%-2s%-11s%-2s%-13s%-2s%-6s%-2s' % (" ", ta.seats[5].button, ta.seats[5].displaybet, \
                                                        ta.seats[4].button, ta.seats[4].displaybet, \
                                                        ta.seats[3].button, ta.seats[3].displaybet, " "))

    #line 10
    if settings.colors_on:
        print(settings.YELLOW + "---------------------------------------" + settings.RESET)
    else:
        print("---------------------------------------")


    #line 11
    print('%-2s%-1s%-5s%-7s%-2s%-1s%-5s%-7s%-2s%-1s%-5s%-7s' % (ta.seats[5].face, " ", ta.seats[5].displaystack, ta.seats[5].clock, \
                                                            ta.seats[4].face, " ", ta.seats[4].displaystack, ta.seats[4].clock, \
                                                            ta.seats[3].face, " ", ta.seats[3].displaystack, ta.seats[3].clock))
    #line 12
    print('%-6s%-2s%-2s%-5s%-6s%-2s%-2s%-5s%-6s%-2s%-2s%-6s' % (ta.seats[5].name[:5], ta.seats[5].displaycard1, ta.seats[5].displaycard2, " ", \
                                                            ta.seats[4].name[:5], ta.seats[4].displaycard1, ta.seats[4].displaycard2, " ", \
                                                            ta.seats[3].name[:5], ta.seats[3].displaycard1, ta.seats[3].displaycard2, " "))

    #line13
    #line0
    print(settings.report_bbv5 + "             " + settings.report_bbv4 + "             " + settings.report_bbv3)

def print_a_indicator_analysis(t, it, ma):
    basic_offset = "    "
    #settings.clearscreen()
    if settings.oldview < 4:
        pass
    else:
        if settings.colors_on:
            print(settings.GREY + "ctrl+c speed/quit" + settings.RESET)
        else:
            print("ctrl+c speed/quit")

    print("iterations:" + str(it))
    if settings.colors_on:
        if settings.analyse_match:
            #we have current match
            print(settings.GREEN + "[+]" + settings.RESET + "matched:" + str(round(ma)))
        else:
            #no current match
            print(settings.RED + "[-]" + settings.RESET + "matched:" + str(round(ma)))
    else:
        if settings.analyse_match:
            #we have current match
            print("[+]matched:" + str(round(ma)))
        else:
            #no current match
            print("[-]matched:" + str(round(ma)))
    player_line = ""
    print(basic_offset)
    for s in t.seats:
        if s.clock != " ":
            player_line += "*"
        elif s.stack  <= 0.1:
            player_line += " "
        else:
            player_line += "."
    print(player_line)