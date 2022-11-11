#copyright (c) 2019
#jodathecoda@yahoo.com

from random import randint
import settings
import checkhands
import rangeeditor
import time
import bots
import display
#functions used by tournament and analyser classes

def strong_draw(flushdraw, straightdraw):
    if flushdraw < 2:
        return True
    elif straightdraw < 2:
        return True
    else:
        return False


def check_to_the_raisor_effect(betting_lead):
    if betting_lead:
        return float(0.4)
    else:
        return float(-0.6)

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

def find_button(table):
    t = table
    db_pos = 6
    for s in range(0,6):
        if t.seats[s].button == settings.image_db:
            db_pos = s
    return db_pos

def find_next_occupied_chair(table, current_seat):
    cur_seat = current_seat
    t = table
    next_oc_position = cur_seat
    if cur_seat == 0:
        if not t.seats[1].available:
            next_oc_position = 1
        elif not t.seats[2].available:
            next_oc_position = 2
        elif not t.seats[3].available:
            next_oc_position = 3
        elif not t.seats[4].available:
            next_oc_position = 4
        elif not t.seats[5].available:
            next_oc_position = 5
        else:
            pass
    elif cur_seat == 1:
        if not t.seats[2].available:
            next_oc_position = 2
        elif not t.seats[3].available:
            next_oc_position = 3
        elif not t.seats[4].available:
            next_oc_position = 4
        elif not t.seats[5].available:
            next_oc_position = 5
        elif not t.seats[0].available:
            next_oc_position = 0
        else:
            pass
    elif cur_seat == 2:
        if not t.seats[3].available:
            next_oc_position = 3
        elif not t.seats[4].available:
            next_oc_position = 4
        elif not t.seats[5].available:
            next_oc_position = 5
        elif not t.seats[0].available:
            next_oc_position = 0
        elif not t.seats[1].available:
            next_oc_position = 1
        else:
            pass
    elif cur_seat == 3:
        if not t.seats[4].available:
            next_oc_position = 4
        elif not t.seats[5].available:
            next_oc_position = 5
        elif not t.seats[0].available:
            next_oc_position = 0
        elif not t.seats[1].available:
            next_oc_position = 1
        elif not t.seats[2].available:
            next_oc_position = 2
        else:
            pass
    elif cur_seat == 4:
        if not t.seats[5].available:
            next_oc_position = 5
        elif not t.seats[0].available:
            next_oc_position = 0
        elif not t.seats[1].available:
            next_oc_position = 1
        elif not t.seats[2].available:
            next_oc_position = 2
        elif not t.seats[3].available:
            next_oc_position = 3
        else:
            pass
    elif cur_seat == 5:
        if not t.seats[0].available:
            next_oc_position = 0
        elif not t.seats[1].available:
            next_oc_position = 1
        elif not t.seats[2].available:
            next_oc_position = 2
        elif not t.seats[3].available:
            next_oc_position = 3
        elif not t.seats[4].available:
            next_oc_position = 4
        else:
            pass
    else: #straddle
        for s in range(0,6):
            if t.seats[s].stack > 0:
                next_oc_position = s        
    return next_oc_position

def count_players_on_table(table):
        t = table
        num_of_players = 0
        for s in t.seats:
            if not s.available:
                num_of_players += 1
        return num_of_players

def find_who_acts_preflop_index(table):
    act_index = 6
    t = table
    db_p = find_button(t)
    next_p = find_next_occupied_chair(t, db_p) # small blind when more than 3 
    nextnext_p = find_next_occupied_chair(t, next_p) # big blind when more than 3
    nextnextnext_p = find_next_occupied_chair(t, nextnext_p) # UTG
    count_p = count_players_on_table(t)
    if count_p < 4:
        act_index = db_p # 2 or 3 players button is first preflop
    else:
        act_index = nextnextnext_p
    return act_index

def find_who_acts_postflop_index(table):
    act_index = 6
    t = table
    db_p = find_button(t)
    next_p = find_next_occupied_chair(t, db_p) # D+1
    act_index = next_p
    return act_index

