#copyright (c) 2019
#jodathecoda@yahoo.com

import os
import time
from random import randint
import settings
import checkhands

premi = ['aa', 'kk', 'qq', 'aks', 'jj', 'ako', 'tt', 'aqs', 'aqo']

broad = ['ajs', 'kqs', 'ats', 'aqo', 'kjs', 'kts', 'ajo', 'kqo', 'ato', 'qjs', 'qts',\
            'jts', 'kjo', 'qjo', 'kto', 'qto', 'jto']

pockp = ['99', '88', '77', '66', '55', '44', '33', '22']

conne = ['t9s', '98s', 't9o', '87s', '98o', '76s', '65s', '87o', '54s', '76o',\
        '43s', '65o', '54o', '32s', '43o', '32o']

gapco = ['j9s', 't8s', 'j9o', '97s', 't8o', '86s', '75s', '97o', '64s', '86o',\
        '53s', '75o', '42s', '64o', '53o', '42o', '85s']

acexx = ['a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a9o', 'a4s','a8o', 'a3s', 'a2s', 'a7o', \
            'a5o', 'a6o', 'a4o', 'a3o', 'a2o']

kingx = ['k9s', 'k8s', 'k7s', 'k9o', 'k6s', 'k5s', 'k4s', 'k8o', 'k3s', 'k7o', \
            'k2s', 'k6o', 'k5o', 'k4o', 'k3o', 'k2o']

trash =    ['q9s', 'q8s', 'j8s', 'q9o', 'q7s', 'q6s', 'j7s', 't7s', 'q5s', 'q8o', \
            'j8o', 'q4s', 'j6s', 't6s', '96s', 'q3s', 'j5s', 'q7o', 'q2s', 'j4s', \
            'j7o', 't7o', 't5s', 'q6o', 'j4s', 'q6o', 'j3s', 'j2s', 'q5o', 't3s', \
            '74s', 't2s', 'q4o', 'j6o', '84s','95s','t4s', '94s', 't6o', '96o', '93s', 'q3o', \
            'j5o', '63s', '92s', '73s', 'q2o', 'j4o', '83s', '52s', '85o', '82s', \
            't5o', '95o', 'j3o', '62s', 't4o', 'j2o', '72s', 't3o', '74o', '84o', \
            't2o', '94o', '93o', '63o', '92o', '73o', '83o', '32o', '52o','82o', \
            '62o','72o']

premi_max = len(premi)
broad_max = len(broad)
pockp_max = len(pockp)
conne_max = len(conne)
gapco_max = len(gapco)
acexx_max = len(acexx)
kingx_max = len(kingx)
trash_max = len(trash)

