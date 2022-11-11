#copyright (c) 2019
#jodathecoda@yahoo.com

import os
import sys
import time
import random
from random import randint
import shutil
import operator
import settings
import tournament
import rank
import viewrange
import rangeeditor
import fisheditor
import learning
import reset
import pokerface
import report
import leaderboards
import analyser
import hudanalyser
import pool

global cwd
cwd = os.getcwd()

settings.pokerpool = pool.Pool()
#settings.pokerpool.update_all() # learning.py

incognito = 0

if len(sys.argv) > 1:
    if sys.argv[1] == 'i':
        #incognito mode
        incognito = 1


if incognito:
    settings.view = 4
    settings.oldview = 4
    #settings.colors_on = 0

#if os.name == 'posix':
settings.fancy = 1
settings.suit_characters = 1
settings.club = '\u2663'
settings.diamond = '\u2666'
settings.heart = '\u2665'
settings.spade = '\u2660'
settings.colors_on = 1
settings.spade = settings.GREY + settings.spade + settings.RESET
settings.heart = settings.RED + settings.heart + settings.RESET
settings.diamond = settings.BLUE + settings.diamond + settings.RESET
settings.club = settings.GREEN + settings.club + settings.RESET

suit_spade = settings.spade
suit_heart = settings.heart
suit_diamond = settings.diamond
suit_club = settings.club

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

replace_dictionary = {'as': 'A' + suit_spade, 'ah': 'A' + suit_heart, 'ad': 'A' + suit_diamond, 'ac': 'A' + suit_club, \
                      'ks': 'K' + suit_spade, 'kh': 'K' + suit_heart, 'kd': 'K' + suit_diamond, 'kc': 'K' + suit_club, \
                      'qs': 'Q' + suit_spade, 'qh': 'Q' + suit_heart, 'qd': 'Q' + suit_diamond, 'qc': 'Q' + suit_club, \
                      'js': 'J' + suit_spade, 'jh': 'J' + suit_heart, 'jd': 'J' + suit_diamond, 'jc': 'J' + suit_club, \
                      'ts': 'T' + suit_spade, 'th': 'T' + suit_heart, 'td': 'T' + suit_diamond, 'tc': 'T' + suit_club, \
                      '9s': '9' + suit_spade, '9h': '9' + suit_heart, '9d': '9' + suit_diamond, '9c': '9' + suit_club, \
                      '8s': '8' + suit_spade, '8h': '8' + suit_heart, '8d': '8' + suit_diamond, '8c': '8' + suit_club, \
                      '7s': '7' + suit_spade, '7h': '7' + suit_heart, '7d': '7' + suit_diamond, '7c': '7' + suit_club, \
                      '6s': '6' + suit_spade, '6h': '6' + suit_heart, '6d': '6' + suit_diamond, '6c': '6' + suit_club, \
                      '5s': '5' + suit_spade, '5h': '5' + suit_heart, '5d': '5' + suit_diamond, '5c': '5' + suit_club, \
                      '4s': '4' + suit_spade, '4h': '4' + suit_heart, '4d': '4' + suit_diamond, '4c': '4' + suit_club, \
                      '3s': '3' + suit_spade, '3h': '3' + suit_heart, '3d': '3' + suit_diamond, '3c': '3' + suit_club, \
                      '2s': '2' + suit_spade, '2h': '2' + suit_heart, '2d': '2' + suit_diamond, '2c': '2' + suit_club
                      }

#initialize hand history buffer
settings.hand_history_buffer = settings.Hand_History_Buffer()



class Hand:
    def __init__(self, startLine, stopLine):
        self.startLine = startLine
        self.stopLine = stopLine

    def suited(self):
        if self.suit1 == self.suit2:
            return True
        else:
            return False

    def printHand(self):
        if settings.fancy and settings.colors_on:
            print("------Start Hand------")
            lines = []
            for liiness in settings.hand_history_buffer.hhb:
                lines.append(liiness)
            #lines = fp.readlines()
            i = self.startLine
            while(i >= self.startLine and i <= self.stopLine):
                #print(lines[i])
                fancy_line = replace_all(lines[i], replace_dictionary)
                print(fancy_line)
                i+=1
            print("------Stop Hand------")
            print(" ")
        else:
            print("------Start Hand------")
            lines = []
            for liiness in settings.hand_history_buffer.hhb:
                lines.append(liiness)
            #lines = fp.readlines()
            i = self.startLine
            while(i >= self.startLine and i <= self.stopLine):
                print(lines[i])
                i+=1
            print("------Stop Hand------")
            print(" ")
print(" ")

def getSelectedHands():
    settings.handreading_hands = [] # reset as this is a new search
    lines = []
    for liinness in settings.hand_history_buffer.hhb:
        lines.append(liinness)

    number_of_players = 0
    var_startLine = 0
    var_stopLine = 0
    var_card1 = "x"
    var_card2 = "x"
    var_suit1 = "x"
    var_suit2 = "x"
    var_game_type = 'z'
    record = 1
    var_name = 0
    var_pot = 0
    for i in range(0, len(lines)):
        first = lines[i].split(' ', 1)[0]
        if first == 'Table':
            var_startLine = i
            number_of_players = lines[i][15]
            if number_of_players == '2':
                #heads up
                var_game_type = 'h'
            elif number_of_players == '3':
                #spingo
                var_game_type = 's'
            elif number_of_players == '6':
                #cash
                var_game_type = 'c'
            elif number_of_players == '8':
                #tournament
                var_game_type = 't'
            else:
                print("no supported game")
                var_game_type = 'z'
                time.sleep(2)

        if (first == 'Dealt'):
            splitted_line = lines[i].split()
            if splitted_line[2] == settings.handreading_selected_bot:
                var_name = 1
                var_card1 = splitted_line[3][1]
                var_suit1 = splitted_line[3][2]
                var_card2 = splitted_line[4][0]
                var_suit2 = splitted_line[4][1]

        if first == 'Total':
            var_stopLine = i
            line_with_pot = lines[i].split(' ', 3 )
            totalpot = line_with_pot[2]
            if totalpot.isdigit():
                var_pot = float(totalpot)
            else:
                var_pot = float(totalpot[1:]) # to remove $ sign

            #check consistency
            if var_stopLine <= var_startLine:
                record = 0

            #check name
            if not var_name:
                record = 0
            #check cards
            if settings.handreading_selected_card1 == 'x' and settings.handreading_selected_card2 == 'x':
                pass
            elif settings.handreading_selected_card1 != 'x' and settings.handreading_selected_card2 != 'x':
                if settings.handreading_selected_card1 != var_card1:
                    if settings.handreading_selected_card1 != var_card2:
                        record = 0
                if settings.handreading_selected_card2 != var_card1:
                    if settings.handreading_selected_card2 != var_card2:
                        record = 0
            elif settings.handreading_selected_card1 != 'x':
                if settings.handreading_selected_card1 != var_card1:
                    if settings.handreading_selected_card1 != var_card2:
                        record = 0
            elif settings.handreading_selected_card2 != 'x':
                if settings.handreading_selected_card2 != var_card1:
                    if settings.handreading_selected_card2 != var_card2:
                        record = 0
                
            #check suit
            if settings.handreading_selected_suited == 's':
                if var_suit1 != var_suit2:
                        record = 0
            #check game type
            if settings.handreading_selected_game_type != 'z':
                if settings.handreading_selected_game_type != var_game_type:
                    record = 0

            if settings.handreading_selected_pot > 0:
                if settings.handreading_selected_pot > var_pot:
                    record = 0

            #record if all good
            if record:
                settings.handreading_hands.append(Hand(var_startLine, var_stopLine))

            var_startLine = i
            var_stopLine = 0
            var_card1 = "x"
            var_card2 = "x"
            var_suit1 = "x"
            var_suit2 = "x"
            var_game_type = 'z'
            record = 1
            var_name = 0
            var_pot = 0