def get_effective_stacks(table, smallblind):
    t = table
    biggest_stack = 0
    smallest_stack = 0
    for s in t.seats:
        if s.card1 != "  ":
            if s.stack > biggest_stack:
                biggest_stack = s.stack
    smallest_stack = biggest_stack
    for s in t.seats:
        if s.card1 != "  ":
            if s.stack < smallest_stack:
                smallest_stack = s.stack
    return round(smallest_stack/(2*smallblind))


def find_smallest_bet(table):
    t = table
    smallest_bet = find_biggest_bet(t)
    for s in t.seats:
        if s.card1 != "  ":
            if smallest_bet > s.bet and s.bet > 0:
                smallest_bet = s.bet
    return smallest_bet

def find_biggest_bet(table):
    t = table
    biggest_bet = 0
    for s in t.seats:
        if biggest_bet < s.bet:
            biggest_bet = s.bet
    return biggest_bet

def checkFold(seat):
    s = seat
    if s.card1 == "  ":
        return True
    else:
        return False

def countNotFoldedYet(t):
    gamblers = 0
    for s in t.seats:
        if s.card1 != "  ":
            gamblers += 1
    return gamblers

def checkAllin(seat):
    s = seat
    if((s.stack == 0) and (not s.available) and (s.bet > 0)):
        return True
    else:
        return False

def check_hand_over_folds(table):
    t = table
    #count players and folds:
    np = count_players_on_table(t)
    #count folds
    nf = 0
    for s in t.seats:
        if s.card1 == "  " and s.stack !=0:
            nf += 1

    if np - nf == 1:
        return True
    else:
        return False

def find_folds(table):
    #count folds
    t = table
    folds = 0
    for s in t.seats:
        if not s.available:
            if s.card1 == "  ":
                folds += 1
    return folds

def one_left_on_street(table):
    t = table
    num_p = count_players_on_table(t)
    folds = find_folds(t)
    if num_p - folds == 1:
        return True
    else:
        return False

def street_over(table):
    t = table
    end = 1
    biggest_bet = find_biggest_bet(t)
    num_p = count_players_on_table(t)
    folds = find_folds(t)
    for s in t.seats:
        if not s.available:           #there is a player on a chair
            if not checkFold(s): #he has not folded /yet/
                if s.stack != 0:      #stack is not zero
                    if s.bet == biggest_bet:
                        pass
                    else:
                        end = 0
    if num_p - folds == 1: 
        end = 1
    return end

def getPreflopPosition(table, name):
    #20 - two players bot is dealer
    #21 - two players bot is D+1
    #30 - three players, bot is dealer
    t = table
    bot_name = name
    first_digit = 0
    second_digit = 0
    dealer_position = 0
    dumblist = []
    dealer_name = ""
    #find dealer name
    dealer_number = find_button(t)
    dealer_name = t.seats[dealer_number].name
    first_digit = count_players_on_table(t) * 10
    #populate dumb list with players and arrange it so dealer button is zero place
    for s in t.seats:
        if not s.available:
            dumblist.append(s.name)
    while(dumblist[0] != dealer_name):
        #remove empty seats
        while "    " in dumblist:
            dumblist.remove("    ")
        x = dumblist.pop()
        dumblist.insert(0,x)
    i = 0
    for l in range(len(dumblist)):
        if dumblist[l] == bot_name:
            second_digit = i
        i += 1
    if (int(first_digit/10)) < second_digit:
        print("error:" + str(int(first_digit/10)) + str(second_digit))
        for s in t.seats:
            print(s.name + " ")
        dumb = input("]")
    return first_digit + second_digit

