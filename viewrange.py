#copyright (c) 2019
#jodathecoda@yahoo.com

import os
import time
import settings

BLANK = " "
BLANKCELL = '   '

def viewrange(colors_on_flag):
    if colors_on_flag:
        CYAN  = '\033[1;36m'
        RESET = '\033[0;0m'
        GREY = '\033[1;30m'
    else:
        CYAN = ""
        GREY = ""
        RESET = ""
    settings.printfishes(settings.allfishes)
    fish = input("enter fish name: ")
    if fish not in settings.allfishes:
        print("unknown fish")
        time.sleep(2)
        settings.print_logo()
    else:
        exitos = 100
        while(exitos):
            settings.print_logo()
            print("select range number:")
            print("0  ug open")
            print("1  hj open")
            print("2  co open")
            print("3  dealer open")
            print("4  sb open")
            print("5  heads up dealer open")
            print("6  heads up big blind defend")
            print("7  defend range vs ug opener when we have position on him")
            print("8  defend range vs ug opener when he has position on us")
            print("9  defend range vs hijack opener in position")
            print("10 defend range vs hijack opener out of position")
            print("11 defend range vs cutoff opener in position")
            print("12 defend range vs cutoff opener out of position")
            print("13 defend range vs dealer button always out of position")
            print("14 defend range vs small blind always in position")
            print("15 under 10 bb push vs 1 villain")
            print("16 under 10 bb push vs 2 villains")
            print("17 under 10 bb push vs bunch of villains")
            print("18 call a push from player who has under 10bb and pushes, no one left after you")
            print("19 call a push from player who has under 10bb and pushes, one left after you to act")
            print("20 call a push from player who has under 10bb and pushes, 2+ left after you to act")
            print("q quit")
            selected = input("]")
            try:
                exitos = int(selected)
            except ValueError:
                exitos = 0
            rangename = "no range"
            selected_file = "notselected"
            if selected == '0':
                selected_file = "fishes/" + fish + "/ranges/ug_open.range"
                rangename = "ug_open.range"
            elif selected == '1':
                selected_file = "fishes/" + fish + "/ranges/hj_open.range"
                rangename = "hj_open.range"
            elif selected == '2':
                selected_file = "fishes/" + fish + "/ranges/co_open.range"
                rangename = "co_open.range"
            elif selected == '3':
                selected_file = "fishes/" + fish + "/ranges/db_open.range"
                rangename = "db_open.range"
            elif selected == '4':
                selected_file = "fishes/" + fish + "/ranges/sb_open.range"
                rangename = "sb_open.range"
            elif selected == '5':
                selected_file = "fishes/" + fish + "/ranges/hd_open.range"
                rangename = "hd_open.range"
            elif selected == '6':
                selected_file = "fishes/" + fish + "/ranges/hb_defend.range"
                rangename = "hb_defend.range"
            elif selected == '7':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_ug_ip.range"
                rangename = "defend_vs_ug_ip.range"
            elif selected == '8':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_ug_op.range"
                rangename = "defend_vs_ug_op.range"
            elif selected == '9':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_hj_ip.range"
                rangename = "defend_vs_hj_ip.range"
            elif selected == '10':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_hj_op.range"
                rangename = "defend_vs_hj_op.range"
            elif selected == '11':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_co_ip.range"
                rangename = "defend_vs_co_ip.range"
            elif selected == '12':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_co_op.range"
                rangename = "defend_vs_co_op.range"
            elif selected == '13':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_db_op.range"
                rangename = "defend_vs_db_op.range"
            elif selected == '14':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_sb_ip.range"
                rangename = "defend_vs_sb_ip.range"
            elif selected == '15':
                selected_file = "fishes/" + fish + "/ranges/under10bb_push_vs_1.range"
                rangename = "under10bb_push_vs_1.range"
            elif selected == '16':
                selected_file = "fishes/" + fish + "/ranges/under10bb_push_vs_2.range"
                rangename = "under10bb_push_vs_2.range"
            elif selected == '17':
                selected_file = "fishes/" + fish + "/ranges/under10bb_push_vs_more.range"
                rangename = "under10bb_push_vs_more.range"
            elif selected == '18':
                selected_file = "fishes/" + fish + "/ranges/call_vs_under10bb_push_0_left_behind.range"
                rangename = "call_vs_under10bb_push_0_left_behind.range"
            elif selected == '19':
                selected_file = "fishes/" + fish + "/ranges/call_vs_under10bb_push_1_left_behind.range"
                rangename = "call_vs_under10bb_push_1_left_behind.range"
            elif selected == '20':
                selected_file = "fishes/" + fish + "/ranges/call_vs_under10bb_push_more_left_behind.range"
                rangename = "call_vs_under10bb_push_more_left_behind.range"
            else:
                print("back to lobby")
                time.sleep(2)

            if selected_file != "notselected":
                lines = []
                try:
                    f = open(selected_file,'r')
                    with f:
                        lines = f.read().splitlines()
                    f.close()
                except IOError:
                    print("no such file" + selected_file)
                    time.sleep(2)
                settings.print_logo()
                print(fish + " " + rangename)
                printline1 = " "
                printline2 = " "
                printline3 = " "
                printline4 = " "
                printline5 = " "
                printline6 = " "
                printline7 = " "
                printline8 = " "
                printline9 = " "
                printline10 = " "
                printline11 = " "
                printline12 = " "
                printline13 = " "
                if 'aa' in lines:
                    printline1 += CYAN + 'AA' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'aks' in lines:
                    printline1 += 'AK' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'aqs' in lines:
                    printline1 += 'AQ' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'ajs' in lines:
                    printline1 += 'AJ' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'ats' in lines:
                    printline1 += 'AT' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'a9s' in lines:
                    printline1 += 'A9' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'a8s' in lines:
                    printline1 += 'A8' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'a7s' in lines:
                    printline1 += 'A7' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'a6s' in lines:
                    printline1 += 'A6' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'a5s' in lines:
                    printline1 += 'A5' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'a4s' in lines:
                    printline1 += 'A4' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'a3s' in lines:
                    printline1 += 'A3' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                if 'a2s' in lines:
                    printline1 += 'A2' + RESET + BLANK
                else:
                    printline1 += BLANKCELL
                #line2
                if 'ako' in lines:
                    printline2 += GREY + 'AK' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'kk' in lines:
                    printline2 += CYAN + 'KK' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'kqs' in lines:
                    printline2 += 'KQ' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'kjs' in lines:
                    printline2 += 'KJ' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'kts' in lines:
                    printline2 += 'KT' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'k9s' in lines:
                    printline2 += 'K9' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'k8s' in lines:
                    printline2 += 'K8' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'k7s' in lines:
                    printline2 += 'K7' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'k6s' in lines:
                    printline2 += 'K6' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'k5s' in lines:
                    printline2 += 'K5' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'k4s' in lines:
                    printline2 += 'K4' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'k3s' in lines:
                    printline2 += 'K3' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                if 'k2s' in lines:
                    printline2 += 'K2' + RESET + BLANK
                else:
                    printline2 += BLANKCELL
                #line3
                if 'aqo' in lines:
                    printline3 += GREY + 'AQ' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'kqo' in lines:
                    printline3 += GREY + 'KQ' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'qq' in lines:
                    printline3 += CYAN + 'QQ' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'qjs' in lines:
                    printline3 += 'QJ' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'qts' in lines:
                    printline3 += 'QT' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'q9s' in lines:
                    printline3 += 'Q9' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'q8s' in lines:
                    printline3 += 'Q8' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'q7s' in lines:
                    printline3 += 'Q7' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'q6s' in lines:
                    printline3 += 'Q6' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'q5s' in lines:
                    printline3 += 'Q5' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'q4s' in lines:
                    printline3 += 'Q4' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'q3s' in lines:
                    printline3 += 'Q3' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                if 'q2s' in lines:
                    printline3 += 'Q2' + RESET + BLANK
                else:
                    printline3 += BLANKCELL
                #line4
                if 'ajo' in lines:
                    printline4 += GREY + 'AJ' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'kjo' in lines:
                    printline4 += GREY + 'KJ' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'qjo' in lines:
                    printline4 += GREY + 'QJ' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'jj' in lines:
                    printline4 += CYAN + 'JJ' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'jts' in lines:
                    printline4 += 'JT' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'j9s' in lines:
                    printline4 += 'J9' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'j8s' in lines:
                    printline4 += 'J8' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'j7s' in lines:
                    printline4 += 'J7' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'j6s' in lines:
                    printline4 += 'J6' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'j5s' in lines:
                    printline4 += 'J5' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'j4s' in lines:
                    printline4 += 'J4' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'j3s' in lines:
                    printline4 += 'J3' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                if 'j2s' in lines:
                    printline4 += 'J2' + RESET + BLANK
                else:
                    printline4 += BLANKCELL
                #line5
                if 'ato' in lines:
                    printline5 += GREY + 'AT' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 'kto' in lines:
                    printline5 += GREY + 'KT' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 'qto' in lines:
                    printline5 += GREY + 'QT' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 'jto' in lines:
                    printline5 += GREY + 'JT' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 'tt' in lines:
                    printline5 += CYAN + 'TT' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 't9s' in lines:
                    printline5 += 'T9' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 't8s' in lines:
                    printline5 += 'T8' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 't7s' in lines:
                    printline5 += 'T7' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 't6s' in lines:
                    printline5 += 'T6' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 't5s' in lines:
                    printline5 += 'T5' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 't4s' in lines:
                    printline5 += 'T4' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 't3s' in lines:
                    printline5 += 'T3' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                if 't2s' in lines:
                    printline5 += 'T2' + RESET + BLANK
                else:
                    printline5 += BLANKCELL
                    #line6
                if 'a9o' in lines:
                    printline6 += GREY + 'A9' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if 'k9o' in lines:
                    printline6 += GREY + 'K9' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if 'q9o' in lines:
                    printline6 += GREY + 'Q9' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if 'j9o' in lines:
                    printline6 += GREY + 'J9' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if 't9o' in lines:
                    printline6 += GREY + 'T9' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if '99' in lines:
                    printline6 += CYAN + '99' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if '98s' in lines:
                    printline6 += '98' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if '97s' in lines:
                    printline6 += '97' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if '96s' in lines:
                    printline6 += '96' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if '95s' in lines:
                    printline6 += '95' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if '94s' in lines:
                    printline6 += '94' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if '93s' in lines:
                    printline6 += '93' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                if '92s' in lines:
                    printline6 += '92' + RESET + BLANK
                else:
                    printline6 += BLANKCELL
                #line7
                if 'a8o' in lines:
                    printline7 += GREY + 'A8' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if 'k8o' in lines:
                    printline7 += GREY + 'K8' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if 'q8o' in lines:
                    printline7 += GREY + 'Q8' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if 'j8o' in lines:
                    printline7 += GREY + 'J8' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if 't8o' in lines:
                    printline7 += GREY + 'T8' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if '98o' in lines:
                    printline7 += GREY + '98' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if '88' in lines:
                    printline7 += CYAN + '88' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if '87s' in lines:
                    printline7 += '87' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if '86s' in lines:
                    printline7 += '86' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if '85s' in lines:
                    printline7 += '85' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if '84s' in lines:
                    printline7 += '84' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if '83s' in lines:
                    printline7 += '83' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                if '82s' in lines:
                    printline7 += '82' + RESET + BLANK
                else:
                    printline7 += BLANKCELL
                #line8
                if 'a7o' in lines:
                    printline8 += GREY + 'A7' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if 'k7o' in lines:
                    printline8 += GREY + 'K7' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if 'q7o' in lines:
                    printline8 += GREY + 'Q7' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if 'j7o' in lines:
                    printline8 += GREY + 'J7' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if 't7o' in lines:
                    printline8 += GREY + 'T7' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if '97o' in lines:
                    printline8 += GREY + '97' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if '87o' in lines:
                    printline8 += GREY + '87' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if '77' in lines:
                    printline8 += CYAN + '77' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if '76s' in lines:
                    printline8 += '76' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if '75s' in lines:
                    printline8 += '75' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if '74s' in lines:
                    printline8 += '74' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if '73s' in lines:
                    printline8 += '73' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                if '72s' in lines:
                    printline8 += '72' + RESET + BLANK
                else:
                    printline8 += BLANKCELL
                #line9
                if 'a6o' in lines:
                    printline9 += GREY + 'A6' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if 'k6o' in lines:
                    printline9 += GREY + 'K6' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if 'q6o' in lines:
                    printline9 += GREY + 'Q6' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if 'j6o' in lines:
                    printline9 += GREY + 'J6' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if 't6o' in lines:
                    printline9 += GREY + 'T6' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if '96o' in lines:
                    printline9 += GREY + '96' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if '86o' in lines:
                    printline9 += GREY + '86' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if '76o' in lines:
                    printline9 += GREY + '76' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if '66' in lines:
                    printline9 += CYAN + '66' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if '65s' in lines:
                    printline9 += '65' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if '64s' in lines:
                    printline9 += '64' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if '63s' in lines:
                    printline9 += '63' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                if '62s' in lines:
                    printline9 += '62' + RESET + BLANK
                else:
                    printline9 += BLANKCELL
                #line10
                if 'a5o' in lines:
                    printline10 += GREY + 'A5' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if 'k5o' in lines:
                    printline10 += GREY + 'K5' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if 'q5o' in lines:
                    printline10 += GREY + 'Q5' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if 'j5o' in lines:
                    printline10 += GREY + 'J5' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if 't5o' in lines:
                    printline10 += GREY + 'T5' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if '95o' in lines:
                    printline10 += GREY + '95' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if '85o' in lines:
                    printline10 += GREY + '85' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if '75o' in lines:
                    printline10 += GREY + '75' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if '65o' in lines:
                    printline10 += GREY + '65' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if '55' in lines:
                    printline10 += CYAN + '55' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if '54s' in lines:
                    printline10 += '54' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if '53s' in lines:
                    printline10 += '53' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                if '52s' in lines:
                    printline10 += '52' + RESET + BLANK
                else:
                    printline10 += BLANKCELL
                #line11
                if 'a4o' in lines:
                    printline11 += GREY + 'A4' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if 'k4o' in lines:
                    printline11 += GREY + 'K4' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if 'q4o' in lines:
                    printline11 += GREY + 'Q4' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if 'j4o' in lines:
                    printline11 += GREY + 'J4' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if 't4o' in lines:
                    printline11 += GREY + 'T4' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if '94o' in lines:
                    printline11 += GREY + '94' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if '84o' in lines:
                    printline11 += GREY + '84' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if '74o' in lines:
                    printline11 += GREY + '74' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if '64o' in lines:
                    printline11 += GREY + '64' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if '54o' in lines:
                    printline11 += GREY + '54' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if '44' in lines:
                    printline11 += CYAN + '44' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if '43s' in lines:
                    printline11 += '43' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                if '42s' in lines:
                    printline11 += '42' + RESET + BLANK
                else:
                    printline11 += BLANKCELL
                #line12
                if 'a3o' in lines:
                    printline12 += GREY + 'A3' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if 'k3o' in lines:
                    printline12 += GREY + 'K3' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if 'q3o' in lines:
                    printline12 += GREY + 'Q3' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if 'j3o' in lines:
                    printline12 += GREY + 'J3' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if 't3o' in lines:
                    printline12 += GREY + 'T3' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if '93o' in lines:
                    printline12 += GREY + '93' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if '83o' in lines:
                    printline12 += GREY + '83' + RESET + BLANK
                else:  
                    printline12 += BLANKCELL
                if '73o' in lines:
                    printline12 += GREY + '73' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if '63o' in lines:
                    printline12 += GREY + '63' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if '53o' in lines:
                    printline12 += GREY + '53' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if '43o' in lines:
                    printline12 += GREY + '43' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if '33' in lines:
                    printline12 += CYAN + '33' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                if '32s' in lines:
                    printline12 += '32' + RESET + BLANK
                else:
                    printline12 += BLANKCELL
                #line13
                if 'a2o' in lines:
                    printline13 += GREY + 'A2' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if 'k2o' in lines:
                    printline13 += GREY + 'K2' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if 'q2o' in lines:
                    printline13 += GREY + 'Q2' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if 'j2o' in lines:
                    printline13 += GREY + 'J2' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if 't2o' in lines:
                    printline13 += GREY + 'T2' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if '92o' in lines:
                    printline13 += GREY + '92' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if '82o' in lines:
                    printline13 += GREY + '82' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if '72o' in lines:
                    printline13 += GREY + '72' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if '62o' in lines:
                    printline13 += GREY + '62' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if '52o' in lines:
                    printline13 += GREY + '52' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if '42o' in lines:
                    printline13 += GREY + '42' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if '32o' in lines:
                    printline13 += GREY + '32' + RESET + BLANK
                else:
                    printline13 += BLANKCELL
                if '22' in lines:
                    printline13 += CYAN + '22' + RESET + BLANK
                else:
                    printline13 += BLANKCELL

                print(" ")
                print(printline1)
                print(printline2)
                print(printline3)
                print(printline4)
                print(printline5)
                print(printline6)
                print(printline7)
                print(printline8)
                print(printline9)
                print(printline10)
                print(printline11)
                print(printline12)
                print(printline13)
                print(" ")
                dumb = input("]")