def game_timings():
    settings.view = settings.oldview
    settings.bot_time_to_act = settings.selected_bot_time_to_act
    settings.bot_time_to_act_preflop = settings.selected_bot_time_to_act_preflop
    settings.bot_time_to_act_flop = settings.selected_bot_time_to_act_flop
    settings.bot_time_to_act_turn = settings.selected_bot_time_to_act_turn
    settings.bot_time_to_act_river = settings.selected_bot_time_to_act_river
    settings.time_to_wait_board = settings.selected_time_to_wait_board
    settings.learning = 0
    if settings.view == 1:
        settings.debug_ranges = 0
        settings.debug_postflop = 0
        settings.debug_ranges_stop_point = 0
        settings.debug_postflop_stop_point = 0  
    elif settings.view == 2:
        settings.debug_ranges = 1
        settings.debug_postflop = 1
        settings.debug_ranges_stop_point = 0
        settings.debug_postflop_stop_point = 0
    elif settings.view == 3:
        settings.view = 2
        settings.debug_ranges = 1
        settings.debug_postflop = 1
        settings.debug_ranges_stop_point = 1
        settings.debug_postflop_stop_point = 1
        settings.bot_time_to_act = 0
        settings.bot_time_to_act_preflop = 0
        settings.bot_time_to_act_flop = 0
        settings.bot_time_to_act_turn = 0
        settings.bot_time_to_act_river = 0
        settings.time_to_wait_board = 0
    elif settings.view == 4:
        settings.debug_ranges = 1
        settings.debug_postflop = 1
        settings.debug_ranges_stop_point = 0
        settings.debug_postflop_stop_point = 0
        settings.bot_time_to_act = 2
        settings.bot_time_to_act_preflop = 2
        settings.bot_time_to_act_flop = 2
        settings.bot_time_to_act_turn = 2
        settings.bot_time_to_act_river = 2
        settings.time_to_wait_board = 6
        settings.colors_on = 0
    elif settings.view == 5:
        settings.view = 4
        settings.bot_time_to_act = 0
        settings.bot_time_to_act_preflop = 0
        settings.bot_time_to_act_flop = 0
        settings.bot_time_to_act_turn = 0
        settings.bot_time_to_act_river = 0
        settings.time_to_wait_board = 0
        settings.debug_postflop = 1
        settings.debug_postflop_stop_point = 1
        settings.debug_ranges = 0
        settings.debug_ranges_stop_point = 0
    else:
        print("error unknown view type")
        dumb = input("]")

# Exit program
def exit_from_main():
    settings.clearscreen()
    sys.exit()

#a analyse
def analyse():
    end_condition = 1
    #clear previous
    settings.bbvals0 = 0
    settings.bbvals1 = 0
    settings.bbvals2 = 0
    settings.bbvals3 = 0
    settings.bbvals4 = 0
    settings.bbvals5 = 0
    settings.bbv0 = "   "
    settings.bbv1 = "   "
    settings.bbv2 = "   "
    settings.bbv3 = "   "
    settings.bbv4 = "   "
    settings.bbv5 = "   "
    
    try:
        settings.analyser_flag = 1
        while(end_condition):
            settings.print_logo_analyser_menu()
            #run analyser
            #set fast speed timings
            #save current timings in local vars to restore it later:
            bot_time_to_act = settings.bot_time_to_act
            bot_time_to_act_preflop = settings.bot_time_to_act_preflop
            bot_time_to_act_flop = settings.bot_time_to_act_flop
            bot_time_to_act_turn = settings.bot_time_to_act_turn
            bot_time_to_act_river = settings.bot_time_to_act_river
            time_to_wait_board = settings.time_to_wait_board
            selected_bot_time_to_act = settings.selected_bot_time_to_act
            selected_bot_time_to_act_preflop = settings.selected_bot_time_to_act_preflop
            selected_bot_time_to_act_flop = settings.selected_bot_time_to_act_flop
            selected_bot_time_to_act_turn = settings.selected_bot_time_to_act_turn
            selected_bot_time_to_act_river = settings.selected_bot_time_to_act_river
            selected_time_to_wait_board = settings.selected_time_to_wait_board
            debug_ranges_stop_point = settings.debug_ranges_stop_point
            debug_ranges = settings.debug_ranges
            debug_postflop = settings.debug_postflop
            debug_postflop_stop_point = settings.debug_postflop_stop_point
            hero = settings.hero
            dealer_bot = settings.dealer_bot
            followfish = settings.followfish

            #set timings for fast speed
            settings.bot_time_to_act = 0
            settings.bot_time_to_act_preflop = 0
            settings.bot_time_to_act_flop = 0
            settings.bot_time_to_act_turn = 0
            settings.bot_time_to_act_river = 0
            settings.time_to_wait_board = 0
            settings.selected_bot_time_to_act = 0
            settings.selected_bot_time_to_act_preflop = 0
            settings.selected_bot_time_to_act_flop = 0
            settings.selected_bot_time_to_act_turn = 0
            settings.selected_bot_time_to_act_river = 0
            settings.selected_time_to_wait_board = 0
            settings.debug_ranges_stop_point = 0
            settings.debug_ranges = 0
            settings.debug_postflop = 0
            settings.debug_postflop_stop_point = 0
            settings.analyse_fast_speed = 1
            settings.hand_history = 0 #turn off hand history
            settings.hero = 'hero'
            settings.dealer_bot = 1
            settings.followfish = ""
            settings.report_bbv0 = " "
            settings.report_bbv1 = " "
            settings.report_bbv2 = " "
            settings.report_bbv3 = " "
            settings.report_bbv4 = " "
            settings.report_bbv5 = " "
            settings.analyse_match = 0

            #run analyser
            end_condition = analyser.run()
            settings.matched = 0

            #after successful report exit and return
            #default timings
            settings.bot_time_to_act = bot_time_to_act
            settings.bot_time_to_act_preflop = bot_time_to_act_preflop
            settings.bot_time_to_act_flop = bot_time_to_act_flop
            settings.bot_time_to_act_turn = bot_time_to_act_turn
            settings.bot_time_to_act_river = bot_time_to_act_river
            settings.time_to_wait_board = time_to_wait_board
            settings.selected_bot_time_to_act = selected_bot_time_to_act
            settings.selected_bot_time_to_act_preflop = selected_bot_time_to_act_preflop
            settings.selected_bot_time_to_act_flop = selected_bot_time_to_act_flop
            settings.selected_bot_time_to_act_turn = selected_bot_time_to_act_turn
            settings.selected_bot_time_to_act_river = selected_bot_time_to_act_river
            settings.selected_time_to_wait_board = selected_time_to_wait_board
            settings.debug_ranges_stop_point = debug_ranges_stop_point
            settings.debug_ranges = debug_ranges
            settings.debug_postflop = debug_postflop
            settings.debug_postflop_stop_point = debug_postflop_stop_point
            #restart analyser
            settings.bbvals0 = 0
            settings.bbvals1 = 0
            settings.bbvals2 = 0
            settings.bbvals3 = 0
            settings.bbvals4 = 0
            settings.bbvals5 = 0
            settings.bbv0 = "   "
            settings.bbv1 = "   "
            settings.bbv2 = "   "
            settings.bbv3 = "   "
            settings.bbv4 = "   "
            settings.bbv5 = "   "
            #restore previous state
            settings.hero = hero
            settings.dealer_bot = dealer_bot
            settings.followfish = followfish
            settings.report_bbv0 = " "
            settings.report_bbv1 = " "
            settings.report_bbv2 = " "
            settings.report_bbv3 = " "
            settings.report_bbv4 = " "
            settings.report_bbv5 = " "
            settings.analyse_match = 0
            settings.analyser_flag = 0 #end analyser
    except:
        print(settings.RESET)
        #restart analyser
        settings.analyser_flag = 0 #end analyser
        settings.bbvals0 = 0
        settings.bbvals1 = 0
        settings.bbvals2 = 0
        settings.bbvals3 = 0
        settings.bbvals4 = 0
        settings.bbvals5 = 0
        settings.bbv0 = "   "
        settings.bbv1 = "   "
        settings.bbv2 = "   "
        settings.bbv3 = "   "
        settings.bbv4 = "   "
        settings.bbv5 = "   "
        settings.hero = 'hero'
        settings.dealer_bot = 1
        settings.followfish = ""
        settings.report_bbv0 = " "
        settings.report_bbv1 = " "
        settings.report_bbv2 = " "
        settings.report_bbv3 = " "
        settings.report_bbv4 = " "
        settings.report_bbv5 = " "
        settings.analyse_match = 0
        settings.analyser_flag = 0
        settings.analyse_fast_speed = 0
        #after successful report exit and return
        #default timings
        settings.bot_time_to_act = bot_time_to_act
        settings.bot_time_to_act_preflop = bot_time_to_act_preflop
        settings.bot_time_to_act_flop = bot_time_to_act_flop
        settings.bot_time_to_act_turn = bot_time_to_act_turn
        settings.bot_time_to_act_river = bot_time_to_act_river
        settings.time_to_wait_board = time_to_wait_board
        settings.selected_bot_time_to_act = selected_bot_time_to_act
        settings.selected_bot_time_to_act_preflop = selected_bot_time_to_act_preflop
        settings.selected_bot_time_to_act_flop = selected_bot_time_to_act_flop
        settings.selected_bot_time_to_act_turn = selected_bot_time_to_act_turn
        settings.selected_bot_time_to_act_river = selected_bot_time_to_act_river
        settings.selected_time_to_wait_board = selected_time_to_wait_board
        settings.debug_ranges_stop_point = debug_ranges_stop_point
        settings.debug_ranges = debug_ranges
        settings.debug_postflop = debug_postflop
        settings.debug_postflop_stop_point = debug_postflop_stop_point
        #restart analyser
        settings.bbvals0 = 0
        settings.bbvals1 = 0
        settings.bbvals2 = 0
        settings.bbvals3 = 0
        settings.bbvals4 = 0
        settings.bbvals5 = 0
        settings.bbv0 = "   "
        settings.bbv1 = "   "
        settings.bbv2 = "   "
        settings.bbv3 = "   "
        settings.bbv4 = "   "
        settings.bbv5 = "   "
        #restore previous state
        settings.hero = hero
        settings.dealer_bot = dealer_bot
        settings.followfish = followfish
        settings.report_bbv0 = " "
        settings.report_bbv1 = " "
        settings.report_bbv2 = " "
        settings.report_bbv3 = " "
        settings.report_bbv4 = " "
        settings.report_bbv5 = " "
        settings.analyse_match = 0
        settings.analyser_flag = 0 #end analyser