def getPreflopPosition_name(table, name):
    #20 - two players bot is dealer
    #21 - two players bot is D+1
    #30 - three players, bot is dealer
    t = table
    bot_name = name
    first_digit = 0
    second_digit = 0
    dealer_position = 0
    dumblist = []
    dealer_name = ""
    #find dealer name
    dealer_number = find_button(t)
    dealer_name = t.seats[dealer_number].name
    first_digit = count_players_on_table(t) * 10
    #populate dumb list with players and arrange it so dealer button is zero place
    for s in t.seats:
        if not s.available:
            dumblist.append(s.name)
    while(dumblist[0] != dealer_name):
        #remove empty seats
        while "    " in dumblist:
            dumblist.remove("    ")
        x = dumblist.pop()
        dumblist.insert(0,x)
    i = 0
    for l in range(len(dumblist)):
        if dumblist[l] == bot_name:
            second_digit = i
        i += 1
    if (int(first_digit/10)) < second_digit:
        print("error:" + str(int(first_digit/10)) + str(second_digit))
        for s in t.seats:
            print(s.name + " ")
        dumb = input("]")
    position_number =  first_digit + second_digit
    position_name = ""
    if position_number == 60 or position_number == 50 or position_number == 40 or position_number == 30:
        position_name = "db" #dealer button
    elif position_number == 20:
        position_name = "hd" #heads up dealer
    elif position_number == 21:
        position_name = "hb" #heads up big blind                 
    elif position_number == 61 or position_number == 51 or position_number == 41 or position_number == 31:
        position_name = "sb" #small blind
    elif position_number == 62 or position_number == 52 or position_number == 42 or position_number == 32:
        position_name = "bb" #big blind
    elif position_number == 63:
        position_name = "ug" #unther the gun
    elif position_number == 64 or position_number == 53:
        position_name = "hj" #highjack
    elif position_number == 65 or position_number == 54 or position_number == 43:
        position_name = "co" #cutoff
    else:
        print("error in current position: " + str(position_number))
        dumb = input("]")
    return position_name

def getStackToPotRatio(table, name):
    t = table
    bot_name = name
    bot_stack = 0.0
    pot = 0.0
    for se in t.seats:
        pot += se.bet
        if se.name == bot_name:
            bot_stack += se.stack
    return round(bot_stack/pot,2)

def remove_item_from_list(the_list, val):
    return [value for value in the_list if value != val]

def wait_showdown(table, smallblind, ante):
    t = table
    biggest_bet = find_biggest_bet(t)
    someone_still_has_chips_and_smaller_bet = 0
    #if postflop all players not folded yet are allin except one, he does not need to play just wait for showdown
    allinbets = 0
    for seet in table.seats:
        if (seet.bet > ((smallblind*2) + ante)) and (seet.stack == 0):
            #there is allin count number of allins
            allinbets += 1
        if seet.stack > 0 and seet.bet < biggest_bet and (seet.card1 in settings.fulldeck):
            #there is still player with decision
            someone_still_has_chips_and_smaller_bet = 1
    gamblers = countNotFoldedYet(table)
    if (allinbets + 1 >= gamblers):
        if not someone_still_has_chips_and_smaller_bet:
            return True
        else:
            return False
    else:
        return False

def debugranges(situation, selectedrange):
    if settings.debug_ranges and settings.view:
        print(" ")
        if settings.colors_on:
            #print(settings.GREY + situation + " " + selectedrange + settings.RESET)
            print(" " + settings.GREY + selectedrange + settings.RESET)
        else:
            #print(situation + " " + selectedrange)
            print(" " + selectedrange)
    else:
        pass

def getFirstLimper(table, smallblind, ante):
        t = table
        first_limper = ""
        biggest_bet = find_biggest_bet(t)
        if biggest_bet > (smallblind*2 + ante):
            #there is no limp
            return first_limper
        num_p = count_players_on_table(t)
        if num_p < 2 or num_p > 6:
            print("error in number of players in function getFirstLimper")
            dumb = input("]")
        for s in t.seats:
            if (s.bet == biggest_bet) and (s.learning_position != 'bb') and (s.learning_position != 'hb'):
                first_limper = s.learning_position
        return first_limper

def getFirstLimperNumber(table, smallblind, ante):
    t = table
    first_limper_number = 7
    biggest_bet = find_biggest_bet(t)
    if biggest_bet > (smallblind*2 + ante):
        #there is no limp
        return first_limper_number
    num_p = count_players_on_table(t)
    if num_p < 2 or num_p > 6:
        print("error in number of players in function getFirstLimperNumber")
        dumb = input("]")
    counter = 0
    for s in t.seats:
        if (s.bet == biggest_bet) and (s.learning_position != 'bb') and (s.learning_position != 'hb'):
            first_limper_number = counter
        counter += 1
    return first_limper_number

