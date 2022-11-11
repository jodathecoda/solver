#copyright (c) 2019
#jodathecoda@yahoo.com

import random
from random import randint
import settings
import seat
from random import shuffle
import pokerface

class Table:
    def __init__(self, list_players, game_type):
        self.seats=[]
        self.stack_cards=[]
        suits = [settings.spade, settings.heart, settings.diamond, settings.club, ']']
        cardz = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A', '[']
        dealer_button = randint(0,5)
        self.board = ""
        self.displayboard = "          "
        self.pot = 0
        self.displaypot = 0
        for l in list_players:
            s = seat.Seat(game_type)
            s.name = l
            s.available = False
            if s.name == settings.hero:
                pass
            self.seats.append(s)
        while len(self.seats) < 6:
            s = seat.Seat(game_type)
            s.empty()
            self.seats.append(s)
        self.seats[dealer_button].button = settings.image_db

    def seats_available(self):
        sa = 0
        for s in self.seats:
            if s.available:
                sa +=1
        return sa

class DummyTable:
    def __init__(self):
        self.seats=[]
        self.stack_cards=[]
        self.pot = 0
        self.displaypot = 0
        self.displayboard = ""
        self.starting_point = "n"
        self.bigblind = 0
        

class AnalysisTable:
    def __init__(self, an_table):
        self.seats=[]
        self.stack_cards=[]
        suits = [settings.spade, settings.heart, settings.diamond, settings.club, ']']
        cardz = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A', '[']
        #dealer_button = button_number
        self.setup_board = an_table.board
        self.bigblind = an_table.bigblind
        self.board = ""
        self.displayboard = "          "
        self.pot = an_table.pot
        self.predefined_pot = an_table.pot
        self.displaypot = str(self.pot)
        self.starting_point = an_table.starting_point
        sit0 = seat.AnalysisSeat(an_table.seats[0])
        sit1 = seat.AnalysisSeat(an_table.seats[1])
        sit2 = seat.AnalysisSeat(an_table.seats[2])
        sit3 = seat.AnalysisSeat(an_table.seats[3])
        sit4 = seat.AnalysisSeat(an_table.seats[4])
        sit5 = seat.AnalysisSeat(an_table.seats[5])
        self.seats.append(sit0)
        self.seats.append(sit1)
        self.seats.append(sit2)
        self.seats.append(sit3)
        self.seats.append(sit4)
        self.seats.append(sit5)
        
    def dont_randomize_seats(self):
        list_of_players = []
        for f in settings.allfishes:
            list_of_players.append(f)
        random.shuffle(list_of_players)
        for s in self.seats:
            #analyser evaluates only preflop ranges,
            #so postflop the fish will be the same
            #redfish and blackfish had 30 aggression,
            #so practically they play the same postflop
            if settings.redfish_seated == 0:
                s.name = "redfish"
                settings.redfish_seated = 1
            else:
                s.name = "blackfish"
                #clear flag for next iteration
                settings.redfish_seated = 0

            if not settings.list_faces:
                p = pokerface.Pokerface()
                settings.list_faces = p.faces
            s.face = settings.list_faces.pop()
            s.paggression = 0 #preflop aggression
            s.faggression = 0 #flop aggression
            s.taggression = 0 #turn aggression
            s.raggression = 0 #river aggression
            s.range_ug_open = [] #ug open
            s.range_hj_open = [] #hj open
            s.range_co_open = [] #co open
            s.range_db_open = [] #dealer open
            s.range_sb_open = [] #sb open
            s.range_hd_open = [] #heads up dealer open
            s.range_hb_defend = [] #heads up big blind defend
            s.range_defend_vs_ug_ip = [] #defend range vs ug opener when we have position on him
            s.range_defend_vs_ug_op = [] #defend range vs ug opener when he has position on us
            s.range_defend_vs_hj_ip = [] #defend range vs hijack opener in position
            s.range_defend_vs_hj_op = [] #defend range vs hijack opener out of position
            s.range_defend_vs_co_ip = [] #defend range vs cutoff opener in position
            s.range_defend_vs_co_op = [] #defend range vs cutoff opener out of position
            s.range_defend_vs_db_op = [] #defend range vs dealer button always out of position
            s.range_defend_vs_sb_ip = [] #defend range vs small blind always in position
            s.range_under10bb_push_vs_1 = [] #under 10 bb push vs 1 villain
            s.range_under10bb_push_vs_2 = [] #under 10 bb push vs 2 villains
            s.range_under10bb_push_vs_more = [] #under 10 bb push vs bunch of villains
            s.range_call_vs_under10bb_push_0_left_behind = [] #call a push from player who has under 10bb and pushes, no one left after you
            s.range_call_vs_under10bb_push_1_left_behind = [] #call a push from player who has under 10bb and pushes, one left after you to act
            s.range_call_vs_under10bb_push_more_left_behind = []
            s.threshold_flop_open_vs_one = 0.0
            s.threshold_flop_bluff_vs_one = 0.0
            s.threshold_flop_call_vs_one = 0.0
            s.threshold_flop_raise_vs_one = 0.0
            s.threshold_flop_call3bet_vs_one = 0.0
            s.threshold_flop_raise4bet_vs_one = 0.0
            s.threshold_flop_shove = 0.0
            #flop threshold values vs more
            s.threshold_flop_open_vs_more = 0.0
            s.threshold_flop_call_vs_more = 0.0
            s.threshold_flop_raise_vs_more = 0.0
            s.threshold_flop_call3bet_vs_more = 0.0
            s.threshold_flop_raise4bet_vs_more = 0.0
            #turn threshold values vs 1
            s.threshold_turn_open_vs_one = 0.0
            s.threshold_turn_bluff_vs_one = 0.0
            s.threshold_turn_call_vs_one = 0.0
            s.threshold_turn_raise_vs_one = 0.0
            s.threshold_turn_call3bet_vs_one = 0.0
            s.threshold_turn_raise4bet_vs_one = 0.0
            s.threshold_turn_shove = 0.0
            #turn threshold values vs more
            s.threshold_turn_open_vs_more = 0.0
            s.threshold_turn_call_vs_more = 0.0
            s.threshold_turn_raise_vs_more = 0.0
            s.threshold_turn_call3bet_vs_more = 0.0
            s.threshold_turn_raise4bet_vs_more = 0.0
            #river threshold values vs 1
            s.threshold_river_open_vs_one = 0.0
            s.threshold_river_bluff_vs_one = 0.0
            s.threshold_river_call_vs_one = 0.0
            s.threshold_river_raise_vs_one = 0.0
            s.threshold_river_call3bet_vs_one = 0.0
            s.threshold_river_raise4bet_vs_one = 0.0
            s.threshold_river_shove = 0.0
            #river threshold values vs more
            s.threshold_river_open_vs_more = 0.0
            s.threshold_river_call_vs_more = 0.0
            s.threshold_river_raise_vs_more = 0.0
            s.threshold_river_call3bet_vs_more = 0.0
            s.threshold_river_raise4bet_vs_more = 0.0
            #acted on each street to know if you have to act when s.bet == biggest_bet
            s.acted_preflop = 0
            s.acted_flop = 0
            s.acted_turn = 0
            s.acted_river = 0

    def randomize_seats(self):
        list_of_players = []
        for f in settings.allfishes:
            list_of_players.append(f)
        random.shuffle(list_of_players)
        for s in self.seats:
            s.name = list_of_players.pop()
            if not settings.list_faces:
                p = pokerface.Pokerface()
                settings.list_faces = p.faces
            s.face = settings.list_faces.pop()
            s.paggression = 0 #preflop aggression
            s.faggression = 0 #flop aggression
            s.taggression = 0 #turn aggression
            s.raggression = 0 #river aggression
            s.range_ug_open = [] #ug open
            s.range_hj_open = [] #hj open
            s.range_co_open = [] #co open
            s.range_db_open = [] #dealer open
            s.range_sb_open = [] #sb open
            s.range_hd_open = [] #heads up dealer open
            s.range_hb_defend = [] #heads up big blind defend
            s.range_defend_vs_ug_ip = [] #defend range vs ug opener when we have position on him
            s.range_defend_vs_ug_op = [] #defend range vs ug opener when he has position on us
            s.range_defend_vs_hj_ip = [] #defend range vs hijack opener in position
            s.range_defend_vs_hj_op = [] #defend range vs hijack opener out of position
            s.range_defend_vs_co_ip = [] #defend range vs cutoff opener in position
            s.range_defend_vs_co_op = [] #defend range vs cutoff opener out of position
            s.range_defend_vs_db_op = [] #defend range vs dealer button always out of position
            s.range_defend_vs_sb_ip = [] #defend range vs small blind always in position
            s.range_under10bb_push_vs_1 = [] #under 10 bb push vs 1 villain
            s.range_under10bb_push_vs_2 = [] #under 10 bb push vs 2 villains
            s.range_under10bb_push_vs_more = [] #under 10 bb push vs bunch of villains
            s.range_call_vs_under10bb_push_0_left_behind = [] #call a push from player who has under 10bb and pushes, no one left after you
            s.range_call_vs_under10bb_push_1_left_behind = [] #call a push from player who has under 10bb and pushes, one left after you to act
            s.range_call_vs_under10bb_push_more_left_behind = []
            s.threshold_flop_open_vs_one = 0.0
            s.threshold_flop_bluff_vs_one = 0.0
            s.threshold_flop_call_vs_one = 0.0
            s.threshold_flop_raise_vs_one = 0.0
            s.threshold_flop_call3bet_vs_one = 0.0
            s.threshold_flop_raise4bet_vs_one = 0.0
            s.threshold_flop_shove = 0.0
            #flop threshold values vs more
            s.threshold_flop_open_vs_more = 0.0
            s.threshold_flop_call_vs_more = 0.0
            s.threshold_flop_raise_vs_more = 0.0
            s.threshold_flop_call3bet_vs_more = 0.0
            s.threshold_flop_raise4bet_vs_more = 0.0
            #turn threshold values vs 1
            s.threshold_turn_open_vs_one = 0.0
            s.threshold_turn_bluff_vs_one = 0.0
            s.threshold_turn_call_vs_one = 0.0
            s.threshold_turn_raise_vs_one = 0.0
            s.threshold_turn_call3bet_vs_one = 0.0
            s.threshold_turn_raise4bet_vs_one = 0.0
            s.threshold_turn_shove = 0.0
            #turn threshold values vs more
            s.threshold_turn_open_vs_more = 0.0
            s.threshold_turn_call_vs_more = 0.0
            s.threshold_turn_raise_vs_more = 0.0
            s.threshold_turn_call3bet_vs_more = 0.0
            s.threshold_turn_raise4bet_vs_more = 0.0
            #river threshold values vs 1
            s.threshold_river_open_vs_one = 0.0
            s.threshold_river_bluff_vs_one = 0.0
            s.threshold_river_call_vs_one = 0.0
            s.threshold_river_raise_vs_one = 0.0
            s.threshold_river_call3bet_vs_one = 0.0
            s.threshold_river_raise4bet_vs_one = 0.0
            s.threshold_river_shove = 0.0
            #river threshold values vs more
            s.threshold_river_open_vs_more = 0.0
            s.threshold_river_call_vs_more = 0.0
            s.threshold_river_raise_vs_more = 0.0
            s.threshold_river_call3bet_vs_more = 0.0
            s.threshold_river_raise4bet_vs_more = 0.0
            #acted on each street to know if you have to act when s.bet == biggest_bet
            s.acted_preflop = 0
            s.acted_flop = 0
            s.acted_turn = 0
            s.acted_river = 0

    def seats_available(self):
        sa = 0
        for s in self.seats:
            if s.available:
                sa +=1
        return sa