#ha
def help_analyse():
    settings.print_logo_menu()
    print("Setup a hand between two and six players.            ")
    print("1. Enter the big blind                               ")
    print("2. Enter stacks                                      ")
    print("3. Enter starting point:  preflop, flop, turn, river ")
    print("4. Enter pot if the starting point is postflop       ")
    print("5. Enter cards or press 'Enter' for random cards     ")
    print("Conventions: ")
    print("th=ten of hearts, 2c=two of clubs, js=jack of spades ")
    print("press Enter for random card.                         ")
    print("                                                     ")
    print("10 000 iterations of this situation will be played,  ")
    print("each iteration with different bot on each position   ")
    print("and report for each position's value in big blinds   ")
    print("will be given. To terminate the report early 'ctrl+c'")
    print("                                                     ")
    print("Each hand starts preflop, and reaching the           ")
    print("'starting point' checks bots' stack to pot ratio.    ")
    print("If the situation does not match the chosen one, the  ")
    print("result of current hand will not be taken into account")
    print("See the [-] or [+] marks for this.                   ")
    print("                                                     ")
    print("Dummy seats:                                         ")
    print("If you need dummy seats for the setup - players that ")
    print("had folded preflop, then for each of these enter     ")
    print("starting stack 1/4 than big blind or less. This way  ")
    print("their positions will be respected, but they will     ")
    print("always fold.")
    dumb = input("]")

#b boteditor
def boteditor():
    settings.print_logo_menu()
    fisheditor.fisheditor()
    settings.clearscreen()

def help_boteditor():
    settings.print_logo_menu()
    print("b Edit bot:                                          ")
    print("In this mode you can edit these properties of bot:   ")
    print("sea type, preflop, flop, turn, river aggression  and ")
    print("range type. All 54 bots in PokerSea are separated in ")
    print("4 player pools: white, yellow, red and black. Bots   ")
    print("from same sea have same ranges. These ranges can be  ")
    print("modified manually from 'r Range view/edit' or during ")
    print("endless learning mode.The aggression is between 20-40")
    print("and it defines the style of play of the bot.         ")
    print("preflop range type: polarized or merged.             ")
    print("To preserve changes, set the bot out-of-school, or   ")
    print("these properties may be changed at endless learning. ")
    print("See 'y - School in/out' section                      ")
    dumb = input("]")

#c cash game
def cash6():
    try:
        settings.wsop_followfish = 0
        settings.ante = 0
        game_timings()
        settings.learning = 0
        settings.hand_history = 1
        loops = settings.loop
        settings.left_loops = settings.loop
        while(loops > 0):
            t = tournament.Tournament(6, 'c')
            t.start()
            t.run()
            loops -= 1
            settings.left_loops -= 1
        return
    except:
        print(settings.RESET)
        return

def help_cash6():
    settings.print_logo_menu()
    print("c Cash game:                                         ")
    print("In cash game, if you have entered as player 'p Player")
    print("On/Off' you will play, if you enter as dealer 'd     ")
    print("Dealer On/Off' you will deal /selected by you/ cards,")
    print("otherwise you enter as observer. If you want to see  ")
    print("more in-depth information about the bot's play, see  ")
    print("the section 'v View type'. The cash game will break  ")
    print("when 3 players are left on the table. Each of the    ")
    print("last 3 will take its remaining stack and table will  ")
    print("break. This is mainly to separate game from heads up ")
    print("and spin-and-go.")
    dumb = input("]")

#d dealer
def dealer_on_off():
    settings.hero = 'hero'
    settings.followfish = ""
    if settings.dealer_bot:
        settings.dealer_bot = 0
    elif settings.dealer_bot == 0:
        settings.dealer_bot = 1

def help_dealer_on_off():
    settings.print_logo_menu()
    print("d Dealer On/Off                                      ")
    print("This option turns human dealer on and off.           ")
    print("Conventions: cards start with small letter           ")
    print("Ranks: a, k, q, j, t, 9, 8, 7, 6, 5, 4, 3, 2         ")
    print("Suits: s, h, d, c                                    ")
    print("Examples:")
    print("Ace of hearts: ah")
    print("Jack of clubs: jc")
    print("Seven of diamonds: 7d")
    print("Two of spades: 2s")
    print("Ten of clubs: tc")
    dumb = input("]")

#e endless
def endless():
    settings.dealer_bot = 1
    settings.wsop_followfish = 1 
    #read left loops file
    loops_left_learning_file = cwd + "/fishes/" + "/left_learning_loops.dat"
    try:
        f = open(loops_left_learning_file, "r")
        lines = f.read().splitlines()
        f.close()
        settings.games_before_learning = int(lines[0])
    except:
        print("Error in reading left loops file")
        dumb = input("]")
    if settings.games_before_learning < 1:
        settings.games_before_learning = settings.games_before_learning_value
    #endless game
    if settings.hero != 'hero':
        print("this is self learning mode, you will be logged off")
        settings.hero = 'hero'
        settings.cards_faceup = 0
        time.sleep(2)
    try:
        settings.ante = 0
        settings.view = 3
        settings.bot_time_to_act = 0
        settings.bot_time_to_act_preflop = 0
        settings.bot_time_to_act_flop = 0
        settings.bot_time_to_act_turn = 0
        settings.bot_time_to_act_river = 0
        settings.time_to_wait_board = 0
        settings.debug_postflop = 0
        settings.debug_postflop_stop_point = 0
        settings.debug_ranges = 0
        settings.debug_ranges_stop_point = 0
        settings.learning = 1
        settings.hand_history = 1
        while True:
            settings.ante = 0
            settings.left_loops = settings.wsop_hu_loops
            loops = settings.wsop_hu_loops
            while(loops > 0):
                t = tournament.Tournament(2, 'h')
                t.start()
                t.run()
                loops -= 1
                settings.left_loops -= 1
            settings.left_loops = settings.wsop_sp_loops
            loops = settings.wsop_sp_loops
            for cntr in range(0,3):
                settings.print_logo()
                print("To stop the session ctrl+c")
                print("time left: " + str(3 - cntr))
                time.sleep(1)
            while(loops > 0):
                t = tournament.Tournament(3, 's')
                t.start()
                t.run()
                loops -= 1
                settings.left_loops -= 1
            settings.left_loops = settings.wsop_ca_loops
            loops = settings.wsop_ca_loops
            for cntr in range(0,3):
                settings.print_logo()
                print("To stop the session ctrl+c")
                print("time left: " + str(3 - cntr))
                time.sleep(1)
            while(loops > 0):
                t = tournament.Tournament(6, 'c')
                t.start()
                t.run()
                loops -= 1
                settings.left_loops -= 1
            settings.left_loops = settings.wsop_mt_loops
            loops = settings.wsop_mt_loops
            for cntr in range(0,3):
                settings.print_logo()
                print("To stop the session ctrl+c")
                print("time left: " + str(3 - cntr))
                time.sleep(1)
            while(loops > 0):
                settings.ante = int(settings.smallblind/2)
                t = tournament.Tournament(54, 't')
                t.start()
                t.run()
                loops -= 1
                settings.left_loops -= 1

            if settings.learning:
                settings.games_before_learning -= 1 #decrement
            loops_left_learning_file = cwd + "/fishes/" + "/left_learning_loops.dat"
            try:
                f = open(loops_left_learning_file, "w")
                f.write(str(settings.games_before_learning) + "\n")
                f.close()
            except:
                print("Error in left loops file")
                dumb = input("]")

            for cntr in range(0,3):
                settings.print_logo()
                print("To stop the session ctrl+c")
                print("time left: " + str(3 - cntr))
                time.sleep(1)

            if (settings.learning) and (settings.games_before_learning < 1):
                if settings.oldview < 4:
                    settings.print_logo()
                    print("learning session in progress")
                    print("please wait...")
                learning.run() #trigger learning process and reset counter
                settings.games_before_learning = settings.games_before_learning_value
                #save this to file if we exit
                loops_left_learning_file = cwd + "/fishes/" + "/left_learning_loops.dat"
                try:
                    f = open(loops_left_learning_file, "w")
                    f.write(str(settings.games_before_learning_value) + "\n")
                    f.close()
                except:
                    print("Error in left loops file")
                    dumb = input("]")

            for cntr in range(0,7):
                settings.print_logo()
                print("To stop the session ctrl+c")
                print("time left: " + str( 7 - cntr))
                time.sleep(1)

    except:
        print(settings.RESET)
        game_timings()
        settings.learning = 0
        return