def getFirstOpener(table, smallblind, ante):
        t = table
        first_opener = ""
        biggest_bet = find_biggest_bet(t)
        num_p = count_players_on_table(t)
        if num_p < 2 or num_p > 6:
            print("error in number of players in function getFirstOpener")
            dumb = input("]")
        for s in t.seats:
            if (s.bet == biggest_bet) and (biggest_bet > (smallblind*2 + ante)):
                first_opener = s.learning_position
        return first_opener

def getFirstOpenerNumber(table, smallblind, ante):
        t = table
        first_opener_number = 7
        biggest_bet = find_biggest_bet(t)
        num_p = count_players_on_table(t)
        if num_p < 2 or num_p > 6:
            print("error in number of players in function getFirstOpenerNumber")
            dumb = input("]")
        counter = 0
        for s in t.seats:
            if (s.bet == biggest_bet) and (biggest_bet > (smallblind*2 + ante)):
                first_opener_number = counter
            counter += 1
        return first_opener_number

def noraise(table):
    if (settings.raise_on_flop == 0 and settings.raise_on_turn == 0 and settings.raise_on_river == 0):
        return True
    else:
        return False

def roundbet(bet):
    base = 5
    try:
        returnbet = 0
        b = float(bet)
        returnbet = base * round(b/base)
        return int(round(returnbet))
    except:
        return int(0)

def checkoverbet(table, smallblind, ante):
    t = table
    gamblers = countNotFoldedYet(t)
    biggest_bet = find_biggest_bet(t)
    smallest_bet = find_smallest_bet(t)
    if gamblers*smallest_bet == 0:
        #take care of errors zero but we should never get here
        return float((biggest_bet - smallest_bet)/(smallblind*2 + ante))
    return float((biggest_bet - smallest_bet)/(gamblers*smallest_bet))

def overbet_postflop(table, name, equx, smallblind, ante):
    t = table
    overbet = checkoverbet(t, smallblind, ante)
    if overbet > 1.2 and noraise(t):
        
        cow_stack_to_pot = getStackToPotRatio(t, name)
        bully_stack_to_pot = 0.0
        biggest_bet = find_biggest_bet(t)
        for bigg in t.seats:
            if bigg.bet == biggest_bet:
                bully_name = bigg.name
                bully_stack_to_pot = getStackToPotRatio(t, bully_name)

        if len(t.board) == 6:
            #overbet on flop
            if overbet < 5:
                settings.raise_on_flop += 1
            else:
                settings.raise_on_flop += 2
        elif len(t.board) == 8:
            #overbet on turn
            if overbet < 5:
                settings.raise_on_turn += 1
            else:
                settings.raise_on_turn += 2
        elif len(t.board) == 10:
            #overbet on river
            if overbet < 5:
                settings.raise_on_river += 1
            else:
                settings.raise_on_river += 2
            
        else:
            print("error in overbet postflop board len")
            dumb = input("]")

def blocking_bet_defense(equx, pot, blocking_bet, street_number):
    street = street_number
    street_offset = 0.0
    if street_number == 6:
        #flop
        street_offset = 0.16
    elif street_number == 8:
        #turn
        street_offset = 0.18
    elif street_number == 10:
        #river
        street_offset = 0.4
    if (blocking_bet < pot/2):
        if equx - street_offset >= (blocking_bet/pot):
            return int(blocking_bet)
        else:
            return int(0)
    else:
        return int(0)

def get_street_aggression(table, name):
    for s in table.seats:
        if s.name == name:
            random_aggression = randint(0,3)
            if random_aggression == 0:
                return s.paggression
            elif random_aggression == 1:
                return s.faggression
            elif random_aggression == 2:
                return s.taggression
            elif random_aggression == 3:
                return s.raggression
            else:
                print("unknown get street aggression in common")
                dumb = input("]")

