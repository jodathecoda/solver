#copyright (c) 2019
#jodathecoda@yahoo.com

import os
import pokerface
import random
from random import shuffle

global cwd
cwd = os.getcwd()

RED   = '\033[1;31m'
BLUE  = '\033[1;34m'
CYAN  = '\033[1;36m'
GREEN = '\033[0;32m'
RESET = '\033[0;0m'
BOLD    = '\033[;1m'
REVERSE = '\033[;7m'
GREY = '\033[1;30m'
YELLOW='\033[0;33m'
RESET= '\033[0m'

suit_club = '\u2663'
suit_diamond = '\u2666'
suit_heart = '\u2665'
suit_spade = '\u2660'

hand_history_maximum_lines = 100000

class Hand_History_Buffer:
    def __init__(self):
        self.hhb = []
        self.max_length = hand_history_maximum_lines
        self.cur_length = 0
        self.filename = cwd + '/fishes/hand_history.dat'
        lines = ""
        if not os.path.isfile(cwd + '/fishes/hand_history.dat'):
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
            f = open(cwd + '/fishes/hand_history.dat', 'w+')
            f.close()
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
            f.close()
        except:
            print("no hand history file")
            dumb = input("]")
        for lin in lines:
            self.cur_length += 1
            self.hhb.append(lin)

        #if we change in settings hand_history_maximum_lines to lower,
        #and before that hand history file has more lines delete older ones
        if len(self.hhb) > self.max_length:
            while len(self.hhb) > self.max_length:
                del self.hhb[0]
        
    def add_line(self, line_to_add):
        if self.cur_length < self.max_length:
            self.hhb.append(line_to_add)
            self.cur_length += 1
        else:
            del self.hhb[0]
            self.hhb.append(line_to_add)

    def write_hh_to_the_file(self):
        with open(self.filename, "w") as f:
            for lins in self.hhb:
                f.write(lins)
        f.close()

    def clear(self):
        self.hhb = []
        self.hhb.append("PokerSea hand history file")

# HUD Analyzer settings
global hudanalyser
hudanalyser = 0

#this is for hudanalyser, dealer will be redfish,
#if he is seated, blackfish will be BB
global redfish_seated
redfish_seated = 0

#HuAnalyzer open size, default is 2.5 BB
huanalyzer_open_size = "2.5"

#HuAnalyzer redfish open
huanalyzer_open = []

#HuAnalyzer redfish call 3bet
huanalyzer_call3bet = []

#HuAnalyzer 3bet from blackfish
huanalyzer_3bet = []

#HuAnalyzer_call blackfish
huanalyzer_call = []

#End HUD Analyzer settings


global nash_stack
#less than 10 bb
nash_stack = 90

global nash_push_fold #when this flag is set bots will use heads up 10 bb nash push fold chart
nash_push_fold = 0

global nash_0 #seat 0 win counter at nash push fold game
nash_0 = 0

global nash_1 #seat 1 win counter at nash push fold game
nash_1 = 0

global nash_fish0 # name of fish 0 in nash game
nash_fish0 = ""

global nash_fish1 # name of fish 0 in nash game
nash_fish1 = ""

global nash_you #player nash counter
nash_you = 0

global nash_villain #villain nash
nash_villain = 0

global pokerpool

global analyser_flag
analyser_flag = 0

global analysed_iterations
analysed_iterations = 0

global threshold_added_open_from_checks
threshold_added_open_from_checks = 0.05 # if there are checks you are more incentive to bet even if you do not have equx, so this will be added to your equx

global dumblind
dumblind = 0

global backcard
backcard = "[]"

global amap
amap = [0,0,0,0,0,0]

global analysis_end
analysis_end = 0

global fold_bar
fold_bar =  "|fold|"

global check_bar
check_bar = "|check|"

global bet_bar
bet_bar =   "|bet|"

global bluff_bar
bluff_bar = "|bluff|"

global call_bar
call_bar =  "|call|"

global raise_bar
raise_bar = "|raise|"

global shove_bar
shove_bar = "|shove|"

global analyse_match
analyse_match = 0

global analyse_fast_speed
analyse_fast_speed = 1 #by default analysis is full speed and view

global enough_analysing_iterations
enough_analysing_iterations = 10000 #when analysing situation, give report after this number

global matched
matched = 0