def help_endless():
    settings.print_logo_menu()
    print("e Endless learning                                   ")
    print("In this mode bots are playing against each other 300  ")
    print("cycles. Each cycle contains on average one heads up, ")
    print("one spin, one cash and one tournament for each bot.  ")
    print("After 300 cycles learning process starts. Weakest bots")
    print("modify their strategy and ranges. The new strategies ")
    print("are preserved when you exit PokerSea. After 300 cycles")
    print("the process starts all over.In this mode the speed is")
    print("fast speed, and the view will switch to Indicator    ")
    print("view. Bots on the table are indicated by dot '.' Bot ")
    print("who is acting is indicated as asterisk '*' Empty     ")
    print("chair is blank' 'One table looks like this:  ...*..  ")
    print("You can stop endless mode at any time 'ctrl+c', but  ")
    print("the best time to do it is between the games.         ")
    print("You can use the option 'f Follow bot' to see how     ")
    print("particular bot is playing in this mode.              ")
    dumb = input("]")

#f follower
def follower():
    settings.hero = 'hero'
    settings.dealer_bot = 1
    if settings.followfish in settings.allfishes:
        settings.followfish = ""
    else:
        settings.print_logo_menu()
        settings.printfishes(settings.allfishes)
        follower = input("enter fish to follow: ")
        if follower in settings.allfishes:
            settings.followfish = follower
            settings.hero = 'hero'
            print("fish to follow: " + settings.followfish)
            time.sleep(2)
        else:
            print("no such fish")
            time.sleep(2)

def help_follower():
    settings.print_logo_menu()
    print("f Follow bot                                         ")
    print("This option is used in endless mode if you want to   ")
    print("see how particular bot is playing. One usage is to   ")
    print("edit this bot ranges and aggression set it out of    ")
    print("school /y School in/out in main menu/ and then follow")
    print("this bot. Another usage is to just watch the best or ")
    print("worst or whichever bot you wish. In endless mode bots")
    print("are playing heads up, spin&go, cash and tournament   ")
    print("and then based on their results the worst half are   ")
    print("learning and change their startegy. This cycle goes  ")
    print("on forever until you stop it. However, to be faster, ")
    print("endless mode uses Indicator view which means 0 delay,")
    print("and bots on the table are indicated by dot '.' Bot   ")
    print("who is acting is indicated as asterisk '*' Empty     ")
    print("chair is blank ' ' One table looks like this:  ...*..")
    print("however, if you have selected bot to follow, when it ")
    print("comes its turn to act in these games, the game will  ")
    print("switch to normal speed and Classic view so you can   ")
    print("see the followed bot's play, then again the game will")
    print("switch full speed and Indicator view.")
    dumb = input("]")

#g help
def gethelp():
    settings.print_logo_menu()
    print("to get help on some topic type:")
    print("<h+letter of topic>")
    print("and press enter in main menu")
    print(" ")
    print("Examples:")
    print("a Analyzer ------> ha help Analyzer")
    print("b Edit bot ------> hb help Edit bot")
    print("c Cash game -----> hc help Cash game")
    print("d Dealer bot ----> hd help Dealer bot")
    print("... and so on")
    print("<any-key> to get back")
    dumb = input("]")

def help_gethelp():
    settings.print_logo_menu()
    print("to get help on some topic type:")
    print("<h+letter of topic>")
    print("and press enter in main menu")
    print(" ")
    print("Examples:")
    print("a Analyzer ------> ha help Analyzer")
    print("b Edit bot ------> hb help Edit bot")
    print("c Cash game -----> hc help Cash game")
    print("d Dealer bot ----> hd help Dealer bot")
    print("... and so on")
    print("<any-key> to get back")
    dumb = input("]")

#h heads up game
def hu():
    try:
        settings.wsop_followfish = 0
        settings.ante = 0
        game_timings()
        settings.learning = 0
        settings.hand_history = 1
        loops = settings.loop
        settings.left_loops = settings.loop
        while(loops > 0):
            t = tournament.Tournament(2, 'h')
            t.start()
            t.run()
            loops -= 1
            settings.left_loops -= 1
        return
    except:
        print(settings.RESET)
        return

def help_hu():
    settings.print_logo_menu()
    print("h Heads Up game:                                     ")
    print("In Heads up game there are two players with blinds   ")
    print("increasing after some time. If you have entered as   ")
    print("player - see 'p PlayerOn/Off' in main menu you will  ")
    print("play, if you enter as dealer 'd Dealer On/Off'       ")
    print("you will deal /selected by you/ cards,otherwise you  ")
    print("enter as observer. In observer mode you watch bots   ")
    print("playing. If you want to see more in-depth information")
    print("about the bot's play, see the section 'v View type'. ")
    dumb = input("]")

#i info for bot
def infobot():
        settings.print_logo()
        settings.printfishes(settings.allfishes)
        fishname = input("enter fish name: ")
        if fishname not in settings.allfishes:
            print("no such fish")
            time.sleep(2)
            return
        settings.print_logo()
        headsup_list = []
        spin_list = []
        cash_list = []
        mtt_list = []
        huvalue = 0.0
        spvalue = 0.0
        cavalue = 0.0
        mtvalue = 0.0
        sea = ""

        string_file = cwd + "/fishes/" + fishname + "/sea.dat"
        if os.path.isfile(string_file):
            filesea = cwd + "/fishes/" + fishname + "/sea.dat"
            try:
                with open(filesea, "r") as f:
                    seacode = f.read()
                f.close()
                if seacode == '0':
                    sea = "white"
                elif seacode == '1':
                    sea = "yellow"
                elif seacode == '2':
                    sea = "red"
                elif seacode == '3':
                    sea = "black"
                else:
                    print("error in assigning sea " + filesea)
                    dumb = input("]")
            except:
                print("no such file " + filesea)
                time.sleep(2)

            filerangetype = cwd + "/fishes/" + fishname + "/rt.dat" #range type 0=merged 1=polarized
            range_type_as_digit = 2
            try:
                with open(filerangetype, "r") as f:
                    range_type_as_digit = int(f.read())
                f.close()
            except:
                print("no such file " + fileaggression)
                time.sleep(2)
            if range_type_as_digit:
                raisingrangetype = "polarized"
            else:
                raisingrangetype = "merged"
            print("name: " + fishname)
            if sea == 'yellow':
            	if settings.colors_on:
            		print(settings.YELLOW + 'yellow sea' + settings.RESET)
            	else:
            		print('yellow sea')
            elif sea == 'red':
            	if settings.colors_on:
            		print(settings.RED + 'red sea' + settings.RESET)
            	else:
            		print('red sea')
            elif sea == 'black':
            	if settings.colors_on:
            		print(settings.GREY + 'black sea' + settings.RESET)
            	else:
            		print('black sea')
            else:
                print('white sea')
            print("range type: " + raisingrangetype)
#########################################################rank
        rinkrank_list = []
        for ff in settings.allfishes:
            ffrank = rank.Rank()
            ffrank.name = ff
            #now for value get last ranking_history digit then sort this
            ffrank_file = cwd + "/fishes/" + ff + "/ranking_history.dat"
            if os.path.isfile(ffrank_file):
                with open(ffrank_file, "r") as fr:
                    lines = fr.readlines()
                    ffrank.value = int(lines[-1])
                fr.close()
                rinkrank_list.append(ffrank)
            else:
                print("no such bot")
                time.sleep(2)
        sorted_ring_rang_list = sorted(rinkrank_list, key=operator.attrgetter('value'), reverse=True)
        countrrr = 0
        for franky in sorted_ring_rang_list:
            if franky.name == fishname:
                print("pokersea rank: " + str(countrrr + 1))
            countrrr += 1