def modify(selected_range, rangename):
    modrange = selected_range

    premi_counter = 0
    broad_counter = 0
    pockp_counter = 0
    conne_counter = 0
    gapco_counter = 0
    acexx_counter = 0
    kingx_counter = 0
    trash_counter = 0

    for hanz in modrange:
        if hanz in premi:
            premi_counter += 1
        elif hanz in broad:
            broad_counter += 1
        elif hanz in pockp:
            pockp_counter += 1
        elif hanz in conne:
            conne_counter += 1
        elif hanz in gapco:
            gapco_counter += 1
        elif hanz in acexx:
            acexx_counter += 1
        elif hanz in kingx:
            kingx_counter += 1
        elif hanz in trash:
            trash_counter += 1
        else:
            print("error in change_range unknown type hanz: " + hanz)
            dumb = input("]")

    add_or_remove_hands = randint(0,3)
    #0 = remove one hand
    #1 = add one hand
    #2,3 = no change

    if add_or_remove_hands == 0:
        if len(modrange) > 5:
            del modrange[-1]
        else:
            pass
    elif add_or_remove_hands == 1:
        #if all ranges are full pass
        if trash_counter == trash_max:
            pass
        else:
            #add one hand start from strongest ranges down to weakest
            not_added = 1
            
            #premiums are with priority, theres no point to add other hand if you still did not fill premiums
            if premi_counter < premi_max:
                for newhand in premi:
                    if not_added and newhand not in modrange:
                        modrange.append(newhand)
                        not_added = 0 #the hand is added
            
            if broad_counter < broad_max and not_added:
                #broadways are second priority
                for newhand in broad:
                    if not_added and newhand not in modrange:
                        modrange.append(newhand)
                        not_added = 0 #the hand is added


            #next with equal priorities are acexx, pockp and conne
            #so go random 0-acexx 1-pockp 2-conne            
            random_choice = 99
            if not_added:
                if (acexx_counter < acexx_max) and (pockp_counter < pockp_max) and (conne_counter < conne_max):
                    random_choice = randint(0,2)
                elif (acexx_counter == acexx_max) and (pockp_counter < pockp_max) and (conne_counter < conne_max):
                    #acexx is full in our range
                    random_choice = randint(1,2)
                elif (acexx_counter < acexx_max) and (pockp_counter == pockp_max) and (conne_counter < conne_max):
                    #pockp is full in our range
                    random_choice = randint(0,1)
                    if random_choice == 1:
                        random_choice = 2
                elif (acexx_counter < acexx_max) and (pockp_counter < pockp_max) and (conne_counter == conne_max):
                    #connectors are full in our range
                    random_choice = randint(0,1)
                elif (acexx_counter == acexx_max) and (pockp_counter == pockp_max) and (conne_counter < conne_max):
                    #acexx and pockp are full in our range
                    random_choice = 2
                elif (acexx_counter == acexx_max) and (pockp_counter < pockp_max) and (conne_counter == conne_max):
                    #acexx and connectors are full in our range
                    random_choice = 1
                elif (acexx_counter < acexx_max) and (pockp_counter == pockp_max) and (conne_counter == conne_max):
                    #pocket pairs and connectors are full in our range
                    random_choice = 0
                elif (acexx_counter == acexx_max) and (pockp_counter == pockp_max) and (conne_counter == conne_max):
                    #all three ranges are full, so random choice stays 99 and go to next priority ranges
                    pass
                else:
                    print("error in ranges acexx pockp and conne adding new hand")
                    dumb = input("]")

            if not_added and random_choice == 0:
                #acexx
                for newhand in acexx:
                    if not_added and newhand not in modrange:
                        modrange.append(newhand)
                        not_added = 0 #the hand is added

            if not_added and random_choice == 1:
                #pockp
                for newhand in pockp:
                    if not_added and newhand not in modrange:
                        modrange.append(newhand)
                        not_added = 0 #the hand is added

            if not_added and random_choice == 2:
                #conne
                for newhand in conne:
                    if not_added and newhand not in modrange:
                        modrange.append(newhand)
                        not_added = 0 #the hand is added

            #next with equal priorities are kingx and gap connectors so go random
            if random_choice == 99 and not_added:
                #all previous ranges are full
                if (kingx_counter < kingx_max) and (gapco_counter < gapco_max):
                    #both ranghes from this priority are available so go random:
                    random_choice = randint(0,1)
                elif (kingx_counter == kingx_max) and (gapco_counter < gapco_max):
                    #kingx range is full
                    random_choice = 1
                elif (kingx_counter < kingx_max) and (gapco_counter == gapco_max):
                    #gapco range is full
                    random_choice = 0

            if not_added and random_choice == 0:
                #kingx
                for newhand in kingx:
                    if not_added and newhand not in modrange:
                        modrange.append(newhand)
                        not_added = 0 #the hand is added

            if not_added and random_choice == 1:
                #gapco
                for newhand in gapco:
                    if not_added and newhand not in modrange:
                        modrange.append(newhand)
                        not_added = 0 #the hand is added

            # and trash hands are last:

            if not_added and trash_counter < trash_max:
                #trash
                for newhand in trash:
                    if not_added and newhand not in modrange:
                        modrange.append(newhand)
                        not_added = 0 #the hand is added
                    
    else:
        pass
    return(modrange)


