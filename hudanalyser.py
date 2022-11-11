#copyright (c) 2019 all rights reserved
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
import pokerface
import seat
import info
import common
import weather
import selectrange
import betsize
import preflop
import formulas
import bots
import display

empty_list = []

display_board_offset0  = "          "
display_board_offset39 = "          "
display_board_offset52 = "          "
display_board_offset65 = "          "
display_board_offseta  = "          "

handlog = ""

dek = ['As', 'Ks', 'Qs', 'Js', 'Ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', \
            'Ah', 'Kh', 'Qh', 'Jh', 'Th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', \
            'Ad', 'Kd', 'Qd', 'Jd', 'Td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', \
            'Ac', 'Kc', 'Qc', 'Jc', 'Tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c' ]

global cwd
cwd = os.getcwd()

BLANK = " "
BLANKCELL = '   '

def get_display_stack(stack):
    displaystack = "  "
    if stack == 0:
        displaystack = "  "
    else:
        displaystack = str(common.roundbet(stack))
    if stack > 99999 or len(str(stack)) > 5:
        dumbstack = common.roundbet(stack/1000)
        displaystack = str(dumbstack) + "k"
    if stack == settings.dumblind*1.5:
        displaystack = "  "
    return displaystack

def get_face():
    face = " "
    if not settings.list_faces:
        p = pokerface.Pokerface()
        settings.list_faces = p.faces
    face = settings.list_faces.pop()
    return face

class AnalysedSeat():
    def __init__(self, card1, card2, button, stack):
        self.card1 = card1 #xx=random_hand
        self.card2 = card2
        self.button = button#" "=no button
        self.value = 0 #value in big blinds for this position
        self.stack = stack
        self.name = "randomfish" #this will be randomized from list of all fishes each iteration

class AnalysedTable():
    def __init__(self, seat0, seat1, seat2, seat3, seat4, seat5, pot, board, bigblind, starting_point):
        self.seats = [seat0, seat1, seat2, seat3, seat4, seat5]
        self.bigblind = bigblind
        self.pot = pot
        self.board = board
        self.starting_point = starting_point