##########################################################end rank
###################################################print aggression
        paggression = 0
        faggression = 0
        taggression = 0
        raggression = 0

        #always get aggression from files

        fileaggression = cwd + "/fishes/" + fishname + "/pa.dat" #preflop aggression
        try:
            with open(fileaggression, "r") as f:
                paggression = int(f.read())
            f.close()
        except:
            print("no such file " + fileaggression)


        fileaggression = cwd + "/fishes/" + fishname + "/fa.dat" #flop aggression
        try:
            with open(fileaggression, "r") as f:
                faggression = int(f.read())
            f.close()
        except:
            print("no such file " + fileaggression)


        fileaggression = cwd + "/fishes/" + fishname + "/ta.dat" #turn aggression
        try:
            with open(fileaggression, "r") as f:
                taggression = int(f.read())
            f.close()
        except:
            print("no such file " + fileaggression)

        fileaggression = cwd + "/fishes/" + fishname + "/ra.dat" #river aggression
        try:
            with open(fileaggression, "r") as f:
                raggression = int(f.read())
            f.close()
        except:
            print("no such file " + fileaggression)

        print("aggression: ")
        if settings.colors_on:
            #preflop with colors
            if paggression < 27:
                print("    preflop: " + settings.GREEN + str(paggression) + settings.RESET)
            elif paggression < 34:
                print("    preflop: " + settings.YELLOW + str(paggression) + settings.RESET)
            else:
                print("    preflop: " + settings.RED + str(paggression) + settings.RESET)

            #flop with colors
            if faggression < 27:
                print("    flop: " + settings.GREEN + str(faggression) + settings.RESET)
            elif faggression < 34:
                print("    flop: " + settings.YELLOW + str(faggression) + settings.RESET)
            else:
                print("    flop: " + settings.RED + str(faggression) + settings.RESET)

            #turn with colors
            if taggression < 27:
                print("    turn: " + settings.GREEN + str(taggression) + settings.RESET)
            elif taggression < 34:
                print("    turn: " + settings.YELLOW + str(taggression) + settings.RESET)
            else:
                print("    turn: " + settings.RED + str(taggression) + settings.RESET)

            #river with colors
            if raggression < 27:
                print("    river: " + settings.GREEN + str(raggression) + settings.RESET)
            elif raggression < 34:
                print("    river: " + settings.YELLOW + str(raggression) + settings.RESET)
            else:
                print("    river: " + settings.RED + str(raggression) + settings.RESET)
        else:
            #no colors
            print("    preflop: " + str(paggression))
            print("    flop: " + str(faggression))
            print("    turn: " + str(taggression))
            print("    river: " + str(raggression))
            
        
        #report history here
        filereport = cwd + "/fishes/" + fishname + "/ranking_history.dat"
        if os.path.isfile(filereport):
            report_list = []
            with open(filereport, "r") as fr:
                lines = fr.readlines()
                for lin in lines:
                    report_list.append(int(lin))
            fr.close()
            report.run(report_list)
            dumb = input("]")
        else:
            print("no such bot 2")
            time.sleep(2)

def help_infobot():
    settings.print_logo_menu()
    print("i Info of bot:                                       ")
    print("Here you can see information about bots. Its 'sea' - ")
    print("this is his playing pool with starting set of ranges,")
    print("which the bot may have modified during endless       ")
    print("learning mode, also here you can see his aggression  ")
    print("factor at each street and PokerSea rank. Additional  ")
    print("information you can see is bot's career so far.      ")
    dumb = input("]")

#j time delays
def timedelays():
    try:    
        settings.print_logo_menu()
        print("select which time to change:")
        print("p = preflop: " + str(settings.bot_time_to_act_preflop))
        print("f = flop: " + str(settings.bot_time_to_act_flop))
        print("t = turn: " + str(settings.bot_time_to_act_turn))
        print("r = river: " + str(settings.bot_time_to_act_river))
        print("b = board: " + str(settings.time_to_wait_board))
        selected_time = input("]")
        if selected_time == 'p':
            settings.selected_bot_time_to_act_preflop = int(input("preflop: "))
            if settings.selected_bot_time_to_act_preflop < 0:
                settings.selected_bot_time_to_act_preflop = 0
            elif settings.selected_bot_time_to_act_preflop > 10:
                settings.selected_bot_time_to_act_preflop = 10
            settings.bot_time_to_act_preflop = settings.selected_bot_time_to_act_preflop
            print("bots time to act preflop set to: " + str(settings.bot_time_to_act_preflop))
            time.sleep(settings.bot_time_to_act_preflop)
        elif selected_time == 'f':
            settings.selected_bot_time_to_act_flop = int(input("flop: "))
            if settings.selected_bot_time_to_act_flop < 0:
                settings.selected_bot_time_to_act_flop = 0
            elif settings.selected_bot_time_to_act_flop > 10:
                settings.selected_bot_time_to_act_flop = 10
            settings.bot_time_to_act_flop = settings.selected_bot_time_to_act_flop
            print("bots time to act flop set to: " + str(settings.bot_time_to_act_flop))
            time.sleep(settings.bot_time_to_act_flop)
        elif selected_time == 't':
            settings.selected_bot_time_to_act_turn = int(input("turn: "))
            if settings.selected_bot_time_to_act_turn < 0:
                settings.selected_bot_time_to_act_turn = 0
            elif settings.selected_bot_time_to_act_turn > 10:
                settings.selected_bot_time_to_act_turn = 10
            settings.bot_time_to_act_turn = settings.selected_bot_time_to_act_turn
            print("bots time to act turn set to: " + str(settings.bot_time_to_act_turn))
            time.sleep(settings.bot_time_to_act_turn)
        elif selected_time == 'r':
            settings.selected_bot_time_to_act_river = int(input("river: "))
            if settings.selected_bot_time_to_act_river < 0:
                settings.selected_bot_time_to_act_river = 0
            elif settings.selected_bot_time_to_act_river > 10:
                settings.selected_bot_time_to_act_river = 10
            settings.bot_time_to_act_river = settings.selected_bot_time_to_act_river
            print("bots time to act river set to: " + str(settings.bot_time_to_act_river))
            time.sleep(settings.bot_time_to_act_river)
        elif selected_time == 'b':
            settings.selected_time_to_wait_board = int(input("board: "))
            if settings.selected_time_to_wait_board < 0:
                settings.selected_time_to_wait_board = 0
            elif settings.selected_time_to_wait_board > 10:
                settings.selected_time_to_wait_board = 10
            settings.time_to_wait_board = settings.selected_time_to_wait_board 
            print("time to wait board: " + str(settings.time_to_wait_board))
            time.sleep(settings.time_to_wait_board)
        else:
            print("back to menu")
            time.sleep(settings.bot_time_to_act_turn)

    except:
            print("back to menu")
            time.sleep(settings.bot_time_to_act_turn)
            return

def help_timedelays():
    settings.print_logo_menu()
    print("j Time delays:                                       ")
    print("Here you can change the time it takes for bot to act ")
    print("on each street. Also you can change the 'board' time,")
    print("this is when at the river at showdown the time board ")
    print("and bot's cards will be exposed before the hand ends ")
    print("these settings are not preserved when you quit.      ")
    dumb = input("]")

#k hand history
def handhistory():
    hand_menu() #make your choice for selecting bot and hands and pots and game type

def hand_menu():
    while(1):
        settings.clearscreen()
        settings.print_logo()
        settings.handreading_selected_display = "[" + settings.handreading_selected_bot + "] "
        if settings.handreading_selected_game_type == 'h':
            settings.handreading_selected_display += "[HeadsUp] "
        if settings.handreading_selected_game_type == 's':
            settings.handreading_selected_display += "[Spin&Go] "
        if settings.handreading_selected_game_type == 'c':
            settings.handreading_selected_display += "[Cash] "
        if settings.handreading_selected_game_type == 't':
            settings.handreading_selected_display += "[Tournament] "
        if settings.handreading_selected_pot != 0.0:
            settings.handreading_selected_display += "[Min Pot: "
            settings.handreading_selected_display += str(settings.handreading_selected_pot)
            settings.handreading_selected_display += "] "
        if settings.handreading_selected_card1 != 'x' or settings.handreading_selected_card2 != 'x':
            settings.handreading_selected_display += "["
            settings.handreading_selected_display += settings.handreading_selected_card1.upper()
            settings.handreading_selected_display += " "
            settings.handreading_selected_display += settings.handreading_selected_card2.upper()
            settings.handreading_selected_display += "] "
        if settings.handreading_selected_suited == 's':
            settings.handreading_selected_display += "[Suited] "

        print(settings.handreading_selected_display)
    
        print("n name")
        print("g game type")
        print("p pot")
        print("h hand")
        print("s suited")
        print("c clear selection")
        print("r report")
        print("b back")
        print("q quit")
        choice = input("] ")
    
        if choice == 'n':
            bot_name_change()
        elif choice == 'g':
            game_type_select()
        elif choice == 'p':
            pot_select()
        elif choice == 'h':
            hand_select()
        elif choice == 's':
            suited_selected()
        elif choice == 'c':
            clear_selection()
        elif choice == 'r':
            reportSelectedHands()
        elif choice == 'b':
            return
        elif choice == 'q':
            quitt()

def bot_name_change():
    settings.print_logo()
    settings.printfishes(settings.allfishes)
    settings.handreading_selected_bot = input("enter name for hand reading: ")

def game_type_select():
    settings.print_logo()
    print("c cash")
    print("s spin&go")
    print("c cash game")
    print("t tournament")
    choice = input("] ")
    ch = choice.lower()
    if ch == 'q':
        exitt()
    elif ch == 'h':
        settings.handreading_selected_game_type = 'h' #headsup game
    elif ch == 's':
        settings.handreading_selected_game_type = 's' #spin game
    elif ch == 'c':
        settings.handreading_selected_game_type = 'c' #cash game
    elif ch == 't':
        settings.handreading_selected_game_type = 't' #tournament
    else:
        print("unknown game selected")
        time.sleep(2)