def betsizing(table, name, defending_range, game_type, smallblind, ante):
    gamblers = countNotFoldedYet(table)
    effective_stacks = get_effective_stacks(table , smallblind)
    bet = 0
    opened_already = 0
    stack = 0
    t = table
    hand = ""
    current_bet = 0
    card1 = "  "
    card2 = "  "
    biggest_bet = find_biggest_bet(t)
    if biggest_bet > smallblind*2 + 6*ante:
        opened_already = 1
    gamblers = countNotFoldedYet(t)
    posname = getPreflopPosition_name(table, name)
    stp = getStackToPotRatio(table, name)
    stack_in_BBs = 0.0
    want_to_bet = 0 #this is if you want to reraise 3x but your whole stack is 5x to go 5x
    splitrangetype = ""
    #find size of stack in big blinds
    for s in table.seats:
        if s.name == name:
            paggression = s.paggression
            card1 = s.card1
            card2 = s.card2
            current_bet = s.bet
            splitrangetype = s.splitrange
            stack = s.stack
            stack_in_BBs = round(s.stack/smallblind*2,2)

    current_range = defending_range
    rnd = randint(0,6)
    defendbet = 0
    calling_range = []
    raising_range = []
    number_of_hands = len(current_range)
    raising_fraction = (paggression*number_of_hands)/100
    #between 20 and 40% raising hands depends on preflop aggression
    special_case = 0
    r4aising_fraction = int(raising_fraction/4)
    if r4aising_fraction < 1:
        special_case = 1

    if special_case:
        #special_case = 0
        for s in table.seats:
            if s.name == name:
                if s.paggression > 34:
                    raising_range = s.range_top1_5 #AA, KK, QQ
                else:
                    raising_range = s.range_top1 #AA, KK
        if len(current_range) > len(raising_range):
            #If there is more hands goes to calling range
            for i in range(0, len(current_range)):
                if current_range[i] not in raising_range:
                    calling_range.append(current_range[i])


    elif splitrangetype == "polarized":
        for i in range(0, r4aising_fraction*3):
            #3/4 of strongest hands goes to value raise
            raising_range.append(current_range[i])
        for i in range (len(current_range) - r4aising_fraction, len(current_range)):
            #last 1/4 to bluff
            raising_range.append(current_range[i])
        for i in range (0, len(current_range)):
            if current_range[i] not in raising_range:
                calling_range.append(current_range[i])
    else:
        #splitrangetype == "merged":
        for i in range(0, r4aising_fraction*4):
            raising_range.append(current_range[i])
        for i in range(r4aising_fraction*4, len(current_range)):
            calling_range.append(current_range[i])

    count_limpers = 0
    for l in t.seats:
        if l.bet == smallblind*2 + ante:
            count_limpers += 1

    limpers = count_limpers - 1 #to get out of big blind

    paggression_factor = round(paggression/10)

    #one out of five times we do not reraise only flat so our calling_range is not capped, i.e. never contains AA KK ...
    rnd = randint(1, 2 + paggression_factor) #less aggressive bots has higher chance to flat
    if special_case:
        #here always raise
        rnd = 1
        special_case = 0
    if rnd == 2 and settings.threebet == 2:
        calling_range = current_range
        raising_range = []
        #raise reraise, so one more option to call
    if rnd == 3: #no raising
        calling_range = current_range
        raising_range = []

    if settings.hudanalyser == 1:
        print(name)
        if opened_already == 0:
            #redfish HB open range
            open_range = settings.huanalyzer_open
        elif settings.threebet > 0:
            #redfish HB call 3bet renage
            raising_range = []
            calling_range = settings.huanalyzer_call3bet
        else:
            #blackfish defends HB
            raising_range = settings.huanalyzer_3bet
            calling_range = settings.huanalyzer_call

    if settings.debug_ranges:
        if not settings.colors_on:
            if opened_already:
                for doublehand in calling_range:
                    if doublehand in raising_range:
                        calling_range.remove(doublehand)
                if (rnd == 3) or (rnd == 2 and settings.threebet == 2):
                    print(" decision to flat call")
                    print(" ")
                    print(" calling range:")
                    rangeeditor.print_range_lines(calling_range)
                else:
                    print(" raising range:")
                    rangeeditor.print_range_lines(raising_range)
                    print(" ")
                    print(" calling range:")
                    rangeeditor.print_range_lines(calling_range)
            else:
                if settings.hudanalyser == 1:
                    open_range = settings.huanalyzer_open
                else:
                    open_range = []
                    open_range = raising_range + calling_range
                rangeeditor.print_range_lines(open_range)
            if settings.debug_ranges_stop_point:
                dumb = input("]")
            else:
                time.sleep(settings.bot_time_to_act_turn*2)
        else: #colors_on
            if opened_already:
                if (rnd == 3) or (rnd == 2 and settings.threebet == 2):
                    open_range_colors = []
                    raising_range_colors = []
                    calling_range_colors = calling_range
                    rangeeditor.print_debug_color_ranges(card1, card2, calling_range_colors, raising_range_colors, open_range_colors)
                else:
                    open_range_colors = []
                    raising_range_colors = raising_range
                    calling_range_colors = calling_range
                    rangeeditor.print_debug_color_ranges(card1, card2, calling_range_colors, raising_range_colors, open_range_colors)
            else:
                if settings.hudanalyser == 1:
                    open_range_colors = settings.huanalyzer_open
                else:
                    open_range_colors = raising_range + calling_range
                raising_range_colors = []
                calling_range_colors = []
                rangeeditor.print_debug_color_ranges(card1, card2, calling_range_colors, raising_range_colors, open_range_colors)
            if settings.debug_ranges_stop_point:
                dumb = input("]")
            else:
                time.sleep(settings.bot_time_to_act_turn*2)

    #if hand in calling_range:
    if checkhands.handInRange(card1, card2, calling_range) and not checkhands.handInRange(card1, card2, raising_range):
        if stack_in_BBs < 10:
            want_to_bet = stack
        elif gamblers == 2 and stp < 1.4:
            want_to_bet = stack
        else:
            if opened_already:
                if biggest_bet - current_bet >= stack:
                    want_to_bet = stack
                else:
                    want_to_bet = biggest_bet - current_bet
                for s in table.seats:
                    if (s.card1 == card1) and (s.card2 == card2):
                        if s.last3bets > 0:
                            s.last3bets -= 1 #reduce
            else:
                # HERE HERE huanalyzer open size
                if settings.hudanalyser:
                    #if hand in open range, use predefined open size
                    if settings.huanalyzer_open_size == "0":
                        #open fold each hand
                        want_to_bet = 0
                    elif settings.huanalyzer_open_size == "2":
                        # bot uses min raise
                        want_to_bet = smallblind*2*2 + ante - current_bet
                    elif settings.huanalyzer_open_size == "2.5":
                        # x2.5
                        want_to_bet = smallblind*2*2.5 + ante - current_bet
                    elif settings.huanalyzer_open_size == "3":
                        # x3
                        want_to_bet = smallblind*2*3 + ante - current_bet
                    elif settings.huanalyzer_open_size == "3.5":
                        # x3
                        want_to_bet = smallblind*2*3.5 + ante - current_bet
                    else:
                        # x2.5
                        want_to_bet = smallblind*2*2.5 + ante - current_bet
                #we open if heads up or spins and someone is shortstack under 10 BBS we limp
                elif effective_stacks < 30 and gamblers < 4:
                    short_stack_on_table = 0
                    for s in t.seats:
                        if s.stack != 0 and s.card1 != "  " and s.stack/smallblind*2 < 10:
                            short_stack_on_table = 1
                    if short_stack_on_table:
                        #we limp
                        want_to_bet = smallblind*2 + ante - current_bet
                    else:
                        want_to_bet = smallblind*2*2 + 6*ante + limpers*2*smallblind - current_bet #we use minbet
                else:
                    rnd = randint(0,9)
                    if rnd == 5:
                        want_to_bet = smallblind*2 + ante - current_bet
                    else:
                        want_to_bet = smallblind*2*3 + 6*ante + limpers*2*smallblind - current_bet #we use 3x for cash and mtt
                    cherrytop = randint(0,3)
                    want_to_bet += cherrytop*smallblind
    
    elif checkhands.handInRange(card1, card2, raising_range):
        if stack_in_BBs < 10:
            want_to_bet = stack
        elif gamblers == 2 and stp < 1.4:
            want_to_bet = stack
        else:
            if opened_already:
                randomized_part_bet = get_street_aggression(table, name)/10
                #this is 20-40
                want_to_bet = biggest_bet*randomized_part_bet + 6*ante + limpers*2*smallblind - current_bet #we use 3x
                for s in table.seats:
                    if s.name == name:
                        s.last3bets += 1 #update
            else:
                #we open if heads up or spins and someone is shortstack under 10 BBS we limp
                if effective_stacks < 30 and gamblers < 4:
                    short_stack_on_table = 0
                    for s in t.seats:
                        if s.stack != 0 and s.card1 != "  " and s.stack/smallblind*2 < 10:
                            short_stack_on_table = 1
                    if short_stack_on_table:
                        #we limp
                        #print("we limp")
                        want_to_bet = smallblind*2 + ante - current_bet
                    else:
                        #print("normal open")
                        want_to_bet = smallblind*2*2 + 6*ante + limpers*2*smallblind - current_bet #we use minbet
                else:
                    #we limp one out of ten times
                    rnd = randint(0,10)
                    if rnd < 1:
                        #we limp big time for debugging
                        want_to_bet = smallblind*2 + ante - current_bet
                    else:
                        want_to_bet = smallblind*2*3 + 6*ante + limpers*2*smallblind - current_bet #we use 3x for cash and mtt
                        cherrytop = randint(0,3)
                        want_to_bet += cherrytop*smallblind
    else:
        #check pot odds
        dealt_hand = card1 + card2
        if (s.learning_position == 'sb' or s.learning_position == 'hb') and (not checkhands.suited(dealt_hand)):
            want_to_bet = 0
        else:
            pot = 0.0
            for w in t.seats:
                pot += w.bet
            pot_odds = 0.0
            pot_odds = round((biggest_bet - current_bet)/pot, 2)
            if pot_odds < 0.29 and checkhands.billchen(dealt_hand) > 1.9: #out of position do not play weak hands
                if stack_in_BBs < 10:
                    want_to_bet = stack
                    #want_to_bet = 0
                elif gamblers == 2 and stp < 1.4:
                    want_to_bet = stack
                    #want_to_bet = 0 hereherehere
                else:
                    if opened_already:
                        #call
                        want_to_bet = biggest_bet - current_bet
                        if settings.debug_ranges:
                            if settings.colors_on:
                                print(settings.CYAN + "light call" + settings.RESET)
                            else:
                                print("light call")
                            if settings.debug_ranges_stop_point:
                                dumb = input("]")
                            else:
                                time.sleep(settings.bot_time_to_act_turn*2)
                    else:
                        want_to_bet = 0
            else:
                want_to_bet = 0
    ratio = want_to_bet/stack
    if ratio > 0.7:
        bet = stack
    else:
        bet = want_to_bet
    
    if bet < 1:
        staack_to_bb = round(stack/(smallblind*2))
        if staack_to_bb < 12:
            stack_to_pot = float(getStackToPotRatio(t, name))
            if stack_to_pot < 0.45:
                bet = stack
                #bet = 0 hereherehere
    rounded_bet = roundbet(bet)
    return rounded_bet