def run(fish):
    range_ug_open = [] #ug open
    selected_file = "fishes/" + fish + "/ranges/ug_open.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "ug_open")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")

    range_hj_open = [] #hj open
    selected_file = "fishes/" + fish + "/ranges/hj_open.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "hj_open")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_co_open = [] #co open
    selected_file = "fishes/" + fish + "/ranges/co_open.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "co_open")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_db_open = [] #dealer open
    selected_file = "fishes/" + fish + "/ranges/db_open.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "db_open")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_sb_open = [] #sb open
    selected_file = "fishes/" + fish + "/ranges/sb_open.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "sb_open")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_hd_open = [] #heads up dealer open
    selected_file = "fishes/" + fish + "/ranges/hd_open.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "hd_open")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_hb_defend = [] #heads up big blind defend
    selected_file = "fishes/" + fish + "/ranges/hb_defend.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "hb_defend")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_defend_vs_ug_ip = [] #defend range vs ug opener when we have position on him
    selected_file = "fishes/" + fish + "/ranges/defend_vs_ug_ip.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "defend_vs_ug_ip")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_defend_vs_ug_op = [] #defend range vs ug opener when he has position on us
    selected_file = "fishes/" + fish + "/ranges/defend_vs_ug_op.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "defend_vs_ug_op")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_defend_vs_hj_ip = [] #defend range vs hijack opener in position
    selected_file = "fishes/" + fish + "/ranges/defend_vs_hj_ip.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "defend_vs_hj_ip")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_defend_vs_hj_op = [] #defend range vs hijack opener out of position
    selected_file = "fishes/" + fish + "/ranges/defend_vs_hj_op.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "defend_vs_hj_op")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_defend_vs_co_ip = [] #defend range vs cutoff opener in position
    selected_file = "fishes/" + fish + "/ranges/defend_vs_co_ip.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "defend_vs_co_ip")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_defend_vs_co_op = [] #defend range vs cutoff opener out of position
    selected_file = "fishes/" + fish + "/ranges/defend_vs_co_op.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "defend_vs_co_op")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_defend_vs_db_op = [] #defend range vs dealer button always out of position
    selected_file = "fishes/" + fish + "/ranges/defend_vs_db_op.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "defend_vs_db_op")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_defend_vs_sb_ip = [] #defend range vs small blind always in position
    selected_file = "fishes/" + fish + "/ranges/defend_vs_sb_ip.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "defend_vs_sb_ip")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_under10bb_push_vs_1 = [] #under 10 bb push vs 1 villain
    selected_file = "fishes/" + fish + "/ranges/under10bb_push_vs_1.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "under10bb_push_vs_1")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_under10bb_push_vs_2 = [] #under 10 bb push vs 2 villains
    selected_file = "fishes/" + fish + "/ranges/under10bb_push_vs_2.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "under10bb_push_vs_2")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_under10bb_push_vs_more = [] #under 10 bb push vs bunch of villains
    selected_file = "fishes/" + fish + "/ranges/under10bb_push_vs_more.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "under10bb_push_vs_more")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_call_vs_under10bb_push_0_left_behind = [] #call a push from player who has under 10bb and pushes, no one left after you
    selected_file = "fishes/" + fish + "/ranges/call_vs_under10bb_push_0_left_behind.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "call_vs_under10bb_push_0_left_behind")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_call_vs_under10bb_push_1_left_behind = [] #call a push from player who has under 10bb and pushes, one left after you to act
    selected_file = "fishes/" + fish + "/ranges/call_vs_under10bb_push_1_left_behind.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "call_vs_under10bb_push_1_left_behind")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    

    range_call_vs_under10bb_push_more_left_behind = [] #call a push from player who has under 10bb and pushes, 2+ left after you to act
    selected_file = "fishes/" + fish + "/ranges/call_vs_under10bb_push_more_left_behind.range"
    selected_range = []
    try:
        f = open(selected_file,'r')
        with f:
            selected_range = f.read().splitlines()
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    try:
        f = open(selected_file,'w+')
        modified_range = modify(selected_range, "call_vs_under10bb_push_more_left_behind")
        for hand in modified_range:
            f.write(hand + "\n")
        f.close()
    except IOError:
        print("no such file" + selected_file)
        dumb = input("]")
    