def hand_select():
    settings.print_logo()
    options = ['2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k' ,'a', 'x']
    settings.handreading_selected_card1 = input("select rank /2-a/ or 'x' for card1: ")
    settings.handreading_selected_card2 = input("select rank /2-a/ or 'x' for card2: ")
    if settings.handreading_selected_card1 not in options:
        settings.handreading_selected_card1 = 'x'
    if settings.handreading_selected_card2 not in options:
        settings.handreading_selected_card2 = 'x'

def pot_select():
    try:
        settings.handreading_selected_pot = float(input("enter minimum pot: "))
        if settings.handreading_selected_pot > 50000.0:
            settings.handreading_selected_pot = 50000.0         
    except:
        settings.handreading_selected_pot = 0.0
    if settings.handreading_selected_pot < 0:
        settings.handreading_selected_pot = 0.0

def reportSelectedHands():
    getSelectedHands()
    print(len(settings.handreading_hands))
    for h in settings.handreading_hands:
        h.printHand()
    print("]Total hands: " + str(len(settings.handreading_hands)))
    dumb = input("]Done")

def suited_selected():
    if settings.handreading_selected_suited == 'z':
        settings.handreading_selected_suited = 's'
    else:
        settings.handreading_selected_suited = 'z'

def clear_selection():
    settings.handreading_selected_display = " "
    settings.handreading_hands = []
    settings.handreading_selected_hand = 'z'
    settings.handreading_selected_pot = 0.0
    settings.handreading_selected_suited = 'z'
    settings.handreading_selected_game_type = 'z'
    settings.handreading_selected_card1 = 'x'
    settings.handreading_selected_card2 = 'x'
    settings.handreading_count_hands = 0
    settings.handreading_selected_bot = "no name"
    settings.handreading_selected_botfold = "z"

def help_handhistory():
    settings.print_logo_menu()
    print("k Hand history:                                      ")
    print("For each bot around last ~200 to ~300 hands are saved")
    print("Select 'n name' to select which bot hands history to ")
    print("view. Select as name 'you' for your own hand history.")
    print("Additional filters:                                  ")
    print("g - game type: review only hands for this game type  ")
    print("p - pot: enter minimal pot for report.               ")
    print("s - suited: view only suited hands                   ")
    print("                                                     ")
    print("h - hand: select specific hand.                      ")
    print("Example ace-x offsuited report:                      ")
    print("card1: 'a' - you have selected card1 to be ace       ")
    print("card2: 'x' - you have selected card2 to be random x  ")
    print("Valid ranks: 'a', 'k', 'q', 'j', 't', '9-2' or 'x'   ")
    print("                                                     ")
    print("r - report: view selected bot's hands                ")
    print("c - clear selection: clear all filters               ")
    dumb = input("]")

#l leaderboard
def leaderboard():
    settings.print_logo()
    leaderboards.run()

def help_leaderboard():
    settings.print_logo_menu()
    print("l Leaderboard:                                       ")
    print("Displays current leaderboard stats of all bots for   ")
    print("different game types: heads up, spin&go, cash and mtt")
    print("Current means last iteration of endless learning mode")
    dumb = input("]")

#n nash heads up game
def nash():
    try:
        settings.nash_0 = 0
        settings.nash_1 = 0
        settings.nash_you = 0
        settings.nash_villain = 0
        nash_fish0 = ""
        nash_fish1 = ""
        settings.nash_push_fold = 1
        settings.wsop_followfish = 0
        settings.ante = 0
        game_timings()
        settings.learning = 0
        settings.hand_history = 1
        loops = settings.loop
        settings.left_loops = settings.loop
        while(1):
            t = tournament.Tournament(2, 'h')
            t.start()
            t.run()
            #loops -= 1
            #settings.left_loops -= 1
        settings.nash_push_fold = 0
        return
    except:
        settings.nash_push_fold = 0
        print(settings.RESET)
        return

def help_nash():
    settings.print_logo_menu()
    print("n Nash Heads Up push/fold game:                                     ")
    print("push/fold game with 10 big blinds, bots use Nash charts")
    dumb = input("]")

#r Range view/edit
def modify_range():
    settings.print_logo_menu()
    rangeeditor.editrange()
    settings.clearscreen()

def help_modify_range():
    settings.print_logo_menu()
    print("Select a bot and range you want to view/edit.        ")
    print("Type hand to add or remove from range.               ")
    print("Conventions:                                         ")
    print("aks - ace-king suited                                ")
    print("ako - ace king offsuit                               ")
    print("44 - pocket fours                                    ")
    dumb = input("]")

#o Colors and layout
def colors_layout():
        try:
            print('\u2663' + '\u2666' + '\u2665' + '\u2660')
            dumb = input("do you see correct characters? y/n: ")
            if dumb == 'y' or dumb == 'Y' or dumb == 'yes' or dumb == 'Yes':
                settings.suit_characters = 1
                settings.club = '\u2663'
                settings.diamond = '\u2666'
                settings.heart = '\u2665'
                settings.spade = '\u2660'
            else:
                settings.suit_characters = 0
                settings.club = 'c'
                settings.diamond = 'd'
                settings.heart = 'h'
                settings.spade = 's'
        except:
            print("suits not available")
            time.sleep(2)
        try:
            print(settings.GREY + settings.spade + settings.RED + settings.heart + settings.BLUE + settings.diamond + settings.GREEN + settings.club + settings.RESET)
            dumb = input("do you see colors? y/n: ")
            if dumb == 'y' or dumb == 'Y' or dumb == 'yes' or dumb == 'Yes':
                settings.colors_on = 1
                settings.spade = settings.GREY + settings.spade + settings.RESET
                settings.heart = settings.RED + settings.heart + settings.RESET
                settings.diamond = settings.BLUE + settings.diamond + settings.RESET
                settings.club = settings.GREEN + settings.club + settings.RESET
            else:
                settings.colors_on = 0
        except:
            print("colors not available")
            time.sleep(2)
        try:
            settings.list_faces = []
            print(pokerface.face1 + " " + pokerface.face2 + " " + pokerface.face3)
            dumb = input("do you see correct symbols? y/n: ")
            if dumb == 'y' or dumb == 'Y' or dumb == 'yes' or dumb == 'Yes':               
                settings.fancy = 1
            else:
                settings.fancy = 0
        except:
            print("characters not available")
            time.sleep(2)

def help_colors_layout():
    settings.print_logo_menu()
    print("o Colors and Layout                                  ")
    print("Pokersea is a command line tool,there are no graphics")
    print("Windows OS console does not support colors or special")
    print("characters - like bot's faces and cards suits. Apart ")
    print("from 'no color, no face', PokerSea will work the same")

    dumb = input("]")

#p player
def player_on_off():
    settings.followfish = ""
    settings.dealer_bot = 1
    if settings.hero == 'hero':
        settings.hero = 'you'
        settings.followfish = "" #successful login removes fish to follow
        settings.dealer_bot = 1 #successful login removes manual dealer
        settings.view = 1
        settings.oldview = 1
        settings.bot_time_to_act = settings.selected_bot_time_to_act
        settings.bot_time_to_act_preflop = settings.selected_bot_time_to_act_preflop
        settings.bot_time_to_act_flop = settings.selected_bot_time_to_act_flop
        settings.bot_time_to_act_turn = settings.selected_bot_time_to_act_turn
        settings.bot_time_to_act_river = settings.selected_bot_time_to_act_river
        settings.time_to_wait_board = settings.selected_time_to_wait_board
        settings.debug_ranges = 0
        settings.debug_postflop = 0
        settings.debug_ranges_stop_point = 0
        settings.debug_postflop_stop_point = 0
        settings.cards_faceup = 0
    else:
        settings.hero = 'hero'
        settings.cards_faceup = 1
        settings.view = 1
        settings.oldview = 1

def help_player_on_off():
    settings.print_logo_menu()
    print("p Player On/Off                                      ")
    print("Switch between player and observer mode.             ")
    dumb = input("]")

#q quit
def quitt():
    settings.hand_history_buffer.write_hh_to_the_file()
    if settings.view < 3:
        settings.print_bye_cards()
        if settings.colors_on:
            print(settings.GREY + "Casino broke the game" + settings.RESET)
        else:
            print("Casino broke the game")
        time.sleep(2)
    sys.exit()

def help_quitt():
    quitt()

#s Spin & Go
def spingo():
    try:
        settings.wsop_followfish = 0
        settings.ante = 0
        game_timings()
        settings.learning = 0
        settings.hand_history = 1
        loops = settings.loop
        settings.left_loops = settings.loop
        while(loops > 0):
            t = tournament.Tournament(3, 's')
            t.start()
            t.run()
            loops -= 1
            settings.left_loops -= 1
        return
    except:
        print(settings.RESET)
        return

