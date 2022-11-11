#copyright (c) 2019
#jodathecoda@yahoo.com

import os
import time
import settings
import checkhands

BLANK = " "
BLANKCELL = '   '
CYAN = ""
GREY = ""
RESET = ""

def editrange():
    settings.printfishes(settings.allfishes)
    lines = []
    fish = input("enter fish name: ")
    if fish not in settings.allfishes:
        print("unknown fish")
        time.sleep(2)
        settings.print_logo()
    elif fish in settings.referencefishes:
        settings.print_logo()
        if (fish == "milkfish" or fish == "yellowfish"):
            print(fish + " is a reference fish - can not be modified")
            print("back to main menu")
            time.sleep(2)
        elif fish == "redfish":
            settings.print_logo()
            get_out = 1
            while(get_out):
                settings.print_logo()
                print("select Heads Up Analyzer range to edit:")
                print("1  heads up dealer open")
                print("2  heads up dealer call 3bet")
                print("q  quit")
                selected = input("]")
                selected_file = "notselected"
                selected_range = "no range"
                if selected == '1':
                    selected_file = "fishes/" + fish + "/ranges/hd_openAnalyzer.range"
                    selected_range = "hd_openAnalyzer.range"
                elif selected == '2':
                    selected_file = "fishes/" + fish + "/ranges/hd_call3betAnalyzer.range"
                    selected_range = "hd_call3betAnalyzer.range"
                else:
                    print("back to main menu")
                    time.sleep(2)
                    get_out = 0
                if selected_file != "notselected":
                    try:
                        f = open(selected_file,'r')
                        with f:
                            lines = f.read().splitlines()
                        f.close()
                    except IOError:
                        print("no such file" + selected_file)
                        dumb = input("]")
                    if settings.colors_on:
                        print_color_range_lines(lines)
                    else:
                        print_range_lines(lines)
                    candidate = ""
                    while(candidate != 'q'):
                        settings.print_logo()
                        print(fish + " " + selected_range)
                        print("add/remove cards to this range. 'q' to quit. example: aks kjo tt 32o")
                        if settings.colors_on:
                            print_color_range_lines(lines)
                        else:
                            print_range_lines(lines)
                        candidate = input("]")
                        if candidate == 'q':
                            pass
                        elif candidate in settings.allcards:
                            if candidate not in lines:
                                lines.append(candidate)
                                if settings.colors_on:
                                    print_color_range_lines(lines)
                                else:
                                    print_range_lines(lines)
                            else:
                                lines.remove(candidate)
                                if settings.colors_on:
                                    print_color_range_lines(lines)
                                else:
                                    print_range_lines(lines)
                        else:
                            print("not valid")
                            time.sleep(2)
                    try:
                        f = open(selected_file,'w')
                        with f:
                            for counter in range(0,len(lines)):
                                f.write(lines[counter] + "\n")
                                
                        f.close()
                        settings.pokerpool.update_all()
                    except IOError:
                        print("no such file" + selected_file)
                        dumb = input("]")

        elif fish == "blackfish":
            get_out = 1
            while(get_out):
                settings.print_logo()
                print("select range to edit:")
                print("3  heads up big blind call")
                print("4  heads up big blind 3bet")
                print("q  quit")
                selected = input("]")
                selected_file = "notselected"
                selected_range = "no range"
                if selected == '3':
                    selected_file = "fishes/" + fish + "/ranges/hb_callAnalyzer.range"
                    selected_range = "hb_callAnalyzer.range"
                elif selected == '4':
                    selected_file = "fishes/" + fish + "/ranges/hb_3betAnalyzer.range"
                    selected_range = "hb_3betAnalyzer.range"
                else:
                    print("back to main menu")
                    time.sleep(2)
                    get_out = 0
                if selected_file != "notselected":
                    try:
                        f = open(selected_file,'r')
                        with f:
                            lines = f.read().splitlines()
                        f.close()
                    except IOError:
                        print("no such file" + selected_file)
                        dumb = input("]")
                    if settings.colors_on:
                        print_color_range_lines(lines)
                    else:
                        print_range_lines(lines)
                    candidate = ""
                    while(candidate != 'q'):
                        settings.print_logo()
                        print(fish + " " + selected_range)
                        print("add/remove cards to this range. 'q' to quit. example: aks kjo tt 32o")
                        if settings.colors_on:
                            print_color_range_lines(lines)
                        else:
                            print_range_lines(lines)
                        candidate = input("]")
                        if candidate == 'q':
                            pass
                        elif candidate in settings.allcards:
                            if candidate not in lines:
                                lines.append(candidate)
                                if settings.colors_on:
                                    print_color_range_lines(lines)
                                else:
                                    print_range_lines(lines)
                            else:
                                lines.remove(candidate)
                                if settings.colors_on:
                                    print_color_range_lines(lines)
                                else:
                                    print_range_lines(lines)
                        else:
                            print("not valid")
                            time.sleep(2)
                    try:
                        f = open(selected_file,'w')
                        with f:
                            for counter in range(0,len(lines)):
                                f.write(lines[counter] + "\n")
                                
                        f.close()
                        settings.pokerpool.update_all()
                    except IOError:
                        print("no such file" + selected_file)
                        dumb = input("]")
        else:
            print("back to main menu")
            time.sleep(2)
    else:
        get_out = 1
        while(get_out):
            settings.print_logo()
            print("select range to edit:")
            print("0  ug open")
            print("1  hj open")
            print("2  co open")
            print("3  dealer open")
            print("4  sb open")
            print("5  heads up dealer open")
            print("6  heads up big blind defend")
            print("7  defend vs ug in position")
            print("8  defend vs ug out of position")
            print("9  defend vs hijack in position")
            print("10 defend vs hijack out of position")
            print("11 defend vs cutoff in position")
            print("12 defend vs cutoff out of position")
            print("13 defend vs dealer button")
            print("14 defend vs small blind")
            print("15 under 10 bb push vs 1 villain")
            print("16 under 10 bb push vs 2 villains")
            print("17 under 10 bb push vs 3+ villains")
            print("18 call under 10bb push, no one left after you to act")
            print("19 call under 10bb push, one left after you to act")
            print("20 call under 10bb push, 2+ left after you to act")
            print("q  quit")
            selected = input("]")
            selected_file = "notselected"
            selected_range = "no range"
            if selected == '0':
                selected_file = "fishes/" + fish + "/ranges/ug_open.range"
                selected_range = "ug_open.range"
            elif selected == '1':
                selected_file = "fishes/" + fish + "/ranges/hj_open.range"
                selected_range = "hj_open.range"
            elif selected == '2':
                selected_file = "fishes/" + fish + "/ranges/co_open.range"
                selected_range = "co_open.range"
            elif selected == '3':
                selected_file = "fishes/" + fish + "/ranges/db_open.range"
                selected_range = "db_open.range"
            elif selected == '4':
                selected_file = "fishes/" + fish + "/ranges/sb_open.range"
                selected_range = "sb_open.range"
            elif selected == '5':
                selected_file = "fishes/" + fish + "/ranges/hd_open.range"
                selected_range =" hd_open.range"
            elif selected == '6':
                selected_file = "fishes/" + fish + "/ranges/hb_defend.range"
                selected_range = "hb_defend.range"
            elif selected == '7':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_ug_ip.range"
                selected_range = "defend_vs_ug_ip.range"
            elif selected == '8':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_ug_op.range"
                selected_range = "defend_vs_ug_op.range"
            elif selected == '9':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_hj_ip.range"
                selected_range = "defend_vs_hj_ip.range"
            elif selected == '10':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_hj_op.range"
                selected_range = "defend_vs_hj_op.range"
            elif selected == '11':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_co_ip.range"
                selected_range = "defend_vs_co_ip.range"
            elif selected == '12':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_co_op.range"
                selected_range = "defend_vs_co_op.range"
            elif selected == '13':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_db_op.range"
                selected_range = "defend_vs_db_op.range"
            elif selected == '14':
                selected_file = "fishes/" + fish + "/ranges/defend_vs_sb_ip.range"
                selected_range = "defend_vs_sb_ip.range"
            elif selected == '15':
                selected_file = "fishes/" + fish + "/ranges/under10bb_push_vs_1.range"
                selected_range = "under10bb_push_vs_1.range"
            elif selected == '16':
                selected_file = "fishes/" + fish + "/ranges/under10bb_push_vs_2.range"
                selected_range = "under10bb_push_vs_2.range"
            elif selected == '17':
                selected_file = "fishes/" + fish + "/ranges/under10bb_push_vs_more.range"
                selected_range = "under10bb_push_vs_more.range"
            elif selected == '18':
                selected_file = "fishes/" + fish + "/ranges/call_vs_under10bb_push_0_left_behind.range"
                selected_range = "call_vs_under10bb_push_0_left_behind.range"
            elif selected == '19':
                selected_file = "fishes/" + fish + "/ranges/call_vs_under10bb_push_1_left_behind.range"
                selected_range = "call_vs_under10bb_push_1_left_behind.range"
            elif selected == '20':
                selected_file = "fishes/" + fish + "/ranges/call_vs_under10bb_push_more_left_behind.range"
                selected_range = "call_vs_under10bb_push_more_left_behind.range"
            else:
                print("back to main menu")
                time.sleep(2)
                get_out = 0
            if selected_file != "notselected":
                try:
                    f = open(selected_file,'r')
                    with f:
                        lines = f.read().splitlines()
                    f.close()
                except IOError:
                    print("no such file" + selected_file)
                    dumb = input("]")
                if settings.colors_on:
                    print_color_range_lines(lines)
                else:
                    print_range_lines(lines)
                candidate = ""
                while(candidate != 'q'):
                    settings.print_logo()
                    print(fish + " " + selected_range)
                    print("add/remove cards to this range. 'q' to quit. example: aks kjo tt 32o")
                    if settings.colors_on:
                        print_color_range_lines(lines)
                    else:
                        print_range_lines(lines)
                    candidate = input("]")
                    if candidate == 'q':
                        pass
                    elif candidate in settings.allcards:
                        if candidate not in lines:
                            lines.append(candidate)
                            if settings.colors_on:
                                print_color_range_lines(lines)
                            else:
                                print_range_lines(lines)
                        else:
                            lines.remove(candidate)
                            if settings.colors_on:
                                print_color_range_lines(lines)
                            else:
                                print_range_lines(lines)
                    else:
                        print("not valid")
                        time.sleep(2)
                try:
                    f = open(selected_file,'w')
                    with f:
                        for counter in range(0,len(lines)):
                            f.write(lines[counter] + "\n")
                            
                    f.close()
                    settings.pokerpool.update_all()
                except IOError:
                    print("no such file" + selected_file)
                    dumb = input("]")


def print_range_lines(liness):
            lines = liness
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
                printline1 += 'AA' + RESET + BLANK
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
            