class Analyser():
    def __init__(self,  an_table_object):
        self.tabl_obj = an_table_object
        self.iterations = 0 #number of iterations
        settings.analysed_iterations = self.iterations
        settings.matched = 0.001 #iterations that matched required situation, remove  dividing by zero
        self.bb = an_table_object.bigblind
        self.smallblind = round(int(an_table_object.bigblind/2))
        #to match the analysed situation if it is on flop, turn, river,
        #we have to compare stack that are in the situation <10 BBs or >10 BBs
        #to the predefined situation to see if table matches.
        self.stp0 = an_table_object.seats[0].stack/(an_table_object.pot + 0.1) #defence from zero pot
        self.stp1 = an_table_object.seats[1].stack/(an_table_object.pot + 0.1)
        self.stp2 = an_table_object.seats[2].stack/(an_table_object.pot + 0.1)
        self.stp3 = an_table_object.seats[3].stack/(an_table_object.pot + 0.1)
        self.stp4 = an_table_object.seats[4].stack/(an_table_object.pot + 0.1)
        self.stp5 = an_table_object.seats[5].stack/(an_table_object.pot + 0.1)
        self.game_type = 'c'

    def match_situation(self, table):
        t = table
        pot = 0
        for s in t.seats:
            pot += s.bet
        match_0 = 0
        match_1 = 0
        match_2 = 0
        match_3 = 0
        match_4 = 0
        match_5 = 0
        #check stp ratio on 6seats
        #and give some buffer to the situation
        
        cur_stp0 = 0
        cur_stp1 = 0
        cur_stp2 = 0
        cur_stp3 = 0
        cur_stp4 = 0
        cur_stp5 = 0

        #seat 0 current stp
        if t.seats[0].stack > 0:
            cur_stp0 = t.seats[0].stack/(pot + 0.1)

        #seat 1 current stp
        if t.seats[1].stack > 0:
            cur_stp1 = t.seats[1].stack/(pot + 0.1)

        #seat 2 current stp
        if t.seats[2].stack > 0:
            cur_stp2 = t.seats[2].stack/(pot + 0.1)

        #seat 3 current stp
        if t.seats[3].stack > 0:
            cur_stp3 = t.seats[3].stack/(pot + 0.1)

        #seat 4 current stp
        if t.seats[4].stack > 0:
            cur_stp4 = t.seats[4].stack/(pot + 0.1)

        #seat 5 current stp
        if t.seats[5].stack > 0:
            cur_stp5 = t.seats[5].stack/(pot + 0.1)

        '''
        print("---inside match_situation ------")
        print("stack0: " + str(t.seats[0].stack))
        print("cur_stp0: " + str(cur_stp0))
        print("reference self.stp0: " + str(self.stp0))
        if self.stp0 < 0.3:
            print("[+]")
        else:
            print("if (cur_stp0 - cur_stp0/2 > self.stp0) or (cur_stp0 + cur_stp0/2 < self.stp0): [-]")
            if (cur_stp0 - cur_stp0/2 > self.stp0) or (cur_stp0 + cur_stp0/2 < self.stp0):
                print("[-]")
            else:
                print("[+]")
        print("stack1: " + str(t.seats[1].stack))
        print("cur_stp1: " + str(cur_stp1))
        print("reference self.stp1: " + str(self.stp1))
        if self.stp1 < 0.3:
            print("[+]")
        else:
            print("if (cur_stp1 - cur_stp1/2 > self.stp1) or (cur_stp1 + cur_stp1/2 < self.stp1): [-]")
            if (cur_stp1 - cur_stp1/2 > self.stp1) or (cur_stp1 + cur_stp1/2 < self.stp1):
                print("[-]")
            else:
                print("[+]")
        print("stack2: " + str(t.seats[2].stack))
        print("cur_stp2: " + str(cur_stp2))
        print("reference self.stp2: " + str(self.stp2))
        if self.stp2 < 0.3:
            print("[+]")
        else:
            print("if (cur_stp2 - cur_stp2/2 > self.stp2) or (cur_stp2 + cur_stp2/2 < self.stp2): [-]")
            if (cur_stp2 - cur_stp2/2 > self.stp2) or (cur_stp2 + cur_stp2/2 < self.stp2):
                print("[-]")
            else:
                print("[+]")
        print("stack3: " + str(t.seats[3].stack))
        print("cur_stp3: " + str(cur_stp3))
        print("reference self.stp3: " + str(self.stp3))
        if self.stp3 < 0.3:
            print("[+]")
        else:
            print("if (cur_stp3 - cur_stp3/2 > self.stp3) or (cur_stp3 + cur_stp3/2 < self.stp3): [-]")
            if (cur_stp3 - cur_stp3/2 > self.stp3) or (cur_stp3 + cur_stp3/2 < self.stp3):
                print("[-]")
            else:
                print("[+]")
        print("stack4: " + str(t.seats[4].stack))
        print("cur_stp4: " + str(cur_stp4))
        print("reference self.stp4: " + str(self.stp4))
        if self.stp4 < 0.3:
            print("[+]")
        else:
            print("if (cur_stp4 - cur_stp4/2 > self.stp4) or (cur_stp4 + cur_stp4/2 < self.stp4): [-]")
            if (cur_stp4 - cur_stp4/2 > self.stp4) or (cur_stp4 + cur_stp4/2 < self.stp4):
                print("[-]")
            else:
                print("[+]")
        print("stack5: " + str(t.seats[5].stack))
        print("cur_stp5: " + str(cur_stp5))
        print("reference self.stp5: " + str(self.stp5))
        if self.stp5 < 0.3:
            print("[+]")
        else:
            print("if (cur_stp5 - cur_stp5/2 > self.stp5) or (cur_stp5 + cur_stp5/2 < self.stp5): [-]")
            if (cur_stp5 - cur_stp5/2 > self.stp5) or (cur_stp5 + cur_stp5/2 < self.stp5):
                print("[-]")
            else:
                print("[+]")
        print("--------------------------------")
        dumb = input("]")
        '''

        #check for match seat0
        #half stp buffer to match the situation
        if self.stp0 < 0.3:
            #we don't need actual check as this sit is not in hand
            match_0 = 1
        else:
            if (cur_stp0 - cur_stp0/2 > self.stp0) or (cur_stp0 + cur_stp0/2 < self.stp0):
                pass
            else:
                #we have a match
                match_0 = 1

        #check for match seat1
        if self.stp1 < 0.3:
            match_1 = 1
        else:
            if (cur_stp1 - cur_stp1/2 > self.stp1) or (cur_stp1 + cur_stp1/2 < self.stp1):
                pass
            else:
                #we have a match
                match_1 = 1

        #check for match seat2
        if self.stp2 < 0.3:
            match_2 = 1
        else:
            if (cur_stp2 - cur_stp2/2 > self.stp2) or (cur_stp2 + cur_stp2/2 < self.stp2):
                pass
            else:
                #we have a match
                match_2 = 1

        #check for match seat3
        if self.stp3 < 0.3:
            match_3 = 1
        else:
            if (cur_stp3 - cur_stp3/2 > self.stp3) or (cur_stp3 + cur_stp3/2 < self.stp3):
                pass
            else:
                #we have a match
                match_3 = 1

        #check for match seat4
        if self.stp4 < 0.3:
            match_4 = 1
        else:
            if (cur_stp4 - cur_stp4/2 > self.stp4) or (cur_stp4 + cur_stp4/2 < self.stp4):
                pass
            else:
                #we have a match
                match_4 = 1

        #check for match seat5
        if self.stp5 < 0.3:
            match_5 = 1
        else:
            if (cur_stp5 - cur_stp5/2 > self.stp5) or (cur_stp5 + cur_stp5/2 < self.stp5):
                pass
            else:
                #we have a match
                match_5 = 1
        
        if (match_0 and match_1 and match_2 and match_3 and match_4 and match_5):
            settings.matched += 1 #count 1 more match
            return int(1)
        else:
            return int(0)

    def clear_hand_add_values_to_positions(self, table):
        t = table
        for s in t.seats:
            s.learning_hand_end_stack = (s.stack / (self.smallblind * 2))
        t.board = ""
        if settings.analyse_match:
            for s in t.seats:
                s.learning_hand_end_stack = (s.stack / (self.smallblind * 2))
            for numb in range(6):
                if numb == 0:
                    settings.bbvals0 += (t.seats[0].learning_hand_end_stack - t.seats[0].learning_hand_start_stack)
                elif numb == 1:
                    settings.bbvals1 += (t.seats[1].learning_hand_end_stack - t.seats[1].learning_hand_start_stack)
                elif numb == 2:
                    settings.bbvals2 += (t.seats[2].learning_hand_end_stack - t.seats[2].learning_hand_start_stack)
                elif numb == 3:
                    settings.bbvals3 += (t.seats[3].learning_hand_end_stack - t.seats[3].learning_hand_start_stack)
                elif numb == 4:
                    settings.bbvals4 += (t.seats[4].learning_hand_end_stack - t.seats[4].learning_hand_start_stack)
                elif numb == 5:
                    settings.bbvals5 += (t.seats[5].learning_hand_end_stack - t.seats[5].learning_hand_start_stack)
                else:
                    print("error in position clear_hand_add_values_to_positions")
                    dumb = input("]")
        else:
            pass

    def clear_hand(self, table):
        for s in table.seats:
            if s.stack == 0:
                s.empty()
        table.board = ""

    def analyseHand(self):
        global handlog
        global threebet
        global cwd    
        
        end_condition = 1

        #analysis will stop and report when :
            #1. matched_iterations == settings.enough_analysing_iterations
            #2. after '1000 iterations there is no new match'

            #wrap it in try/catch with ctrl+c to switch analyse_fast_speed
        settings.analyser_flag = 1 #analysis in progress
        while(end_condition):
            try:
                if settings.matched >= settings.enough_analysing_iterations:
                    settings.analysis_end = 1
                    end_condition = 0
                    settings.analyser_flag = 0 # end of analysis

                t = table.AnalysisTable(self.tabl_obj)
                t.dont_randomize_seats()
                tables = []
                tables.append(t)

                #checkpoint
                if self.iterations == 1000:
                    if settings.matched < 3:
                        settings.analyse_fast_speed = 0
                        display.display_tables_analyser(t, self.iterations, settings.matched)
                        print("situation is rare,")
                        print("can not be simulated")
                        dumb = input("]")
                        return
                if self.iterations == 2000:
                    if settings.matched < 6:
                        settings.analyse_fast_speed = 0
                        display.display_tables_analyser(t, self.iterations, settings.matched)
                        print("situation is rare,")
                        print("can not be simulated")
                        dumb = input("]")
                        return
                if self.iterations == 3000:
                    if settings.matched < 9:
                        settings.analyse_fast_speed = 0
                        display.display_tables_analyser(t, self.iterations, settings.matched)
                        print("situation is rare,")
                        print("can not be simulated")
                        dumb = input("]")
                        return
                if self.iterations == 4000:
                    if settings.matched < 12:
                        settings.analyse_fast_speed = 0
                        display.display_tables_analyser(t, self.iterations, settings.matched)
                        print("situation is rare,")
                        print("can not be simulated")
                        dumb = input("]")
                        return
                if self.iterations == 5000:
                    if settings.matched < 15:
                        settings.analyse_fast_speed = 0
                        display.display_tables_analyser(t, self.iterations, settings.matched)
                        print("situation is rare,")
                        print("can not be simulated")
                        dumb = input("]")
                        return
                if self.iterations == 6000:
                    if settings.matched < 18:
                        settings.analyse_fast_speed = 0
                        display.display_tables_analyser(t, self.iterations, settings.matched)
                        print("situation is rare,")
                        print("can not be simulated")
                        dumb = input("]")
                        return
                if self.iterations == 7000:
                    if settings.matched < 21:
                        settings.analyse_fast_speed = 0
                        display.display_tables_analyser(t, self.iterations, settings.matched)
                        print("situation is rare,")
                        print("can not be simulated")
                        dumb = input("]")
                        return
                if self.iterations == 8000:
                    if settings.matched < 24:
                        settings.analyse_fast_speed = 0
                        display.display_tables_analyser(t, self.iterations, settings.matched)
                        print("situation is rare,")
                        print("can not be simulated")
                        dumb = input("]")
                        return
                if self.iterations == 9000:
                    if settings.matched < 27:
                        settings.analyse_fast_speed = 0
                        display.display_tables_analyser(t, self.iterations, settings.matched)
                        print("situation is rare,")
                        print("can not be simulated")
                        dumb = input("]")
                        return
                
                

                self.iterations += 1
                settings.analysed_iterations = self.iterations
                settings.threebet = 0 # clear all previous reraises
                settings.total_pot = 0
                handlog = " "
            
                if t.starting_point == 'p':
                    t.board = " "
                elif t.starting_point == 'f':
                    t.board = t.setup_board[:6]
                elif t.starting_point == 't':
                    t.board = t.setup_board[:8]
                elif t.starting_point == 'r':
                    t.board = t.setup_board[:10]
                else:
                    print("unknown start point")
                    dumb = input("]")
            
                #settings.print_logo_analyser_menu()
                settings.hand_history_list = []
                settings.imported_list_preflop = []

                settings.turnstealing_attempt = 0 #clear flag
                settings.turnstealing_defend = 0 #clear flag
                settings.raise_on_flop = 0 #clear flag
                settings.raise_on_turn = 0 #clear flag
                settings.raise_on_river = 0 #clear flag
                settings.gamblers_acted_on_flop = 0
                settings.gamblers_acted_on_turn = 0
                settings.gamblers_acted_on_river = 0
                settings.left_gamblers = 0
                settings.first_flop = 0
                settings.first_turn = 0
                settings.first_river = 0
                settings.left_to_act_flop = 0
                settings.left_to_act_turn = 0
                settings.left_to_act_river = 0
                settings.checks_on_flop = 0 #clear flag
                settings.checks_on_turn = 0
                settings.checks_on_river = 0

                #clear pot
                t.pot = 0
                start_sum = 0
                endsum = 0
                self.ante = 0
                self.smallblind = int(t.bigblind/2)

                #clear seats
                for s in t.seats:
                    s.want_to_push = 0
                    s.stack = common.roundbet(s.stack)
                    s.equx_flop = 0.0
                    s.equx_turn = 0.0
                    s.equx_river = 0.0
                    s.bet = 0
                    s.last3bets = 0
                    s.oldbet = 0
                    #s.card1 = "  "
                    #s.card2 = "  "
                    s.vbetflag = 0
                    s.cbetflag = 0
                    s.floatandsteal = 0
                    s.learning_range_name = ""
                    s.learning_suit = "no"
                    s.learning_hand = ""
                    s.learning_sample = 0
                    s.learning_hand_start_stack = 0.0
                    s.learning_hand_end_stack = 0.0
                    s.learning_position = ""
                    s.learning_name = s.name
                    s.stp = 0 #stack to pot ratio
                    s.acted_preflop = 0
                    s.acted_flop = 0
                    s.acted_turn = 0
                    s.acted_river = 0
                    range_type_as_digit = 2
                    if s.stack < 0:
                        print("]error stack less than zero")
                        dumb = input("]")
                    
                    settings.pokerpool.update_fish(s)
                
                settings.print_logo_analyser_action()

                #clear empty seats:
                for s in t.seats:
                    if s.stack < 0.5:
                        s.empty()

                #if there is a predefined pot, give it to the players
                #in the setup situation so it can accur:
                #for example if setup situation 2 bots have stacks of 1000
                #and on the flop the pot is 1000, then preflop
                #bots have to start with 1500
                #setup pot give to all players
                #so after preflop and other streets
                #play they can get to situation
                #that matches

                if t.starting_point != 'p':
                    #preflop pot is small blind + big blind and always matches
                    added_to_stack = 0
                    gamblers = common.count_players_on_table(t)
                    dummy_gamblers = 0
                    for siits in t.seats:
                        if siits.stack > 0 and  siits.stack  <= settings.dumblind*1.5: #we have a dummy gambler
                            dummy_gamblers += 1

                    if (gamblers - dummy_gamblers) > 0:
                        added_to_stack = int(common.roundbet(t.predefined_pot/(gamblers - dummy_gamblers)))
                    else:
                        print("error no one on the table")
                        dumb = input("]")
                    for s in t.seats:
                        if s.stack > settings.dumblind*1.5:
                            #if there is a non dummy gambler, add to his starting stack
                            s.stack += added_to_stack

                #get for each seat the stacks in bbs so we can get the difference at the end of hand
                for s in t.seats:
                    s.learning_hand_start_stack = (s.stack / (self.smallblind * 2))
                

                deck = ['as', 'ks', 'qs', 'js', 'ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', \
                    'ah', 'kh', 'qh', 'jh', 'th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', \
                    'ad', 'kd', 'qd', 'jd', 'td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', \
                    'ac', 'kc', 'qc', 'jc', 'tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c' ]

                random.shuffle(deck)
                t.stack_cards = []
                for cardz in deck:
                    t.stack_cards.append(cardz)

    
                #here we need to setup the cards that are coming if
                #they are predefined for the analysis in a way that
                #bots do not know it when play, also need to remove
                #from table.stack_cards the predefined ones and also
                #the hole cards
                
                board_card = ""
                board_card = t.setup_board[0] + t.setup_board[1]
                if board_card in t.stack_cards:
                    t.stack_cards = common.remove_item_from_list(t.stack_cards, board_card)

                board_card = ""
                board_card = t.setup_board[2] + t.setup_board[3]
                if board_card in t.stack_cards:
                    t.stack_cards = common.remove_item_from_list(t.stack_cards, board_card)

                board_card = ""
                board_card = t.setup_board[4] + t.setup_board[5]
                if board_card in t.stack_cards:
                    t.stack_cards = common.remove_item_from_list(t.stack_cards, board_card)

                board_card = ""
                board_card = t.setup_board[6] + t.setup_board[7]
                if board_card in t.stack_cards:
                    t.stack_cards = common.remove_item_from_list(t.stack_cards, board_card)

                board_card = ""
                board_card = t.setup_board[8] + t.setup_board[9]
                if board_card in t.stack_cards:
                    t.stack_cards = common.remove_item_from_list(t.stack_cards, board_card)

                dealt_cards = []
                #remove dealt cards
                for s in t.seats:
                    dealt_cards.append(s.card1)
                    dealt_cards.append(s.card2)

                for card in dealt_cards:
                    if card in t.stack_cards:
                        t.stack_cards = common.remove_item_from_list(t.stack_cards, card)

                random.shuffle(t.stack_cards)

                for s in t.seats:
                    if not s.available:
                        s.learning_position = ""
                        position_number = common.getPreflopPosition(t, s.name)
                        if position_number == 60 or position_number == 50 or position_number == 40 or position_number == 30:
                            s.learning_position = "db" #dealer button
                        elif position_number == 20:
                            s.learning_position = "hd" #heads up dealer
                        elif position_number == 21:
                            s.learning_position = "hb" #heads up big blind                 
                        elif position_number == 61 or position_number == 51 or position_number == 41 or position_number == 31:
                            s.learning_position = "sb" #small blind
                        elif position_number == 62 or position_number == 52 or position_number == 42 or position_number == 32:
                            s.learning_position = "bb" #big blind
                        elif position_number == 63:
                            s.learning_position = "ug" #unther the gun
                        elif position_number == 64 or position_number == 53:
                            s.learning_position = "hj" #highjack
                        elif position_number == 65 or position_number == 54 or position_number == 43:
                            s.learning_position = "co" #cutoff
                        else:
                            print("error in current position: " + str(position_number))
                            dumb = input("]")

                #give cards if missing
                for s in t.seats:
                    if s.card1 == '[]':
                        s.card1 = t.stack_cards.pop()
                    if s.card2 == '[]':
                        s.card2 = t.stack_cards.pop()


            #PREFLOP
                antes = common.countNotFoldedYet(t)*self.ante
                cur_pot = self.smallblind*3 + antes
                for s in t.seats:
                    s.stp = common.roundbet(s.stack/cur_pot)
                t.board = ""
                #clear match flag
                settings.analyse_match = 0
                #always start from flop, just don't count situations
                #that do not match

                #we clear pot as preflop
                #will take blinds on regular way
                t.pot = 0

                if t.starting_point == 'p':
                    #if starting point is preflop, we have matched the situation
                    settings.matched += 1
                    settings.analyse_match = 1
                else:
                    settings.analyse_match = 0 

                handlog += "start sum\n"
                start_sum = common.checksum(t)
                # take blinds
                num_p = common.count_players_on_table(t)
                if num_p == 0:
                    print("no players on table!")
                    dumb = input("]")
                elif num_p == 1:
                    print("only one player on table!")
                    dumb = input("]")
                elif num_p == 2:
                    #heads up rules dealer is sb
                    db_p = common.find_button(t)
                    if t.seats[db_p].stack >= (self.smallblind + self.ante):
                        t.seats[db_p].bet = self.smallblind + self.ante
                        t.seats[db_p].stack -= self.smallblind
                    else:
                        #allin
                        t.seats[db_p].bet += t.seats[db_p].stack
                        t.seats[db_p].stack = 0
                    t.pot += t.seats[db_p].bet
                    if settings.hand_history:
                        common.update_total_pot(t)
                        hand_history_line = "" + t.seats[db_p].name + " post " + str(t.seats[db_p].bet) + "\n"
                        settings.imported_list_preflop.append(hand_history_line)
                    
                    next_p = common.find_next_occupied_chair(t, db_p)
                    if t.seats[next_p].stack >= (self.smallblind*2 + self.ante):
                        t.seats[next_p].bet = self.smallblind*2 + self.ante
                        t.seats[next_p].stack -= self.smallblind*2
                    else:
                        #allin
                        t.seats[next_p].bet += t.seats[next_p].stack
                        t.seats[next_p].stack = 0
                    t.pot += t.seats[next_p].bet
                    if settings.hand_history:
                        common.update_total_pot(t)
                        hand_history_line = "" + t.seats[next_p].name + " post " + str(t.seats[next_p].bet) + "\n"
                        settings.imported_list_preflop.append(hand_history_line)
                else:
                    #normal rules d +sb +h
                    db_p = common.find_button(t)
                    next_p = common.find_next_occupied_chair(t, db_p)
                    if t.seats[next_p].stack >= self.smallblind:
                        t.seats[next_p].bet = self.smallblind + self.ante
                        t.seats[next_p].stack -= self.smallblind
                    else:
                        t.seats[next_p].bet = t.seats[next_p].stack
                        t.seats[next_p].stack = 0
                    t.pot += t.seats[next_p].bet
                    if settings.hand_history:
                        common.update_total_pot(t)
                        hand_history_line = "" + t.seats[next_p].name + " post " + str(t.seats[next_p].bet) + "\n"
                        settings.imported_list_preflop.append(hand_history_line)
                
                    nextnext_p = common.find_next_occupied_chair(t, next_p)
                    if t.seats[nextnext_p].stack >= self.smallblind*2:
                        t.seats[nextnext_p].bet = self.smallblind*2 + self.ante
                        t.seats[nextnext_p].stack -= self.smallblind*2
                    else:
                        t.seats[nextnext_p].bet = t.seats[nextnext_p].stack
                        t.seats[nextnext_p].stack = 0            
                    t.pot += t.seats[nextnext_p].bet
                    if settings.hand_history:
                        common.update_total_pot(t)
                        hand_history_line = "" + t.seats[nextnext_p].name + " post " + str(t.seats[nextnext_p].bet) + "\n"
                        settings.imported_list_preflop.append(hand_history_line)

            
                display.display_tables_analyser(t, self.iterations, settings.matched)
                
                #preflop
                handlog += "before blinds -> after blinds\n"
                temp_sum = common.checksum(t)
                
                for s in t.seats:
                    if s.available == 0:
                        s.preorbits += 1
                common.playHandpreflop(t, self.game_type, self.smallblind, self.ante, tables)
                for s in t.seats:
                    if not s.available:
                        if not common.checkFold(s):
                            if s.vbetflag:
                                s.vbet += 1
                if common.check_hand_over_folds(t):
                    self.clear_hand(t)

                else:
                    handlog += "preflop\n"
                    temp_sum = common.checksum(t)
                    
                    #first card on flop
                    if t.setup_board[0] != '[' and t.setup_board[0] != " ":
                        #get predefined card first on flop rank and suit
                        t.board = t.setup_board[0]
                        t.board += t.setup_board[1]
                    else:
                        #get random card from stack_cards
                        t.board = t.stack_cards.pop()
                    #second card on flop
                    if t.setup_board[2] != '[' and t.setup_board[2] != " ":
                        #get predefined card second on flop rank and suit
                        t.board += t.setup_board[2]
                        t.board += t.setup_board[3]
                    else:
                        #get random card from stack_cards
                        t.board += t.stack_cards.pop()
                    #third card on flop
                    if t.setup_board[4] != '[' and t.setup_board[4] != " ":
                        #get predefined card second on flop rank and suit
                        t.board += t.setup_board[4]
                        t.board += t.setup_board[5]
                    else:
                        #get random card from stack_cards
                        t.board += t.stack_cards.pop()
                    #hand history
                    if settings.hand_history:
                        hand_history_line = "*** FLOP *** [" + t.board + "]\n"
                        settings.hand_history_buffer.add_line(hand_history_line)

                    #hand history
                    if settings.hand_history:
                        hand_history_line = "*** FLOP *** [" + t.board + "]\n"
                        settings.hand_history_buffer.add_line(hand_history_line)

                    for s in t.seats:
                        if s.available == 0:
                            s.floporbits += 1
                    #flop
                    if t.starting_point == 'f':
                        #if starting point is flop check
                        #stack to pot ratios if match
                        settings.analyse_match = self.match_situation(t)
                    common.playHandpostflop(t, self.game_type, self.smallblind, self.ante, tables)
                    for s in t.seats:
                        if not s.available:
                            if not common.checkFold(s):
                                if s.cbetflag:
                                    s.cbet += 1
                if common.check_hand_over_folds(t):
                    self.clear_hand(t)
                else:
                    #turn
                    handlog += "turn\n"
                    temp_sum = common.checksum(t)
                    
                    if t.setup_board[6] != '[' and t.setup_board[6] != " ":
                        #get predefined card on turn rank and suit
                        t.board += t.setup_board[6]
                        t.board += t.setup_board[7]
                    else:
                        #get random card from stack_cards
                        t.board += t.stack_cards.pop()
                    #hand history
                    if settings.hand_history:
                        hand_history_line = "*** TURN *** [" + t.board + "]\n"
                        settings.hand_history_buffer.add_line(hand_history_line)
                    
                    if t.starting_point == 't':
                        #if starting point is turn check
                        #stack to pot ratios if match
                        settings.analyse_match = self.match_situation(t)
                    common.playHandpostflop(t, self.game_type, self.smallblind, self.ante, tables)

                if common.check_hand_over_folds(t):
                    self.clear_hand(t)
                else:
                    #river
                    handlog += "river\n"
                    temp_sum = common.checksum(t)
                    
                    if t.setup_board[8] != '[' and t.setup_board[8] != " ":
                        #get predefined card on river rank and suit
                        t.board += t.setup_board[8]
                        t.board += t.setup_board[9]
                    else:
                        #get random card from stack_cards
                        t.board += t.stack_cards.pop()
                    #hand history
                    if settings.hand_history:
                        hand_history_line = "*** RIVER *** [" + t.board + "]\n"
                        settings.hand_history_buffer.add_line(hand_history_line)

                    if t.starting_point == 'r':
                        #if starting point is river check
                        #stack to pot ratios if match
                        settings.analyse_match = self.match_situation(t)
                    common.playHandpostflop(t, self.game_type, self.smallblind, self.ante, tables)

                    if not settings.cards_faceup:
                        settings.toggle_cards_faceup = 1
                        settings.cards_faceup = 1
                        display.display_tables_analyser(t, self.iterations, settings.matched)
                    else:
                        pass

                    if settings.toggle_cards_faceup:
                        settings.cards_faceup = 0
                        settings.toggle_cards_faceup = 0

                
                if common.check_hand_over_folds(t):
                    self.clear_hand_add_values_to_positions(t)
                    if settings.debug_postflop_stop_point:
                        dumb = input("]")
                    else:
                        time.sleep(settings.bot_time_to_act_turn)
                else:
                    while(t.pot > 0.1):
                        break_from_while = 0
                        showdown_seats = []
                        splitters = []
                        for s in t.seats:
                            if not s.available:           #there is a player on a chair
                                if not common.checkFold(s): #he has not folded /yet/
                                    if s.bet:             #if this is not the first iteration
                                        showdown_seats.append(s)

                        if len(showdown_seats) == 1:    #have to get out of while and finish hand
                            showdown_seats[0].stack += showdown_seats[0].bet
                            t.pot = 0
                            break_from_while = 1

                        if break_from_while:
                            break

                        flist_cards = []
                        if len(showdown_seats) == 2:
                            fcard1 = form.format_card_for_calculating(showdown_seats[0].card1)
                            fcard2 = form.format_card_for_calculating(showdown_seats[0].card2)
                            fcard3 = form.format_card_for_calculating(showdown_seats[1].card1)
                            fcard4 = form.format_card_for_calculating(showdown_seats[1].card2)
                            flist_cards.append(fcard1)
                            flist_cards.append(fcard2)
                            flist_cards.append(fcard3)
                            flist_cards.append(fcard4)
                        elif len(showdown_seats) == 3:
                            fcard1 = form.format_card_for_calculating(showdown_seats[0].card1)
                            fcard2 = form.format_card_for_calculating(showdown_seats[0].card2)
                            fcard3 = form.format_card_for_calculating(showdown_seats[1].card1)
                            fcard4 = form.format_card_for_calculating(showdown_seats[1].card2)
                            fcard5 = form.format_card_for_calculating(showdown_seats[2].card1)
                            fcard6 = form.format_card_for_calculating(showdown_seats[2].card2)
                            flist_cards.append(fcard1)
                            flist_cards.append(fcard2)
                            flist_cards.append(fcard3)
                            flist_cards.append(fcard4)
                            flist_cards.append(fcard5)
                            flist_cards.append(fcard6)
                        elif len(showdown_seats) == 4:
                            fcard1 = form.format_card_for_calculating(showdown_seats[0].card1)
                            fcard2 = form.format_card_for_calculating(showdown_seats[0].card2)
                            fcard3 = form.format_card_for_calculating(showdown_seats[1].card1)
                            fcard4 = form.format_card_for_calculating(showdown_seats[1].card2)
                            fcard5 = form.format_card_for_calculating(showdown_seats[2].card1)
                            fcard6 = form.format_card_for_calculating(showdown_seats[2].card2)
                            fcard7 = form.format_card_for_calculating(showdown_seats[3].card1)
                            fcard8 = form.format_card_for_calculating(showdown_seats[3].card2)
                            flist_cards.append(fcard1)
                            flist_cards.append(fcard2)
                            flist_cards.append(fcard3)
                            flist_cards.append(fcard4)
                            flist_cards.append(fcard5)
                            flist_cards.append(fcard6)
                            flist_cards.append(fcard7)
                            flist_cards.append(fcard8)
                        elif len(showdown_seats) == 5:
                            fcard1 = form.format_card_for_calculating(showdown_seats[0].card1)
                            fcard2 = form.format_card_for_calculating(showdown_seats[0].card2)
                            fcard3 = form.format_card_for_calculating(showdown_seats[1].card1)
                            fcard4 = form.format_card_for_calculating(showdown_seats[1].card2)
                            fcard5 = form.format_card_for_calculating(showdown_seats[2].card1)
                            fcard6 = form.format_card_for_calculating(showdown_seats[2].card2)
                            fcard7 = form.format_card_for_calculating(showdown_seats[3].card1)
                            fcard8 = form.format_card_for_calculating(showdown_seats[3].card2)
                            fcard9 = form.format_card_for_calculating(showdown_seats[4].card1)
                            fcard10 = form.format_card_for_calculating(showdown_seats[4].card2)
                            flist_cards.append(fcard1)
                            flist_cards.append(fcard2)
                            flist_cards.append(fcard3)
                            flist_cards.append(fcard4)
                            flist_cards.append(fcard5)
                            flist_cards.append(fcard6)
                            flist_cards.append(fcard7)
                            flist_cards.append(fcard8)
                            flist_cards.append(fcard9)
                            flist_cards.append(fcard10)
                        elif len(showdown_seats) == 6:
                            fcard1 = form.format_card_for_calculating(showdown_seats[0].card1)
                            fcard2 = form.format_card_for_calculating(showdown_seats[0].card2)
                            fcard3 = form.format_card_for_calculating(showdown_seats[1].card1)
                            fcard4 = form.format_card_for_calculating(showdown_seats[1].card2)
                            fcard5 = form.format_card_for_calculating(showdown_seats[2].card1)
                            fcard6 = form.format_card_for_calculating(showdown_seats[2].card2)
                            fcard7 = form.format_card_for_calculating(showdown_seats[3].card1)
                            fcard8 = form.format_card_for_calculating(showdown_seats[3].card2)
                            fcard9 = form.format_card_for_calculating(showdown_seats[4].card1)
                            fcard10 = form.format_card_for_calculating(showdown_seats[4].card2)
                            fcard11 = form.format_card_for_calculating(showdown_seats[5].card1)
                            fcard12 = form.format_card_for_calculating(showdown_seats[5].card2)
                            flist_cards.append(fcard1)
                            flist_cards.append(fcard2)
                            flist_cards.append(fcard3)
                            flist_cards.append(fcard4)
                            flist_cards.append(fcard5)
                            flist_cards.append(fcard6)
                            flist_cards.append(fcard7)
                            flist_cards.append(fcard8)
                            flist_cards.append(fcard9)
                            flist_cards.append(fcard10)
                            flist_cards.append(fcard11)
                            flist_cards.append(fcard12)
                        else:
                            print("error unsupported number 2-6 of showdown seats")
                            dumb = input("]")

                        fboard = form.format_board_for_calculating(t.board)
                        resultlist = []
                        resultlist = calculator.find_equity(flist_cards, fboard)
                        del resultlist[0]
                        length = len(resultlist)
                        counter = 0
                        for counter in range(0,length):
                            showdown_seats[counter].showdown_result = float(resultlist[counter])

                        allzeros = True
                        for counter in range(0,length):
                            if showdown_seats[counter].showdown_result > 0.01:
                                allzeros = False
                        if allzeros:
                            for counter in range(0,length):
                                showdown_seats[counter].showdown_result = float(1.0/len(showdown_seats))

                        if length == 1:
                            # the man who covered all gets back his bet and gets out of the list:
                            for ss in showdown_seats:
                                ss.stack += ss.bet
                                ss.bet = 0
                                ss.card1 = "  "
                        else:
                            #more than one left and pot to contest
                            show_res_one = 0 # flag if there will be someone with res = 1
                            for ss in showdown_seats:
                                if ss.showdown_result == 1:
                                    dead_money = 0.0
                                    #collect in dead money also blinds and previous bets that had folded during play    
                                    for s in t.seats:
                                        if common.checkFold(s):
                                            if s.bet != 0:
                                                dead_money += s.bet
                                                s.bet = 0
                                    ss.stack += dead_money
                                    t.pot -= dead_money
                                    dead_money = 0
                                    #go again trough that list and take money from everybody if it is not you and then get out of showdown
                                    for subs in showdown_seats:
                                        if ss.bet >= subs.bet:
                                            ss.stack += subs.bet
                                            t.pot -= subs.bet
                                            if ss.name != subs.name:
                                                subs.bet = 0
                                        else:
                                            ss.stack += ss.bet
                                            t.pot -= subs.bet
                                            if ss.name != subs.name:
                                                subs.bet -= ss.bet

                                    ss.card1 = "  "
                                    ss.bet = 0
                                    t.pot = 0.0
                                    for s in showdown_seats:
                                        t.pot += s.bet
        
                                    showdown_seats.remove(ss)
                                    splitters = [] # clear so far splitters
                                    show_res_one = 1
                                    ### break here to go to the while
                                else: 
                                    splitters.append(ss)
                            if show_res_one == 0:        
                                if ((len(splitters)) and (t.pot > 0.001)):
                                    #if there are splitters or zero results
                                    #we get here if nobody has showdown result 1 which means split pot, except those who had showdown results zero,
                                    #but we still can not remove them as if they had bigger stacks, after removing the split players
                                    #they can have the 1 showdown value or just cover everybodyhave to sort all with nonzero showdown value
                                    #and from smaller to the bigger
                                    #gets its share and get out of showdown for this will create list with splitters
                                    #if there is last splitter left, he covers other splitters must remove splitters list but stay in showdown_list
                                    #to compete with others for what has left as his bet
                                    #splitters = []
                                    #we have to add zerolist = [] which includes showdown players with zero result.
                                    #we will take their share of the bet for others in splitter list untill their bet is zero or until they left with
                                    #something - this means they cover the splitters and will again participate in the next iterations,
                                    #but they will not take anything from pot during this particular iteration because have zero /less than splitters/ share
                                    #sort splitters by betsize and after that reverse the list so we have smaller first, after that create zerolist
                                    #find biggest and smaller bet to get the range
                                    
                                    #bubblesort
                                    n = len(splitters)
                                    for i in range(n):
                                        for j in range(0,n-i-1):
                                            if splitters[j].bet > splitters[j+1].bet:
                                                splitters[j],splitters[j+1] = splitters[j+1], splitters[j]

                                    rev_splitters = list(reversed(splitters))

                                    zerolist = []
                                    for rsp in rev_splitters:
                                        if rsp.showdown_result == 0:
                                            zerolist.append(rsp)
                                
                                    biggest_bet_rev_splitters = 0
                                    for rvs in rev_splitters:
                                        if rvs.bet > biggest_bet_rev_splitters:
                                            biggest_bet_rev_splitters = rvs.bet


                                #from zerolist return to stack and subtract from bet everything that is left for each player in zerolist
                                    for z in zerolist:                            
                                        if z.bet > biggest_bet_rev_splitters:
                                            z.stack += z.bet - biggest_bet_rev_splitters
                                            z.bet -= biggest_bet_rev_splitters

                                #collect dead_money_pot
                                    dead_money_pot = 0.0
                                    for z in zerolist:
                                        dead_money_pot += z.bet
                                        z.bet = 0
                                #collect in dead money also blinds and previous bets that had folded during play    
                                    for s in t.seats:
                                        if common.checkFold(s):
                                            if s.bet != 0:
                                                dead_money_pot += s.bet
                                                s.bet = 0

                                    t.pot -= dead_money_pot
                                    rev_sum = 0
                                    for rvs in rev_splitters:
                                        rev_sum += rvs.bet

                                    dead_one_percent = dead_money_pot/100
                                    rev_split_one_percent = rev_sum/100

                                    for rvs in rev_splitters:
                                        if rvs.showdown_result != 0:
                                            rvs.stack += rvs.bet/rev_split_one_percent * dead_one_percent
                                            dead_money_pot -= rvs.bet/rev_split_one_percent * dead_one_percent

                                    live_money = 0.0
                                    for rvs in rev_splitters:
                                        if rvs not in zerolist:
                                            live_money += rvs.bet

                                    one_percent_live_money = live_money/100

                                    for rvs in rev_splitters:
                                        if rvs not in zerolist:
                                            rvs.stack += ((rvs.bet / one_percent_live_money) * live_money)/100
                                            t.pot -= ((rvs.bet / one_percent_live_money) * live_money)/100
                                            rvs.bet = 0
                                    for s in t.seats:
                                        s.stack = common.roundbet(s.stack)

                    if settings.debug_postflop_stop_point:
                        dumb = input("]")
                    else:
                        time.sleep(settings.time_to_wait_board)
                    self.clear_hand_add_values_to_positions(t)
                    for s in t.seats:
                        s.card1 = "  "
                        s.card2 = "  "
                        s.bet = 0
                    t.board = ""

                dorecord = 1

                if settings.hand_history:
                    hand_history_line = "*** SUMMARY ***\n"
                    settings.hand_history_buffer.add_line(hand_history_line)
                    hand_history_line = "Total pot " + str(settings.total_pot) + " | Rake " + str(settings.rake) + "%\n"
                    settings.hand_history_buffer.add_line(hand_history_line)
                    hand_history_line = "\n"
                    settings.hand_history_buffer.add_line(hand_history_line)
                    hand_history_line = "\n"
                    settings.hand_history_buffer.add_line(hand_history_line)

                players_left_with_stacks = 0
                for s in t.seats:
                    if s.stack > 0:
                      players_left_with_stacks += 1
            except:
                print(" ") # this is for ^C
                print("q quit analyzer")
                print("s switch speed")
                #toggle speed anyway
                if not settings.analyse_fast_speed:
                    settings.analyse_fast_speed = 1
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
                else:
                    #slow speed
                    settings.analyse_fast_speed = 0
                    settings.bot_time_to_act = 3
                    settings.bot_time_to_act_preflop = 3
                    settings.bot_time_to_act_flop = 3
                    settings.bot_time_to_act_turn = 3
                    settings.bot_time_to_act_river = 3
                    settings.time_to_wait_board = 8
                    settings.selected_bot_time_to_act = 3
                    settings.selected_bot_time_to_act_preflop = 3
                    settings.selected_bot_time_to_act_flop = 3
                    settings.selected_bot_time_to_act_turn = 3
                    settings.selected_bot_time_to_act_river = 3
                    settings.selected_time_to_wait_board = 8
                    settings.debug_ranges_stop_point = 0
                    settings.debug_ranges = 1
                    settings.debug_postflop = 1
                    settings.debug_postflop_stop_point = 0
                choice = input("]")
                if choice == 'q':
                    return
        #if settings.hudanalyser:
        #    print("open bet sizing: " + settings.huanalyzer_open_size)