def help_spingo():
    settings.print_logo_menu()
    print("s Spin & Go game:                                    ")
    print("In Spin&Go game there are three players with blinds  ")
    print("increasing after some time. If you have entered as   ")
    print("player - see 'p PlayerOn/Off' in main menu you will  ")
    print("play, if you enter as dealer 'd Dealer On/Off'       ")
    print("you will deal /selected by you/ cards, otherwise you ")
    print("enter as observer. In observer mode you watch bots   ")
    print("playing. If you want to see more in-depth information")
    print("about the bot's play, see the section 'v View type'. ")
    dumb = input("]")

#t Tournament
def mtt():
    try:
        settings.wsop_followfish = 0
        settings.ante = int(settings.smallblind/2)
        game_timings()
        settings.learning = 0
        settings.hand_history = 1
        loops = settings.loop
        settings.left_loops = settings.loop
        settings.ante = int(settings.smallblind/2)
        while(loops > 0):
            t = tournament.Tournament(54, 't')
            t.start()
            t.run()
            loops -= 1
            settings.left_loops -= 1
        return
    except:
        print(settings.RESET)
        return

def help_mtt():
    settings.print_logo_menu()
    print("t Tournament game:                                   ")
    print("In Tournament game all of the 54 bots are playing.   ")
    print("9 tables with 6 players. Ante and blinds increasing  ")
    print("as tournament levels go by. If you have entered as   ")
    print("player - see 'p PlayerOn/Off' in main menu you will  ")
    print("play, if you enter as dealer 'd Dealer On/Off'       ")
    print("you will deal /selected by you/ cards, otherwise you ")
    print("enter as observer. In observer mode you watch bots   ")
    print("playing. If you want to see more in-depth information")
    print("about the bot's play, see the section 'v View type'. ")
    dumb = input("]")

#u
def help_hudanalyzer():
    settings.print_logo_menu()
    print("Simplified holdem heads up game - no 4 bets preflop!")
    print("DB /DealerButton/ can open with size from 2 up to 3.5")
    print("Blinds are 10/20, Stacks are 1000 /50BB effective stacks/")
    print("DB starts with fold or open bet size predefined by you:")
    print("0xBigblind /always fold, even if the hand is in open range/")
    print("this is for reference reason: If DB adopts strategy worst")
    print("than 'always fold', it is useless. Other open options ")
    print("when the hand dealt to him is in his open range are:")
    print("2xBigblinds /minraise/, 2.5x, 3x or 3.5x")
    print("BB can raise, or call. If BB raises, DB can call or fold.")
    print("For DB and BB are used redfish and blackfish, which have")
    print("same postflop game. This way, the analysis will be ")
    print("focused on: Position, preflop open size and 4 ranges: ")
    print("for DB :  (1) open  (2) call after 3bet from BB")
    print("for BB:   (3) call  (4) 3Bet preflop")
    print("The ranges can be edited from main menu:")
    print("r - Range view/edit, choose redfish or blackfish.")
    print("redfish (1) and (2) ranges, or blackfish (3) and (4).")
    print("Editing ranges is only for this HudAnalyzer, it")
    print("will not affect their ranges for other games, as these")
    print("two are reference fishes - do not change their strategy.")
    print("redfish has the positional advantage as he has the button.")
    print("The result after 10 000 iterations will be displayed in")
    print("bigblinds/hand won or loss.")
    dumb = input("]")

def hudanalyzer():
    settings.hudanalyser = 1
    end_condition = 1
    settings.redfish_seated = 0
    #clear previous
    settings.bbvals0 = 0
    settings.bbvals1 = 0
    settings.bbvals2 = 0
    settings.bbvals3 = 0
    settings.bbvals4 = 0
    settings.bbvals5 = 0
    settings.bbv0 = "   "
    settings.bbv1 = "   "
    settings.bbv2 = "   "
    settings.bbv3 = "   "
    settings.bbv4 = "   "
    settings.bbv5 = "   "
    
    try:
        settings.analyser_flag = 1
        while(end_condition):
            settings.print_logo_analyser_menu()
            #run analyser
            #set fast speed timings
            #save current timings in local vars to restore it later:
            bot_time_to_act = settings.bot_time_to_act
            bot_time_to_act_preflop = settings.bot_time_to_act_preflop
            bot_time_to_act_flop = settings.bot_time_to_act_flop
            bot_time_to_act_turn = settings.bot_time_to_act_turn
            bot_time_to_act_river = settings.bot_time_to_act_river
            time_to_wait_board = settings.time_to_wait_board
            selected_bot_time_to_act = settings.selected_bot_time_to_act
            selected_bot_time_to_act_preflop = settings.selected_bot_time_to_act_preflop
            selected_bot_time_to_act_flop = settings.selected_bot_time_to_act_flop
            selected_bot_time_to_act_turn = settings.selected_bot_time_to_act_turn
            selected_bot_time_to_act_river = settings.selected_bot_time_to_act_river
            selected_time_to_wait_board = settings.selected_time_to_wait_board
            debug_ranges_stop_point = settings.debug_ranges_stop_point
            debug_ranges = settings.debug_ranges
            debug_postflop = settings.debug_postflop
            debug_postflop_stop_point = settings.debug_postflop_stop_point
            hero = settings.hero
            dealer_bot = settings.dealer_bot
            followfish = settings.followfish

            #set timings for fast speed
            settings.bot_time_to_act = 0
            settings.bot_time_to_act_preflop = 0
            settings.bot_time_to_act_flop = 0
            settings.bot_time_to_act_turn = 0
            settings.bot_time_to_act_river = 0
            settings.time_to_wait_board = 0
            settings.selected_bot_time_to_act = 0
            settings.selected_bot_time_to_act_preflop = 0
            settings.selected_bot_time_to_act_flop = 0
            settings.selected_bot_time_to_act_turn = 0
            settings.selected_bot_time_to_act_river = 0
            settings.selected_time_to_wait_board = 0
            settings.debug_ranges_stop_point = 0
            settings.debug_ranges = 0
            settings.debug_postflop = 0
            settings.debug_postflop_stop_point = 0
            settings.analyse_fast_speed = 1
            settings.hand_history = 0 #turn off hand history
            settings.hero = 'hero'
            settings.dealer_bot = 1
            settings.followfish = ""
            settings.report_bbv0 = " "
            settings.report_bbv1 = " "
            settings.report_bbv2 = " "
            settings.report_bbv3 = " "
            settings.report_bbv4 = " "
            settings.report_bbv5 = " "
            settings.analyse_match = 0

            #run analyser
            end_condition = hudanalyser.run()
            settings.matched = 0

            #after successful report exit and return
            #default timings
            settings.bot_time_to_act = bot_time_to_act
            settings.bot_time_to_act_preflop = bot_time_to_act_preflop
            settings.bot_time_to_act_flop = bot_time_to_act_flop
            settings.bot_time_to_act_turn = bot_time_to_act_turn
            settings.bot_time_to_act_river = bot_time_to_act_river
            settings.time_to_wait_board = time_to_wait_board
            settings.selected_bot_time_to_act = selected_bot_time_to_act
            settings.selected_bot_time_to_act_preflop = selected_bot_time_to_act_preflop
            settings.selected_bot_time_to_act_flop = selected_bot_time_to_act_flop
            settings.selected_bot_time_to_act_turn = selected_bot_time_to_act_turn
            settings.selected_bot_time_to_act_river = selected_bot_time_to_act_river
            settings.selected_time_to_wait_board = selected_time_to_wait_board
            settings.debug_ranges_stop_point = debug_ranges_stop_point
            settings.debug_ranges = debug_ranges
            settings.debug_postflop = debug_postflop
            settings.debug_postflop_stop_point = debug_postflop_stop_point
            #restart analyser
            settings.bbvals0 = 0
            settings.bbvals1 = 0
            settings.bbvals2 = 0
            settings.bbvals3 = 0
            settings.bbvals4 = 0
            settings.bbvals5 = 0
            settings.bbv0 = "   "
            settings.bbv1 = "   "
            settings.bbv2 = "   "
            settings.bbv3 = "   "
            settings.bbv4 = "   "
            settings.bbv5 = "   "
            #restore previous state
            settings.hero = hero
            settings.dealer_bot = dealer_bot
            settings.followfish = followfish
            settings.report_bbv0 = " "
            settings.report_bbv1 = " "
            settings.report_bbv2 = " "
            settings.report_bbv3 = " "
            settings.report_bbv4 = " "
            settings.report_bbv5 = " "
            settings.analyse_match = 0
            settings.analyser_flag = 0 #end analyser
            settings.hudanalyser = 0
    except:
        print(settings.RESET)
        #restart analyser
        settings.analyser_flag = 0 #end analyser
        settings.bbvals0 = 0
        settings.bbvals1 = 0
        settings.bbvals2 = 0
        settings.bbvals3 = 0
        settings.bbvals4 = 0
        settings.bbvals5 = 0
        settings.bbv0 = "   "
        settings.bbv1 = "   "
        settings.bbv2 = "   "
        settings.bbv3 = "   "
        settings.bbv4 = "   "
        settings.bbv5 = "   "
        settings.hero = 'hero'
        settings.dealer_bot = 1
        settings.followfish = ""
        settings.report_bbv0 = " "
        settings.report_bbv1 = " "
        settings.report_bbv2 = " "
        settings.report_bbv3 = " "
        settings.report_bbv4 = " "
        settings.report_bbv5 = " "
        settings.analyse_match = 0
        settings.analyser_flag = 0
        settings.analyse_fast_speed = 0
        #after successful report exit and return
        #default timings
        settings.bot_time_to_act = bot_time_to_act
        settings.bot_time_to_act_preflop = bot_time_to_act_preflop
        settings.bot_time_to_act_flop = bot_time_to_act_flop
        settings.bot_time_to_act_turn = bot_time_to_act_turn
        settings.bot_time_to_act_river = bot_time_to_act_river
        settings.time_to_wait_board = time_to_wait_board
        settings.selected_bot_time_to_act = selected_bot_time_to_act
        settings.selected_bot_time_to_act_preflop = selected_bot_time_to_act_preflop
        settings.selected_bot_time_to_act_flop = selected_bot_time_to_act_flop
        settings.selected_bot_time_to_act_turn = selected_bot_time_to_act_turn
        settings.selected_bot_time_to_act_river = selected_bot_time_to_act_river
        settings.selected_time_to_wait_board = selected_time_to_wait_board
        settings.debug_ranges_stop_point = debug_ranges_stop_point
        settings.debug_ranges = debug_ranges
        settings.debug_postflop = debug_postflop
        settings.debug_postflop_stop_point = debug_postflop_stop_point
        #restart analyser
        settings.bbvals0 = 0
        settings.bbvals1 = 0
        settings.bbvals2 = 0
        settings.bbvals3 = 0
        settings.bbvals4 = 0
        settings.bbvals5 = 0
        settings.bbv0 = "   "
        settings.bbv1 = "   "
        settings.bbv2 = "   "
        settings.bbv3 = "   "
        settings.bbv4 = "   "
        settings.bbv5 = "   "
        #restore previous state
        settings.hero = hero
        settings.dealer_bot = dealer_bot
        settings.followfish = followfish
        settings.report_bbv0 = " "
        settings.report_bbv1 = " "
        settings.report_bbv2 = " "
        settings.report_bbv3 = " "
        settings.report_bbv4 = " "
        settings.report_bbv5 = " "
        settings.analyse_match = 0
        settings.analyser_flag = 0 #end analyser
        settings.hudanalyser = 0

    
    
