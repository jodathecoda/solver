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
import formulas
import bots
import display

empty_list = []

display_board_offset0  = "          "
display_board_offset39 = "          "
display_board_offset52 = "          "
display_board_offset65 = "          "

handlog = ""
backcard = '[]'

global cwd
cwd = os.getcwd()

BLANK = " "
BLANKCELL = '   '

class Tournament:
    def __init__(self,num, game_type):
        if settings.hero != 'hero':
            self.starting_players = num-1
        else:
            self.starting_players = num
        self.left_players = num
        self.iterations_to_next_level = settings.iterations_to_next_level
        settings.current_iterations_to_next_level = self.iterations_to_next_level
        self.iterations = 0
        settings.current_iterations = self.iterations
        self.smallblind = settings.smallblind
        self.ante = settings.ante
        self.tables=[]
        self.game_type = game_type
        if self.game_type == 'c':
            self.end_condition = settings.end_condition
        else:
            self.end_condition = 1
        
        if self.game_type == 't':
            self.iterations_to_next_level = 20*settings.iterations_to_next_level #currently this means 200
        if self.game_type == 's':
            #spins are a little faster
            self.iterations_to_next_level = settings.iterations_to_next_level - 1

        settings.current_iterations_to_next_level = self.iterations_to_next_level

    def start(self):   
        settings.last6 = []
        settings.last5 = []
        settings.last4 = []
        settings.last3 = []
        settings.last2 = []
        shuff_players = settings.allfishes
        list_players = []
        random.shuffle(shuff_players)
        for c in range(0,self.starting_players):
            list_players.append(shuff_players[c])      
        if settings.hero != 'hero':
            list_players.append(settings.hero)
        random.shuffle(list_players)
        settings.current_game = self.game_type
        settings.participants = list_players
        if len((list_players)) == 54:
            t = table.Table(list_players[0:6], self.game_type)
            self.tables.append(t)
            t = table.Table(list_players[6:12], self.game_type)
            self.tables.append(t)
            t = table.Table(list_players[12:18], self.game_type)
            self.tables.append(t)
            t = table.Table(list_players[18:24], self.game_type)
            self.tables.append(t)
            t = table.Table(list_players[24:30], self.game_type)
            self.tables.append(t)
            t = table.Table(list_players[30:36], self.game_type)
            self.tables.append(t)
            t = table.Table(list_players[36:42], self.game_type)
            self.tables.append(t)
            t = table.Table(list_players[42:48], self.game_type)
            self.tables.append(t)
            t = table.Table(list_players[48:54], self.game_type)
            self.tables.append(t)
        else:  #one table  
            t = table.Table(list_players, self.game_type)
            self.tables.append(t)

        for t in self.tables:
            for s in t.seats:
                if s.name in settings.allfishes:
                    #always get aggression from files
                    settings.pokerpool.update_fish(s)

    def take_ante(self, table):
        t = table
        pot = 0
        for s in t.seats:
            if not s.available:
                if s.stack <= self.ante:
                    s.bet = s.stack
                    pot += s.stack
                    s.stack = 0
                else:
                    s.bet = self.ante
                    s.stack -= self.ante
                    pot += self.ante
                if settings.hand_history:
                    common.update_total_pot(t)
                    hand_history_line = s.name + " post " + str(s.bet) + "\n"
                    settings.imported_list_preflop.append(hand_history_line)
        return pot

    def deal_card(self, table, cardplace, cardnumber):
        card = "  "
        if settings.dealer_bot:
            card = table.stack_cards.pop()
        else:
            done = 1
            while(done):
                settings.print_logo()
                if settings.view < 4:
                    display.display_tables(table, self.game_type, self.smallblind, self.ante, self.tables)
                print(" ")
                card = input("deal for " + cardplace + " card" + str(cardnumber) + ":")
                if card in table.stack_cards:
                    table.stack_cards.remove(card)
                    done = 0
                    print("card dealed")
                    time.sleep(1)
                else:
                    print("not valid, try again")
                    time.sleep(1)
        return card


    def startHand(self, table):
        global handlog
        global threebet
        global cwd
        
        settings.threebet = 0 # clear all previous reraises
        settings.total_pot = 0
        handlog = " "
        t = table
        settings.hand_history_list = []
        settings.imported_list_preflop = []
        if self.game_type == 't' and settings.hero != 'hero':
            hero_is_on_the_table = 0
            #if player is logged in to play, other tables at tournament will be played fast speed so he does not wait
            for se in t.seats:
                if se.name == settings.hero:
                    hero_is_on_the_table = 1
            
            if hero_is_on_the_table == 0:
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
            else:
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

        if settings.followfish in settings.allfishes and settings.wsop_followfish:
            follow_fish_is_on_the_table = 0
            for se in t.seats:
                if se.name == settings.followfish:
                    follow_fish_is_on_the_table = 1

            if follow_fish_is_on_the_table == 1:
                settings.view = 2
                settings.bot_time_to_act = settings.selected_bot_time_to_act
                settings.bot_time_to_act_preflop = settings.selected_bot_time_to_act_preflop
                settings.bot_time_to_act_flop = settings.selected_bot_time_to_act_flop
                settings.bot_time_to_act_turn = settings.selected_bot_time_to_act_turn
                settings.bot_time_to_act_river = settings.selected_bot_time_to_act_river
                settings.time_to_wait_board = settings.selected_time_to_wait_board
                settings.debug_ranges = 1
                settings.debug_postflop = 1
                settings.debug_ranges_stop_point = 0
                settings.debug_postflop_stop_point = 0
            else:
                #revert back if changed settings
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

        #clear bets as it is new hand clear cards
        for s in t.seats:
            s.want_to_push = 0
            s.stack = common.roundbet(s.stack)
            s.equx_flop = 0.0
            s.equx_turn = 0.0
            s.equx_river = 0.0
            s.bet = 0
            s.oldbet = 0
            s.card1 = "  "
            s.card2 = "  "
            s.floatandsteal = 0
            s.vbetflag = 0
            s.cbetflag = 0
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
            if s.stack < 0:
                print("]error stack less than zero")
                dumb = input("]")
            range_type_as_digit = 2
        #clear pot
        t.pot = 0
        start_sum = 0
        endsum = 0

        #PREFLOP
        antes = common.countNotFoldedYet(t)*self.ante
        cur_pot = self.smallblind*3 + antes
        for s in t.seats:
            s.stp = common.roundbet(s.stack/cur_pot)
            s.learning_hand_start_stack = (s.stack / (self.smallblind * 2))
        # take ante from all players
        if self.game_type == 't' and settings.ante > 0:
            t.pot = self.take_ante(t)
        else:
            self.ante = 0
        handlog += "start sum\n"
        start_sum = common.checksum(t)
        # take blinds
        num_p = common.count_players_on_table(t)
        if num_p == 0:
            print("no players on table!")
            time.sleep(2)
        elif num_p == 1:
            print("only one player on table!")
            time.sleep(2)
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
        #t.pot fix bug
        if self.ante:
            t.pot -= 2*self.ante #one for big blind and one for small blind

        display.display_tables(t, self.game_type, self.smallblind, self.ante, self.tables)
        deck = ['as', 'ks', 'qs', 'js', 'ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', \
                'ah', 'kh', 'qh', 'jh', 'th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', \
                'ad', 'kd', 'qd', 'jd', 'td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', \
                'ac', 'kc', 'qc', 'jc', 'tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c' ]
        random.shuffle(deck)
        table.stack_cards = []
        for cardz in deck:
            table.stack_cards.append(cardz)

        for s in t.seats:
            if not s.available:
                #learning position taken off learning so we can use it in postflop to estimate ranges
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

                s.card1 = self.deal_card(t, s.learning_position, 1)
                s.card2 = self.deal_card(t, s.learning_position, 2)
                dealt_hand = s.card1 + s.card2
                
                
                #learning:


        display.display_tables(t, self.game_type, self.smallblind, self.ante, self.tables)

        #hand history
        if settings.hand_history:
            hand_history_line = "PokerSea Hand #" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ":  "
            settings.hand_history_list.append(hand_history_line)
            if self.game_type == 'c':
                hand_history_line = "Hold'em No Limit ($" + str(self.smallblind) + "/$" + str(self.smallblind*2) + " USD) - " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            else:
                hand_history_line = "Tournament #" + datetime.datetime.now().strftime("%Y%m%d%H%M") + ", $" + str(self.smallblind) + "+ $" + str(self.smallblind) + " USD Hold'em No Limit - Level (" + str(self.smallblind) + "/" + str(self.smallblind*2) + ") - " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            settings.hand_history_list.append(hand_history_line)
            hand_history_line = "Table Pokersea "
            if self.game_type == 'h':
                hand_history_line += "2-max Seat#"
            elif self.game_type == 's':
                hand_history_line += "3-max Seat#"
            elif self.game_type == 'c':
                hand_history_line += "6-max Seat#"
            else:# for recognizing tourney from cash in hand reader
                hand_history_line += "8-max Seat#"
                
            for counter in range(0,5):
                if t.seats[counter].button == settings.image_db:
                    hand_history_line += str(counter) + " is button\n"
                    settings.hand_history_list.append(hand_history_line)

            count_s = 0
            for count_s in range(0,6):
                if not t.seats[count_s].available:
                    hand_history_line = "Seat " + str(count_s) + ": " + t.seats[count_s].name + " (" + str(t.seats[count_s].stack) + " in chips)\n"
                    settings.hand_history_list.append(hand_history_line)

            hand_history_line = "*** HOLE CARDS ***\n"
            settings.hand_history_list.append(hand_history_line)

            for s in t.seats:
                if not s.available:
                    hand_history_line = "Dealt to " + s.name + " [" + s.card1 + " " + s.card2 + "]" + "\n"
                    settings.hand_history_list.append(hand_history_line)
            
            for cure_line in settings.hand_history_list:
                settings.hand_history_buffer.add_line(cure_line)

            hand_history_line = "*** PREFLOP ***\n"
            settings.hand_history_buffer.add_line(hand_history_line)
            for linz in settings.imported_list_preflop:
                settings.hand_history_buffer.add_line(linz)
                

        #preflop
        if settings.hero == 'you':
            found_you = 0
            for tt in self.tables:
                for ss in tt.seats:
                    if ss.name == 'you':
                        found_you = 1
            if found_you:
                settings.cards_faceup = 0
            else:
                settings.cards_faceup = 1
                settings.view = settings.oldview
                settings.bot_time_to_act = settings.selected_bot_time_to_act
                settings.bot_time_to_act_preflop = settings.selected_bot_time_to_act_preflop
                settings.bot_time_to_act_flop = settings.selected_bot_time_to_act_flop
                settings.bot_time_to_act_turn = settings.selected_bot_time_to_act_turn
                settings.bot_time_to_act_river = settings.selected_bot_time_to_act_river
                settings.time_to_wait_board = settings.selected_time_to_wait_board
                settings.learning = 0
                settings.debug_ranges = 1
                settings.debug_postflop = 1
                settings.debug_ranges_stop_point = 0
                settings.debug_postflop_stop_point = 0


        handlog += "before blinds -> after blinds\n"
        temp_sum = common.checksum(t)
        
        for s in t.seats:
            if s.available == 0:
                s.preorbits += 1
        common.playHandpreflop(t, self.game_type, self.smallblind, self.ante, self.tables)
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
            
            t.board += self.deal_card(t, 'flop', 1)
            t.board += self.deal_card(t, 'flop', 2)
            t.board += self.deal_card(t, 'flop', 3)
            #hand history
            if settings.hand_history:
                hand_history_line = "*** FLOP *** [" + t.board + "]\n"
                settings.hand_history_buffer.add_line(hand_history_line)

            for s in t.seats:
                if s.available == 0:
                    s.floporbits += 1
            common.playHandpostflop(t, self.game_type, self.smallblind, self.ante, self.tables)
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
            
            t.board += self.deal_card(t, 'turn', 1)
            #hand history
            if settings.hand_history:
                hand_history_line = "*** TURN *** [" + t.board + "]\n"
                settings.hand_history_buffer.add_line(hand_history_line)

            common.playHandpostflop(t, self.game_type, self.smallblind, self.ante, self.tables)

        if common.check_hand_over_folds(t):
            self.clear_hand(t)
        else:
            #river
            handlog += "river\n"
            temp_sum = common.checksum(t)
            
            t.board += self.deal_card(t, 'river', 1)
            #hand history
            if settings.hand_history:
                hand_history_line = "*** RIVER *** [" + t.board + "]\n"
                settings.hand_history_buffer.add_line(hand_history_line)

            common.playHandpostflop(t, self.game_type, self.smallblind, self.ante, self.tables)

            if not settings.cards_faceup:
                settings.toggle_cards_faceup = 1
                settings.cards_faceup = 1
                display.display_tables(t, self.game_type, self.smallblind, self.ante, self.tables)
            else:
                pass

            if settings.toggle_cards_faceup:
                settings.cards_faceup = 0
                settings.toggle_cards_faceup = 0

            
        if common.check_hand_over_folds(t):
            self.clear_hand(t)
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
            self.clear_hand(t)
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

    def clear_hand(self, table):
        for s in table.seats:
            if s.stack == 0:
                s.empty()
        table.board = ""

    def run(self):
        check = 0
        while self.end_condition < self.count_players_final_table():
            tablez = 0
            for t in self.tables:
                tablez += 1
            if tablez == 1:
                november_niners = self.count_players_final_table()
                #final table
                if november_niners == 6:
                    if not settings.last6:
                        for s in self.tables[0].seats:
                            settings.last6.append(s.name)
                elif november_niners == 5:
                    if not settings.last5:
                        for s in self.tables[0].seats:
                            settings.last5.append(s.name)
                elif november_niners == 4:
                    if not settings.last4:
                        for s in self.tables[0].seats:
                            settings.last4.append(s.name)
                elif november_niners == 3:
                    if not settings.last3:
                        for s in self.tables[0].seats:
                            settings.last3.append(s.name)
                elif november_niners == 2:
                    if not settings.last2:
                        for s in self.tables[0].seats:
                            settings.last2.append(s.name)
                else:
                    print("error in november niners count:" + str(november_niners))
                    dumb = input("]")

                if settings.last5:
                    for s in settings.last5:
                        if s[0] == " ":
                            settings.last5.remove(s)

                if settings.last4:
                    for s in settings.last4:
                        if s[0] == " ":
                            settings.last4.remove(s)

                if settings.last3:
                    for s in settings.last3:
                        if s[0] == " ":
                            settings.last3.remove(s)

                if settings.last2:
                    for s in settings.last2:
                        if s[0] == " ":
                            settings.last2.remove(s)

            #set buttons
            for t in self.tables:
                cur_db = common.find_button(t)
                next_av_pos = common.find_next_occupied_chair(t, cur_db)
                #set new button
                if not t.seats[next_av_pos].available:
                    #clear all buttons
                    for s in t.seats:
                        s.button = " "
                    t.seats[next_av_pos].button = settings.image_db
                else:
                    nextnext_av_pos = common.find_next_occupied_chair(t, next_av_pos)
                    if not t.seats[nextnext_av_pos].available:
                        #clear all buttons
                        for s in t.seats:
                            s.button = " "
                        t.seats[nextnext_av_pos].button = settings.image_db
                    else:
                        print("error in asigning dealer button")

            player_out = [9,9] #[table, player]
            seats_counter = 0
            for t in self.tables:
                seats_counter = common.count_players_on_table(t)
                if seats_counter < 2:
                    pass
                else:
                    self.startHand(t)
                    if self.game_type != 'c':
                        if settings.nash_push_fold:
                            settings.nash_fish0 = t.seats[0].name
                            settings.nash_fish1 = t.seats[1].name
                            
                        self.iterations += 1
                        settings.current_iterations = self.iterations
                        if self.iterations == self.iterations_to_next_level:
                            self.iterations = 0
                            settings.current_iterations = self.iterations
                            if self.game_type == 't':
                                self.iterations_to_next_level = len(self.tables) * 20  + 11 - len(self.tables)# for mtt twenty hands per table
                                settings.current_iterations_to_next_level = self.iterations_to_next_level
                                self.smallblind *= 2
                                self.ante *= 2
                            elif self.game_type == 's':
                                #spin and go slower
                                self.smallblind = common.roundbet(self.smallblind + self.smallblind/2)
                            else:
                                self.smallblind *= 2
                            if settings.view == 1 or settings.view == 2:
                                print("blinds level: " + str(self.smallblind) + "/" + str(self.smallblind*2))
                                if settings.debug_postflop_stop_point:
                                    dumb = input("]")
                                else:
                                    time.sleep(2)
                            if settings.view > 3:
                                print("bl: " + str(self.smallblind) + "/" + str(self.smallblind*2))
                                if settings.debug_postflop_stop_point:
                                    dumb = input("]")
                                else:
                                    time.sleep(2)
            self.rearrange_tables()
        theleaderboard = []
        checksum = 0
        for s in self.tables[0].seats:
            if s.stack:
                theleaderboard.append(s.name)

        if settings.last2:
            for l in settings.last2:
                if l != theleaderboard[0]:
                    theleaderboard.append(l)

        if settings.last3:
            for l in settings.last3:
                if l not in theleaderboard:
                    theleaderboard.append(l)

        if settings.last4:
            for l in settings.last4:
                if l not in theleaderboard:
                    theleaderboard.append(l)

        if settings.last5:
            for l in settings.last5:
                if l not in theleaderboard:
                    theleaderboard.append(l)

        if settings.last6:
            for l in settings.last6:
                if l not in theleaderboard:
                    theleaderboard.append(l)

        #game is over, you can charge participants with byuin
        if settings.nash_push_fold:
            if theleaderboard[0] == "you":
                settings.nash_you += 1
            elif theleaderboard[1] == "you":
                settings.nash_villain += 1
            elif theleaderboard[0] == settings.nash_fish0:
                settings.nash_0 += 1
            else:
                settings.nash_1 += 1
        else:
            for fishname in settings.participants:
                if fishname in settings.allfishes:
                    huvalue = 0.0
                    spvalue = 0.0
                    cavalue = 0.0
                    mtvalue = 0.0
                    filename = cwd + "/fishes/" + fishname + "/bankroll.dat"
                    try:
                        with open(filename, "r+") as f:
                            lines = f.read().splitlines()
                            huvalue = float(lines[0].replace('\U00002013', '-'))
                            spvalue = float(lines[1].replace('\U00002013', '-'))
                            cavalue = float(lines[2].replace('\U00002013', '-'))
                            mtvalue = float(lines[3].replace('\U00002013', '-'))
                        f.close()

                        if self.game_type == 'h':
                            if settings.nash_push_fold:
                                pass                            
                            else:
                                huvalue -= 1.0
                        elif self.game_type == 's':
                            spvalue -= 1.0
                        elif self.game_type == 'c':
                            cavalue -= round(settings.starting_stacks + settings.starting_stacks/3)
                        elif self.game_type == 't':
                            mtvalue -= 1.0
                        else:
                            print("unknown game type")
                            dumb = input("]")
                    except:
                        print("no such file 2" + filename)
                        dumb = input("]")
                    try:
                        with open(filename, "r+") as f:
                            if huvalue != 0.0:
                                f.write(str(huvalue) + "\n")
                            else:
                                f.write("0.0\n")
                            if spvalue != 0.0:
                                f.write(str(spvalue) + "\n")
                            else:
                                f.write("0.0\n")
                            if cavalue != 0.0:
                                f.write(str(cavalue) + "\n")
                            else:
                                f.write("0.0\n")
                            if mtvalue != 0.0:
                                f.write(str(mtvalue) + "\n")
                            else:
                                f.write("0.0\n")
                        f.close()
                    except:
                        print("no such file 2.5" + filename)
                        dumb = input("]")
                    
            #if this is a cash game?
            if self.game_type == 'c':
                for s in self.tables[0].seats:
                    if (s.stack > 0):
                        s.stack = common.roundbet(s.stack)
                        if s.name == settings.hero:
                            pass
                        else:
                            filename = cwd + "/fishes/" + s.name + "/bankroll.dat"
                            huvalue = 0.0
                            spvalue = 0.0
                            cavalue = 0.0
                            mtvalue = 0.0
                            try:
                                with open(filename, "r") as f:
                                    lines = f.read().splitlines()
                                    huvalue = float(lines[0].replace('\U00002013', '-'))
                                    spvalue = float(lines[1].replace('\U00002013', '-'))
                                    cavalue = float(lines[2].replace('\U00002013', '-'))
                                    mtvalue = float(lines[3].replace('\U00002013', '-'))
                                f.close()
                            except:
                                print("no such file 7" + filename)
                                dumb = input("]")
                            try:
                                with open(filename, "w") as f:
                                    cavalue += s.stack
                                    f.write(str(huvalue) + "\n")
                                    f.write(str(spvalue) + "\n")
                                    f.write(str(cavalue) + "\n")
                                    f.write(str(mtvalue) + "\n")
                                f.close()
                            except:
                                print("no such file 7" + filename)
                                dumb = input("]")
                                                
                            
                if settings.view == 1 or settings.view == 2:
                    print("table is closed!")
                    time.sleep(3)
            elif self.game_type == 't':
                if settings.view == 1 or settings.view == 2:
                    print("the winner is: " + theleaderboard[0])
                    time.sleep(3)
                while "    " in theleaderboard:
                    theleaderboard.remove("    ")
                if len(theleaderboard) == 5:
                    settings.mttprize = [21,15,9,5,4]
                elif len(theleaderboard) == 4:
                    settings.mttprize = [22,16,10,6]
                elif len(theleaderboard) == 3:
                    settings.mttprize = [24,18,12]
                elif len(theleaderboard) == 2:
                    settings.mttprize = [30,24]
                elif len(theleaderboard) == 1:
                    settings.mttprize = [54]
                for count in range(len(theleaderboard)):
                    if theleaderboard[count] == settings.hero:
                        #fishname = theleaderboard[count]
                        #we have human player
                        pass
                    else:
                        fishname = theleaderboard[count]
                        filename = cwd + "/fishes/" + fishname + "/bankroll.dat"
                        try:
                            with open(filename, "r") as f:
                                lines = f.read().splitlines()
                                huvalue = float(lines[0].replace('\U00002013', '-'))
                                spvalue = float(lines[1].replace('\U00002013', '-'))
                                cavalue = float(lines[2].replace('\U00002013', '-'))
                                mtvalue = float(lines[3].replace('\U00002013', '-'))
                            f.close()
                        except:
                            print("no such file 11" + filename)
                            dumb = input("]")
                        mtvalue += settings.mttprize[count]
                        try:
                            with open(filename, "w") as f:
                                if huvalue != 0.0:
                                    f.write(str(huvalue) + "\n")
                                else:
                                    f.write("0.0\n")
                                if spvalue != 0.0:
                                    f.write(str(spvalue) + "\n")
                                else:
                                    f.write("0.0\n")
                                if cavalue != 0.0:
                                    f.write(str(cavalue) + "\n")
                                else:
                                    f.write("0.0\n")
                                if mtvalue != 0.0:
                                    f.write(str(mtvalue) + "\n")
                                else:
                                    f.write("0.0\n")
                            f.close()
                        except:
                            print("no such file 12" + filename)
                            dumb = input("]")
                settings.mttprize = [19,14,9,5,4,3] #reset back to normal for the next tourney


            elif self.game_type == 's':
                if settings.view == 1 or settings.view == 2:
                    print("the winner is: " + theleaderboard[0]) 
                    time.sleep(3)
                if theleaderboard[0] == settings.hero:
                    #fishname = theleaderboard[0]
                    #we have human player
                    pass
                else:
                    fishname = theleaderboard[0]
                    filename = cwd + "/fishes/" + fishname + "/bankroll.dat"
                    try:
                        with open(filename, "r") as f:
                            lines = f.read().splitlines()
                            huvalue = float(lines[0].replace('\U00002013', '-'))
                            spvalue = float(lines[1].replace('\U00002013', '-'))
                            cavalue = float(lines[2].replace('\U00002013', '-'))
                            mtvalue = float(lines[3].replace('\U00002013', '-'))
                        f.close()
                    except:
                        print("no such file 15" + filename)
                        dumb = input("]")
                    spvalue += settings.spinprize
                    try:
                        with open(filename, "w") as f:
                            if huvalue != 0.0:
                                f.write(str(huvalue) + "\n")
                            else:
                                f.write("0.0\n")
                            if spvalue != 0.0:
                                f.write(str(spvalue) + "\n")
                            else:
                                f.write("0.0\n")
                            if cavalue != 0.0:
                                f.write(str(cavalue) + "\n")
                            else:
                                f.write("0.0\n")
                            if mtvalue != 0.0:
                                f.write(str(mtvalue) + "\n")
                            else:
                                f.write("0.0\n")
                        f.close()
                    except:
                        print("no such file 16" + filename)
                        dumb = input("]")
                
            elif self.game_type == 'h' and settings.nash_push_fold == 0:
                if settings.view == 1 or settings.view == 2:
                    print("the winner is: " + theleaderboard[0])
                    time.sleep(5)            
                if theleaderboard[0] == settings.hero:
                    #fishname = theleaderboard[0]
                    #we have human player
                    pass
                else:
                    fishname = theleaderboard[0]
                    filename = cwd + "/fishes/" + fishname + "/bankroll.dat"
                    try:
                        with open(filename, "r") as f:
                            lines = f.read().splitlines()
                            huvalue = float(lines[0].replace('\U00002013', '-'))
                            spvalue = float(lines[1].replace('\U00002013', '-'))
                            cavalue = float(lines[2].replace('\U00002013', '-'))
                            mtvalue = float(lines[3].replace('\U00002013', '-'))
                        f.close()
                    except:
                        print("no such file 19" + filename)
                        dumb = input("]")
                    huvalue += settings.huprize
                    try:
                        with open(filename, "w") as f:
                            if huvalue != 0.0:
                                f.write(str(huvalue) + "\n")
                            else:
                                f.write("0.0\n")
                            if spvalue != 0.0:
                                f.write(str(spvalue) + "\n")
                            else:
                                f.write("0.0\n")
                            if cavalue != 0.0:
                                f.write(str(cavalue) + "\n")
                            else:
                                f.write("0.0\n")
                            if mtvalue != 0.0:
                                f.write(str(mtvalue) + "\n")
                            else:
                                f.write("0.0\n")
                        f.close()
                    except:
                        print("no such file 20" + filename)
                        dumb = input("]")
            else:
                #print("error in type of tournament for prizes")
                #nash heads up
                time.sleep(2)

        endsum = 0
        for s in t.seats:
            endsum += s.stack
        if settings.checksum:
            print("endsum: " + str(endsum))
   
    def count_chairs_without_last_table(self):
        available_seats = 0
        for i in range(0,len(self.tables)-1):
            available_seats += self.tables[i].seats_available()
        return available_seats

    def count_players_final_table(self):
        players_on_last_table = 0
        try:
            for s in self.tables[0].seats:
                if not s.available:
                    players_on_last_table +=1
        except:
            print("tournament aborts")
            print("zero players on last table")
            dumb = input("]")
            players_on_last_table = 0
        return players_on_last_table

    def count_players_last_table(self):
        players_on_last_table = 0
        for s in self.tables[-1].seats:
            if not s.available:
                players_on_last_table +=1
        return players_on_last_table

    def rearrange_tables(self):
        moving_players = []
        av_seats = self.count_chairs_without_last_table()
        av_players = self.count_players_last_table()
        if av_seats >= av_players:
            for s in self.tables[-1].seats:
                if not s.available:
                    moving_players.append(s)
            self.tables = self.tables[:-1]
            for t in range(0,len(self.tables)):
                for s in range(0,len(self.tables[t].seats)):
                    if self.tables[t].seats[s].available:
                        if moving_players:
                            for m in moving_players:
                                m.cbet = 0
                                m.vbet = 0
                                m.last3bets = 0
                                m.preorbits = 0.001
                                m.preallin = 0
                                m.prebigbet = 0 #counter if opens more than 5x and reraises more than 5x a.k.a. maniac
                                m.last5betscrazy = 0 # if he played normally but got crazy recently
                                m.floporbits = 0.001 # to prevent division by zero in displays
                                m.cbetflag = 0
                                m.vbetflag = 0
                                #clear stats as they are moving to new table
                            self.tables[t].seats[s] = moving_players.pop()