#the value in bbs/matched in each position for anaylsing hand, it
#will be preserved during iterations

global report_bbv0
report_bbv0 = ""
global report_bbv1
report_bbv1 = ""
global report_bbv2
report_bbv2 = ""
global report_bbv3
report_bbv3 = ""
global report_bbv4
report_bbv4 = ""
global report_bbv5
report_bbv5 = ""

global bbvals0
bbvals0 = 0
global bbvals1
bbvals1 = 0
global bbvals2
bbvals2 = 0
global bbvals3
bbvals3 = 0
global bbvals4
bbvals4 = 0
global bbvals5
bbvals5 = 0

global bbv0
bbv0 = "   "
global bbv1
bbv1 = "   "
global bbv2
bbv2 = "   "
global bbv3
bbv3 = "   "
global bbv4
bbv4 = "   "
global bbv5
bbv5 = "   "

global hand_history_list
hand_history_list = []

global imported_list_preflop
imported_list_preflop = []

global hand_history_buffer

global wsop_followfish
wsop_followfish = 0 #fish will be followed only in wsop

global followfish  #if you want to follow how particular fish plays
followfish = ""

global debug_develop
debug_develop = 0

global oldview 
oldview = 1 #this is for returning old view after wsop

global colors_on
colors_on = 1

global fancy
fancy = 1

global suit_characters
suit_characters = 1

global debug_special_moves
debug_special_moves = 0 #stop point for special moves

global turnstealing_attempt # when flop checks trough
turnstealing_attempt = 0

global turnstealing_defend # when flop checks trough and someone bets
turnstealing_defend = 0

global terminal_size
terminal_size = 0
try:
    from shutil import get_terminal_size
except ImportError:
    terminal_size = 100

def printfishes(list_of_fishes):
    counter = 0
    for x in range(len(list_of_fishes)):
        print(list_of_fishes[x], end='')
        print("    ", end='')
        counter += 1
        if counter == 5:
            print("\n")
            counter = 0
    print("\n")

def clearscreen():
    if os.system('cls' if os.name == 'nt' else 'clear'):
        if not terminal_size:
            print("\n" * get_terminal_size().lines, end='')
        else:
            print("\n" * terminal_size, end='')
                