#v View type
def view_select():
    settings.print_logo()
    print("select view:")
    print("1-classic, 2-insight-info, 3-step-by-step")
    #print("4-incognito, 5-incognito-by-step:")
    valid_view_choices = ['1', '2', '3']
    trynewview = input("]")
    if trynewview in valid_view_choices:
        settings.oldview = int(trynewview)
    else:
        print("not valid")
        time.sleep(2)

    if settings.oldview < 1 or settings.oldview > 5:
        settings.oldview = 1
        game_timings()
            
    if settings.oldview == 2 or settings.oldview == 3 or settings.oldview == 5:
        if settings.hero != 'hero':
            print("Can not use special views Player mode is On")
            time.sleep(2)
        else:
            game_timings()

    elif settings.oldview > 0 and settings.oldview < 6:
        game_timings()

def help_view_select():
    settings.print_logo_menu()
    print("v View type:                                         ")
    print("In observer mode, select between 3 available views.  ")
    print("First is classic, the second one gives you more      ")
    print("indepth information during game play like ranges and ")
    print("decisions bots take. The third view is like the      ")
    print("second but with stop point at each decision. To      ")
    print("change views you must be in observer mode see        ")
    print("/p Player On/Off/ in menu                            ")
    dumb = input("]")

#y School in out
def school_in_out():
    print("type name of fish to move it to the other group, q quit:")
    inschool = []
    outofschool=[]
    for riba in settings.allfishes:
        inschool.append(riba)
    if not os.path.isfile('fishes/out_of_school.dat'):
        open('fishes/out_of_school.dat', 'a').close()
    f = open('fishes/out_of_school.dat',"r")
    lines = f.read().splitlines()
    f.close()
    for l in lines:
        outofschool.append(l)
    for o in outofschool:
        if o in inschool:
            inschool.remove(o)
    if settings.view < 4:
        settings.print_logo()
    print("In school: ")
    settings.printfishes(inschool)
    print("Out of school: ")
    settings.printfishes(outofschool)
    candidate = ""
    while(candidate != 'q'):
        candidate = input("]")
        if candidate in inschool:
            inschool.remove(candidate)
            outofschool.append(candidate)
            if settings.view < 4:
                settings.print_logo()
            print("In school: ")
            settings.printfishes(inschool)
            print("Out of school: ")
            settings.printfishes(outofschool)
        elif candidate in outofschool:
            if candidate in settings.referencefishes:
                print(candidate + " is a reference fish can not be modified")
                candidate = 'q'
                time.sleep(2)
            else:
                outofschool.remove(candidate)
                inschool.append(candidate)
                if settings.view < 4:
                    settings.print_logo()
                print("In school: ")
                settings.printfishes(inschool)
                print("Out of school: ")
                settings.printfishes(outofschool)
        elif candidate == 'q':
            f = open('fishes/out_of_school.dat',"w")
            for cc in outofschool:
                f.write(cc + "\n")
            f.close()
        else:
            f = open('fishes/out_of_school.dat',"w")
            for cc in outofschool:
                f.write(cc + "\n")
            f.close()
            print("no such fish")
            time.sleep(2)
            candidate = 'q'

def help_school_in_out():
    settings.print_logo_menu()
    print("y School in/out:                            ")
    print("Select bots to put in and out of school.    ")
    print("In endless learning mode only bots that     ")
    print("are in schoolwill change their strategies   ")
    print("and ranges. There are 4 reference bots      ")
    print("that are always out of school:")
    print("milkfish, yellowfish, redfish and blackfish.")
    dumb = input("]")

#main lobby
while(1):
    try:
        settings.print_logo_menu()
        if settings.view < 4:
            print('a Analyzer')
            print('b Bot editor')
            print('c Cash game')
            print('d Dealer On/Off')
            print('e Endless learning')
            print('f Follow bot')
            print('g Get Help')
            print('h Heads Up game')
            print('i Info of bot')
            print('j Time delays')
            print('k Hand history')
            print('l Leaderboard')
            print('n Nash push/fold')
            print('o Colors and Layout')
            print('p Player On/Off')
            print('q Quit')
            print('r Range view/edit')
            print('s Spin & Go game')
            print('t Tournament game')
            print('u Heads Up Analyzer')
            print('v View type')
            #print("x Hud on/off")
            print('y School in/out')
            #print('z Reset bots')

        else:
            print("main")
        choice = input("]")
        if choice == 'a':
            analyse()
        elif choice == 'ha':
            help_analyse()
        elif choice == 'b':
            boteditor()
        elif choice == 'hb':
            help_boteditor()
        elif choice == 'c':
            cash6()
        elif choice == 'hc':
            help_cash6()
        elif choice == 'd':
            dealer_on_off()
        elif choice == 'hd':
            help_dealer_on_off()
        elif choice == 'q':
            quitt()
        elif choice == 'hq':
            help_quitt()
        elif choice == 'e':
            endless()
        elif choice == 'he':
            help_endless()
        elif choice == 'f':
            follower()
        elif choice == 'hf':
            help_follower()
        elif choice == 'g':
            gethelp()
        elif choice == 'hg':
            help_gethelp()
        elif choice == 'h':
            hu()
        elif choice == 'hh':
            help_hu()
        elif choice == 'i':
            infobot()
        elif choice == 'hi':
            help_infobot()
        elif choice == 'j':
            timedelays()
        elif choice == 'hj':
            help_timedelays()
        elif choice == 'k':
            handhistory()
        elif choice == 'hk':
            help_handhistory()
        elif choice == 'l':
            leaderboard()
        elif choice == 'hl':
            help_leaderboard()
        elif choice == 'n':
            nash()
        elif choice == 'hn':
            help_nash()
        elif choice == 'o':
            colors_layout()
        elif choice == 'ho':
            help_colors_layout()
        elif choice == 'p':
            player_on_off()
        elif choice == 'hp':
            help_player_on_off()
        elif choice == 'q':
            quitt()
        elif choice == 'hq':
            help_quitt()
        elif choice == 'r':
            modify_range()
        elif choice == 'hr':
            help_modify_range()
        elif choice == 's':
            spingo()
        elif choice == 'hs':
            help_spingo()
        elif choice == 't':
            mtt()
        elif choice == 'ht':
            help_mtt()
        elif choice == 'u':
            hudanalyzer()
        elif choice == 'hu':
            help_hudanalyzer()
        elif choice == 'v':
            view_select()
        elif choice == 'hv':
            help_view_select()
        elif choice == 'y':
            school_in_out()
        elif choice == 'hy':
            help_school_in_out()
        else:
            pass

    except:
        print(settings.RESET)
        exit_from_main()
