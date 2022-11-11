#copyright (c) 2019
#jodathecoda@yahoo.com

import settings
import random
from random import randint
import pokerface

def displayhand(hand):
	cur_hand = hand
	vis_hand = cur_hand.replace('a', 'A')
	cur_hand = vis_hand
	vis_hand = cur_hand.replace('k', 'K')
	cur_hand = vis_hand
	vis_hand = cur_hand.replace('q', 'Q')
	cur_hand = vis_hand
	vis_hand = cur_hand.replace('j', 'J')
	cur_hand = vis_hand
	vis_hand = cur_hand.replace('t', 'T')
	cur_hand = vis_hand
	vis_hand = cur_hand.replace("s", settings.spade)
	cur_hand = vis_hand
	vis_hand = cur_hand.replace("d", settings.diamond)
	cur_hand = vis_hand
	vis_hand = cur_hand.replace("h", settings.heart)
	cur_hand = vis_hand
	vis_hand = cur_hand.replace("c", settings.club)
	return vis_hand

class Seat:
    def __init__(self, game_type):
        if not settings.list_faces:
            p = pokerface.Pokerface()
            settings.list_faces = p.faces
        self.face = settings.list_faces.pop()
        if game_type == 'h':
            if settings.nash_push_fold:
                self.stack = settings.nash_stack
            else:
                self.stack = round(settings.starting_stacks)
        elif game_type == 's':
            self.stack = round(settings.starting_stacks/3)
        elif game_type == 'c':
            self.stack = round(settings.starting_stacks + settings.starting_stacks/3)
        elif game_type == 't':
            self.stack = round(settings.starting_stacks*2)
        self.displaystack = "  "
        self.clock = " "
        self.name = " "
        self.sea = "blue sea"
        self.splitrange = "unknown"
        self.paggression = 0 #preflop aggression
        self.faggression = 0 #flop aggression
        self.taggression = 0 #turn aggression
        self.raggression = 0 #river aggression
        self.card1 = "  "
        self.card2 = "  "
        self.displaycard1 = "  "
        self.displaycard2 = "  "
        self.displaybet = "  "
        self.button = " "
        self.betting_lead = 0
        self.bet = 0
        self.last3bets = 0
        self.oldbet = 0
        self.want_to_push = 0
        self.showdown_result = 0.0
        self.available = False
        self.floatandsteal = 0
        self.vbetflag = 0 # this is for counting only 1 when multiple bets in one street
        self.cbetflag = 0 # the same for flop
        self.preorbits = 0.001 #this is for counting preflop orbits for VPIP for HUD
        self.preallin = 0 #counter if jamming every hand
        self.prebigbet = 0 #counter if opens more than 5x and reraises more than 5x a.k.a. maniac
        self.last5betscrazy = 0 #counter if played normally for some time but go crazy recently
        self.floporbits = 0.001 #this is for counting plays on flop for HUD 1 to prevent division by zero in display
        self.vbet = 0 #this is vpip / voluntary put money in pot stat/
        self.cbet = 0 # this is putting money in flop cbet ot donk bet
        self.equx_flop = 0.0
        self.equx_turn = 0.0
        self.equx_river = 0.0
        self.learning_suit = "no"
        self.learning_hand = ""
        self.learning_sample = 0
        self.learning_hand_start_stack = 0.0
        self.learning_hand_end_stack = 0.0
        self.learning_position = ""
        self.learning_name = "   "
        self.range_ug_open = [] #ug open
        self.range_hj_open = [] #hj open
        self.range_co_open = [] #co open
        self.range_db_open = [] #dealer open
        self.range_sb_open = [] #sb open
        self.range_hd_open = [] #heads up dealer open
        self.range_hb_defend = [] #heads up big blind defend
        self.range_defend_vs_ug_ip = [] #defend range vs ug opener when we have position on him
        self.range_defend_vs_ug_op = [] #defend range vs ug opener when he has position on us
        self.range_defend_vs_hj_ip = [] #defend range vs hijack opener in position
        self.range_defend_vs_hj_op = [] #defend range vs hijack opener out of position
        self.range_defend_vs_co_ip = [] #defend range vs cutoff opener in position
        self.range_defend_vs_co_op = [] #defend range vs cutoff opener out of position
        self.range_defend_vs_db_op = [] #defend range vs dealer button always out of position
        self.range_defend_vs_sb_ip = [] #defend range vs small blind always in position
        self.range_under10bb_push_vs_1 = [] #under 10 bb push vs 1 villain
        self.range_under10bb_push_vs_2 = [] #under 10 bb push vs 2 villains
        self.range_under10bb_push_vs_more = [] #under 10 bb push vs bunch of villains
        self.range_call_vs_under10bb_push_0_left_behind = [] #call a push from player who has under 10bb and pushes, no one left after you
        self.range_call_vs_under10bb_push_1_left_behind = [] #call a push from player who has under 10bb and pushes, one left after you to act
        self.range_call_vs_under10bb_push_more_left_behind = [] #call a push from player who has under 10bb and pushes, 2+ left after you to act
        self.range_fold = []
        self.range_top1 = ['aa', 'kk']
        self.range_ak = ['aks', 'ako']
        self.range_aq = ['aqs', 'aqo']
        self.range_top1_5 = ['aa', 'kk', 'qq']
        self.range_top1_8 = ['aa', 'kk', 'qq', 'jj']
        self.range_top2_3 = ['aa', 'kk', 'qq', 'jj', 'tt']
        self.range_top2_7 = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99']
        self.range_pp = ['aa', 'kk', 'qq', 'jj', 'tt', '99', '88', '77', '66', '55', '44', '33', '22']
        self.range_top4_1 = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako']
        self.range_top4_5 = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako', 'ajs']
        self.range_top6 = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako', 'ajs', 'kqs', '88', 'ats', 'aqo']
        self.range_safe = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako', 'ajs', 'kqs', '88', 'ats', 'aqo', '77', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'ajo', 'ato', 'a9o', 'a8o', 'kqo']
        self.range_wide = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako', 'ajs', 'kqs', '88',\
                         'ats', 'aqo', '77', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'ajo', 'ato', 'a9o', 'a8o', 'kqo', 'qts', 'qto',\
                             'a7o', 'a6o', 'a5o', 'a4o', 'a3o', 'a2o', 'kqo', 'kjs', 'kjo', 'kts', 'kto', 'qjs', 'qjo', 'jts', 'jto', 't9s', \
                                 '66', '55', '44', '33', '22', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s']
        self.range_preflop_light = ['43s', '42s', '54s', '53s', '65s', '64s', '76s', '75s', '87s', '86s', '98s', '97s']
        self.range_atc = [] #any two cards
        self.range_nash_heads_up_10bb_push = ['aa', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'a7s' ,'a6s', 'a5s', 'a4s', 'a3s', 'a2s', \
                                              'ako', 'kk', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', \
                                              'aqo', 'kqo', 'qq', 'qjs', 'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s', \
                                              'ajo', 'kjo', 'qjo', 'jj', 'jts', 'j9s', 'j8s', 'j7s', 'j6s', 'j5s', 'j4s', 'j3s',        \
                                              'ato', 'kto', 'qto', 'jto', 'tt', 't9s', 't8s', 't7s', 't6s', 't5s', 't4s',               \
                                              'a9o', 'k9o', 'q9o', 'j9o', 't9o', '99', '98s', '97s', '96s', '95s',                      \
                                              'a8o', 'k8o', 'q8o', 'j8o', 't8o', '98o', '88', '87s', '86s', '85s', '84s',               \
                                              'a7o', 'k7o', 'q7o',               '97o', '87o', '77', '76s', '75s', '74s',               \
                                              'a6o', 'k6o',                                    '76o', '66', '65s', '64s',               \
                                              'a5o', 'k5o',                                                 '55',  '54s',               \
                                              'a4o', 'k4o',                                                         '44',               \
                                              'a3o', 'k3o',                                                                '33',        \
                                              'a2o', 'k2o',                                                                       '22'  ]
        self.range_nash_heads_up_10bb_call = ['aa', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'a7s' ,'a6s', 'a5s', 'a4s', 'a3s', 'a2s', \
                                              'ako', 'kk', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', \
                                              'aqo', 'kqo', 'qq', 'qjs', 'qts', 'q9s', 'q8s', 'q7s',                                    \
                                              'ajo', 'kjo', 'qjo', 'jj', 'jts', 'j9s', 'j8s',                                           \
                                              'ato', 'kto', 'qto', 'jto', 'tt', 't9s',                                                  \
                                              'a9o', 'k9o', 'q9o',              '99',                                                   \
                                              'a8o', 'k8o',                            '88',                                            \
                                              'a7o', 'k7o',                                   '77',                                     \
                                              'a6o', 'k6o',                                           '66',                             \
                                              'a5o', 'k5o',                                                 '55',                       \
                                              'a4o',                                                              '44',                 \
                                              'a3o',                                                                     '33',          \
                                              'a2o',                                                                           '22'     ]
        
        self.stp = 0 #stack to pot ratio
        #flop threshold values vs 1
        self.threshold_flop_open_vs_one = 0.0
        self.threshold_flop_bluff_vs_one = 0.0
        self.threshold_flop_call_vs_one = 0.0
        self.threshold_flop_raise_vs_one = 0.0
        self.threshold_flop_call3bet_vs_one = 0.0
        self.threshold_flop_raise4bet_vs_one = 0.0
        self.threshold_flop_shove = 0.0
        #flop threshold values vs more
        self.threshold_flop_open_vs_more = 0.0
        self.threshold_flop_call_vs_more = 0.0
        self.threshold_flop_raise_vs_more = 0.0
        self.threshold_flop_call3bet_vs_more = 0.0
        self.threshold_flop_raise4bet_vs_more = 0.0
        #turn threshold values vs 1
        self.threshold_turn_open_vs_one = 0.0
        self.threshold_turn_bluff_vs_one = 0.0
        self.threshold_turn_call_vs_one = 0.0
        self.threshold_turn_raise_vs_one = 0.0
        self.threshold_turn_call3bet_vs_one = 0.0
        self.threshold_turn_raise4bet_vs_one = 0.0
        self.threshold_turn_shove = 0.0
        #turn threshold values vs more
        self.threshold_turn_open_vs_more = 0.0
        self.threshold_turn_call_vs_more = 0.0
        self.threshold_turn_raise_vs_more = 0.0
        self.threshold_turn_call3bet_vs_more = 0.0
        self.threshold_turn_raise4bet_vs_more = 0.0
        #river threshold values vs 1
        self.threshold_river_open_vs_one = 0.0
        self.threshold_river_bluff_vs_one = 0.0
        #self.threshold_river_call_vs_one = 0.0
        self.threshold_river_raise_vs_one = 0.0
        self.threshold_river_call3bet_vs_one = 0.0
        self.threshold_river_raise4bet_vs_one = 0.0
        self.threshold_river_shove = 0.0
        #river threshold values vs more
        self.threshold_river_open_vs_more = 0.0
        self.threshold_river_call_vs_more = 0.0
        self.threshold_river_raise_vs_more = 0.0
        self.threshold_river_call3bet_vs_more = 0.0
        self.threshold_river_raise4bet_vs_more = 0.0
        #acted on each street to know if you have to act when s.bet == biggest_bet
        self.acted_preflop = 0
        self.acted_flop = 0
        self.acted_turn = 0
        self.acted_river = 0


    def empty(self):
        self.name = "    "
        self.face = " "
        self.stack = 0
        self.displaystack = "  "
        self.clock = " "
        self.card1 = "  "
        self.card2 = "  "
        self.displaycard1 = "  "
        self.displaycard2 = "  "
        #self.button = " " do not clear button because man with button get get knocked out to be consistent with next hand
        self.bet = 0
        self.last3bets = 0
        self.displaybet = "  "
        self.showdown_result = 0.0
        self.available = True
        self.preorbits = 0.001
        self.floporbits = 0.001 # to prevent division by zero on hud displays
        self.vbet = 0
        self.cbet = 0
        self.betting_lead = 0
        self.floatandsteal = 0
        self.preallin = 0 #counter if jamming every hand
        self.prebigbet = 0 #counter if opens more than 5x and reraises more than 5x a.k.a. maniac
        self.last5betscrazy = 0 #counter if played normally for some time but go crazy recently
        self.range_ug_open = []
        self.range_hj_open = []
        self.range_co_open = []
        self.range_db_open = []
        self.range_sb_open = []
        self.range_defend_vs_ug_ip = [] #defend range vs ug opener when we have position on him
        self.range_defend_vs_ug_op = [] #defend range vs ug opener when he has position on us
        self.range_defend_vs_hj_ip = [] #defend range vs hijack opener in position
        self.range_defend_vs_hj_op = [] #defend range vs hijack opener out of position
        self.range_defend_vs_co_ip = [] #defend range vs cutoff opener in position
        self.range_defend_vs_co_op = [] #defend range vs cutoff opener out of position
        self.range_defend_vs_db_op = [] #defend range vs dealer button always out of position
        self.range_defend_vs_sb_ip = [] #defend range vs small blind always in position
        self.range_under10bb_push_vs_1 = [] #under 10 bb push vs 1 villain
        self.range_under10bb_push_vs_2 = [] #under 10 bb push vs 2 villains
        self.range_under10bb_push_vs_more = [] #under 10 bb push vs bunch of villains
        self.range_call_vs_under10bb_push_0_left_behind = [] #call a push from player who has under 10bb and pushes, no one left after you
        self.range_call_vs_under10bb_push_1_left_behind = [] #call a push from player who has under 10bb and pushes, one left after you to act
        self.range_call_vs_under10bb_push_more_left_behind = [] #call a push from player who has under 10bb and pushes, 2+ left after you to act
        self.stp = 0 #stack to pot ratio
        #flop threshold values vs 1
        self.threshold_flop_open_vs_one = 0.0
        self.threshold_flop_bluff_vs_one = 0.0
        self.threshold_flop_call_vs_one = 0.0
        self.threshold_flop_raise_vs_one = 0.0
        self.threshold_flop_call3bet_vs_one = 0.0
        self.threshold_flop_raise4bet_vs_one = 0.0
        self.threshold_flop_shove = 0.0
        #flop threshold values vs more
        self.threshold_flop_open_vs_more = 0.0
        self.threshold_flop_call_vs_more = 0.0
        self.threshold_flop_raise_vs_more = 0.0
        self.threshold_flop_call3bet_vs_more = 0.0
        self.threshold_flop_raise4bet_vs_more = 0.0
        #turn threshold values vs 1
        self.threshold_turn_open_vs_one = 0.0
        self.threshold_turn_bluff_vs_one = 0.0
        self.threshold_turn_call_vs_one = 0.0
        self.threshold_turn_raise_vs_one = 0.0
        self.threshold_turn_call3bet_vs_one = 0.0
        self.threshold_turn_raise4bet_vs_one = 0.0
        self.threshold_turn_shove = 0.0
        #turn threshold values vs more
        self.threshold_turn_open_vs_more = 0.0
        self.threshold_turn_call_vs_more = 0.0
        self.threshold_turn_raise_vs_more = 0.0
        self.threshold_turn_call3bet_vs_more = 0.0
        self.threshold_turn_raise4bet_vs_more = 0.0
        #river threshold values vs 1
        self.threshold_river_open_vs_one = 0.0
        self.threshold_river_bluff_vs_one = 0.0
        #self.threshold_river_call_vs_one = 0.0
        self.threshold_river_raise_vs_one = 0.0
        self.threshold_river_call3bet_vs_one = 0.0
        self.threshold_river_raise4bet_vs_one = 0.0
        self.threshold_river_shove = 0.0
        #river threshold values vs more
        self.threshold_river_open_vs_more = 0.0
        self.threshold_river_call_vs_more = 0.0
        self.threshold_river_raise_vs_more = 0.0
        self.threshold_river_call3bet_vs_more = 0.0
        self.threshold_river_raise4bet_vs_more = 0.0
        #acted on each street to know if you have to act when s.bet == biggest_bet
        self.acted_preflop = 0
        self.acted_flop = 0
        self.acted_turn = 0
        self.acted_river = 0
        #acted on each street to know if you have to act when s.bet == biggest_bet
        self.acted_preflop = 0
        self.acted_flop = 0
        self.acted_turn = 0
        self.acted_river = 0

class DummySeat:
    def __init__(self, stack, card1, card2):
        self.name = ""
        self.button = " "
        self.clock = "  "
        self.displaycard1 = displayhand(card1)
        self.displaycard2 = displayhand(card2)
        self.displaybet = "    "
        self.displaystack = "   "
        self.face = "  "
        self.card1 = card1
        self.card2 = card2

class AnalysisSeat:
    def __init__(self, an_seat):
        if not settings.list_faces:
            p = pokerface.Pokerface()
            settings.list_faces = p.faces
        self.face = settings.list_faces.pop()
        self.stack = an_seat.stack
        self.displaystack = "  "
        self.clock = " "
        self.name = " "
        self.sea = "blue sea"
        self.splitrange = "unknown"
        self.paggression = 0 #preflop aggression
        self.faggression = 0 #flop aggression
        self.taggression = 0 #turn aggression
        self.raggression = 0 #river aggression
        self.card1 = an_seat.card1
        self.card2 = an_seat.card2
        self.displaycard1 = "  "
        self.displaycard2 = "  "
        self.displaybet = "  "
        self.button = an_seat.button
        self.bet = 0
        self.last3bets = 0
        self.betting_lead = 0
        self.oldbet = 0
        self.floatandsteal = 0
        self.want_to_push = 0
        self.showdown_result = 0.0
        self.available = False
        self.vbetflag = 0 # this is for counting only 1 when multiple bets in one street
        self.cbetflag = 0 # the same for flop
        self.preorbits = 0.001 #this is for counting preflop orbits for VPIP for HUD
        self.preallin = 0 #counter if jamming every hand
        self.prebigbet = 0 #counter if opens more than 5x and reraises more than 5x a.k.a. maniac
        self.last5betscrazy = 0 #counter if played normally for some time but go crazy recently
        self.floporbits = 0.001 #this is for counting plays on flop for HUD 1 to prevent division by zero in display
        self.vbet = 0 #this is vpip / voluntary put money in pot stat/
        self.cbet = 0 # this is putting money in flop cbet ot donk bet
        self.equx_flop = 0.0
        self.equx_turn = 0.0
        self.equx_river = 0.0
        self.learning_suit = "no"
        self.learning_hand = ""
        self.learning_sample = 0
        self.learning_hand_start_stack = 0.0
        self.learning_hand_end_stack = 0.0
        self.learning_position = ""
        self.learning_name = "   "
        self.range_ug_open = [] #ug open
        self.range_hj_open = [] #hj open
        self.range_co_open = [] #co open
        self.range_db_open = [] #dealer open
        self.range_sb_open = [] #sb open
        self.range_hd_open = [] #heads up dealer open
        self.range_hb_defend = [] #heads up big blind defend
        self.range_defend_vs_ug_ip = [] #defend range vs ug opener when we have position on him
        self.range_defend_vs_ug_op = [] #defend range vs ug opener when he has position on us
        self.range_defend_vs_hj_ip = [] #defend range vs hijack opener in position
        self.range_defend_vs_hj_op = [] #defend range vs hijack opener out of position
        self.range_defend_vs_co_ip = [] #defend range vs cutoff opener in position
        self.range_defend_vs_co_op = [] #defend range vs cutoff opener out of position
        self.range_defend_vs_db_op = [] #defend range vs dealer button always out of position
        self.range_defend_vs_sb_ip = [] #defend range vs small blind always in position
        self.range_under10bb_push_vs_1 = [] #under 10 bb push vs 1 villain
        self.range_under10bb_push_vs_2 = [] #under 10 bb push vs 2 villains
        self.range_under10bb_push_vs_more = [] #under 10 bb push vs bunch of villains
        self.range_call_vs_under10bb_push_0_left_behind = [] #call a push from player who has under 10bb and pushes, no one left after you
        self.range_call_vs_under10bb_push_1_left_behind = [] #call a push from player who has under 10bb and pushes, one left after you to act
        self.range_call_vs_under10bb_push_more_left_behind = [] #call a push from player who has under 10bb and pushes, 2+ left after you to act
        self.range_fold = []
        self.range_top1 = ['aa', 'kk']
        self.range_ak = ['aks', 'ako']
        self.range_aq = ['aqs', 'aqo']
        self.range_top1_5 = ['aa', 'kk', 'qq']
        self.range_top1_8 = ['aa', 'kk', 'qq', 'jj']
        self.range_top2_3 = ['aa', 'kk', 'qq', 'jj', 'tt']
        self.range_top2_7 = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99']
        self.range_pp = ['aa', 'kk', 'qq', 'jj', 'tt', '99', '88', '77', '66', '55', '44', '33', '22']
        self.range_top4_1 = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako']
        self.range_top4_5 = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako', 'ajs']
        self.range_top6 = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako', 'ajs', 'kqs', '88', 'ats', 'aqo']
        self.range_safe = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako', 'ajs', 'kqs', '88', 'ats', 'aqo', '77', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'ajo', 'ato', 'a9o', 'a8o', 'kqo']
        self.range_wide = ['aa', 'kk', 'qq', 'jj', 'tt', 'aks', '99', 'aqs', 'ako', 'ajs', 'kqs', '88',\
                         'ats', 'aqo', '77', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', 'ajo', 'ato', 'a9o', 'a8o', 'kqo', 'qts', 'qto',\
                             'a7o', 'a6o', 'a5o', 'a4o', 'a3o', 'a2o', 'kqo', 'kjs', 'kjo', 'kts', 'kto', 'qjs', 'qjo', 'jts', 'jto', 't9s', \
                                 '66', '55', '44', '33', '22', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s']
        self.range_preflop_light = ['43s', '42s', '54s', '53s', '65s', '64s', '76s', '75s', '87s', '86s', '98s', '97s']
        self.range_atc = [] #any two cards
        self.stp = 0 #stack to pot ratio
        #flop threshold values vs 1
        self.threshold_flop_open_vs_one = 0.0
        self.threshold_flop_bluff_vs_one = 0.0
        self.threshold_flop_call_vs_one = 0.0
        self.threshold_flop_raise_vs_one = 0.0
        self.threshold_flop_call3bet_vs_one = 0.0
        self.threshold_flop_raise4bet_vs_one = 0.0
        self.threshold_flop_shove = 0.0
        #flop threshold values vs more
        self.threshold_flop_open_vs_more = 0.0
        self.threshold_flop_call_vs_more = 0.0
        self.threshold_flop_raise_vs_more = 0.0
        self.threshold_flop_call3bet_vs_more = 0.0
        self.threshold_flop_raise4bet_vs_more = 0.0
        #turn threshold values vs 1
        self.threshold_turn_open_vs_one = 0.0
        self.threshold_turn_bluff_vs_one = 0.0
        self.threshold_turn_call_vs_one = 0.0
        self.threshold_turn_raise_vs_one = 0.0
        self.threshold_turn_call3bet_vs_one = 0.0
        self.threshold_turn_raise4bet_vs_one = 0.0
        self.threshold_turn_shove = 0.0
        #turn threshold values vs more
        self.threshold_turn_open_vs_more = 0.0
        self.threshold_turn_call_vs_more = 0.0
        self.threshold_turn_raise_vs_more = 0.0
        self.threshold_turn_call3bet_vs_more = 0.0
        self.threshold_turn_raise4bet_vs_more = 0.0
        #river threshold values vs 1
        self.threshold_river_open_vs_one = 0.0
        self.threshold_river_bluff_vs_one = 0.0
        #self.threshold_river_call_vs_one = 0.0
        self.threshold_river_raise_vs_one = 0.0
        self.threshold_river_call3bet_vs_one = 0.0
        self.threshold_river_raise4bet_vs_one = 0.0
        self.threshold_river_shove = 0.0
        #river threshold values vs more
        self.threshold_river_open_vs_more = 0.0
        self.threshold_river_call_vs_more = 0.0
        self.threshold_river_raise_vs_more = 0.0
        self.threshold_river_call3bet_vs_more = 0.0
        self.threshold_river_raise4bet_vs_more = 0.0
        #acted on each street to know if you have to act when s.bet == biggest_bet
        self.acted_preflop = 0
        self.acted_flop = 0
        self.acted_turn = 0
        self.acted_river = 0


    def empty(self):
        self.name = "    "
        self.face = " "
        self.stack = 0
        self.displaystack = "  "
        self.clock = " "
        self.card1 = "  "
        self.card2 = "  "
        self.displaycard1 = "  "
        self.displaycard2 = "  "
        #self.button = " " do not clear button because man with button get get knocked out to be consistent with next hand
        self.bet = 0
        self.last3bets = 0
        self.displaybet = "  "
        self.showdown_result = 0.0
        self.available = True
        self.preorbits = 0.001
        self.floporbits = 0.001 # to prevent division by zero on hud displays
        self.vbet = 0
        self.cbet = 0
        self.betting_lead = 0
        self.floatandsteal = 0
        self.preallin = 0 #counter if jamming every hand
        self.prebigbet = 0 #counter if opens more than 5x and reraises more than 5x a.k.a. maniac
        self.last5betscrazy = 0 #counter if played normally for some time but go crazy recently
        self.range_ug_open = []
        self.range_hj_open = []
        self.range_co_open = []
        self.range_db_open = []
        self.range_sb_open = []
        self.range_defend_vs_ug_ip = [] #defend range vs ug opener when we have position on him
        self.range_defend_vs_ug_op = [] #defend range vs ug opener when he has position on us
        self.range_defend_vs_hj_ip = [] #defend range vs hijack opener in position
        self.range_defend_vs_hj_op = [] #defend range vs hijack opener out of position
        self.range_defend_vs_co_ip = [] #defend range vs cutoff opener in position
        self.range_defend_vs_co_op = [] #defend range vs cutoff opener out of position
        self.range_defend_vs_db_op = [] #defend range vs dealer button always out of position
        self.range_defend_vs_sb_ip = [] #defend range vs small blind always in position
        self.range_under10bb_push_vs_1 = [] #under 10 bb push vs 1 villain
        self.range_under10bb_push_vs_2 = [] #under 10 bb push vs 2 villains
        self.range_under10bb_push_vs_more = [] #under 10 bb push vs bunch of villains
        self.range_call_vs_under10bb_push_0_left_behind = [] #call a push from player who has under 10bb and pushes, no one left after you
        self.range_call_vs_under10bb_push_1_left_behind = [] #call a push from player who has under 10bb and pushes, one left after you to act
        self.range_call_vs_under10bb_push_more_left_behind = [] #call a push from player who has under 10bb and pushes, 2+ left after you to act
        self.stp = 0 #stack to pot ratio
        #flop threshold values vs 1
        self.threshold_flop_open_vs_one = 0.0
        self.threshold_flop_bluff_vs_one = 0.0
        self.threshold_flop_call_vs_one = 0.0
        self.threshold_flop_raise_vs_one = 0.0
        self.threshold_flop_call3bet_vs_one = 0.0
        self.threshold_flop_raise4bet_vs_one = 0.0
        self.threshold_flop_shove = 0.0
        #flop threshold values vs more
        self.threshold_flop_open_vs_more = 0.0
        self.threshold_flop_call_vs_more = 0.0
        self.threshold_flop_raise_vs_more = 0.0
        self.threshold_flop_call3bet_vs_more = 0.0
        self.threshold_flop_raise4bet_vs_more = 0.0
        #turn threshold values vs 1
        self.threshold_turn_open_vs_one = 0.0
        self.threshold_turn_bluff_vs_one = 0.0
        self.threshold_turn_call_vs_one = 0.0
        self.threshold_turn_raise_vs_one = 0.0
        self.threshold_turn_call3bet_vs_one = 0.0
        self.threshold_turn_raise4bet_vs_one = 0.0
        self.threshold_turn_shove = 0.0
        #turn threshold values vs more
        self.threshold_turn_open_vs_more = 0.0
        self.threshold_turn_call_vs_more = 0.0
        self.threshold_turn_raise_vs_more = 0.0
        self.threshold_turn_call3bet_vs_more = 0.0
        self.threshold_turn_raise4bet_vs_more = 0.0
        #river threshold values vs 1
        self.threshold_river_open_vs_one = 0.0
        self.threshold_river_bluff_vs_one = 0.0
        #self.threshold_river_call_vs_one = 0.0
        self.threshold_river_raise_vs_one = 0.0
        self.threshold_river_call3bet_vs_one = 0.0
        self.threshold_river_raise4bet_vs_one = 0.0
        self.threshold_river_shove = 0.0
        #river threshold values vs more
        self.threshold_river_open_vs_more = 0.0
        self.threshold_river_call_vs_more = 0.0
        self.threshold_river_raise_vs_more = 0.0
        self.threshold_river_call3bet_vs_more = 0.0
        self.threshold_river_raise4bet_vs_more = 0.0
        #acted on each street to know if you have to act when s.bet == biggest_bet
        self.acted_preflop = 0
        self.acted_flop = 0
        self.acted_turn = 0
        self.acted_river = 0