global allcards
allcards = ['aa', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s', \
             'ako', 'kk', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s', \
             'aqo', 'kqo', 'qq', 'qjs', 'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s', \
             'ajo', 'kjo', 'qjo', 'jj', 'jts', 'j9s', 'j8s', 'j7s', 'j6s', 'j5s', 'j4s', 'j3s', 'j2s', \
             'ato', 'kto', 'qto', 'jto', 'tt', 't9s', 't8s', 't7s', 't6s', 't5s', 't4s', 't3s', 't2s', \
             'a9o', 'k9o', 'q9o', 'j9o', 't9o', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s', \
             'a8o', 'k8o', 'q8o', 'j8o', 't8o', '98o', '88', '87s', '86s', '85s', '84s', '83s', '82s', \
             'a7o', 'k7o', 'q7o', 'j7o', 't7o', '97o', '87o', '77', '76s', '75s', '74s', '73s', '72s', \
             'a6o', 'k6o', 'q6o', 'j6o', 't6o', '96o', '86o', '76o', '66', '65s', '64s', '63s', '62s', \
             'a5o', 'k5o', 'q5o', 'j5o', 't5o', '95o', '85o', '75o', '65o', '55', '54s', '53s', '52s', \
             'a4o', 'k4o', 'q4o', 'j4o', 't4o', '94o', '84o', '74o', '64o', '54o', '44', '43s', '42s', \
             'a3o', 'k3o', 'q3o', 'j3o', 't3o', '93o', '83o', '73o', '63o', '53o', '43o', '33', '32s', \
             'a2o', 'k2o', 'q2o', 'j2o', 't2o', '92o', '82o', '72o', '62o', '52o', '42o', '32o', '22', ]

global fulldeck
fulldeck =      ['as', 'ks', 'qs', 'js', 'ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', \
                 'ah', 'kh', 'qh', 'jh', 'th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', \
                 'ad', 'kd', 'qd', 'jd', 'td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', \
                 'ac', 'kc', 'qc', 'jc', 'tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c' ]

global checks_on_flop #the more checks on flop, the bigger chance for next to open
checks_on_flop = 0

global checks_on_turn #the more checks on turn, the bigger chance for next to open
checks_on_turn = 0

global checks_on_river #the more checks on flop, the bigger chance for next to open
checks_on_river = 0

global flush #to indicate how many cards need to complete flush on board
flush = 5

global straight #to indicate how many cards need to complete straight on board
straight = 5

global myflush #to indicate how many cards need to complete flush on board + myhand
myflush = 5

global mystraight #to indicate how many cards need to complete straight on board + my hand
mystraight = 5

global raise_on_flop
raise_on_flop = 0

global raise_on_turn
raise_on_turn = 0

global raise_on_river
raise_on_river = 0

global tough_spot_range
tough_spot_range = ['aa', 'kk', 'qq', 'jj', 'tt', '99','aqs', 'aks', 'ako', '98s', '87s', '76s']

global gamblers_acted_on_flop
gamblers_acted_on_flop = 0

global gamblers_acted_on_turn
gamblers_acted_on_turn = 0

global gamblers_acted_on_river
gamblers_acted_on_river = 0

global left_gamblers
left_gamblers = 0

global left_to_act_flop
left_to_act_flop = 0

global left_to_act_turn
left_to_act_turn = 0

global left_to_act_river
left_to_act_river = 0

global autopilot
autopilot = 0 # this is player always to play flop and checkback postflop for debug

global debug_postflop
debug_postflop = 0

global debug_postflop_stop_point
debug_postflop_stop_point = 0

global action_current_street
action_current_street = "" #this is to see previous actions on current street

global crazybets_hero
crazybets_hero = 0

global preorbits_hero
preorbits_hero = 0.001

global threebet_postflop # to determine on flop if pot is 3bet so arrange ranges on villain
threebet_postflop = 0

global qt #this is to switch between qt4 and textgui
qt = 0

global left_loops
left_loops = 300

global wsop_hu_loops
#wsop_hu_loops = 27
wsop_hu_loops = 27

global wsop_sp_loops
#wsop_sp_loops = 18
wsop_sp_loops = 18

global wsop_ca_loops
#wsop_ca_loops = 9
wsop_ca_loops = 9

global wsop_mt_loops
wsop_mt_loops = 1

#human gui
global gui_bet
gui_bet = 0.0 # for gui for player

global gui_bigblind
gui_bigblind = 0.0

global gui_currentbet
gui_currentbet = 0.0

global gui_stack
gui_stack = 0.0

global gui_biggestbet
gui_biggestbet = 0.0

global gui_pot
gui_pot = 0.0

global learning
learning = 0 #this is absolete. when playing wsop learning is on when other games learning is off

global games_before_learning #games before trigger learning
games_before_learning = 3

global games_before_learning_value #reset value
games_before_learning_value = 300

global debugging_learning
debugging_learning = 0 # to see what is recorded in files of bots: winbig winsmall nochange losesmall losebig

global debug_learning_stop_point
debug_learning_stop_point = 0 #to stop when printed debugging info or to sleep

global debug_learning_sleep
debug_learning_sleep = 0 # seconds to sleep if not stoppping point to read the situation and selected range

global threebet
threebet = 0 #if the pot is reraised

global act_instead_of_bot
act_instead_of_bot = 0

global debug_ranges_stop_point
debug_ranges_stop_point = 0 #if it is 1 the game stops when reach, otherwise print it sleep 2 secs and continue

global debug_ranges
debug_ranges = 0

global allranges
allranges = ['range_ug_open', 'range_hj_open', 'range_co_open', 'range_db_open', 'range_sb_open', 'range_hd_open', 'range_hb_defend', \
             'range_defend_vs_ug_ip', 'range_defend_vs_ug_op', 'range_defend_vs_hj_ip', 'range_defend_vs_hj_op', 'range_defend_vs_co_ip', \
             'range_defend_vs_co_op', 'range_defend_vs_db_op', 'range_defend_vs_sb_ip', 'range_under10bb_push_vs_1', 'range_under10bb_push_vs_2', \
             'range_under10bb_push_vs_more', 'range_call_vs_under10bb_push_0_left_behind', 'range_call_vs_under10bb_push_1_left_behind', \
             'range_call_vs_under10bb_push_more_left_behind ']

global allfishes
allfishes = ['angelfish', 'barfish', 'batfish', 'blackfish', 'blowfish', 'bluefish', 'candlefish', 'catfish', 'cowfish', 'dartfish', \
            'dogfish', 'firefish', 'flagfish', 'frogfish', 'goldfish', 'hagfish', 'icefish', 'jawfish', 'jellyfish', 'knifefish', 'ladyfish', \
            'lampfish', 'lightfish', 'lionfish', 'manefish', 'milkfish', 'monkfish', 'moonfish', 'needlefish', 'oilfish', 'pariotfish', \
            'pearlfish', 'pencilfish', 'ponyfish', 'quillfish', 'rabbitfish', 'ragfish', 'razorfish', 'redfish', 'ricefish', 'rockfish', 'sablefish', \
            'sawfish', 'spearfish', 'spookfish', 'stonefish', 'sunfish', 'swordfish', 'triggerfish', 'velvetfish', 'waspfish', 'xrayfish', 'yellowfish', 'zebrafish']

global referencefishes
referencefishes = ['milkfish', 'yellowfish', 'redfish', 'blackfish']

global handreading_selected_display
handreading_selected_display = " "

global handreading_hands
handreading_hands = []

global handreading_selected_hand
handreading_selected_hand = 'z'

global handreading_selected_pot
handreading_selected_pot = 0.0

global handreading_selected_suited
handreading_selected_suited = 'z'

global handreading_selected_game_type
handreading_selected_game_type = 'z'

global handreading_selected_card1
handreading_selected_card1 = 'x'

global handreading_selected_card2
handreading_selected_card2 = 'x'

global handreading_count_hands
handreading_count_hands = 0

global handreading_selected_bot
handreading_selected_bot = "no name"

global handreading_selected_botfold
handreading_selected_botfold = "z"


global total_pot #this is for total pot of hand for hand history save
total_pot = 0

global hand_history #save hand history
hand_history = 0

global hud
hud = 0 #head up display

global logo # this option is for raspberry pi
logo = 1

global current_game
current_game = 'z'

global participants
participants = []

global view
view = 1 #1 is original display, 2 is insight info  3 is indicator only 4 incognito 5 incognito + info

global checksum
checksum = 0 # this is for debug info

global roundsign
roundsign = 3

global last6
last6 = []

global last5
last5 = []

global last4
last4 = []

global last3
last3 = []

global last2
last2 = []

global four_colors_deck
four_colors_deck = 1

global cards_back
cards_back = backcard

global cards_fold
cards_fold = "  "

global image_db
image_db = "D"

global image_cl
image_cl = "?"

global club
club = "c"

global diamond
diamond = "d"

global heart
heart = "h"

global spade
spade = "s"

global hero
hero = 'hero'

global starting_stacks
starting_stacks = 1500

global end_condition #this is for cash games, they will break at 3 players left
end_condition = 3

global rake
rake = 0

global dealer_bot
dealer_bot = 1

global iterations_to_next_level
iterations_to_next_level = 10

global current_iterations
current_iterations = 10

global current_iterations_to_next_level
current_iterations_to_next_level = 10

global smallblind
smallblind = 10

global list_faces
list_faces = []
list_faces = pokerface.faces
random.shuffle(list_faces)

global sounds_on
sounds_on = 0

global ante
ante = 0

global bot_time_to_act
bot_time_to_act = 3

global bot_time_to_act_preflop
bot_time_to_act_preflop = 3

global bot_time_to_act_flop
bot_time_to_act_flop = 3

global bot_time_to_act_turn
bot_time_to_act_turn = 3

global bot_time_to_act_river
bot_time_to_act_river = 3

global time_to_wait_board
time_to_wait_board = 5

global selected_bot_time_to_act
selected_bot_time_to_act = 3

global selected_bot_time_to_act_preflop
selected_bot_time_to_act_preflop = 3

global selected_bot_time_to_act_flop
selected_bot_time_to_act_flop = 3

global selected_bot_time_to_act_turn
selected_bot_time_to_act_turn = 3

global selected_bot_time_to_act_river
selected_bot_time_to_act_river = 3

global selected_time_to_wait_board
selected_time_to_wait_board = 5

global cards_faceup
cards_faceup = 1

global toggle_cards_faceup #this option is if you play to show cards on the river, then go back to no faceup
toggle_cards_faceup = 0

global loop
loop = 1  #how many loops of the game when bots playing

global hubuyin
hubuyin = 1

global huprize
huprize = 2

global spinbuyin
spinbuyin = 1

global spinprize
spinprize = 3

global mttbuyin
mttbuyin = 1

global mttprize
mttprize = [19,14,9,5,4,3]

def print_bye_cards():
    dek = ['As', 'Ks', 'Qs', 'Js', 'Ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s', \
            'Ah', 'Kh', 'Qh', 'Jh', 'Th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h', \
            'Ad', 'Kd', 'Qd', 'Jd', 'Td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d', \
            'Ac', 'Kc', 'Qc', 'Jc', 'Tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c' ]
    random.shuffle(dek)
    c1 = dek[1]
    c2 = dek[2]
    rank1 = c1[0]
    suit1 = c1[1]
    rank2 = c2[0]
    suit2 = c2[1]

    #spade card1
    if suit1 == 's':
        if fancy:
            suit1 = suit_spade
            if colors_on:
                suit1 = GREY + suit1 + RESET
    #spade card2
    if suit2 == 's':
        if fancy:
            suit2 = suit_spade
            if colors_on:
                suit2 = GREY + suit2 + RESET
    #heart card1
    if suit1 == 'h':
        if fancy:
            suit1 = suit_heart
            if colors_on:
                suit1 = RED + suit1 + RESET
    #heart card2
    if suit2 == 'h':
        if fancy:
            suit2 = suit_heart
            if colors_on:
                suit2 = RED + suit2 + RESET
    #diamond card1
    if suit1 == 'd':
        if fancy:
            suit1 = suit_diamond
            if colors_on:
                suit1 = BLUE + suit1 + RESET
    #diamond card2
    if suit2 == 'd':
        if fancy:
            suit2 = suit_diamond
            if colors_on:
                suit2 = BLUE + suit2 + RESET
    #club card1
    if suit1 == 'c':
        if fancy:
            suit1 = suit_club
            if colors_on:
                suit1 = GREEN + suit1 + RESET
    #club card2
    if suit2 == 'c':
        if fancy:
            suit2 = suit_club
            if colors_on:
                suit2 = GREEN + suit2 + RESET
    #print(rank1 + suit1 + " " + rank2 + suit2)
    if fancy:
        print("")
        print(" ___")
        print("|" + rank1 + suit1 + " |___")
        print("|   |" + rank2 + suit2 + " |")
        #print("|" + rank1 + suit1 + "|   |")
        

def print_logo():
    clearscreen()
    #print("logo")
    if oldview < 4:
        if hero == 'hero':
            if not dealer_bot:
                if colors_on and fancy:
                    print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + "     " + YELLOW + "dealer" + RESET)
                    print(GREY + "            ctrl+c lobby" + RESET)
                elif colors_on:
        	        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + "     " + YELLOW + "dealer" + RESET)
        	        print(GREY + "            ctrl+c lobby" + RESET)
                else:
        	        print("          ~~~ PokerSea ~~~" + "      " + "dealer")
        	        print("            ctrl+c lobby")
            elif followfish not in allfishes:
                if colors_on and fancy:
                    print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~"  + "     " + GREY + "observer" + RESET)
                    print(GREY + "            ctrl+c lobby" + RESET)
                elif colors_on:
        	        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + "     " + GREY + "observer" + RESET)
        	        print(GREY + "            ctrl+c lobby" + RESET)
                else:
        	        print("          ~~~ PokerSea ~~~" + "      " + "observer" )
        	        print("            ctrl+c lobby")
            else:
                if colors_on and fancy:
                    print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + " follower:" + followfish[:3] + RESET)
                    print(GREY + "            ctrl+c lobby" + RESET)
                elif colors_on:
        	        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~ " + "follower:" + followfish[:3] + RESET)
        	        print(GREY + "            ctrl+c lobby" + RESET)
                else:
        	        print("          ~~~ PokerSea ~~~" + " follower:" + followfish[:3])
        	        print("            ctrl+c lobby")
        else:
            if colors_on and fancy:
                print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + GREEN + "      " + "player" + RESET)
                print(GREY + "            ctrl+c lobby" + RESET)
            elif colors_on:
        	    print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + GREEN + "      " + "player" + RESET)
        	    print(GREY + "            ctrl+c lobby" + RESET)
            else:
        	    print("          ~~~ PokerSea ~~~" + "      " + "player")
        	    print("            ctrl+c lobby")
        print(" ")
    else:
        print(" ")