def remove_cards_from_deck(the_deck, card):
   return [value for value in the_deck if value != card]

def help():
    print("set up custom situation, it")
    print("will go 10 000 iterations.")
    print("Each position will get random")
    print("bot each iteration. At the end")
    print("get report of the big blinds")
    print("won or lost from each position")
    dumb = input("]")

def run():

    #HuAnalyzer redfish open
    settings.huanalyzer_open = []

    #HuAnalyzer redfish call 3bet
    settings.huanalyzer_call3bet = []

    #HuAnalyzer 3bet from blackfish
    settings.huanalyzer_3bet = []

    #HuAnalyzer_call blackfish
    settings.huanalyzer_call = []

    #HuAnalyzer redfish open
    selected_file = "fishes/redfish/ranges/hd_openAnalyzer.range"
    selected_range = "hd_openAnalyzer.range"
    try:
        f = open(selected_file,'r')
        with f:
            lines = f.read().splitlines()
        f.close()
        for l in lines:
            settings.huanalyzer_open.append(l)
    except IOError:
        print("no such file: " + selected_file)
        dumb = input("]")

    #HuAnalyzer redfish call 3bet
    selected_file = "fishes/redfish/ranges/hd_call3betAnalyzer.range"
    selected_range = "hd_call3betAnalyzer.range"
    try:
        f = open(selected_file,'r')
        with f:
            lines = f.read().splitlines()
        f.close()
        for l in lines:
            settings.huanalyzer_call3bet.append(l)
    except IOError:
        print("no such file: " + selected_file)
        dumb = input("]")

    #HuAnalyzer_call blackfish
    selected_file = "fishes/blackfish/ranges/hb_callAnalyzer.range"
    selected_range = "hb_callAnalyzer.range"
    try:
        f = open(selected_file,'r')
        with f:
            lines = f.read().splitlines()
        f.close()
        for l in lines:
            settings.huanalyzer_call.append(l)
    except IOError:
        print("no such file: " + selected_file)
        dumb = input("]")
    
    #HuAnalyzer 3bet from blackfish
    selected_file = "fishes/blackfish/ranges/hb_3betAnalyzer.range"
    selected_range = "hb_3betAnalyzer.range"
    try:
        f = open(selected_file,'r')
        with f:
            lines = f.read().splitlines()
        f.close()
        for l in lines:
            settings.huanalyzer_3bet.append(l)
    except IOError:
        print("no such file: " + selected_file)
        dumb = input("]")


    analysis_end = 0
    #starting conditions for analyser
    allcards = ['as', 'ks', 'qs', 'js', 'ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', \
                'ah', 'kh', 'qh', 'jh', 'th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', \
                'ad', 'kd', 'qd', 'jd', 'td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', \
                'ac', 'kc', 'qc', 'jc', 'tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c']
    stack0 = 1000
    stack1 = 1000
    stack2 = 0
    stack3 = 0
    stack4 = 0
    stack5 = 0
    button_number = 0 #seat 0 is always button
    bigblind = 20
    pot = 0
    board = ""
    starting_point = 'p' #p=preflop, f=flop, t=turn, r=river
    flopcard1 = settings.backcard   #xx is random card each iteration
    flopcard2 = settings.backcard
    flopcard3 = settings.backcard
    turncard = settings.backcard
    rivercard = settings.backcard
    card01 = settings.backcard #seat0 card1
    card02 = settings.backcard #seat0 card2
    card11 = settings.backcard #seat1 card1
    card12 = settings.backcard #seat1 card2
    card21 = settings.backcard #seat2 card1
    card22 = settings.backcard #seat2 card2
    card31 = settings.backcard #seat3 card1
    card32 = settings.backcard #seat3 card2
    card41 = settings.backcard #seat4 card1
    card42 = settings.backcard #seat4 card2
    card51 = settings.backcard #seat5 card1
    card52 = settings.backcard #seat5 card2

    settings.print_logo_analyser_menu()

    dum_seat0 = seat.DummySeat(0, '  ', '  ')
    dum_seat1 = seat.DummySeat(0, '  ', '  ')
    dum_seat2 = seat.DummySeat(0, '  ', '  ')
    dum_seat3 = seat.DummySeat(0, '  ', '  ')
    dum_seat4 = seat.DummySeat(0, '  ', '  ')
    dum_seat5 = seat.DummySeat(0, '  ', '  ')
    dum_tab = table.DummyTable()
    dum_seat0.button = settings.image_db
    dum_tab.seats.append(dum_seat0)
    dum_tab.seats.append(dum_seat1)
    dum_tab.seats.append(dum_seat2)
    dum_tab.seats.append(dum_seat3)
    dum_tab.seats.append(dum_seat4)
    dum_tab.seats.append(dum_seat5)
    display.print_a_dummy_table(dum_tab)

    dum_tab.seats[0].name = "seat0"
    dum_tab.seats[1].name = "seat1"
    dum_tab.seats[2].name = "seat2"
    dum_tab.seats[3].name = "seat3"
    dum_tab.seats[4].name = "seat4"
    dum_tab.seats[5].name = "seat5"

    we_got_situation = 0


    valid_choice = 1
    settings.dumblind = 20
    settings.amap = [0,0,0,0,0,0]




    dum_tab.seats[0].displaystack = get_display_stack(stack0)
    if dum_tab.seats[0].displaystack != "  ":
        settings.amap[0] = 1
    dum_tab.seats[0].face = get_face()

    dum_tab.seats[1].displaystack = get_display_stack(stack1)
    if dum_tab.seats[1].displaystack != "  ":
        settings.amap[1] = 1
    dum_tab.seats[1].face = get_face()
    we_got_situation = 1
    print("we got situation")
    display.print_a_dummy_table(dum_tab)
    #dumb = input("]6")

    stack2 = 0
    stack3 = 0
    stack4 = 0
    stack5 = 0
    if stack2 > 1:
        print(" ")
        print("enter stack for seat3:")
        stack = input("]")
        if stack.isdigit() and int(stack) >= 0:
            if int(stack) < settings.dumblind:
                stack3 = settings.dumblind*1.5
            else:
                stack3 = int(stack)
            if bigblind*1000 < stack3:
                print("too deep, can not set more than 1000 big blinds stack")
                print("stack set to 1000 big blinds")
                stack3 = bigblind*1000
            dum_tab.seats[3].displaystack = get_display_stack(stack3)
            if dum_tab.seats[3].displaystack != "  ":
                settings.amap[3] = 1
            dum_tab.seats[3].face = get_face()
        else:
            stack3 = 0
            stack4 = 0
            stack5 = 0
        display.print_a_dummy_table(dum_tab)


    if stack3 > 1:
        print(" ")
        print("enter stack for seat4:")
        stack = input("]")
        if stack.isdigit() and int(stack) >= 0:
            if int(stack) < settings.dumblind:
                stack4 = settings.dumblind*1.5
            else:
                stack4 = int(stack)
            if bigblind*1000 < stack4:
                print("too deep, can not set more than 1000 big blinds stack")
                print("stack set to 1000 big blinds")
                stack4 = bigblind*1000
            dum_tab.seats[4].displaystack = get_display_stack(stack4)
            if dum_tab.seats[4].displaystack != "  ":
                settings.amap[4] = 1
            dum_tab.seats[4].face = get_face()
        else:
            stack4 = 0
            stack5 = 0
        display.print_a_dummy_table(dum_tab)

    if stack4 > 1:
        print(" ")
        print("enter stack for seat5:")
        stack = input("]")
        if stack.isdigit() and int(stack) >= 0:
            if int(stack) < settings.dumblind:
                stack5 = settings.dumblind*1.5
            else:
                stack5 = int(stack)
            if bigblind*1000 < stack5:
                print("too deep, can not set more than 1000 big blinds stack")
                print("stack set to 1000 big blinds")
                stack5 = bigblind*1000
            dum_tab.seats[5].displaystack = get_display_stack(stack5)
            if dum_tab.seats[5].displaystack != "  ":
                settings.amap[5] = 1
            dum_tab.seats[5].face = get_face()
        else:
            stack5 = 0
        #display.print_a_dummy_table(dum_tab)

    if we_got_situation:

        #enter starting point
        valid_choice = 1
        valid_choices = ['p', 'f', 't', 'r']
        while valid_choice:
            display.print_a_dummy_table(dum_tab)
            print(" ")
            print("enter starting point")
            print("p=preflop, f=flop, t=turn, r=river:")
            dumbbut = "p"
            if dumbbut in valid_choices:
                starting_point = dumbbut
                dum_tab.starting_point = dumbbut
                valid_choice = 0
            else:
                print("not valid")
        #display.print_a_dummy_table(dum_tab)

        if starting_point != 'p':
            #enter pot only if starting point is not preflop,
            #else it will be small blind + big blind
            valid_choice = 1
            while valid_choice:
                print(" ")
                print("enter pot:")
                dumbbut = input("]")
                if dumbbut.isdigit() and (int(dumbbut) > -1):
                    pot = int(dumbbut)
                    dum_tab.pot = pot
                    valid_choice = 0
                else:
                    print("not valid")
            display.print_a_dummy_table(dum_tab)

        #flop card1
        flopcard1 = '[]'
        board += flopcard1
        dum_tab.displayboard += common.displayhand(flopcard1)
        #display.print_a_dummy_table(dum_tab)
        
        #flop card2
        flopcard2 = '[]'
        board += flopcard2
        dum_tab.displayboard += common.displayhand(flopcard2)
        #display.print_a_dummy_table(dum_tab)

        #flop card3
        flopcard3 = '[]'
        board += flopcard3
        dum_tab.displayboard += common.displayhand(flopcard3)
        #display.print_a_dummy_table(dum_tab)

        #turn card
        turncard = '[]'
        board += turncard
        dum_tab.displayboard += common.displayhand(turncard)
        #display.print_a_dummy_table(dum_tab)

        #river card
        rivercard = '[]'
        board += rivercard
        print("board: " + board)
        dum_tab.displayboard += common.displayhand(rivercard)
        #display.print_a_dummy_table(dum_tab)

        #seat0 hole cards
        dum_tab.seats[0].displaycard1 = '[]'
        dum_tab.seats[0].displaycard2 = '[]'
        dum_tab.seats[1].displaycard1 = '[]'
        dum_tab.seats[1].displaycard2 = '[]'

        #seat2 hole cards
        if stack2 > 0:
            print(" ")
            print("enter seat2 card1:")
            dumbbut = input("]")
            if dumbbut in allcards:
                card21 = dumbbut
                allcards = remove_cards_from_deck(allcards, card21)
                dum_tab.seats[2].displaycard1 = common.displayhand(card21)
            else:
                #random card will be given at each iteration
                dum_tab.seats[2].displaycard1 = '[]'
            display.print_a_dummy_table(dum_tab)
            print(" ")
            print("enter seat2 card2:")
            dumbbut = input("]")
            if dumbbut in allcards:
                card22 = dumbbut
                allcards = remove_cards_from_deck(allcards, card22)
                dum_tab.seats[2].displaycard2 = common.displayhand(card22)
            else:
                #random card will be given at each iteration
                dum_tab.seats[2].displaycard2 = '[]'
            display.print_a_dummy_table(dum_tab)    
        else:
            #clear cards as folded
            card21 = "  "
            card22 = "  "

        #seat3 hole cards
        if stack3 > 0:
            print(" ")
            print("enter seat3 card1:")
            dumbbut = input("]")
            if dumbbut in allcards:
                card31 = dumbbut
                allcards = remove_cards_from_deck(allcards, card31)
                dum_tab.seats[3].displaycard1 = common.displayhand(card31)
            else:
                #random card will be given at each iteration
                dum_tab.seats[3].displaycard1 = '[]'
            display.print_a_dummy_table(dum_tab)
            print(" ")
            print("enter seat3 card2:")
            dumbbut = input("]")
            if dumbbut in allcards:
                card32 = dumbbut
                allcards = remove_cards_from_deck(allcards, card32)
                dum_tab.seats[3].displaycard2 = common.displayhand(card32)
            else:
                #random card will be given at each iteration
                dum_tab.seats[3].displaycard2 = '[]'
            display.print_a_dummy_table(dum_tab)     
        else:
            #clear cards as folded
            card31 = "  "
            card32 = "  "

        #seat4 hole cards
        if stack4 > 0:
            print(" ")
            print("enter seat4 card1:")
            dumbbut = input("]")
            if dumbbut in allcards:
                card41 = dumbbut
                allcards = remove_cards_from_deck(allcards, card41)
                dum_tab.seats[4].displaycard1 = common.displayhand(card41)
            else:
                #random card will be given at each iteration
                dum_tab.seats[4].displaycard1 = '[]'
            display.print_a_dummy_table(dum_tab)
            print(" ")
            print("enter seat4 card2:")
            dumbbut = input("]")
            if dumbbut in allcards:
                card42 = dumbbut
                allcards = remove_cards_from_deck(allcards, card42)
                dum_tab.seats[4].displaycard2 = common.displayhand(card42)
            else:
                #random card will be given at each iteration
                dum_tab.seats[4].displaycard2 = '[]'
            display.print_a_dummy_table(dum_tab)    
        else:
            #clear cards as folded
            card41 = "  "
            card42 = "  "

        #seat4 hole cards
        if stack5 > 0:
            print(" ")
            print("enter seat5 card1:")
            dumbbut = input("]")
            if dumbbut in allcards:
                card51 = dumbbut
                allcards = remove_cards_from_deck(allcards, card51)
                dum_tab.seats[5].displaycard1 = common.displayhand(card51)
            else:
                #random card will be given at each iteration
                dum_tab.seats[5].displaycard1 = '[]'
            display.print_a_dummy_table(dum_tab)
            print(" ")
            print("enter seat5 card2:")
            dumbbut = input("]")
            if dumbbut in allcards:
                card52 = dumbbut
                allcards = remove_cards_from_deck(allcards, card52)
                dum_tab.seats[5].displaycard2 = common.displayhand(card52)
            else:
                #random card will be given at each iteration
                dum_tab.seats[5].displaycard2 = '[]'
            display.print_a_dummy_table(dum_tab)    
        else:
            #clear cards as folded
            card51 = "  "
            card52 = "  "

        #print(" ")
        #print("Is this the correct setup? y/n")
        answers = ['0', '2', '2.5', '3', '3.5']
        answer = ""
        while answer not in answers:
            display.print_a_dummy_table(dum_tab)
            print(" ")
            print("Select open size: [0, 2, 2.5 , 3 , 3.5]")
            answer = input("]")
        if answer in answers:
            settings.huanalyzer_open_size = answer
            #continue analysis
            analysed_seat0 = AnalysedSeat(card01, card02, 'D', stack0)
            analysed_seat1 = AnalysedSeat(card11, card12, ' ', stack1)
            analysed_seat2 = AnalysedSeat(card21, card22, ' ', stack2)
            analysed_seat3 = AnalysedSeat(card31, card32, ' ', stack3)
            analysed_seat4 = AnalysedSeat(card41, card42, ' ', stack4)
            analysed_seat5 = AnalysedSeat(card51, card52, ' ', stack5)
            analysed_table = AnalysedTable(analysed_seat0, analysed_seat1, analysed_seat2, analysed_seat3, analysed_seat4, analysed_seat5, pot, board, bigblind, starting_point)
            an = Analyser(analysed_table) #init start condition
            an.analyseHand()
            ###########################start
            
            big_blinds_value0 = settings.bbv0 
            big_blinds_value1 = settings.bbv1
            big_blinds_value2 = settings.bbv2 
            big_blinds_value3 = settings.bbv3 
            big_blinds_value4 = settings.bbv4 
            big_blinds_value5 = settings.bbv5 


            #line0
            #display.print_a_dummy_table(dum_tab)
            #line13

            #print(" ")
            #dumb = input("[end report]")
            return 0
        else:
            pass
    else:
        print(" ")
        print("less than 2 bots have stacks")
        dumb = input("]")
        return 0
            
        