def print_debug_color_ranges(card1, card2, calling_range, raising_range, open_range):
    if settings.colors_on:
        RED = '\033[1;31m'
        BLUE  = '\033[1;34m'
        CYAN  = '\033[1;36m'
        GREEN = '\033[0;32m'
        RESET = '\033[0;0m'
        BOLD  = '\033[;1m'
        REVERSE = '\033[;7m'
        GREY = '\033[1;30m'
        YELLOW ='\033[0;33m'
        RESET = '\033[0m'
        hand = card1 + card2
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
        #line1
        #aa
        if checkhands.pocket_pairs(hand) and card1[0] == 'a':
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'AA' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'AA' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'AA' + RESET + BLANK
            else:
                printline1 += GREY + 'AA' + RESET + BLANK
        elif 'aa' in raising_range:
            printline1 += RED + 'AA' + RESET + BLANK
        elif 'aa' in calling_range:
            printline1 += BLUE + 'AA' + RESET + BLANK
        elif 'aa' in open_range:
            printline1 += GREEN + 'AA' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #aks
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == 'k' or card1[0] == 'k' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'AK' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'AK' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'AK' + RESET + BLANK
            else:
                printline1 += GREY + 'AK' + RESET + BLANK
        elif 'aks' in raising_range:
            printline1 += RED + 'AK' + RESET + BLANK
        elif 'aks' in calling_range:
            printline1 += BLUE + 'AK' + RESET + BLANK
        elif 'aks' in open_range:
            printline1 += GREEN + 'AK' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #aqs
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == 'q' or card1[0] == 'q' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'AQ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'AQ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'AQ' + RESET + BLANK
            else:
                printline1 += GREY + 'AQ' + RESET + BLANK
        elif 'aqs' in raising_range:
            printline1 += RED + 'AQ' + RESET + BLANK
        elif 'aqs' in calling_range:
            printline1 += BLUE + 'AQ' + RESET + BLANK
        elif 'aqs' in open_range:
            printline1 += GREEN + 'AQ' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #ajs
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == 'j' or card1[0] == 'j' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'AJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'AJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'AJ' + RESET + BLANK
            else:
                printline1 += GREY + 'AJ' + RESET + BLANK
        elif 'ajs' in raising_range:
            printline1 += RED + 'AJ' + RESET + BLANK
        elif 'ajs' in calling_range:
            printline1 += BLUE + 'AJ' + RESET + BLANK
        elif 'ajs' in open_range:
            printline1 += GREEN + 'AJ' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #ats
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == 't' or card1[0] == 't' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'AT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'AT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'AT' + RESET + BLANK
            else:
                printline1 += GREY + 'AT' + RESET + BLANK
        elif 'ats' in raising_range:
            printline1 += RED + 'AT' + RESET + BLANK
        elif 'ats' in calling_range:
            printline1 += BLUE + 'AT' + RESET + BLANK
        elif 'ats' in open_range:
            printline1 += GREEN + 'AT' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #a9s
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == '9' or card1[0] == '9' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'A9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'A9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'A9' + RESET + BLANK
            else:
                printline1 += GREY + 'A9' + RESET + BLANK
        elif 'a9s' in raising_range:
            printline1 += RED + 'A9' + RESET + BLANK
        elif 'a9s' in calling_range:
            printline1 += BLUE + 'A9' + RESET + BLANK
        elif 'a9s' in open_range:
            printline1 += GREEN + 'A9' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #a8s
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == '8' or card1[0] == '8' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'A8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'A8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'A8' + RESET + BLANK
            else:
                printline1 += GREY + 'A8' + RESET + BLANK
        elif 'a8s' in raising_range:
            printline1 += RED + 'A8' + RESET + BLANK
        elif 'a8s' in calling_range:
            printline1 += BLUE + 'A8' + RESET + BLANK
        elif 'a8s' in open_range:
            printline1 += GREEN + 'A8' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #a7s
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == '7' or card1[0] == '7' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'A7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'A7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'A7' + RESET + BLANK
            else:
                printline1 += GREY + 'A7' + RESET + BLANK
        elif 'a7s' in raising_range:
            printline1 += RED + 'A7' + RESET + BLANK
        elif 'a7s' in calling_range:
            printline1 += BLUE + 'A7' + RESET + BLANK
        elif 'a7s' in open_range:
            printline1 += GREEN + 'A7' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #a6s
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == '6' or card1[0] == '6' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'A6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'A6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'A6' + RESET + BLANK
            else:
                printline1 += GREY + 'A6' + RESET + BLANK
        elif 'a6s' in raising_range:
            printline1 += RED + 'A6' + RESET + BLANK
        elif 'a6s' in calling_range:
            printline1 += BLUE + 'A6' + RESET + BLANK
        elif 'a6s' in open_range:
            printline1 += GREEN + 'A6' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #a5s
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == '5' or card1[0] == '5' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'A5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'A5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'A5' + RESET + BLANK
            else:
                printline1 += GREY + 'A5' + RESET + BLANK
        elif 'a5s' in raising_range:
            printline1 += RED + 'A5' + RESET + BLANK
        elif 'a5s' in calling_range:
            printline1 += BLUE + 'A5' + RESET + BLANK
        elif 'a5s' in open_range:
            printline1 += GREEN + 'A5' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #a4s
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == '4' or card1[0] == '4' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'A4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'A4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'A4' + RESET + BLANK
            else:
                printline1 += GREY + 'A4' + RESET + BLANK
        elif 'a4s' in raising_range:
            printline1 += RED + 'A4' + RESET + BLANK
        elif 'a4s' in calling_range:
            printline1 += BLUE + 'A4' + RESET + BLANK
        elif 'a4s' in open_range:
            printline1 += GREEN + 'A4' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #a3s
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == '3' or card1[0] == '3' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'A3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'A3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'A3' + RESET + BLANK
            else:
                printline1 += GREY + 'A3' + RESET + BLANK
        elif 'a3s' in raising_range:
            printline1 += RED + 'A3' + RESET + BLANK
        elif 'a3s' in calling_range:
            printline1 += BLUE + 'A3' + RESET + BLANK
        elif 'a3s' in open_range:
            printline1 += GREEN + 'A3' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #a2s
        if checkhands.suited(hand) and (card1[0] == 'a' and card2[0] == '2' or card1[0] == '2' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline1 += YELLOW + 'A2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline1 += CYAN + 'A2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline1 += CYAN + 'A2' + RESET + BLANK
            else:
                printline1 += GREY + 'A2' + RESET + BLANK
        elif 'a2s' in raising_range:
            printline1 += RED + 'A2' + RESET + BLANK
        elif 'a2s' in calling_range:
            printline1 += BLUE + 'A2' + RESET + BLANK
        elif 'a2s' in open_range:
            printline1 += GREEN + 'A2' + RESET + BLANK
        else:
            printline1 += BLANKCELL
        #line2
        #ako
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == 'k' or card1[0] == 'k' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'AK' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'AK' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'AK' + RESET + BLANK
            else:
                printline2 += GREY + 'AK' + RESET + BLANK
        elif 'ako' in raising_range:
            printline2 += RED + 'AK' + RESET + BLANK
        elif 'ako' in calling_range:
            printline2 += BLUE + 'AK' + RESET + BLANK
        elif 'ako' in open_range:
            printline2 += GREEN + 'AK' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #kk
        if checkhands.pocket_pairs(hand) and (card1[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'KK' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'KK' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'KK' + RESET + BLANK
            else:
                printline2 += GREY + 'KK' + RESET + BLANK
        elif 'kk' in raising_range:
            printline2 += RED + 'KK' + RESET + BLANK
        elif 'kk' in calling_range:
            printline2 += BLUE + 'KK' + RESET + BLANK
        elif 'kk' in open_range:
            printline2 += GREEN + 'KK' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #kqs
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == 'q' or card1[0] == 'q' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'KQ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'KQ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'KQ' + RESET + BLANK
            else:
                printline2 += GREY + 'KQ' + RESET + BLANK
        elif 'kqs' in raising_range:
            printline2 += RED + 'KQ' + RESET + BLANK
        elif 'kqs' in calling_range:
            printline2 += BLUE + 'KQ' + RESET + BLANK
        elif 'kqs' in open_range:
            printline2 += GREEN + 'KQ' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #kjs
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == 'j' or card1[0] == 'j' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'KJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'KJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'KJ' + RESET + BLANK
            else:
                printline2 += GREY + 'KJ' + RESET + BLANK
        elif 'kjs' in raising_range:
            printline2 += RED + 'KJ' + RESET + BLANK
        elif 'kjs' in calling_range:
            printline2 += BLUE + 'KJ' + RESET + BLANK
        elif 'kjs' in open_range:
            printline2 += GREEN + 'KJ' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #kts
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == 't' or card1[0] == 't' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'KT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'KT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'KT' + RESET + BLANK
            else:
                printline2 += GREY + 'KT' + RESET + BLANK
        elif 'kts' in raising_range:
            printline2 += RED + 'KT' + RESET + BLANK
        elif 'kts' in calling_range:
            printline2 += BLUE + 'KT' + RESET + BLANK
        elif 'kts' in open_range:
            printline2 += GREEN + 'KT' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #k9s
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == '9' or card1[0] == '9' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'K9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'K9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'K9' + RESET + BLANK
            else:
                printline2 += GREY + 'K9' + RESET + BLANK
        elif 'k9s' in raising_range:
            printline2 += RED + 'K9' + RESET + BLANK
        elif 'k9s' in calling_range:
            printline2 += BLUE + 'K9' + RESET + BLANK
        elif 'k9s' in open_range:
            printline2 += GREEN + 'K9' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #k8s
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == '8' or card1[0] == '8' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'K8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'K8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'K8' + RESET + BLANK
            else:
                printline2 += GREY + 'K8' + RESET + BLANK
        elif 'k8s' in raising_range:
            printline2 += RED + 'K8' + RESET + BLANK
        elif 'k8s' in calling_range:
            printline2 += BLUE + 'K8' + RESET + BLANK
        elif 'k8s' in open_range:
            printline2 += GREEN + 'K8' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #k7s
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == '7' or card1[0] == '7' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'K7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'K7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'K7' + RESET + BLANK
            else:
                printline2 += GREY + 'K7' + RESET + BLANK
        elif 'k7s' in raising_range:
            printline2 += RED + 'K7' + RESET + BLANK
        elif 'k7s' in calling_range:
            printline2 += BLUE + 'K7' + RESET + BLANK
        elif 'k7s' in open_range:
            printline2 += GREEN + 'K7' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #k6s
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == '6' or card1[0] == '6' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'K6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'K6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'K6' + RESET + BLANK
            else:
                printline2 += GREY + 'K6' + RESET + BLANK
        elif 'k6s' in raising_range:
            printline2 += RED + 'K6' + RESET + BLANK
        elif 'k6s' in calling_range:
            printline2 += BLUE + 'K6' + RESET + BLANK
        elif 'k6s' in open_range:
            printline2 += GREEN + 'K6' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #k5s
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == '5' or card1[0] == '5' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'K5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'K5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'K5' + RESET + BLANK
            else:
                printline2 += GREY + 'K5' + RESET + BLANK
        elif 'k5s' in raising_range:
            printline2 += RED + 'K5' + RESET + BLANK
        elif 'k5s' in calling_range:
            printline2 += BLUE + 'K5' + RESET + BLANK
        elif 'k5s' in open_range:
            printline2 += GREEN + 'K5' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #k4s
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == '4' or card1[0] == '4' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'K4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'K4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'K4' + RESET + BLANK
            else:
                printline2 += GREY + 'K4' + RESET + BLANK
        elif 'k4s' in raising_range:
            printline2 += RED + 'K4' + RESET + BLANK
        elif 'k4s' in calling_range:
            printline2 += BLUE + 'K4' + RESET + BLANK
        elif 'k4s' in open_range:
            printline2 += GREEN + 'K4' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #k3s
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == '3' or card1[0] == '3' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'K3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'K3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'K3' + RESET + BLANK
            else:
                printline2 += GREY + 'K3' + RESET + BLANK
        elif 'k3s' in raising_range:
            printline2 += RED + 'K3' + RESET + BLANK
        elif 'k3s' in calling_range:
            printline2 += BLUE + 'K3' + RESET + BLANK
        elif 'k3s' in open_range:
            printline2 += GREEN + 'K3' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #k2s
        if checkhands.suited(hand) and (card1[0] == 'k' and card2[0] == '2' or card1[0] == '2' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline2 += YELLOW + 'K2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline2 += CYAN + 'K2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline2 += CYAN + 'K2' + RESET + BLANK
            else:
                printline2 += GREY + 'K2' + RESET + BLANK
        elif 'k2s' in raising_range:
            printline2 += RED + 'K2' + RESET + BLANK
        elif 'k2s' in calling_range:
            printline2 += BLUE + 'K2' + RESET + BLANK
        elif 'k2s' in open_range:
            printline2 += GREEN + 'K2' + RESET + BLANK
        else:
            printline2 += BLANKCELL
        #line3
        #aqo
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == 'q' or card1[0] == 'q' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'AQ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'AQ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'AQ' + RESET + BLANK
            else:
                printline3 += GREY + 'AQ' + RESET + BLANK
        elif 'aqo' in raising_range:
            printline3 += RED + 'AQ' + RESET + BLANK
        elif 'aqo' in calling_range:
            printline3 += BLUE + 'AQ' + RESET + BLANK
        elif 'aqo' in open_range:
            printline3 += GREEN + 'AQ' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #kqo
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == 'q' or card1[0] == 'q' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'KQ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'KQ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'KQ' + RESET + BLANK
            else:
                printline3 += GREY + 'KQ' + RESET + BLANK
        elif 'kqo' in raising_range:
            printline3 += RED + 'KQ' + RESET + BLANK
        elif 'kqo' in calling_range:
            printline3 += BLUE + 'KQ' + RESET + BLANK
        elif 'kqo' in open_range:
            printline3 += GREEN + 'KQ' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #qq
        if checkhands.pocket_pairs(hand) and (card1[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'QQ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'QQ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'QQ' + RESET + BLANK
            else:
                printline3 += GREY + 'QQ' + RESET + BLANK
        elif 'qq' in raising_range:
            printline3 += RED + 'QQ' + RESET + BLANK
        elif 'qq' in calling_range:
            printline3 += BLUE + 'QQ' + RESET + BLANK
        elif 'qq' in open_range:
            printline3 += GREEN + 'QQ' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #qjs
        if checkhands.suited(hand) and (card1[0] == 'q' and card2[0] == 'j' or card1[0] == 'j' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'QJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'QJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'QJ' + RESET + BLANK
            else:
                printline3 += GREY + 'QJ' + RESET + BLANK
        elif 'qjs' in raising_range:
            printline3 += RED + 'QJ' + RESET + BLANK
        elif 'qjs' in calling_range:
            printline3 += BLUE + 'QJ' + RESET + BLANK
        elif 'qjs' in open_range:
            printline3 += GREEN + 'QJ' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #qts
        if checkhands.suited(hand) and (card1[0] == 'q' and card2[0] == 't' or card1[0] == 't' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'QT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'QT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'QT' + RESET + BLANK
            else:
                printline3 += GREY + 'QT' + RESET + BLANK
        elif 'qts' in raising_range:
            printline3 += RED + 'QT' + RESET + BLANK
        elif 'qts' in calling_range:
            printline3 += BLUE + 'QT' + RESET + BLANK
        elif 'qts' in open_range:
            printline3 += GREEN + 'QT' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #q9s
        if checkhands.suited(hand) and (card1[0] == 'q' and card2[0] == '9' or card1[0] == '9' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'Q9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'Q9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'Q9' + RESET + BLANK
            else:
                printline3 += GREY + 'Q9' + RESET + BLANK
        elif 'q9s' in raising_range:
            printline3 += RED + 'Q9' + RESET + BLANK
        elif 'q9s' in calling_range:
            printline3 += BLUE + 'Q9' + RESET + BLANK
        elif 'q9s' in open_range:
            printline3 += GREEN + 'Q9' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #q8s
        if checkhands.suited(hand) and (card1[0] == 'q' and card2[0] == '8' or card1[0] == '8' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'Q8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'Q8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'Q8' + RESET + BLANK
            else:
                printline3 += GREY + 'Q8' + RESET + BLANK
        elif 'q8s' in raising_range:
            printline3 += RED + 'Q8' + RESET + BLANK
        elif 'q8s' in calling_range:
            printline3 += BLUE + 'Q8' + RESET + BLANK
        elif 'q8s' in open_range:
            printline3 += GREEN + 'Q8' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #q7s
        if checkhands.suited(hand) and (card1[0] == 'q' and card2[0] == '7' or card1[0] == '7' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'Q7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'Q7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'Q7' + RESET + BLANK
            else:
                printline3 += GREY + 'Q7' + RESET + BLANK
        elif 'q7s' in raising_range:
            printline3 += RED + 'Q7' + RESET + BLANK
        elif 'q7s' in calling_range:
            printline3 += BLUE + 'Q7' + RESET + BLANK
        elif 'q7s' in open_range:
            printline3 += GREEN + 'Q7' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #q6s
        if checkhands.suited(hand) and (card1[0] == 'q' and card2[0] == '6' or card1[0] == '6' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'Q6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'Q6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'Q6' + RESET + BLANK
            else:
                printline3 += GREY + 'Q6' + RESET + BLANK
        elif 'q6s' in raising_range:
            printline3 += RED + 'Q6' + RESET + BLANK
        elif 'q6s' in calling_range:
            printline3 += BLUE + 'Q6' + RESET + BLANK
        elif 'q6s' in open_range:
            printline3 += GREEN + 'Q6' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #q5s
        if checkhands.suited(hand) and (card1[0] == 'q' and card2[0] == '5' or card1[0] == '5' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'Q5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'Q5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'Q5' + RESET + BLANK
            else:
                printline3 += GREY + 'Q5' + RESET + BLANK
        elif 'q5s' in raising_range:
            printline3 += RED + 'Q5' + RESET + BLANK
        elif 'q5s' in calling_range:
            printline3 += BLUE + 'Q5' + RESET + BLANK
        elif 'q5s' in open_range:
            printline3 += GREEN + 'Q5' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #q4s
        if checkhands.suited(hand) and (card1[0] == 'q' and card2[0] == '4' or card1[0] == '4' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'Q4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'Q4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'Q4' + RESET + BLANK
            else:
                printline3 += GREY + 'Q4' + RESET + BLANK
        elif 'q4s' in raising_range:
            printline3 += RED + 'Q4' + RESET + BLANK
        elif 'q4s' in calling_range:
            printline3 += BLUE + 'Q4' + RESET + BLANK
        elif 'q4s' in open_range:
            printline3 += GREEN + 'Q4' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #q3s
        if checkhands.suited(hand) and (card1[0] == 'q' and card2[0] == '3' or card1[0] == '3' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'Q3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'Q3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'Q3' + RESET + BLANK
            else:
                printline3 += GREY + 'Q3' + RESET + BLANK
        elif 'q3s' in raising_range:
            printline3 += RED + 'Q3' + RESET + BLANK
        elif 'q3s' in calling_range:
            printline3 += BLUE + 'Q3' + RESET + BLANK
        elif 'q3s' in open_range:
            printline3 += GREEN + 'Q3' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #q2s
        if checkhands.suited(hand) and (card1[0] == 'q' and card2[0] == '2' or card1[0] == '2' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline3 += YELLOW + 'Q2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline3 += CYAN + 'Q2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline3 += CYAN + 'Q2' + RESET + BLANK
            else:
                printline3 += GREY + 'Q2' + RESET + BLANK
        elif 'q2s' in raising_range:
            printline3 += RED + 'Q2' + RESET + BLANK
        elif 'q2s' in calling_range:
            printline3 += BLUE + 'Q2' + RESET + BLANK
        elif 'q2s' in open_range:
            printline3 += GREEN + 'Q2' + RESET + BLANK
        else:
            printline3 += BLANKCELL
        #line4
        #ajo
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == 'j' or card1[0] == 'j' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'AJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'AJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'AJ' + RESET + BLANK
            else:
                printline4 += GREY + 'AJ' + RESET + BLANK
        elif 'ajo' in raising_range:
            printline4 += RED + 'AJ' + RESET + BLANK
        elif 'ajo' in calling_range:
            printline4 += BLUE + 'AJ' + RESET + BLANK
        elif 'ajo' in open_range:
            printline4 += GREEN + 'AJ' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #kjo
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == 'j' or card1[0] == 'j' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'KJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'KJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'KJ' + RESET + BLANK
            else:
                printline4 += GREY + 'KJ' + RESET + BLANK
        elif 'kjo' in raising_range:
            printline4 += RED + 'KJ' + RESET + BLANK
        elif 'kjo' in calling_range:
            printline4 += BLUE + 'KJ' + RESET + BLANK
        elif 'kjo' in open_range:
            printline4 += GREEN + 'KJ' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #qjo
        if (not checkhands.suited(hand)) and (card1[0] == 'q' and card2[0] == 'j' or card1[0] == 'j' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'QJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'QJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'QJ' + RESET + BLANK
            else:
                printline4 += GREY + 'QJ' + RESET + BLANK
        elif 'qjo' in raising_range:
            printline4 += RED + 'QJ' + RESET + BLANK
        elif 'qjo' in calling_range:
            printline4 += BLUE + 'QJ' + RESET + BLANK
        elif 'qjo' in open_range:
            printline4 += GREEN + 'QJ' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #jj
        if checkhands.pocket_pairs(hand) and (card1[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'JJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'JJ' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'JJ' + RESET + BLANK
            else:
                printline4 += GREY + 'JJ' + RESET + BLANK
        elif 'jj' in raising_range:
            printline4 += RED + 'JJ' + RESET + BLANK
        elif 'jj' in calling_range:
            printline4 += BLUE + 'JJ' + RESET + BLANK
        elif 'jj' in open_range:
            printline4 += GREEN + 'JJ' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #jts
        if checkhands.suited(hand) and (card1[0] == 'j' and card2[0] == 't' or card1[0] == 't' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'JT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'JT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'JT' + RESET + BLANK
            else:
                printline4 += GREY + 'JT' + RESET + BLANK
        elif 'jts' in raising_range:
            printline4 += RED + 'JT' + RESET + BLANK
        elif 'jts' in calling_range:
            printline4 += BLUE + 'JT' + RESET + BLANK
        elif 'jts' in open_range:
            printline4 += GREEN + 'JT' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #j9s
        if checkhands.suited(hand) and (card1[0] == 'j' and card2[0] == '9' or card1[0] == '9' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'J9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'J9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'J9' + RESET + BLANK
            else:
                printline4 += GREY + 'J9' + RESET + BLANK
        elif 'j9s' in raising_range:
            printline4 += RED + 'J9' + RESET + BLANK
        elif 'j9s' in calling_range:
            printline4 += BLUE + 'J9' + RESET + BLANK
        elif 'j9s' in open_range:
            printline4 += GREEN + 'J9' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #j8s
        if checkhands.suited(hand) and (card1[0] == 'j' and card2[0] == '8' or card1[0] == '8' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'J8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'J8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'J8' + RESET + BLANK
            else:
                printline4 += GREY + 'J8' + RESET + BLANK
        elif 'j8s' in raising_range:
            printline4 += RED + 'J8' + RESET + BLANK
        elif 'j8s' in calling_range:
            printline4 += BLUE + 'J8' + RESET + BLANK
        elif 'j8s' in open_range:
            printline4 += GREEN + 'J8' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #j7s
        if checkhands.suited(hand) and (card1[0] == 'j' and card2[0] == '7' or card1[0] == '7' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'J7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'J7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'J7' + RESET + BLANK
            else:
                printline4 += GREY + 'J7' + RESET + BLANK
        elif 'j7s' in raising_range:
            printline4 += RED + 'J7' + RESET + BLANK
        elif 'j7s' in calling_range:
            printline4 += BLUE + 'J7' + RESET + BLANK
        elif 'j7s' in open_range:
            printline4 += GREEN + 'J7' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #j6s
        if checkhands.suited(hand) and (card1[0] == 'j' and card2[0] == '6' or card1[0] == '6' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'J6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'J6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'J6' + RESET + BLANK
            else:
                printline4 += GREY + 'J6' + RESET + BLANK
        elif 'j6s' in raising_range:
            printline4 += RED + 'J6' + RESET + BLANK
        elif 'j6s' in calling_range:
            printline4 += BLUE + 'J6' + RESET + BLANK
        elif 'j6s' in open_range:
            printline4 += GREEN + 'J6' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #j5s
        if checkhands.suited(hand) and (card1[0] == 'j' and card2[0] == '5' or card1[0] == '5' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'J5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'J5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'J5' + RESET + BLANK
            else:
                printline4 += GREY + 'J5' + RESET + BLANK
        elif 'j5s' in raising_range:
            printline4 += RED + 'J5' + RESET + BLANK
        elif 'j5s' in calling_range:
            printline4 += BLUE + 'J5' + RESET + BLANK
        elif 'j5s' in open_range:
            printline4 += GREEN + 'J5' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #j4s
        if checkhands.suited(hand) and (card1[0] == 'j' and card2[0] == '4' or card1[0] == '4' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'J4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'J4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'J4' + RESET + BLANK
            else:
                printline4 += GREY + 'J4' + RESET + BLANK
        elif 'j4s' in raising_range:
            printline4 += RED + 'J4' + RESET + BLANK
        elif 'j4s' in calling_range:
            printline4 += BLUE + 'J4' + RESET + BLANK
        elif 'j4s' in open_range:
            printline4 += GREEN + 'J4' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #j3s
        if checkhands.suited(hand) and (card1[0] == 'j' and card2[0] == '3' or card1[0] == '3' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'J3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'J3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'J3' + RESET + BLANK
            else:
                printline4 += GREY + 'J3' + RESET + BLANK
        elif 'j3s' in raising_range:
            printline4 += RED + 'J3' + RESET + BLANK
        elif 'j3s' in calling_range:
            printline4 += BLUE + 'J3' + RESET + BLANK
        elif 'j3s' in open_range:
            printline4 += GREEN + 'J3' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #j2s
        if checkhands.suited(hand) and (card1[0] == 'j' and card2[0] == '2' or card1[0] == '2' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline4 += YELLOW + 'J2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline4 += CYAN + 'J2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline4 += CYAN + 'J2' + RESET + BLANK
            else:
                printline4 += GREY + 'J2' + RESET + BLANK
        elif 'j2s' in raising_range:
            printline4 += RED + 'J2' + RESET + BLANK
        elif 'j2s' in calling_range:
            printline4 += BLUE + 'J2' + RESET + BLANK
        elif 'j2s' in open_range:
            printline4 += GREEN + 'J2' + RESET + BLANK
        else:
            printline4 += BLANKCELL
        #line5
        #ato
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == 't' or card1[0] == 't' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'AT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'AT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'AT' + RESET + BLANK
            else:
                printline5 += GREY + 'AT' + RESET + BLANK
        elif 'ato' in raising_range:
            printline5 += RED + 'AT' + RESET + BLANK
        elif 'ato' in calling_range:
            printline5 += BLUE + 'AT' + RESET + BLANK
        elif 'ato' in open_range:
            printline5 += GREEN + 'AT' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #kto
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == 't' or card1[0] == 't' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'KT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'KT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'KT' + RESET + BLANK
            else:
                printline5 += GREY + 'KT' + RESET + BLANK
        elif 'kto' in raising_range:
            printline5 += RED + 'KT' + RESET + BLANK
        elif 'kto' in calling_range:
            printline5 += BLUE + 'KT' + RESET + BLANK
        elif 'kto' in open_range:
            printline5 += GREEN + 'KT' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #qto
        if (not checkhands.suited(hand)) and (card1[0] == 'q' and card2[0] == 't' or card1[0] == 't' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'QT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'QT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'QT' + RESET + BLANK
            else:
                printline5 += GREY + 'QT' + RESET + BLANK
        elif 'qto' in raising_range:
            printline5 += RED + 'QT' + RESET + BLANK
        elif 'qto' in calling_range:
            printline5 += BLUE + 'QT' + RESET + BLANK
        elif 'qto' in open_range:
            printline5 += GREEN + 'QT' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #jto
        if (not checkhands.suited(hand)) and (card1[0] == 'j' and card2[0] == 't' or card1[0] == 't' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'JT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'JT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'JT' + RESET + BLANK
            else:
                printline5 += GREY + 'JT' + RESET + BLANK
        elif 'jto' in raising_range:
            printline5 += RED + 'JT' + RESET + BLANK
        elif 'jto' in calling_range:
            printline5 += BLUE + 'JT' + RESET + BLANK
        elif 'jto' in open_range:
            printline5 += GREEN + 'JT' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #tt
        if checkhands.pocket_pairs(hand) and (card1[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'TT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'TT' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'TT' + RESET + BLANK
            else:
                printline5 += GREY + 'TT' + RESET + BLANK
        elif 'tt' in raising_range:
            printline5 += RED + 'TT' + RESET + BLANK
        elif 'tt' in calling_range:
            printline5 += BLUE + 'TT' + RESET + BLANK
        elif 'tt' in open_range:
            printline5 += GREEN + 'TT' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #t9s
        if checkhands.suited(hand) and (card1[0] == 't' and card2[0] == '9' or card1[0] == '9' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'T9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'T9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'T9' + RESET + BLANK
            else:
                printline5 += GREY + 'T9' + RESET + BLANK
        elif 't9s' in raising_range:
            printline5 += RED + 'T9' + RESET + BLANK
        elif 't9s' in calling_range:
            printline5 += BLUE + 'T9' + RESET + BLANK
        elif 't9s' in open_range:
            printline5 += GREEN + 'T9' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #t8s
        if checkhands.suited(hand) and (card1[0] == 't' and card2[0] == '8' or card1[0] == '8' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'T8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'T8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'T8' + RESET + BLANK
            else:
                printline5 += GREY + 'T8' + RESET + BLANK
        elif 't8s' in raising_range:
            printline5 += RED + 'T8' + RESET + BLANK
        elif 't8s' in calling_range:
            printline5 += BLUE + 'T8' + RESET + BLANK
        elif 't8s' in open_range:
            printline5 += GREEN + 'T8' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #t7s
        if checkhands.suited(hand) and (card1[0] == 't' and card2[0] == '7' or card1[0] == '7' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'T7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'T7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'T7' + RESET + BLANK
            else:
                printline5 += GREY + 'T7' + RESET + BLANK
        elif 't7s' in raising_range:
            printline5 += RED + 'T7' + RESET + BLANK
        elif 't7s' in calling_range:
            printline5 += BLUE + 'T7' + RESET + BLANK
        elif 't7s' in open_range:
            printline5 += GREEN + 'T7' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #t6s
        if checkhands.suited(hand) and (card1[0] == 't' and card2[0] == '6' or card1[0] == '6' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'T6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'T6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'T6' + RESET + BLANK
            else:
                printline5 += GREY + 'T6' + RESET + BLANK
        elif 't6s' in raising_range:
            printline5 += RED + 'T6' + RESET + BLANK
        elif 't6s' in calling_range:
            printline5 += BLUE + 'T6' + RESET + BLANK
        elif 't6s' in open_range:
            printline5 += GREEN + 'T6' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #t5s
        if checkhands.suited(hand) and (card1[0] == 't' and card2[0] == '5' or card1[0] == '5' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'T5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'T5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'T5' + RESET + BLANK
            else:
                printline5 += GREY + 'T5' + RESET + BLANK
        elif 't5s' in raising_range:
            printline5 += RED + 'T5' + RESET + BLANK
        elif 't5s' in calling_range:
            printline5 += BLUE + 'T5' + RESET + BLANK
        elif 't5s' in open_range:
            printline5 += GREEN + 'T5' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #t4s
        if checkhands.suited(hand) and (card1[0] == 't' and card2[0] == '4' or card1[0] == '4' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'T4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'T4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'T4' + RESET + BLANK
            else:
                printline5 += GREY + 'T4' + RESET + BLANK
        elif 't4s' in raising_range:
            printline5 += RED + 'T4' + RESET + BLANK
        elif 't4s' in calling_range:
            printline5 += BLUE + 'T4' + RESET + BLANK
        elif 't4s' in open_range:
            printline5 += GREEN + 'T4' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #t3s
        if checkhands.suited(hand) and (card1[0] == 't' and card2[0] == '3' or card1[0] == '3' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'T3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'T3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'T3' + RESET + BLANK
            else:
                printline5 += GREY + 'T3' + RESET + BLANK
        elif 't3s' in raising_range:
            printline5 += RED + 'T3' + RESET + BLANK
        elif 't3s' in calling_range:
            printline5 += BLUE + 'T3' + RESET + BLANK
        elif 't3s' in open_range:
            printline5 += GREEN + 'T3' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #t2s
        if checkhands.suited(hand) and (card1[0] == 't' and card2[0] == '2' or card1[0] == '2' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline5 += YELLOW + 'T2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline5 += CYAN + 'T2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline5 += CYAN + 'T2' + RESET + BLANK
            else:
                printline5 += GREY + 'T2' + RESET + BLANK
        elif 't2s' in raising_range:
            printline5 += RED + 'T2' + RESET + BLANK
        elif 't2s' in calling_range:
            printline5 += BLUE + 'T2' + RESET + BLANK
        elif 't2s' in open_range:
            printline5 += GREEN + 'T2' + RESET + BLANK
        else:
            printline5 += BLANKCELL
        #line6
        #a9o
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == '9' or card1[0] == '9' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + 'A9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + 'A9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + 'A9' + RESET + BLANK
            else:
                printline6 += GREY + 'A9' + RESET + BLANK
        elif 'a9o' in raising_range:
            printline6 += RED + 'A9' + RESET + BLANK
        elif 'a9o' in calling_range:
            printline6 += BLUE + 'A9' + RESET + BLANK
        elif 'a9o' in open_range:
            printline6 += GREEN + 'A9' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #k9o
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == '9' or card1[0] == '9' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + 'K9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + 'K9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + 'K9' + RESET + BLANK
            else:
                printline6 += GREY + 'K9' + RESET + BLANK
        elif 'k9o' in raising_range:
            printline6 += RED + 'K9' + RESET + BLANK
        elif 'k9o' in calling_range:
            printline6 += BLUE + 'K9' + RESET + BLANK
        elif 'k9o' in open_range:
            printline6 += GREEN + 'K9' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #q9o
        if (not checkhands.suited(hand)) and (card1[0] == 'q' and card2[0] == '9' or card1[0] == '9' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + 'Q9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + 'Q9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + 'Q9' + RESET + BLANK
            else:
                printline6 += GREY + 'Q9' + RESET + BLANK
        elif 'q9o' in raising_range:
            printline6 += RED + 'Q9' + RESET + BLANK
        elif 'q9o' in calling_range:
            printline6 += BLUE + 'Q9' + RESET + BLANK
        elif 'q9o' in open_range:
            printline6 += GREEN + 'Q9' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #j9o
        if (not checkhands.suited(hand)) and (card1[0] == 'j' and card2[0] == '9' or card1[0] == '9' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + 'J9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + 'J9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + 'J9' + RESET + BLANK
            else:
                printline6 += GREY + 'J9' + RESET + BLANK
        elif 'j9o' in raising_range:
            printline6 += RED + 'J9' + RESET + BLANK
        elif 'j9o' in calling_range:
            printline6 += BLUE + 'J9' + RESET + BLANK
        elif 'j9o' in open_range:
            printline6 += GREEN + 'J9' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #t9o
        if (not checkhands.suited(hand)) and (card1[0] == 't' and card2[0] == '9' or card1[0] == '9' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + 'T9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + 'T9' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + 'T9' + RESET + BLANK
            else:
                printline6 += GREY + 'T9' + RESET + BLANK
        elif 't9o' in raising_range:
            printline6 += RED + 'T9' + RESET + BLANK
        elif 't9o' in calling_range:
            printline6 += BLUE + 'T9' + RESET + BLANK
        elif 't9o' in open_range:
            printline6 += GREEN + 'T9' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #99
        if checkhands.pocket_pairs(hand) and (card1[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + '99' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + '99' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + '99' + RESET + BLANK
            else:
                printline6 += GREY + '99' + RESET + BLANK
        elif '99' in raising_range:
            printline6 += RED + '99' + RESET + BLANK
        elif '99' in calling_range:
            printline6 += BLUE + '99' + RESET + BLANK
        elif '99' in open_range:
            printline6 += GREEN + '99' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #98s
        if checkhands.suited(hand) and (card1[0] == '9' and card2[0] == '8' or card1[0] == '8' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + '98' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + '98' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + '98' + RESET + BLANK
            else:
                printline6 += GREY + '98' + RESET + BLANK
        elif '98s' in raising_range:
            printline6 += RED + '98' + RESET + BLANK
        elif '98s' in calling_range:
            printline6 += BLUE + '98' + RESET + BLANK
        elif '98s' in open_range:
            printline6 += GREEN + '98' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #97s
        if checkhands.suited(hand) and (card1[0] == '9' and card2[0] == '7' or card1[0] == '7' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + '97' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + '97' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + '97' + RESET + BLANK
            else:
                printline6 += GREY + '97' + RESET + BLANK
        elif '97s' in raising_range:
            printline6 += RED + '97' + RESET + BLANK
        elif '97s' in calling_range:
            printline6 += BLUE + '97' + RESET + BLANK
        elif '97s' in open_range:
            printline6 += GREEN + '97' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #96s
        if checkhands.suited(hand) and (card1[0] == '9' and card2[0] == '6' or card1[0] == '6' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + '96' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + '96' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + '96' + RESET + BLANK
            else:
                printline6 += GREY + '96' + RESET + BLANK
        elif '96s' in raising_range:
            printline6 += RED + '96' + RESET + BLANK
        elif '96s' in calling_range:
            printline6 += BLUE + '96' + RESET + BLANK
        elif '96s' in open_range:
            printline6 += GREEN + '96' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #95s
        if checkhands.suited(hand) and (card1[0] == '9' and card2[0] == '5' or card1[0] == '5' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + '95' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + '95' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + '95' + RESET + BLANK
            else:
                printline6 += GREY + '95' + RESET + BLANK
        elif '95s' in raising_range:
            printline6 += RED + '95' + RESET + BLANK
        elif '95s' in calling_range:
            printline6 += BLUE + '95' + RESET + BLANK
        elif '95s' in open_range:
            printline6 += GREEN + '95' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #94s
        if checkhands.suited(hand) and (card1[0] == '9' and card2[0] == '4' or card1[0] == '4' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + '94' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + '94' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + '94' + RESET + BLANK
            else:
                printline6 += GREY + '94' + RESET + BLANK
        elif '94s' in raising_range:
            printline6 += RED + '94' + RESET + BLANK
        elif '94s' in calling_range:
            printline6 += BLUE + '94' + RESET + BLANK
        elif '94s' in open_range:
            printline6 += GREEN + '94' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #93s
        if checkhands.suited(hand) and (card1[0] == '9' and card2[0] == '3' or card1[0] == '3' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + '93' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + '93' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + '93' + RESET + BLANK
            else:
                printline6 += GREY + '93' + RESET + BLANK
        elif '93s' in raising_range:
            printline6 += RED + '93' + RESET + BLANK
        elif '93s' in calling_range:
            printline6 += BLUE + '93' + RESET + BLANK
        elif '93s' in open_range:
            printline6 += GREEN + '93' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #92s
        if checkhands.suited(hand) and (card1[0] == '9' and card2[0] == '2' or card1[0] == '2' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline6 += YELLOW + '92' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline6 += CYAN + '92' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline6 += CYAN + '92' + RESET + BLANK
            else:
                printline6 += GREY + '92' + RESET + BLANK
        elif '92s' in raising_range:
            printline6 += RED + '92' + RESET + BLANK
        elif '92s' in calling_range:
            printline6 += BLUE + '92' + RESET + BLANK
        elif '92s' in open_range:
            printline6 += GREEN + '92' + RESET + BLANK
        else:
            printline6 += BLANKCELL
        #line7
        #a8o
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == '8' or card1[0] == '8' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + 'A8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + 'A8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + 'A8' + RESET + BLANK
            else:
                printline7 += GREY + 'A8' + RESET + BLANK
        elif 'a8o' in raising_range:
            printline7 += RED + 'A8' + RESET + BLANK
        elif 'a8o' in calling_range:
            printline7 += BLUE + 'A8' + RESET + BLANK
        elif 'a8o' in open_range:
            printline7 += GREEN + 'A8' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #k8o
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == '8' or card1[0] == '8' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + 'K8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + 'K8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + 'K8' + RESET + BLANK
            else:
                printline7 += GREY + 'K8' + RESET + BLANK
        elif 'k8o' in raising_range:
            printline7 += RED + 'K8' + RESET + BLANK
        elif 'k8o' in calling_range:
            printline7 += BLUE + 'K8' + RESET + BLANK
        elif 'k8o' in open_range:
            printline7 += GREEN + 'K8' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #q8o
        if (not checkhands.suited(hand)) and (card1[0] == 'q' and card2[0] == '8' or card1[0] == '8' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + 'Q8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + 'Q8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + 'Q8' + RESET + BLANK
            else:
                printline7 += GREY + 'Q8' + RESET + BLANK
        elif 'q8o' in raising_range:
            printline7 += RED + 'Q8' + RESET + BLANK
        elif 'q8o' in calling_range:
            printline7 += BLUE + 'Q8' + RESET + BLANK
        elif 'q8o' in open_range:
            printline7 += GREEN + 'Q8' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #j8o
        if (not checkhands.suited(hand)) and (card1[0] == 'j' and card2[0] == '8' or card1[0] == '8' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + 'J8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + 'J8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + 'J8' + RESET + BLANK
            else:
                printline7 += GREY + 'J8' + RESET + BLANK
        elif 'j8o' in raising_range:
            printline7 += RED + 'J8' + RESET + BLANK
        elif 'j8o' in calling_range:
            printline7 += BLUE + 'J8' + RESET + BLANK
        elif 'j8o' in open_range:
            printline7 += GREEN + 'J8' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #t8o
        if (not checkhands.suited(hand)) and (card1[0] == 't' and card2[0] == '8' or card1[0] == '8' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + 'T8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + 'T8' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + 'T8' + RESET + BLANK
            else:
                printline7 += GREY + 'T8' + RESET + BLANK
        elif 't8o' in raising_range:
            printline7 += RED + 'T8' + RESET + BLANK
        elif 't8o' in calling_range:
            printline7 += BLUE + 'T8' + RESET + BLANK
        elif 't8o' in open_range:
            printline7 += GREEN + 'T8' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #98o
        if (not checkhands.suited(hand)) and (card1[0] == '9' and card2[0] == '8' or card1[0] == '8' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + '98' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + '98' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + '98' + RESET + BLANK
            else:
                printline7 += GREY + '98' + RESET + BLANK
        elif '98o' in raising_range:
            printline7 += RED + '98' + RESET + BLANK
        elif '98o' in calling_range:
            printline7 += BLUE + '98' + RESET + BLANK
        elif '98o' in open_range:
            printline7 += GREEN + '98' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #88
        if checkhands.pocket_pairs(hand) and (card1[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + '88' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + '88' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + '88' + RESET + BLANK
            else:
                printline7 += GREY + '88' + RESET + BLANK
        elif '88' in raising_range:
            printline7 += RED + '88' + RESET + BLANK
        elif '88' in calling_range:
            printline7 += BLUE + '88' + RESET + BLANK
        elif '88' in open_range:
            printline7 += GREEN + '88' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #87s
        if checkhands.suited(hand) and (card1[0] == '8' and card2[0] == '7' or card1[0] == '7' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + '87' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + '87' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + '87' + RESET + BLANK
            else:
                printline7 += GREY + '87' + RESET + BLANK
        elif '87s' in raising_range:
            printline7 += RED + '87' + RESET + BLANK
        elif '87s' in calling_range:
            printline7 += BLUE + '87' + RESET + BLANK
        elif '87s' in open_range:
            printline7 += GREEN + '87' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #86s
        if checkhands.suited(hand) and (card1[0] == '8' and card2[0] == '6' or card1[0] == '6' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + '86' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + '86' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + '86' + RESET + BLANK
            else:
                printline7 += GREY + '86' + RESET + BLANK
        elif '86s' in raising_range:
            printline7 += RED + '86' + RESET + BLANK
        elif '86s' in calling_range:
            printline7 += BLUE + '86' + RESET + BLANK
        elif '86s' in open_range:
            printline7 += GREEN + '86' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #85s
        if checkhands.suited(hand) and (card1[0] == '8' and card2[0] == '5' or card1[0] == '5' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + '85' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + '85' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + '85' + RESET + BLANK
            else:
                printline7 += GREY + '85' + RESET + BLANK
        elif '85s' in raising_range:
            printline7 += RED + '85' + RESET + BLANK
        elif '85s' in calling_range:
            printline7 += BLUE + '85' + RESET + BLANK
        elif '85s' in open_range:
            printline7 += GREEN + '85' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #84s
        if checkhands.suited(hand) and (card1[0] == '8' and card2[0] == '4' or card1[0] == '4' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + '84' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + '84' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + '84' + RESET + BLANK
            else:
                printline7 += GREY + '84' + RESET + BLANK
        elif '84s' in raising_range:
            printline7 += RED + '84' + RESET + BLANK
        elif '84s' in calling_range:
            printline7 += BLUE + '84' + RESET + BLANK
        elif '84s' in open_range:
            printline7 += GREEN + '84' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #83s
        if checkhands.suited(hand) and (card1[0] == '8' and card2[0] == '3' or card1[0] == '3' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + '83' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + '83' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + '83' + RESET + BLANK
            else:
                printline7 += GREY + '83' + RESET + BLANK
        elif '83s' in raising_range:
            printline7 += RED + '83' + RESET + BLANK
        elif '83s' in calling_range:
            printline7 += BLUE + '83' + RESET + BLANK
        elif '83s' in open_range:
            printline7 += GREEN + '83' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #82s
        if checkhands.suited(hand) and (card1[0] == '8' and card2[0] == '2' or card1[0] == '2' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline7 += YELLOW + '82' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline7 += CYAN + '82' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline7 += CYAN + '82' + RESET + BLANK
            else:
                printline7 += GREY + '82' + RESET + BLANK
        elif '82s' in raising_range:
            printline7 += RED + '82' + RESET + BLANK
        elif '82s' in calling_range:
            printline7 += BLUE + '82' + RESET + BLANK
        elif '82s' in open_range:
            printline7 += GREEN + '82' + RESET + BLANK
        else:
            printline7 += BLANKCELL
        #line8
        #a7o
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == '7' or card1[0] == '7' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + 'A7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + 'A7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + 'A7' + RESET + BLANK
            else:
                printline8 += GREY + 'A7' + RESET + BLANK
        elif 'a7o' in raising_range:
            printline8 += RED + 'A7' + RESET + BLANK
        elif 'a7o' in calling_range:
            printline8 += BLUE + 'A7' + RESET + BLANK
        elif 'a7o' in open_range:
            printline8 += GREEN + 'A7' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #k7o
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == '7' or card1[0] == '7' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + 'K7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + 'K7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + 'K7' + RESET + BLANK
            else:
                printline8 += GREY + 'K7' + RESET + BLANK
        elif 'k7o' in raising_range:
            printline8 += RED + 'K7' + RESET + BLANK
        elif 'k7o' in calling_range:
            printline8 += BLUE + 'K7' + RESET + BLANK
        elif 'k7o' in open_range:
            printline8 += GREEN + 'K7' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #q7o
        if (not checkhands.suited(hand)) and (card1[0] == 'q' and card2[0] == '7' or card1[0] == '7' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + 'Q7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + 'Q7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + 'Q7' + RESET + BLANK
            else:
                printline8 += GREY + 'Q7' + RESET + BLANK
        elif 'q7o' in raising_range:
            printline8 += RED + 'Q7' + RESET + BLANK
        elif 'q7o' in calling_range:
            printline8 += BLUE + 'Q7' + RESET + BLANK
        elif 'q7o' in open_range:
            printline8 += GREEN + 'Q7' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #j7o
        if (not checkhands.suited(hand)) and (card1[0] == 'j' and card2[0] == '7' or card1[0] == '7' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + 'J7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + 'J7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + 'J7' + RESET + BLANK
            else:
                printline8 += GREY + 'J7' + RESET + BLANK
        elif 'j7o' in raising_range:
            printline8 += RED + 'J7' + RESET + BLANK
        elif 'j7o' in calling_range:
            printline8 += BLUE + 'J7' + RESET + BLANK
        elif 'j7o' in open_range:
            printline8 += GREEN + 'J7' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #t7o
        if (not checkhands.suited(hand)) and (card1[0] == 't' and card2[0] == '7' or card1[0] == '7' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + 'T7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + 'T7' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + 'T7' + RESET + BLANK
            else:
                printline8 += GREY + 'T7' + RESET + BLANK
        elif 't7o' in raising_range:
            printline8 += RED + 'T7' + RESET + BLANK
        elif 't7o' in calling_range:
            printline8 += BLUE + 'T7' + RESET + BLANK
        elif 't7o' in open_range:
            printline8 += GREEN + 'T7' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #97o
        if (not checkhands.suited(hand)) and (card1[0] == '9' and card2[0] == '7' or card1[0] == '7' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + '97' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + '97' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + '97' + RESET + BLANK
            else:
                printline8 += GREY + '97' + RESET + BLANK
        elif '97o' in raising_range:
            printline8 += RED + '97' + RESET + BLANK
        elif '97o' in calling_range:
            printline8 += BLUE + '97' + RESET + BLANK
        elif '97o' in open_range:
            printline8 += GREEN + '97' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #87o
        if (not checkhands.suited(hand)) and (card1[0] == '8' and card2[0] == '7' or card1[0] == '7' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + '87' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + '87' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + '87' + RESET + BLANK
            else:
                printline8 += GREY + '87' + RESET + BLANK
        elif '87o' in raising_range:
            printline8 += RED + '87' + RESET + BLANK
        elif '87o' in calling_range:
            printline8 += BLUE + '87' + RESET + BLANK
        elif '87o' in open_range:
            printline8 += GREEN + '87' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #77
        if checkhands.pocket_pairs(hand) and (card1[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + '77' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + '77' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + '77' + RESET + BLANK
            else:
                printline8 += GREY + '77' + RESET + BLANK
        elif '77' in raising_range:
            printline8 += RED + '77' + RESET + BLANK
        elif '77' in calling_range:
            printline8 += BLUE + '77' + RESET + BLANK
        elif '77' in open_range:
            printline8 += GREEN + '77' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #76s
        if checkhands.suited(hand) and (card1[0] == '7' and card2[0] == '6' or card1[0] == '6' and card2[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + '76' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + '76' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + '76' + RESET + BLANK
            else:
                printline8 += GREY + '76' + RESET + BLANK
        elif '76s' in raising_range:
            printline8 += RED + '76' + RESET + BLANK
        elif '76s' in calling_range:
            printline8 += BLUE + '76' + RESET + BLANK
        elif '76s' in open_range:
            printline8 += GREEN + '76' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #75s
        if checkhands.suited(hand) and (card1[0] == '7' and card2[0] == '5' or card1[0] == '5' and card2[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + '75' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + '75' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + '75' + RESET + BLANK
            else:
                printline8 += GREY + '75' + RESET + BLANK
        elif '75s' in raising_range:
            printline8 += RED + '75' + RESET + BLANK
        elif '75s' in calling_range:
            printline8 += BLUE + '75' + RESET + BLANK
        elif '75s' in open_range:
            printline8 += GREEN + '75' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #74s
        if checkhands.suited(hand) and (card1[0] == '7' and card2[0] == '4' or card1[0] == '4' and card2[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + '74' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + '74' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + '74' + RESET + BLANK
            else:
                printline8 += GREY + '74' + RESET + BLANK
        elif '74s' in raising_range:
            printline8 += RED + '74' + RESET + BLANK
        elif '74s' in calling_range:
            printline8 += BLUE + '74' + RESET + BLANK
        elif '74s' in open_range:
            printline8 += GREEN + '74' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #73s
        if checkhands.suited(hand) and (card1[0] == '7' and card2[0] == '3' or card1[0] == '3' and card2[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + '73' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + '73' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + '73' + RESET + BLANK
            else:
                printline8 += GREY + '73' + RESET + BLANK
        elif '73s' in raising_range:
            printline8 += RED + '73' + RESET + BLANK
        elif '73s' in calling_range:
            printline8 += BLUE + '73' + RESET + BLANK
        elif '73s' in open_range:
            printline8 += GREEN + '73' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #72s
        if checkhands.suited(hand) and (card1[0] == '7' and card2[0] == '2' or card1[0] == '2' and card2[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline8 += YELLOW + '72' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline8 += CYAN + '72' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline8 += CYAN + '72' + RESET + BLANK
            else:
                printline8 += GREY + '72' + RESET + BLANK
        elif '72s' in raising_range:
            printline8 += RED + '72' + RESET + BLANK
        elif '72s' in calling_range:
            printline8 += BLUE + '72' + RESET + BLANK
        elif '72s' in open_range:
            printline8 += GREEN + '72' + RESET + BLANK
        else:
            printline8 += BLANKCELL
        #line9
        #a6o
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == '6' or card1[0] == '6' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + 'A6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + 'A6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + 'A6' + RESET + BLANK
            else:
                printline9 += GREY + 'A6' + RESET + BLANK
        elif 'a6o' in raising_range:
            printline9 += RED + 'A6' + RESET + BLANK
        elif 'a6o' in calling_range:
            printline9 += BLUE + 'A6' + RESET + BLANK
        elif 'a6o' in open_range:
            printline9 += GREEN + 'A6' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #k6o
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == '6' or card1[0] == '6' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + 'K6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + 'K6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + 'K6' + RESET + BLANK
            else:
                printline9 += GREY + 'K6' + RESET + BLANK
        elif 'k6o' in raising_range:
            printline9 += RED + 'K6' + RESET + BLANK
        elif 'k6o' in calling_range:
            printline9 += BLUE + 'K6' + RESET + BLANK
        elif 'k6o' in open_range:
            printline9 += GREEN + 'K6' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #q6o
        if (not checkhands.suited(hand)) and (card1[0] == 'q' and card2[0] == '6' or card1[0] == '6' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + 'Q6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + 'Q6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + 'Q6' + RESET + BLANK
            else:
                printline9 += GREY + 'Q6' + RESET + BLANK
        elif 'q6o' in raising_range:
            printline9 += RED + 'Q6' + RESET + BLANK
        elif 'q6o' in calling_range:
            printline9 += BLUE + 'Q6' + RESET + BLANK
        elif 'q6o' in open_range:
            printline9 += GREEN + 'Q6' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #j6o
        if (not checkhands.suited(hand)) and (card1[0] == 'j' and card2[0] == '6' or card1[0] == '6' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + 'J6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + 'J6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + 'J6' + RESET + BLANK
            else:
                printline9 += GREY + 'J6' + RESET + BLANK
        elif 'j6o' in raising_range:
            printline9 += RED + 'J6' + RESET + BLANK
        elif 'j6o' in calling_range:
            printline9 += BLUE + 'J6' + RESET + BLANK
        elif 'j6o' in open_range:
            printline9 += GREEN + 'J6' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #t6o
        if (not checkhands.suited(hand)) and (card1[0] == 't' and card2[0] == '6' or card1[0] == '6' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + 'T6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + 'T6' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + 'T6' + RESET + BLANK
            else:
                printline9 += GREY + 'T6' + RESET + BLANK
        elif 't6o' in raising_range:
            printline9 += RED + 'T6' + RESET + BLANK
        elif 't6o' in calling_range:
            printline9 += BLUE + 'T6' + RESET + BLANK
        elif 't6o' in open_range:
            printline9 += GREEN + 'T6' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #96o
        if (not checkhands.suited(hand)) and (card1[0] == '9' and card2[0] == '6' or card1[0] == '6' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + '96' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + '96' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + '96' + RESET + BLANK
            else:
                printline9 += GREY + '96' + RESET + BLANK
        elif '96o' in raising_range:
            printline9 += RED + '96' + RESET + BLANK
        elif '96o' in calling_range:
            printline9 += BLUE + '96' + RESET + BLANK
        elif '96o' in open_range:
            printline9 += GREEN + '96' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #86o
        if (not checkhands.suited(hand)) and (card1[0] == '8' and card2[0] == '6' or card1[0] == '6' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + '86' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + '86' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + '86' + RESET + BLANK
            else:
                printline9 += GREY + '86' + RESET + BLANK
        elif '86o' in raising_range:
            printline9 += RED + '86' + RESET + BLANK
        elif '86o' in calling_range:
            printline9 += BLUE + '86' + RESET + BLANK
        elif '86o' in open_range:
            printline9 += GREEN + '86' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #76o
        if (not checkhands.suited(hand)) and (card1[0] == '7' and card2[0] == '6' or card1[0] == '6' and card2[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + '76' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + '76' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + '76' + RESET + BLANK
            else:
                printline9 += GREY + '76' + RESET + BLANK
        elif '76o' in raising_range:
            printline9 += RED + '76' + RESET + BLANK
        elif '76o' in calling_range:
            printline9 += BLUE + '76' + RESET + BLANK
        elif '76o' in open_range:
            printline9 += GREEN + '76' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #66
        if checkhands.pocket_pairs(hand) and (card1[0] == '6'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + '66' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + '66' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + '66' + RESET + BLANK
            else:
                printline9 += GREY + '66' + RESET + BLANK
        elif '66' in raising_range:
            printline9 += RED + '66' + RESET + BLANK
        elif '66' in calling_range:
            printline9 += BLUE + '66' + RESET + BLANK
        elif '66' in open_range:
            printline9 += GREEN + '66' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #65s
        if checkhands.suited(hand) and (card1[0] == '6' and card2[0] == '5' or card1[0] == '5' and card2[0] == '6'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + '65' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + '65' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + '65' + RESET + BLANK
            else:
                printline9 += GREY + '65' + RESET + BLANK
        elif '65s' in raising_range:
            printline9 += RED + '65' + RESET + BLANK
        elif '65s' in calling_range:
            printline9 += BLUE + '65' + RESET + BLANK
        elif '65s' in open_range:
            printline9 += GREEN + '65' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #64s
        if checkhands.suited(hand) and (card1[0] == '6' and card2[0] == '4' or card1[0] == '4' and card2[0] == '6'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + '64' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + '64' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + '64' + RESET + BLANK
            else:
                printline9 += GREY + '64' + RESET + BLANK
        elif '64s' in raising_range:
            printline9 += RED + '64' + RESET + BLANK
        elif '64s' in calling_range:
            printline9 += BLUE + '64' + RESET + BLANK
        elif '64s' in open_range:
            printline9 += GREEN + '64' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #63s
        if checkhands.suited(hand) and (card1[0] == '6' and card2[0] == '3' or card1[0] == '3' and card2[0] == '6'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + '63' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + '63' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + '63' + RESET + BLANK
            else:
                printline9 += GREY + '63' + RESET + BLANK
        elif '63s' in raising_range:
            printline9 += RED + '63' + RESET + BLANK
        elif '63s' in calling_range:
            printline9 += BLUE + '63' + RESET + BLANK
        elif '63s' in open_range:
            printline9 += GREEN + '63' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #62s
        if checkhands.suited(hand) and (card1[0] == '6' and card2[0] == '2' or card1[0] == '2' and card2[0] == '6'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline9 += YELLOW + '62' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline9 += CYAN + '62' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline9 += CYAN + '62' + RESET + BLANK
            else:
                printline9 += GREY + '62' + RESET + BLANK
        elif '62s' in raising_range:
            printline9 += RED + '62' + RESET + BLANK
        elif '62s' in calling_range:
            printline9 += BLUE + '62' + RESET + BLANK
        elif '62s' in open_range:
            printline9 += GREEN + '62' + RESET + BLANK
        else:
            printline9 += BLANKCELL
        #line10
        #a5o
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == '5' or card1[0] == '5' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + 'A5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + 'A5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + 'A5' + RESET + BLANK
            else:
                printline10 += GREY + 'A5' + RESET + BLANK
        elif 'a5o' in raising_range:
            printline10 += RED + 'A5' + RESET + BLANK
        elif 'a5o' in calling_range:
            printline10 += BLUE + 'A5' + RESET + BLANK
        elif 'a5o' in open_range:
            printline10 += GREEN + 'A5' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #k5o
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == '5' or card1[0] == '5' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + 'K5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + 'K5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + 'K5' + RESET + BLANK
            else:
                printline10 += GREY + 'K5' + RESET + BLANK
        elif 'k5o' in raising_range:
            printline10 += RED + 'K5' + RESET + BLANK
        elif 'k5o' in calling_range:
            printline10 += BLUE + 'K5' + RESET + BLANK
        elif 'k5o' in open_range:
            printline10 += GREEN + 'K5' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #q5o
        if (not checkhands.suited(hand)) and (card1[0] == 'q' and card2[0] == '5' or card1[0] == '5' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + 'Q5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + 'Q5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + 'Q5' + RESET + BLANK
            else:
                printline10 += GREY + 'Q5' + RESET + BLANK
        elif 'q5o' in raising_range:
            printline10 += RED + 'Q5' + RESET + BLANK
        elif 'q5o' in calling_range:
            printline10 += BLUE + 'Q5' + RESET + BLANK
        elif 'q5o' in open_range:
            printline10 += GREEN + 'Q5' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #j5o
        if (not checkhands.suited(hand)) and (card1[0] == 'j' and card2[0] == '5' or card1[0] == '5' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + 'J5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + 'J5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + 'J5' + RESET + BLANK
            else:
                printline10 += GREY + 'J5' + RESET + BLANK
        elif 'j5o' in raising_range:
            printline10 += RED + 'J5' + RESET + BLANK
        elif 'j5o' in calling_range:
            printline10 += BLUE + 'J5' + RESET + BLANK
        elif 'j5o' in open_range:
            printline10 += GREEN + 'J5' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #t5o
        if (not checkhands.suited(hand)) and (card1[0] == 't' and card2[0] == '5' or card1[0] == '5' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + 'T5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + 'T5' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + 'T5' + RESET + BLANK
            else:
                printline10 += GREY + 'T5' + RESET + BLANK
        elif 't5o' in raising_range:
            printline10 += RED + 'T5' + RESET + BLANK
        elif 't5o' in calling_range:
            printline10 += BLUE + 'T5' + RESET + BLANK
        elif 't5o' in open_range:
            printline10 += GREEN + 'T5' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #95o
        if (not checkhands.suited(hand)) and (card1[0] == '9' and card2[0] == '5' or card1[0] == '5' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + '95' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + '95' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + '95' + RESET + BLANK
            else:
                printline10 += GREY + '95' + RESET + BLANK
        elif '95o' in raising_range:
            printline10 += RED + '95' + RESET + BLANK
        elif '95o' in calling_range:
            printline10 += BLUE + '95' + RESET + BLANK
        elif '95o' in open_range:
            printline10 += GREEN + '95' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #85o
        if (not checkhands.suited(hand)) and (card1[0] == '8' and card2[0] == '5' or card1[0] == '5' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + '85' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + '85' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + '85' + RESET + BLANK
            else:
                printline10 += GREY + '85' + RESET + BLANK
        elif '85o' in raising_range:
            printline10 += RED + '85' + RESET + BLANK
        elif '85o' in calling_range:
            printline10 += BLUE + '85' + RESET + BLANK
        elif '85o' in open_range:
            printline10 += GREEN + '85' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #75o
        if (not checkhands.suited(hand)) and (card1[0] == '7' and card2[0] == '5' or card1[0] == '5' and card2[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + '75' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + '75' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + '75' + RESET + BLANK
            else:
                printline10 += GREY + '75' + RESET + BLANK
        elif '75o' in raising_range:
            printline10 += RED + '75' + RESET + BLANK
        elif '75o' in calling_range:
            printline10 += BLUE + '75' + RESET + BLANK
        elif '75o' in open_range:
            printline10 += GREEN + '75' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #65o
        if (not checkhands.suited(hand)) and (card1[0] == '6' and card2[0] == '5' or card1[0] == '5' and card2[0] == '6'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + '65' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + '65' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + '65' + RESET + BLANK
            else:
                printline10 += GREY + '65' + RESET + BLANK
        elif '65o' in raising_range:
            printline10 += RED + '65' + RESET + BLANK
        elif '65o' in calling_range:
            printline10 += BLUE + '65' + RESET + BLANK
        elif '65o' in open_range:
            printline10 += GREEN + '65' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #55
        if checkhands.pocket_pairs(hand) and (card1[0] == '5'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + '55' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + '55' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + '55' + RESET + BLANK
            else:
                printline10 += GREY + '55' + RESET + BLANK
        elif '55' in raising_range:
            printline10 += RED + '55' + RESET + BLANK
        elif '55' in calling_range:
            printline10 += BLUE + '55' + RESET + BLANK
        elif '55' in open_range:
            printline10 += GREEN + '55' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #54s
        if checkhands.suited(hand) and (card1[0] == '5' and card2[0] == '4' or card1[0] == '4' and card2[0] == '5'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + '54' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + '54' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + '54' + RESET + BLANK
            else:
                printline10 += GREY + '54' + RESET + BLANK
        elif '54s' in raising_range:
            printline10 += RED + '54' + RESET + BLANK
        elif '54s' in calling_range:
            printline10 += BLUE + '54' + RESET + BLANK
        elif '54s' in open_range:
            printline10 += GREEN + '54' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #53s
        if checkhands.suited(hand) and (card1[0] == '5' and card2[0] == '3' or card1[0] == '3' and card2[0] == '5'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + '53' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + '53' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + '53' + RESET + BLANK
            else:
                printline10 += GREY + '53' + RESET + BLANK
        elif '53s' in raising_range:
            printline10 += RED + '53' + RESET + BLANK
        elif '53s' in calling_range:
            printline10 += BLUE + '53' + RESET + BLANK
        elif '53s' in open_range:
            printline10 += GREEN + '53' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #52s
        if checkhands.suited(hand) and (card1[0] == '5' and card2[0] == '2' or card1[0] == '2' and card2[0] == '5'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline10 += YELLOW + '52' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline10 += CYAN + '52' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline10 += CYAN + '52' + RESET + BLANK
            else:
                printline10 += GREY + '52' + RESET + BLANK
        elif '52s' in raising_range:
            printline10 += RED + '52' + RESET + BLANK
        elif '52s' in calling_range:
            printline10 += BLUE + '52' + RESET + BLANK
        elif '52s' in open_range:
            printline10 += GREEN + '52' + RESET + BLANK
        else:
            printline10 += BLANKCELL
        #line11
        #a4o
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == '4' or card1[0] == '4' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + 'A4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + 'A4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + 'A4' + RESET + BLANK
            else:
                printline11 += GREY + 'A4' + RESET + BLANK
        elif 'a4o' in raising_range:
            printline11 += RED + 'A4' + RESET + BLANK
        elif 'a4o' in calling_range:
            printline11 += BLUE + 'A4' + RESET + BLANK
        elif 'a4o' in open_range:
            printline11 += GREEN + 'A4' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #k4o
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == '4' or card1[0] == '4' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + 'K4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + 'K4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + 'K4' + RESET + BLANK
            else:
                printline11 += GREY + 'K4' + RESET + BLANK
        elif 'k4o' in raising_range:
            printline11 += RED + 'K4' + RESET + BLANK
        elif 'k4o' in calling_range:
            printline11 += BLUE + 'K4' + RESET + BLANK
        elif 'k4o' in open_range:
            printline11 += GREEN + 'K4' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #q4o
        if (not checkhands.suited(hand)) and (card1[0] == 'q' and card2[0] == '4' or card1[0] == '4' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + 'Q4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + 'Q4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + 'Q4' + RESET + BLANK
            else:
                printline11 += GREY + 'Q4' + RESET + BLANK
        elif 'q4o' in raising_range:
            printline11 += RED + 'Q4' + RESET + BLANK
        elif 'q4o' in calling_range:
            printline11 += BLUE + 'Q4' + RESET + BLANK
        elif 'q4o' in open_range:
            printline11 += GREEN + 'Q4' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #j4o
        if (not checkhands.suited(hand)) and (card1[0] == 'j' and card2[0] == '4' or card1[0] == '4' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + 'J4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + 'J4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + 'J4' + RESET + BLANK
            else:
                printline11 += GREY + 'J4' + RESET + BLANK
        elif 'j4o' in raising_range:
            printline11 += RED + 'J4' + RESET + BLANK
        elif 'j4o' in calling_range:
            printline11 += BLUE + 'J4' + RESET + BLANK
        elif 'j4o' in open_range:
            printline11 += GREEN + 'J4' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #t4o
        if (not checkhands.suited(hand)) and (card1[0] == 't' and card2[0] == '4' or card1[0] == '4' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + 'T4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + 'T4' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + 'T4' + RESET + BLANK
            else:
                printline11 += GREY + 'T4' + RESET + BLANK
        elif 't4o' in raising_range:
            printline11 += RED + 'T4' + RESET + BLANK
        elif 't4o' in calling_range:
            printline11 += BLUE + 'T4' + RESET + BLANK
        elif 't4o' in open_range:
            printline11 += GREEN + 'T4' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #94o
        if (not checkhands.suited(hand)) and (card1[0] == '9' and card2[0] == '4' or card1[0] == '4' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + '94' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + '94' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + '94' + RESET + BLANK
            else:
                printline11 += GREY + '94' + RESET + BLANK
        elif '94o' in raising_range:
            printline11 += RED + '94' + RESET + BLANK
        elif '94o' in calling_range:
            printline11 += BLUE + '94' + RESET + BLANK
        elif '94o' in open_range:
            printline11 += GREEN + '94' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #84o
        if (not checkhands.suited(hand)) and (card1[0] == '8' and card2[0] == '4' or card1[0] == '4' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + '84' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + '84' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + '84' + RESET + BLANK
            else:
                printline11 += GREY + '84' + RESET + BLANK
        elif '84o' in raising_range:
            printline11 += RED + '84' + RESET + BLANK
        elif '84o' in calling_range:
            printline11 += BLUE + '84' + RESET + BLANK
        elif '84o' in open_range:
            printline11 += GREEN + '84' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #74o
        if (not checkhands.suited(hand)) and (card1[0] == '7' and card2[0] == '4' or card1[0] == '4' and card2[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + '74' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + '74' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + '74' + RESET + BLANK
            else:
                printline11 += GREY + '74' + RESET + BLANK
        elif '74o' in raising_range:
            printline11 += RED + '74' + RESET + BLANK
        elif '74o' in calling_range:
            printline11 += BLUE + '74' + RESET + BLANK
        elif '74o' in open_range:
            printline11 += GREEN + '74' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #64o
        if (not checkhands.suited(hand)) and (card1[0] == '6' and card2[0] == '4' or card1[0] == '4' and card2[0] == '6'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + '64' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + '64' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + '64' + RESET + BLANK
            else:
                printline11 += GREY + '64' + RESET + BLANK
        elif '64o' in raising_range:
            printline11 += RED + '64' + RESET + BLANK
        elif '64o' in calling_range:
            printline11 += BLUE + '64' + RESET + BLANK
        elif '64o' in open_range:
            printline11 += GREEN + '64' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #54o
        if (not checkhands.suited(hand)) and (card1[0] == '5' and card2[0] == '4' or card1[0] == '4' and card2[0] == '5'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + '54' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + '54' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + '54' + RESET + BLANK
            else:
                printline11 += GREY + '54' + RESET + BLANK
        elif '54o' in raising_range:
            printline11 += RED + '54' + RESET + BLANK
        elif '54o' in calling_range:
            printline11 += BLUE + '54' + RESET + BLANK
        elif '54o' in open_range:
            printline11 += GREEN + '54' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #44
        if checkhands.pocket_pairs(hand) and (card1[0] == '4'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + '44' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + '44' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + '44' + RESET + BLANK
            else:
                printline11 += GREY + '44' + RESET + BLANK
        elif '44' in raising_range:
            printline11 += RED + '44' + RESET + BLANK
        elif '44' in calling_range:
            printline11 += BLUE + '44' + RESET + BLANK
        elif '44' in open_range:
            printline11 += GREEN + '44' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #43s
        if checkhands.suited(hand) and (card1[0] == '4' and card2[0] == '3' or card1[0] == '3' and card2[0] == '4'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + '43' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + '43' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + '43' + RESET + BLANK
            else:
                printline11 += GREY + '43' + RESET + BLANK
        elif '43s' in raising_range:
            printline11 += RED + '43' + RESET + BLANK
        elif '43s' in calling_range:
            printline11 += BLUE + '43' + RESET + BLANK
        elif '43s' in open_range:
            printline11 += GREEN + '43' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #42s
        if checkhands.suited(hand) and (card1[0] == '4' and card2[0] == '2' or card1[0] == '2' and card2[0] == '4'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline11 += YELLOW + '42' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline11 += CYAN + '42' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline11 += CYAN + '42' + RESET + BLANK
            else:
                printline11 += GREY + '42' + RESET + BLANK
        elif '42s' in raising_range:
            printline11 += RED + '42' + RESET + BLANK
        elif '42s' in calling_range:
            printline11 += BLUE + '42' + RESET + BLANK
        elif '42s' in open_range:
            printline11 += GREEN + '42' + RESET + BLANK
        else:
            printline11 += BLANKCELL
        #line12
        #a3o
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == '3' or card1[0] == '3' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + 'A3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + 'A3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + 'A3' + RESET + BLANK
            else:
                printline12 += GREY + 'A3' + RESET + BLANK
        elif 'a3o' in raising_range:
            printline12 += RED + 'A3' + RESET + BLANK
        elif 'a3o' in calling_range:
            printline12 += BLUE + 'A3' + RESET + BLANK
        elif 'a3o' in open_range:
            printline12 += GREEN + 'A3' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #k3o
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == '3' or card1[0] == '3' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + 'K3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + 'K3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + 'K3' + RESET + BLANK
            else:
                printline12 += GREY + 'K3' + RESET + BLANK
        elif 'k3o' in raising_range:
            printline12 += RED + 'K3' + RESET + BLANK
        elif 'k3o' in calling_range:
            printline12 += BLUE + 'K3' + RESET + BLANK
        elif 'k3o' in open_range:
            printline12 += GREEN + 'K3' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #q3o
        if (not checkhands.suited(hand)) and (card1[0] == 'q' and card2[0] == '3' or card1[0] == '3' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + 'Q3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + 'Q3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + 'Q3' + RESET + BLANK
            else:
                printline12 += GREY + 'Q3' + RESET + BLANK
        elif 'q3o' in raising_range:
            printline12 += RED + 'Q3' + RESET + BLANK
        elif 'q3o' in calling_range:
            printline12 += BLUE + 'Q3' + RESET + BLANK
        elif 'q3o' in open_range:
            printline12 += GREEN + 'Q3' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #j3o
        if (not checkhands.suited(hand)) and (card1[0] == 'j' and card2[0] == '3' or card1[0] == '3' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + 'J3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + 'J3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + 'J3' + RESET + BLANK
            else:
                printline12 += GREY + 'J3' + RESET + BLANK
        elif 'j3o' in raising_range:
            printline12 += RED + 'J3' + RESET + BLANK
        elif 'j3o' in calling_range:
            printline12 += BLUE + 'J3' + RESET + BLANK
        elif 'j3o' in open_range:
            printline12 += GREEN + 'J3' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #t3o
        if (not checkhands.suited(hand)) and (card1[0] == 't' and card2[0] == '3' or card1[0] == '3' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + 'T3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + 'T3' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + 'T3' + RESET + BLANK
            else:
                printline12 += GREY + 'T3' + RESET + BLANK
        elif 't3o' in raising_range:
            printline12 += RED + 'T3' + RESET + BLANK
        elif 't3o' in calling_range:
            printline12 += BLUE + 'T3' + RESET + BLANK
        elif 't3o' in open_range:
            printline12 += GREEN + 'T3' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #93o
        if (not checkhands.suited(hand)) and (card1[0] == '9' and card2[0] == '3' or card1[0] == '3' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + '93' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + '93' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + '93' + RESET + BLANK
            else:
                printline12 += GREY + '93' + RESET + BLANK
        elif '93o' in raising_range:
            printline12 += RED + '93' + RESET + BLANK
        elif '93o' in calling_range:
            printline12 += BLUE + '93' + RESET + BLANK
        elif '93o' in open_range:
            printline12 += GREEN + '93' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #83o
        if (not checkhands.suited(hand)) and (card1[0] == '8' and card2[0] == '3' or card1[0] == '3' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + '83' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + '83' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + '83' + RESET + BLANK
            else:
                printline12 += GREY + '83' + RESET + BLANK
        elif '83o' in raising_range:
            printline12 += RED + '83' + RESET + BLANK
        elif '83o' in calling_range:
            printline12 += BLUE + '83' + RESET + BLANK
        elif '83o' in open_range:
            printline12 += GREEN + '83' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #73o
        if (not checkhands.suited(hand)) and (card1[0] == '7' and card2[0] == '3' or card1[0] == '3' and card2[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + '73' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + '73' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + '73' + RESET + BLANK
            else:
                printline12 += GREY + '73' + RESET + BLANK
        elif '73o' in raising_range:
            printline12 += RED + '73' + RESET + BLANK
        elif '73o' in calling_range:
            printline12 += BLUE + '73' + RESET + BLANK
        elif '73o' in open_range:
            printline12 += GREEN + '73' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #63o
        if (not checkhands.suited(hand)) and (card1[0] == '6' and card2[0] == '3' or card1[0] == '3' and card2[0] == '6'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + '63' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + '63' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + '63' + RESET + BLANK
            else:
                printline12 += GREY + '63' + RESET + BLANK
        elif '63o' in raising_range:
            printline12 += RED + '63' + RESET + BLANK
        elif '63o' in calling_range:
            printline12 += BLUE + '63' + RESET + BLANK
        elif '63o' in open_range:
            printline12 += GREEN + '63' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #53o
        if (not checkhands.suited(hand)) and (card1[0] == '5' and card2[0] == '3' or card1[0] == '3' and card2[0] == '5'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + '53' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + '53' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + '53' + RESET + BLANK
            else:
                printline12 += GREY + '53' + RESET + BLANK
        elif '53o' in raising_range:
            printline12 += RED + '53' + RESET + BLANK
        elif '53o' in calling_range:
            printline12 += BLUE + '53' + RESET + BLANK
        elif '53o' in open_range:
            printline12 += GREEN + '53' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #43o
        if (not checkhands.suited(hand)) and (card1[0] == '4' and card2[0] == '3' or card1[0] == '3' and card2[0] == '4'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + '43' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + '43' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + '43' + RESET + BLANK
            else:
                printline12 += GREY + '43' + RESET + BLANK
        elif '43o' in raising_range:
            printline12 += RED + '43' + RESET + BLANK
        elif '43o' in calling_range:
            printline12 += BLUE + '43' + RESET + BLANK
        elif '43o' in open_range:
            printline12 += GREEN + '43' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #33
        if checkhands.pocket_pairs(hand) and (card1[0] == '3'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + '33' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + '33' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + '33' + RESET + BLANK
            else:
                printline12 += GREY + '33' + RESET + BLANK
        elif '33' in raising_range:
            printline12 += RED + '33' + RESET + BLANK
        elif '33' in calling_range:
            printline12 += BLUE + '33' + RESET + BLANK
        elif '33' in open_range:
            printline12 += GREEN + '33' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #32s
        if checkhands.suited(hand) and (card1[0] == '3' and card2[0] == '2' or card1[0] == '2' and card2[0] == '3'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline12 += YELLOW + '32' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline12 += CYAN + '32' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline12 += CYAN + '32' + RESET + BLANK
            else:
                printline12 += GREY + '32' + RESET + BLANK
        elif '32s' in raising_range:
            printline12 += RED + '32' + RESET + BLANK
        elif '32s' in calling_range:
            printline12 += BLUE + '32' + RESET + BLANK
        elif '32s' in open_range:
            printline12 += GREEN + '32' + RESET + BLANK
        else:
            printline12 += BLANKCELL
        #line13
        #a2o
        if (not checkhands.suited(hand)) and (card1[0] == 'a' and card2[0] == '2' or card1[0] == '2' and card2[0] == 'a'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + 'A2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + 'A2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + 'A2' + RESET + BLANK
            else:
                printline13 += GREY + 'A2' + RESET + BLANK
        elif 'a2o' in raising_range:
            printline13 += RED + 'A2' + RESET + BLANK
        elif 'a2o' in calling_range:
            printline13 += BLUE + 'A2' + RESET + BLANK
        elif 'a2o' in open_range:
            printline13 += GREEN + 'A2' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #k2o
        if (not checkhands.suited(hand)) and (card1[0] == 'k' and card2[0] == '2' or card1[0] == '2' and card2[0] == 'k'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + 'K2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + 'K2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + 'K2' + RESET + BLANK
            else:
                printline13 += GREY + 'K2' + RESET + BLANK
        elif 'k2o' in raising_range:
            printline13 += RED + 'K2' + RESET + BLANK
        elif 'k2o' in calling_range:
            printline13 += BLUE + 'K2' + RESET + BLANK
        elif 'k2o' in open_range:
            printline13 += GREEN + 'K2' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #q2o
        if (not checkhands.suited(hand)) and (card1[0] == 'q' and card2[0] == '2' or card1[0] == '2' and card2[0] == 'q'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + 'Q2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + 'Q2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + 'Q2' + RESET + BLANK
            else:
                printline13 += GREY + 'Q2' + RESET + BLANK
        elif 'q2o' in raising_range:
            printline13 += RED + 'Q2' + RESET + BLANK
        elif 'q2o' in calling_range:
            printline13 += BLUE + 'Q2' + RESET + BLANK
        elif 'q2o' in open_range:
            printline13 += GREEN + 'Q2' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #j2o
        if (not checkhands.suited(hand)) and (card1[0] == 'j' and card2[0] == '2' or card1[0] == '2' and card2[0] == 'j'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + 'J2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + 'J2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + 'J2' + RESET + BLANK
            else:
                printline13 += GREY + 'J2' + RESET + BLANK
        elif 'j2o' in raising_range:
            printline13 += RED + 'J2' + RESET + BLANK
        elif 'j2o' in calling_range:
            printline13 += BLUE + 'J2' + RESET + BLANK
        elif 'j2o' in open_range:
            printline13 += GREEN + 'J2' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #t2o
        if (not checkhands.suited(hand)) and (card1[0] == 't' and card2[0] == '2' or card1[0] == '2' and card2[0] == 't'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + 'T2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + 'T2' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + 'T2' + RESET + BLANK
            else:
                printline13 += GREY + 'T2' + RESET + BLANK
        elif 't2o' in raising_range:
            printline13 += RED + 'T2' + RESET + BLANK
        elif 't2o' in calling_range:
            printline13 += BLUE + 'T2' + RESET + BLANK
        elif 't2o' in open_range:
            printline13 += GREEN + 'T2' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #92o
        if (not checkhands.suited(hand)) and (card1[0] == '9' and card2[0] == '2' or card1[0] == '2' and card2[0] == '9'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + '92' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + '92' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + '92' + RESET + BLANK
            else:
                printline13 += GREY + '92' + RESET + BLANK
        elif '92o' in raising_range:
            printline13 += RED + '92' + RESET + BLANK
        elif '92o' in calling_range:
            printline13 += BLUE + '92' + RESET + BLANK
        elif '92o' in open_range:
            printline13 += GREEN + '92' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #82o
        if (not checkhands.suited(hand)) and (card1[0] == '8' and card2[0] == '2' or card1[0] == '2' and card2[0] == '8'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + '82' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + '82' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + '82' + RESET + BLANK
            else:
                printline13 += GREY + '82' + RESET + BLANK
        elif '82o' in raising_range:
            printline13 += RED + '82' + RESET + BLANK
        elif '82o' in calling_range:
            printline13 += BLUE + '82' + RESET + BLANK
        elif '82o' in open_range:
            printline13 += GREEN + '82' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #72o
        if (not checkhands.suited(hand)) and (card1[0] == '7' and card2[0] == '2' or card1[0] == '2' and card2[0] == '7'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + '72' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + '72' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + '72' + RESET + BLANK
            else:
                printline13 += GREY + '72' + RESET + BLANK
        elif '72o' in raising_range:
            printline13 += RED + '72' + RESET + BLANK
        elif '72o' in calling_range:
            printline13 += BLUE + '72' + RESET + BLANK
        elif '72o' in open_range:
            printline13 += GREEN + '72' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #62o
        if (not checkhands.suited(hand)) and (card1[0] == '6' and card2[0] == '2' or card1[0] == '2' and card2[0] == '6'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + '62' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + '62' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + '62' + RESET + BLANK
            else:
                printline13 += GREY + '62' + RESET + BLANK
        elif '62o' in raising_range:
            printline13 += RED + '62' + RESET + BLANK
        elif '62o' in calling_range:
            printline13 += BLUE + '62' + RESET + BLANK
        elif '62o' in open_range:
            printline13 += GREEN + '62' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #52o
        if (not checkhands.suited(hand)) and (card1[0] == '5' and card2[0] == '2' or card1[0] == '2' and card2[0] == '5'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + '52' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + '52' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + '52' + RESET + BLANK
            else:
                printline13 += GREY + '52' + RESET + BLANK
        elif '52o' in raising_range:
            printline13 += RED + '52' + RESET + BLANK
        elif '52o' in calling_range:
            printline13 += BLUE + '52' + RESET + BLANK
        elif '52o' in open_range:
            printline13 += GREEN + '52' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #42o
        if (not checkhands.suited(hand)) and (card1[0] == '4' and card2[0] == '2' or card1[0] == '2' and card2[0] == '4'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + '42' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + '42' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + '42' + RESET + BLANK
            else:
                printline13 += GREY + '42' + RESET + BLANK
        elif '42o' in raising_range:
            printline13 += RED + '42' + RESET + BLANK
        elif '42o' in calling_range:
            printline13 += BLUE + '42' + RESET + BLANK
        elif '42o' in open_range:
            printline13 += GREEN + '42' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #32o
        if (not checkhands.suited(hand)) and (card1[0] == '3' and card2[0] == '2' or card1[0] == '2' and card2[0] == '3'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + '32' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + '32' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + '32' + RESET + BLANK
            else:
                printline13 += GREY + '32' + RESET + BLANK
        elif '32o' in raising_range:
            printline13 += RED + '32' + RESET + BLANK
        elif '32o' in calling_range:
            printline13 += BLUE + '32' + RESET + BLANK
        elif '32o' in open_range:
            printline13 += GREEN + '32' + RESET + BLANK
        else:
            printline13 += BLANKCELL
        #22
        if checkhands.pocket_pairs(hand) and (card1[0] == '2'):
            if checkhands.handInRange(card1, card2, raising_range):
                printline13 += YELLOW + '22' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, calling_range):
                printline13 += CYAN + '22' + RESET + BLANK
            elif checkhands.handInRange(card1, card2, open_range):
                printline13 += CYAN + '22' + RESET + BLANK
            else:
                printline13 += GREY + '22' + RESET + BLANK
        elif '22' in raising_range:
            printline13 += RED + '22' + RESET + BLANK
        elif '22' in calling_range:
            printline13 += BLUE + '22' + RESET + BLANK
        elif '22' in open_range:
            printline13 += GREEN + '22' + RESET + BLANK
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

def print_color_range_lines(liness):
            RED = '\033[1;31m'
            BLUE  = '\033[1;34m'
            CYAN  = '\033[1;36m'
            GREEN = '\033[0;32m'
            RESET = '\033[0;0m'
            BOLD  = '\033[;1m'
            REVERSE = '\033[;7m'
            GREY = '\033[1;30m'
            YELLOW ='\033[0;33m'
            RESET = '\033[0m'
            lines = liness
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