def print_logo_menu():
    clearscreen()
    if oldview < 4:
        if hero == 'hero':
            if not dealer_bot:
                if colors_on and fancy:
                    print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + "      " + YELLOW + "dealer" + RESET)
                    print(GREY + "            ctrl+c quit" + RESET)

                elif colors_on:
                    print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + "      " + YELLOW + "dealer" + RESET)
                    print(GREY + "            ctrl+c quit" + RESET)
                else:
                    print("          ~~~ PokerSea ~~~" + "      " + "dealer")
                    print("            ctrl+c quit")
                print(" ")
            elif followfish not in allfishes:
                agreement_file = cwd + "/user_agreement.dat"
                if os.path.isfile(agreement_file):
                    if colors_on and fancy:
                        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~"  + "     " + GREY + "observer" + RESET)
                        print(GREY + "            ctrl+c quit" + RESET)
                    elif colors_on:
                        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + "     " + GREY + "observer" + RESET)
                        print(GREY + "            ctrl+c quit" + RESET)
                    else:
                        print("          ~~~ PokerSea ~~~" + "     " + "observer")
                        print("            ctrl+c quit")
                    print(" ")
                else:
                    if colors_on and fancy:
                        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~")
                        print(GREY + "            ctrl+c quit" + RESET)
                    elif colors_on:
                        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~")
                        print(GREY + "            ctrl+c quit" + RESET)
                    else:
                        print("          ~~~ PokerSea ~~~")
                        print("            ctrl+c quit")
                    print(" ")

            else:
                if colors_on and fancy:
                    print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + " follower:" + followfish[:3] + RESET)
                    print(GREY + "            ctrl+c quit" + RESET)
                elif colors_on:
                    print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + " follower:" + followfish[:3] + RESET)
                    print(GREY + "            ctrl+c quit" + RESET)
                else:
                    print("          ~~~ PokerSea ~~~" + " follower:" + followfish[:3])
                    print("            ctrl+c quit")
                print(" ")
        else:
            if colors_on and fancy:
                print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + GREEN + "      " + "player" + RESET)
                print(GREY + "            ctrl+c quit" + RESET)
            elif colors_on:
        	    print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + GREEN + "      " + "player" + RESET)
        	    print(GREY + "            ctrl+c quit" + RESET)
            else:
                print("          ~~~ PokerSea ~~~" + "      " + "player")
                print("            ctrl+c quit")
            print(" ")

    else:
        pass