def turnsteal_defend(fish_aggression, fish_equx, cur_bet, thetable):
    return_bet = 0
    turn_gamblers = countNotFoldedYet(thetable)
    if ((settings.checks_on_flop == turn_gamblers) and (turn_gamblers < 4)):
        #there might be turn steal
        biggest_bet = find_biggest_bet(thetable)
        defend_decision = randint(0,100)
        if defend_decision <= fish_aggression:
            #defend from potential turn steal
            settings.turnstealing_defend = 1
            if fish_equx > (0.75 - fish_aggression/100):
                #call we have some equity
                return_bet =  int(biggest_bet - cur_bet)
            else:
                #reraise
                return_bet = int(2.5 * biggest_bet)
        else:
            return_bet = 0
    return return_bet

def turnsteal_attack(fish_aggression, thetable, waitingshowdown, smallblind):
    return_bet = 0
    if waitingshowdown:
        return return_bet 
    steal = 0.0
    turn_gamblers = countNotFoldedYet(thetable)
    biggest_bet = find_biggest_bet(thetable)
    pota = 0
    no_one_bet_on_turn = 1
    for se in thetable.seats:
        pota += se.bet
        if se.bet < biggest_bet:
            no_one_bet_on_turn = 0
    if ((settings.checks_on_flop == turn_gamblers) and (turn_gamblers < 4) and (no_one_bet_on_turn == 0)):
        return_bet = 0
        steal_decision = randint(0,100)
        if steal_decision <= fish_aggression:
            #try to steal the turn
            settings.turnstealing_attempt = 1
            random_size = randint(0,2)
            if randint:
                return_bet = int(2/3*pota)
            else:
                return_bet = int(1/2*pota)
            cherrytop = randint(0,80)
            if cherrytop <= fish_aggression:
                #add some extra chips to bet
                addition_chips = randint(0,3)
                return_bet += (addition_chips*smallblind)
        else:
            #no steal attempt
            return_bet = 0
    return return_bet

