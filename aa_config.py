buttonAA.config(bg = '#BDBDB7')
    if 'AA' in selected_range:
        if var.get()  == 1: #A
            prio = 0
            counter_lightblue = 0
            counter_blue = 0
            counter_red = 0
            counter_green = 0
            counter_orange = 0
            counter_yellow = 0
            for hand in expander.expandPP('AA'):
                for hh in a_check_fold:
                    if hand == hh.pohand:
                        counter_blue += 1
                        if prio < 1:
                            prio = 1
                for hh in a_bet_fold:
                    if hand == hh.pohand:
                        counter_lightblue += 1
                        if prio < 2:
                            prio = 2
                for hh in a_check_call:
                    if hand == hh.pohand:
                        counter_green += 1
                        if prio < 3:
                            prio = 3
                for hh in a_bet_call:
                    if hand == hh.pohand:
                        counter_orange += 1
                        if prio < 4:
                            prio = 4
                for hh in a_check_raise:
                    if hand == hh.pohand:
                        counter_red += 1
                        if prio < 5:
                            prio = 5
            colorlist = []
            colorlist.append(counter_blue)
            colorlist.append(counter_lightblue)
            colorlist.append(counter_green)
            colorlist.append(counter_orange)
            colorlist.append(counter_red)
            colorlist.sort(reverse=True)
            if colorlist[0] > colorlist[1]:
                #color the button with the most common action occurence,
                #if two are equal, color it purple
                buttonAA.config(bg = colorlist[0])
            else:
                buttonAA.config(bg ='purple')
        elif var.get() == 2: #B
            prio = 0
            for hand in expander.expandPP('AA'):
                for hh in b_fold:
                    if hand == hh.pohand:
                        ###print("1--------------" + hand)
                        if prio < 1:
                            prio = 1
                for hh in b_call:
                    if hand == hh.pohand:
                        ###print("2")
                        if prio < 1:
                            prio = 2
                for hh in b_raise:
                    if hand == hh.pohand:
                        ###print("3")
                        if prio < 1:
                            prio = 3
            if prio == 3:
                buttonAA.config(bg = 'red')
            elif prio == 2:
                buttonAA.config(bg = 'yellow')
            elif prio == 1:
                buttonAA.config(bg = 'blue')
            else:
                pass
        elif var.get() == 3: #C
            prio = 0
            for hand in expander.expandPP('AA'):
                for hh in c_bet_fold:
                    if hand == hh.pohand:
                        ###print("1--------------" + hand)
                        if prio < 1:
                            prio = 1
                for hh in c_check:
                    if hand == hh.pohand:
                        ###print("2")
                        if prio < 2:
                            prio = 2
                for hh in c_bet_call:
                    if hand == hh.pohand:
                        ###print("3")
                        if prio < 3:
                            prio = 3
            if prio == 3:
                buttonAA.config(bg = 'orange')
            elif prio == 2:
                buttonAA.config(bg = 'green')
            elif prio == 1:
                buttonAA.config(bg = 'lightblue')
            else:
                pass