def print_logo_analyser_action():
    clearscreen()
    #if not analyse_fast_speed:
    if oldview < 4:
        if colors_on and fancy:
            print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + CYAN + "      " + "analyzer" + RESET)
            print(GREY + "          ctrl+c speed/quit" + RESET)
        elif colors_on:
            print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + CYAN + "      " + "analyzer" + RESET)
            print(GREY + "          ctrl+c speed/quit" + RESET)
        else:
            print("          ~~~ PokerSea ~~~" + "      " + "analyzer")
            print("          ctrl+c speed/quit")
        print(" ")
    else:
        pass

def print_logo_analyser_menu():
    clearscreen()
    if colors_on and fancy:
        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + CYAN + "      " + "analyzer" + RESET)
        print(GREY + "            ctrl+c cancel" + RESET)
    elif colors_on:
        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + CYAN + "      " + "analyzer" + RESET)
        print(GREY + "            ctrl+c cancel" + RESET)
    else:
        print("          ~~~ PokerSea ~~~" + "      " + "analyzer")
        print("            ctrl+c clear")
    print(" ")

def print_logo_teacher():
    clearscreen()
    if colors_on and fancy:
        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + RED + "      " + "teacher" + RESET)
        print(GREY + "            ctrl+c stop" + RESET)
    elif colors_on:
        print(BLUE + "          ~~~ " + RESET + "PokerSea " + BLUE + "~~~" + RED + "      " + "teacher" + RESET)
        print(GREY + "            ctrl+c stop" + RESET)
    else:
        print("          ~~~ PokerSea ~~~" + "      " + "teacher")
        print("            ctrl+c stop")
    print(" ")