def update_total_pot(table):
    t = table
    settings.total_pot = 0
    for seeds in t.seats:
        settings.total_pot += seeds.bet

def checksum(table):
    global handlog
    if not settings.checksum:
        return 0
    checksum = 0
    t = table
    for s in t.seats:
        checksum += (s.stack + s.bet)
        handlog += "s: " + str(s.stack) + " b: " + str(s.bet) +  " cards: " + s.card1 + s.card2 + " board: " + t.board + "\n"
    return checksum

def betting_round(table, street, game_type, smallblind, ante, tables):
    st = street
    t = table
    for s in t.seats:
        s.clock = " "
    if st == 0:
        #preflop                    
        for s in t.seats[find_who_acts_preflop_index(t):]:
                bots.bot_act(t,s,st, game_type, smallblind, ante, tables)
        for s in t.seats[:find_who_acts_preflop_index(t)]:
                bots.bot_act(t,s,st, game_type, smallblind, ante, tables)
    else:
        #postflop 
        for s in t.seats[find_who_acts_postflop_index(t):]:
                bots.bot_act(t,s,st, game_type, smallblind, ante, tables)
        for s in t.seats[:find_who_acts_postflop_index(t)]:
                bots.bot_act(t,s,st, game_type, smallblind, ante, tables)       
    #display.display_tables(t, game_type, smallblind, ante, tables)
    if not settings.analyser_flag:
        display.display_tables(table, game_type, smallblind, ante, tables)
    else:
        #analyser
        display.display_tables_analyser(table, settings.analysed_iterations, settings.matched)

def playHandpreflop(table, game_type, smallblind, ante, tables):
    t = table
    endstreet = 1
    betting_round(t, 0, game_type, smallblind, ante, tables)
    if street_over(t):
        endstreet = 0
    if check_hand_over_folds(t):
        endstreet = 0
        for s in t.seats:
            if not checkFold(s):
                s.stack += t.pot
                s.stack = roundbet(s.stack)
                s.bet = 0
                t.pot = 0
                t.board = ""

    while(endstreet):
        betting_round(t, 0, game_type, smallblind, ante, tables)
        if street_over(t):
            endstreet = 0
        if check_hand_over_folds(t):
            endstreet = 0
            for s in t.seats:
                if not checkFold(s):
                    s.stack += t.pot
                    s.stack = roundbet(s.stack)
                    s.bet = 0
                    t.pot = 0
                    t.board = ""

def playHandpostflop(table, game_type, smallblind, ante, tables):
    t = table
    endstreet = 1
    betting_round(t, 1, game_type, smallblind, ante, tables)
    if street_over(t):
        endstreet = 0
    if check_hand_over_folds(t):
        endstreet = 0
        for s in t.seats:
            if not checkFold(s):
                s.stack += t.pot - (t.pot*settings.rake/100)
                s.stack = roundbet(s.stack)
                s.bet = 0
                t.pot = 0
                t.board = ""

    while(endstreet):
        betting_round(t, 1, game_type, smallblind, ante, tables)
        if street_over(t):
            endstreet = 0
        if check_hand_over_folds(t):
            endstreet = 0
            for s in t.seats:
                if not checkFold(s):
                    s.stack += t.pot - (t.pot*settings.rake/100)
                    s.bet = 0
                    t.pot = 0
                    t.board = ""
    
