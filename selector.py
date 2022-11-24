import tkinter as tk

import expander

mywindow = tk.Tk()
mywindow.geometry("500x500")

#new
color_suited = '#CDCD85'
color_suited_selected = '#FFFF40'

color_offsuit = '#C1C1CD'
color_offsuit_selected = '#8F8FBC'

color_pp = '#CDCDB7'
color_pp_selected = '#8B8B00'



color_spade = 'grey'
color_heart = 'orange'
color_diamond = 'lightblue'
color_club = 'lightgreen'

color_spade_selected = 'black'
color_heart_selected = 'red'
color_diamond_selected = 'blue'
color_club_selected = 'green'

suit_club = '\u2663'
suit_diamond = '\u2666'
suit_heart = '\u2665'
suit_spade = '\u2660'

selected_range = []
board_cards = []

slideValue = 0


#board cards functions A
def pressAs():
    if 'As' in board_cards:
        print('As=0')
        board_cards.remove('As')
        buttonAs.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('As=1')
            board_cards.append('As')
            buttonAs.config(bg=color_spade_selected, fg=color_spade)

def pressAh():
    if 'Ah' in board_cards:
        print('Ah=0')
        board_cards.remove('Ah')
        buttonAh.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('Ah=1')
            board_cards.append('Ah')
            buttonAh.config(bg=color_heart_selected, fg=color_heart)

def pressAd():
    if 'Ad' in board_cards:
        print('Ad=0')
        board_cards.remove('Ad')
        buttonAd.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('Ad=1')
            board_cards.append('Ad')
            buttonAd.config(bg=color_diamond_selected, fg=color_diamond)

def pressAc():
    if 'Ac' in board_cards:
        print('Ac=0')
        board_cards.remove('Ac')
        buttonAc.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('Ac=1')
            board_cards.append('Ac')
            buttonAc.config(bg=color_club_selected, fg=color_club)

#board cards functions K
def pressKs():
    if 'Ks' in board_cards:
        print('Ks=0')
        board_cards.remove('Ks')
        buttonKs.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('Ks=1')
            board_cards.append('Ks')
            buttonKs.config(bg=color_spade_selected, fg=color_spade)

def pressKh():
    if 'Kh' in board_cards:
        print('Kh=0')
        board_cards.remove('Kh')
        buttonKh.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('Kh=1')
            board_cards.append('Kh')
            buttonKh.config(bg=color_heart_selected, fg=color_heart)

def pressKd():
    if 'Kd' in board_cards:
        print('Kd=0')
        board_cards.remove('Kd')
        buttonKd.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('Kd=1')
            board_cards.append('Kd')
            buttonKd.config(bg=color_diamond_selected, fg=color_diamond)

def pressKc():
    if 'Kc' in board_cards:
        print('Kc=0')
        board_cards.remove('Kc')
        buttonKc.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('Kc=1')
            board_cards.append('Kc')
            buttonKc.config(bg=color_club_selected, fg=color_club)

#board cards functions Q
def pressQs():
    if 'Qs' in board_cards:
        print('Qs=0')
        board_cards.remove('Qs')
        buttonQs.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('Qs=1')
            board_cards.append('Qs')
            buttonQs.config(bg=color_spade_selected, fg=color_spade)

def pressQh():
    if 'Qh' in board_cards:
        print('Qh=0')
        board_cards.remove('Qh')
        buttonQh.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('Qh=1')
            board_cards.append('Qh')
            buttonQh.config(bg=color_heart_selected, fg=color_heart)

def pressQd():
    if 'Qd' in board_cards:
        print('Qd=0')
        board_cards.remove('Qd')
        buttonQd.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('Qd=1')
            board_cards.append('Qd')
            buttonQd.config(bg=color_diamond_selected, fg=color_diamond)

def pressQc():
    if 'Qc' in board_cards:
        print('Qc=0')
        board_cards.remove('Qc')
        buttonQc.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('Qc=1')
            board_cards.append('Qc')
            buttonQc.config(bg=color_club_selected, fg=color_club)

#board cards functions J
def pressJs():
    if 'Js' in board_cards:
        print('Js=0')
        board_cards.remove('Js')
        buttonJs.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('Js=1')
            board_cards.append('Js')
            buttonJs.config(bg=color_spade_selected, fg=color_spade)

def pressJh():
    if 'Jh' in board_cards:
        print('Jh=0')
        board_cards.remove('Jh')
        buttonJh.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('Jh=1')
            board_cards.append('Jh')
            buttonJh.config(bg=color_heart_selected, fg=color_heart)

def pressJd():
    if 'Jd' in board_cards:
        print('Jd=0')
        board_cards.remove('Jd')
        buttonJd.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('Jd=1')
            board_cards.append('Jd')
            buttonJd.config(bg=color_diamond_selected, fg=color_diamond)

def pressJc():
    if 'Jc' in board_cards:
        print('Jc=0')
        board_cards.remove('Jc')
        buttonJc.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('Jc=1')
            board_cards.append('Jc')
            buttonJc.config(bg=color_club_selected, fg=color_club)

#board cards functions T
def pressTs():
    if 'Ts' in board_cards:
        print('Ts=0')
        board_cards.remove('Ts')
        buttonTs.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('Ts=1')
            board_cards.append('Ts')
            buttonTs.config(bg=color_spade_selected, fg=color_spade)

def pressTh():
    if 'Th' in board_cards:
        print('Th=0')
        board_cards.remove('Th')
        buttonTh.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('Th=1')
            board_cards.append('Th')
            buttonTh.config(bg=color_heart_selected, fg=color_heart)

def pressTd():
    if 'Td' in board_cards:
        print('Td=0')
        board_cards.remove('Td')
        buttonTd.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('Td=1')
            board_cards.append('Td')
            buttonTd.config(bg=color_diamond_selected, fg=color_diamond)

def pressTc():
    if 'Tc' in board_cards:
        print('Tc=0')
        board_cards.remove('Tc')
        buttonTc.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('Tc=1')
            board_cards.append('Tc')
            buttonTc.config(bg=color_club_selected, fg=color_club)


#board cards functions 9
def press9s():
    if '9s' in board_cards:
        print('9s=0')
        board_cards.remove('9s')
        button9s.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('9s=1')
            board_cards.append('9s')
            button9s.config(bg=color_spade_selected, fg=color_spade)

def press9h():
    if '9h' in board_cards:
        print('9h=0')
        board_cards.remove('9h')
        button9h.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('9h=1')
            board_cards.append('9h')
            button9h.config(bg=color_heart_selected, fg=color_heart)

def press9d():
    if '9d' in board_cards:
        print('9d=0')
        board_cards.remove('9d')
        button9d.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('9d=1')
            board_cards.append('9d')
            button9d.config(bg=color_diamond_selected, fg=color_diamond)

def press9c():
    if '9c' in board_cards:
        print('9c=0')
        board_cards.remove('9c')
        button9c.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('9c=1')
            board_cards.append('9c')
            button9c.config(bg=color_club_selected, fg=color_club)

#board cards functions 8
def press8s():
    if '8s' in board_cards:
        print('8s=0')
        board_cards.remove('8s')
        button8s.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('8s=1')
            board_cards.append('8s')
            button8s.config(bg=color_spade_selected, fg=color_spade)

def press8h():
    if '8h' in board_cards:
        print('8h=0')
        board_cards.remove('8h')
        button8h.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('8h=1')
            board_cards.append('8h')
            button8h.config(bg=color_heart_selected, fg=color_heart)

def press8d():
    if '8d' in board_cards:
        print('8d=0')
        board_cards.remove('8d')
        button8d.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('8d=1')
            board_cards.append('8d')
            button8d.config(bg=color_diamond_selected, fg=color_diamond)

def press8c():
    if '8c' in board_cards:
        print('8c=0')
        board_cards.remove('8c')
        button8c.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('8c=1')
            board_cards.append('8c')
            button8c.config(bg=color_club_selected, fg=color_club)

#board cards functions 7
def press7s():
    if '7s' in board_cards:
        print('7s=0')
        board_cards.remove('7s')
        button7s.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('7s=1')
            board_cards.append('7s')
            button7s.config(bg=color_spade_selected, fg=color_spade)

def press7h():
    if '7h' in board_cards:
        print('7h=0')
        board_cards.remove('7h')
        button7h.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('7h=1')
            board_cards.append('7h')
            button7h.config(bg=color_heart_selected, fg=color_heart)

def press7d():
    if '7d' in board_cards:
        print('7d=0')
        board_cards.remove('7d')
        button7d.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('7d=1')
            board_cards.append('7d')
            button7d.config(bg=color_diamond_selected, fg=color_diamond)

def press7c():
    if '7c' in board_cards:
        print('7c=0')
        board_cards.remove('7c')
        button7c.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('7c=1')
            board_cards.append('7c')
            button7c.config(bg=color_club_selected, fg=color_club)

#board cards functions 6
def press6s():
    if '6s' in board_cards:
        print('6s=0')
        board_cards.remove('6s')
        button6s.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('6s=1')
            board_cards.append('6s')
            button6s.config(bg=color_spade_selected, fg=color_spade)

def press6h():
    if '6h' in board_cards:
        print('6h=0')
        board_cards.remove('6h')
        button6h.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('6h=1')
            board_cards.append('6h')
            button6h.config(bg=color_heart_selected, fg=color_heart)

def press6d():
    if '6d' in board_cards:
        print('6d=0')
        board_cards.remove('6d')
        button6d.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('6d=1')
            board_cards.append('6d')
            button6d.config(bg=color_diamond_selected, fg=color_diamond)

def press6c():
    if '6c' in board_cards:
        print('6c=0')
        board_cards.remove('6c')
        button6c.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('6c=1')
            board_cards.append('6c')
            button6c.config(bg=color_club_selected, fg=color_club)

#board cards functions 5
def press5s():
    if '5s' in board_cards:
        print('5s=0')
        board_cards.remove('5s')
        button5s.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('5s=1')
            board_cards.append('5s')
            button5s.config(bg=color_spade_selected, fg=color_spade)

def press5h():
    if '5h' in board_cards:
        print('5h=0')
        board_cards.remove('5h')
        button5h.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('5h=1')
            board_cards.append('5h')
            button5h.config(bg=color_heart_selected, fg=color_heart)

def press5d():
    if '5d' in board_cards:
        print('5d=0')
        board_cards.remove('5d')
        button5d.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('5d=1')
            board_cards.append('5d')
            button5d.config(bg=color_diamond_selected, fg=color_diamond)
            
def press5c():
    if '5c' in board_cards:
        print('5c=0')
        board_cards.remove('5c')
        button5c.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('5c=1')
            board_cards.append('5c')
            button5c.config(bg=color_club_selected, fg=color_club)

#board cards functions 4
def press4s():
    if '4s' in board_cards:
        print('4s=0')
        board_cards.remove('4s')
        button4s.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('4s=1')
            board_cards.append('4s')
            button4s.config(bg=color_spade_selected, fg=color_spade)

def press4h():
    if '4h' in board_cards:
        print('4h=0')
        board_cards.remove('4h')
        button4h.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('4h=1')
            board_cards.append('4h')
            button4h.config(bg=color_heart_selected, fg=color_heart)

def press4d():
    if '4d' in board_cards:
        print('4d=0')
        board_cards.remove('4d')
        button4d.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('4d=1')
            board_cards.append('4d')
            button4d.config(bg=color_diamond_selected, fg=color_diamond)
            
def press4c():
    if '4c' in board_cards:
        print('4c=0')
        board_cards.remove('4c')
        button4c.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('4c=1')
            board_cards.append('4c')
            button4c.config(bg=color_club_selected, fg=color_club)

#board cards functions 3
def press3s():
    if '3s' in board_cards:
        print('3s=0')
        board_cards.remove('3s')
        button3s.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('3s=1')
            board_cards.append('3s')
            button3s.config(bg=color_spade_selected, fg=color_spade)

def press3h():
    if '3h' in board_cards:
        print('3h=0')
        board_cards.remove('3h')
        button3h.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('3h=1')
            board_cards.append('3h')
            button3h.config(bg=color_heart_selected, fg=color_heart)

def press3d():
    if '3d' in board_cards:
        print('3d=0')
        board_cards.remove('3d')
        button3d.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('3d=1')
            board_cards.append('3d')
            button3d.config(bg=color_diamond_selected, fg=color_diamond)
            
def press3c():
    if '3c' in board_cards:
        print('3c=0')
        board_cards.remove('3c')
        button3c.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('3c=1')
            board_cards.append('3c')
            button3c.config(bg=color_club_selected, fg=color_club)

#board cards functions 2
def press2s():
    if '2s' in board_cards:
        print('2s=0')
        board_cards.remove('2s')
        button2s.config(bg=color_spade, fg=color_spade_selected)
    else:
        if len(board_cards) < 5:
            print('2s=1')
            board_cards.append('2s')
            button2s.config(bg=color_spade_selected, fg=color_spade)

def press2h():
    if '2h' in board_cards:
        print('2h=0')
        board_cards.remove('2h')
        button2h.config(bg=color_heart, fg=color_heart_selected)
    else:
        if len(board_cards) < 5:
            print('2h=1')
            board_cards.append('2h')
            button2h.config(bg=color_heart_selected, fg=color_heart)

def press2d():
    if '2d' in board_cards:
        print('2d=0')
        board_cards.remove('2d')
        button2d.config(bg=color_diamond, fg=color_diamond_selected)
    else:
        if len(board_cards) < 5:
            print('2d=1')
            board_cards.append('2d')
            button2d.config(bg=color_diamond_selected, fg=color_diamond)
            
def press2c():
    if '2c' in board_cards:
        print('2c=0')
        board_cards.remove('2c')
        button2c.config(bg=color_club, fg=color_club_selected)
    else:
        if len(board_cards) < 5:
            print('2c=1')
            board_cards.append('2c')
            button2c.config(bg=color_club_selected, fg=color_club)



def open_secondary_window():
    # Create secondary (or popup) window.
    secondary_window = tk.Toplevel()
    secondary_window.title("Secondary Window")
    secondary_window.config(width=200, height=200)
    # Create a button to close (destroy) this window.
    button_close = tk.Button(
        secondary_window,
        text="Close window",
        command=secondary_window.destroy
    )
    button_close.place(x=20, y=20)

#Label
#label = tk.Label(mywindow, text="Label Text")
#label.grid(row=0,column=1)

def buttonPress():
    print(selected_range)
    #print("Button Pressed!!")
    #Slider.set(0)
    expanded_range = []
    temporary_range_offsuit = []
    temporary_range_suit = []
    temporary_range_pp = []
    open_secondary_window()

    #Suited
    for hand in selected_range:
        if 's' in hand:
            temporary_range_suit = expander.expandSuit(hand)
            for hand in temporary_range_suit:
                if hand not in expanded_range:
                    expanded_range.append(hand)
        elif 'o' in hand:
            temporary_range_offsuit = expander.expandOffsuit(hand)
            for hand in temporary_range_offsuit:
                if hand not in expanded_range:
                    expanded_range.append(hand)
        elif 'o' not in hand and 's' not in hand:
            temporary_range_pp = expander.expandPP(hand)
            for hand in temporary_range_pp:
                if hand not in expanded_range:
                    expanded_range.append(hand)
        else:
            print("unknown hand")
            dumb = input("]")

    #PocketPairs
    fillrange = round(len(expanded_range)*100/1326,2)
    print("expanded range: " + str(len(expanded_range)) + "/1326   " + str(round(len(expanded_range)*100/1326,2)) + "%")
    Slider.set(round(fillrange))
    print(expanded_range)
    #popupwindow.mainloop()

#pocket pairs handlers

def pressAA():
    print("AA")
    if 'AA' in selected_range:
        selected_range.remove('AA')
        buttonAA.config(bg = color_pp)
    else:
        selected_range.append('AA')
        buttonAA.config(bg = color_pp_selected)
        #open_secondary_window()

def pressKK():
    print("KK")
    if 'KK' in selected_range:
        selected_range.remove('KK')
        buttonKK.config(bg = color_pp)
    else:
        selected_range.append('KK')
        buttonKK.config(bg = color_pp_selected)

def pressQQ():
    print("QQ")
    if 'QQ' in selected_range:
        selected_range.remove('QQ')
        buttonQQ.config(bg = color_pp)
    else:
        selected_range.append('QQ')
        buttonQQ.config(bg = color_pp_selected)

def pressJJ():
    print("JJ")
    if 'JJ' in selected_range:
        selected_range.remove('JJ')
        buttonJJ.config(bg = color_pp)
    else:
        selected_range.append('JJ')
        buttonJJ.config(bg = color_pp_selected)

def pressTT():
    print("TT")
    if 'TT' in selected_range:
        selected_range.remove('TT')
        buttonTT.config(bg = color_pp)
    else:
        selected_range.append('TT')
        buttonTT.config(bg = color_pp_selected)

def press99():
    print("99")
    if '99' in selected_range:
        selected_range.remove('99')
        button99.config(bg = color_pp)
    else:
        selected_range.append('99')
        button99.config(bg = color_pp_selected)

def press88():
    print("88")
    if '88' in selected_range:
        selected_range.remove('88')
        button88.config(bg = color_pp)
    else:
        selected_range.append('88')
        button88.config(bg = color_pp_selected)

def press77():
    print("77")
    if '77' in selected_range:
        selected_range.remove('77')
        button77.config(bg = color_pp)
    else:
        selected_range.append('77')
        button77.config(bg = color_pp_selected)

def press66():
    print("66")
    if '66' in selected_range:
        selected_range.remove('66')
        button66.config(bg = color_pp)
    else:
        selected_range.append('66')
        button66.config(bg = color_pp_selected)

def press55():
    print("55")
    if '55' in selected_range:
        selected_range.remove('55')
        button55.config(bg = color_pp)
    else:
        selected_range.append('55')
        button55.config(bg = color_pp_selected)

def press44():
    print("44")
    if '44' in selected_range:
        selected_range.remove('44')
        button44.config(bg = color_pp)
    else:
        selected_range.append('44')
        button44.config(bg = color_pp_selected)

def press33():
    print("33")
    if '33' in selected_range:
        selected_range.remove('33')
        button33.config(bg = color_pp)
    else:
        selected_range.append('33')
        button33.config(bg = color_pp_selected)

def press22():
    print("22")
    if '22' in selected_range:
        selected_range.remove('22')
        button22.config(bg = color_pp)
    else:
        selected_range.append('22')
        button22.config(bg = color_pp_selected)
        #print("range: " + str(len(selected_range)))

#suited handlers A
def pressAKs():
    print("AKs")
    if 'AKs' in selected_range:
        buttonAKs.config(bg = color_suited)
        selected_range.remove('AKs')
    else:
        buttonAKs.config(bg = color_suited_selected)
        selected_range.append('AKs')       

def pressAQs():
    print("AQs")
    if 'AQs' in selected_range:
        selected_range.remove('AQs')
        buttonAQs.config(bg = color_suited)
    else:
        selected_range.append('AQs')
        buttonAQs.config(bg = color_suited_selected)

def pressAJs():
    print("AJs")
    if 'AJs' in selected_range:
        selected_range.remove('AJs')
        buttonAJs.config(bg = color_suited)
    else:
        selected_range.append('AJs')
        buttonAJs.config(bg = color_suited_selected)

def pressATs():
    print("ATs")
    if 'ATs' in selected_range:
        selected_range.remove('ATs')
        buttonATs.config(bg = color_suited)
    else:
        selected_range.append('ATs')
        buttonATs.config(bg = color_suited_selected)

def pressA9s():
    print("A9s")
    if 'A9s' in selected_range:
        selected_range.remove('A9s')
        buttonA9s.config(bg = color_suited)
    else:
        selected_range.append('A9s')
        buttonA9s.config(bg = color_suited_selected)

def pressA8s():
    print("A8s")
    if 'A8s' in selected_range:
        selected_range.remove('A8s')
        buttonA8s.config(bg = color_suited)
    else:
        selected_range.append('A8s')
        buttonA8s.config(bg = color_suited_selected)

def pressA7s():
    print("A7s")
    if 'A7s' in selected_range:
        selected_range.remove('A7s')
        buttonA7s.config(bg = color_suited)
    else:
        selected_range.append('A7s')
        buttonA7s.config(bg = color_suited_selected)

def pressA6s():
    print("A6s")
    if 'A6s' in selected_range:
        selected_range.remove('A6s')
        buttonA6s.config(bg = color_suited)
    else:
        selected_range.append('A6s')
        buttonA6s.config(bg = color_suited_selected)

def pressA5s():
    print("A5s")
    if 'A5s' in selected_range:
        selected_range.remove('A5s')
        buttonA5s.config(bg = color_suited)
    else:
        selected_range.append('A5s')
        buttonA5s.config(bg = color_suited_selected)

def pressA4s():
    print("A4s")
    if 'A4s' in selected_range:
        selected_range.remove('A4s')
        buttonA4s.config(bg = color_suited)
    else:
        selected_range.append('A4s')
        buttonA4s.config(bg = color_suited_selected)

def pressA3s():
    print("A3s")
    if 'A3s' in selected_range:
        selected_range.remove('A3s')
        buttonA3s.config(bg = color_suited)
    else:
        selected_range.append('A3s')
        buttonA3s.config(bg = color_suited_selected)

def pressA2s():
    print("A2s")
    if 'A2s' in selected_range:
        selected_range.remove('A2s')
        buttonA2s.config(bg = color_suited)
    else:
        selected_range.append('A2s')
        buttonA2s.config(bg = color_suited_selected)

#suited handlers K
    
def pressKQs():
    print("KQs")
    if 'KQs' in selected_range:
        selected_range.remove('KQs')
        buttonKQs.config(bg = color_suited)
    else:
        selected_range.append('KQs')
        buttonKQs.config(bg = color_suited_selected)

def pressKJs():
    print("KJs")
    if 'KJs' in selected_range:
        selected_range.remove('KJs')
        buttonKJs.config(bg = color_suited)
    else:
        selected_range.append('KJs')
        buttonKJs.config(bg = color_suited_selected)

def pressKTs():
    print("KTs")
    if 'KTs' in selected_range:
        selected_range.remove('KTs')
        buttonKTs.config(bg = color_suited)
    else:
        selected_range.append('KTs')
        buttonKTs.config(bg = color_suited_selected)

def pressK9s():
    print("K9s")
    if 'K9s' in selected_range:
        selected_range.remove('K9s')
        buttonK9s.config(bg = color_suited)
    else:
        selected_range.append('K9s')
        buttonK9s.config(bg = color_suited_selected)

def pressK8s():
    print("K8s")
    if 'K8s' in selected_range:
        selected_range.remove('K8s')
        buttonK8s.config(bg = color_suited)
    else:
        selected_range.append('K8s')
        buttonK8s.config(bg = color_suited_selected)

def pressK7s():
    print("K7s")
    if 'K7s' in selected_range:
        selected_range.remove('K7s')
        buttonK7s.config(bg = color_suited)
    else:
        selected_range.append('K7s')
        buttonK7s.config(bg = color_suited_selected)

def pressK6s():
    print("K6s")
    if 'K6s' in selected_range:
        selected_range.remove('K6s')
        buttonK6s.config(bg = color_suited)
    else:
        selected_range.append('K6s')
        buttonK6s.config(bg = color_suited_selected)

def pressK5s():
    print("K5s")
    if 'K5s' in selected_range:
        selected_range.remove('K5s')
        buttonK5s.config(bg = color_suited)
    else:
        selected_range.append('K5s')
        buttonK5s.config(bg = color_suited_selected)

def pressK4s():
    print("K4s")
    if 'K4s' in selected_range:
        selected_range.remove('K4s')
        buttonK4s.config(bg = color_suited)
    else:
        selected_range.append('K4s')
        buttonK4s.config(bg = color_suited_selected)

def pressK3s():
    print("K3s")
    if 'K3s' in selected_range:
        selected_range.remove('K3s')
        buttonK3s.config(bg = color_suited)
    else:
        selected_range.append('K3s')
        buttonK3s.config(bg = color_suited_selected)

def pressK2s():
    print("K2s")
    if 'K2s' in selected_range:
        selected_range.remove('K2s')
        buttonK2s.config(bg = color_suited)
    else:
        selected_range.append('K2s')
        buttonK2s.config(bg = color_suited_selected)

#suited handlers Q

def pressQJs():
    print("QJs")
    if 'QJs' in selected_range:
        selected_range.remove('QJs')
        buttonQJs.config(bg = color_suited)
    else:
        selected_range.append('QJs')
        buttonQJs.config(bg = color_suited_selected)

def pressQTs():
    print("QTs")
    if 'QTs' in selected_range:
        selected_range.remove('QTs')
        buttonQTs.config(bg = color_suited)
    else:
        selected_range.append('QTs')
        buttonQTs.config(bg = color_suited_selected)

def pressQ9s():
    print("Q9s")
    if 'Q9s' in selected_range:
        selected_range.remove('Q9s')
        buttonQ9s.config(bg = color_suited)
    else:
        selected_range.append('Q9s')
        buttonQ9s.config(bg = color_suited_selected)

def pressQ8s():
    print("Q8s")
    if 'Q8s' in selected_range:
        selected_range.remove('Q8s')
        buttonQ8s.config(bg = color_suited)
    else:
        selected_range.append('Q8s')
        buttonQ8s.config(bg = color_suited_selected)

def pressQ7s():
    print("Q7s")
    if 'Q7s' in selected_range:
        selected_range.remove('Q7s')
        buttonQ7s.config(bg = color_suited)
    else:
        selected_range.append('Q7s')
        buttonQ7s.config(bg = color_suited_selected)

def pressQ6s():
    print("Q6s")
    if 'Q6s' in selected_range:
        selected_range.remove('Q6s')
        buttonQ6s.config(bg = color_suited)
    else:
        selected_range.append('Q6s')
        buttonQ6s.config(bg = color_suited_selected)

def pressQ5s():
    print("Q5s")
    if 'Q5s' in selected_range:
        selected_range.remove('Q5s')
        buttonQ5s.config(bg = color_suited)
    else:
        selected_range.append('Q5s')
        buttonQ5s.config(bg = color_suited_selected)

def pressQ4s():
    print("Q4s")
    if 'Q4s' in selected_range:
        selected_range.remove('Q4s')
        buttonQ4s.config(bg = color_suited)
    else:
        selected_range.append('Q4s')
        buttonQ4s.config(bg = color_suited_selected)

def pressQ3s():
    print("Q3s")
    if 'Q3s' in selected_range:
        selected_range.remove('Q3s')
        buttonQ3s.config(bg = color_suited)
    else:
        selected_range.append('Q3s')
        buttonQ3s.config(bg = color_suited_selected)

def pressQ2s():
    print("Q2s")
    if 'Q2s' in selected_range:
        selected_range.remove('Q2s')
        buttonQ2s.config(bg = color_suited)
    else:
        selected_range.append('Q2s')
        buttonQ2s.config(bg = color_suited_selected)

#suited handlers J

def pressJTs():
    print("JTs")
    if 'JTs' in selected_range:
        selected_range.remove('JTs')
        buttonJTs.config(bg = color_suited)
    else:
        selected_range.append('JTs')
        buttonJTs.config(bg = color_suited_selected)

def pressJ9s():
    print("J9s")
    if 'J9s' in selected_range:
        selected_range.remove('J9s')
        buttonJ9s.config(bg = color_suited)
    else:
        selected_range.append('J9s')
        buttonJ9s.config(bg = color_suited_selected)

def pressJ8s():
    print("J8s")
    if 'J8s' in selected_range:
        selected_range.remove('J8s')
        buttonJ8s.config(bg = color_suited)
    else:
        selected_range.append('J8s')
        buttonJ8s.config(bg = color_suited_selected)

def pressJ7s():
    print("J7s")
    if 'J7s' in selected_range:
        selected_range.remove('J7s')
        buttonJ7s.config(bg = color_suited)
    else:
        selected_range.append('J7s')
        buttonJ7s.config(bg = color_suited_selected)

def pressJ6s():
    print("J6s")
    if 'J6s' in selected_range:
        selected_range.remove('J6s')
        buttonJ6s.config(bg = color_suited)
    else:
        selected_range.append('J6s')
        buttonJ6s.config(bg = color_suited_selected)

def pressJ5s():
    print("J5s")
    if 'J5s' in selected_range:
        selected_range.remove('J5s')
        buttonJ5s.config(bg = color_suited)
    else:
        selected_range.append('J5s')
        buttonJ5s.config(bg = color_suited_selected)

def pressJ4s():
    print("J4s")
    if 'J4s' in selected_range:
        selected_range.remove('J4s')
        buttonJ4s.config(bg = color_suited)
    else:
        selected_range.append('J4s')
        buttonJ4s.config(bg = color_suited_selected)

def pressJ3s():
    print("J3s")
    if 'J3s' in selected_range:
        selected_range.remove('J3s')
        buttonJ3s.config(bg = color_suited)
    else:
        selected_range.append('J3s')
        buttonJ3s.config(bg = color_suited_selected)

def pressJ2s():
    print("J2s")
    if 'J2s' in selected_range:
        selected_range.remove('J2s')
        buttonT2s.config(bg = color_suited)
    else:
        selected_range.append('J2s')
        buttonJ2s.config(bg = color_suited_selected)

#suited handlers T

def pressT9s():
    print("T9s")
    if 'T9s' in selected_range:
        selected_range.remove('T9s')
        buttonT9s.config(bg = color_suited)
    else:
        selected_range.append('T9s')
        buttonT9s.config(bg = color_suited_selected)

def pressT8s():
    print("T8s")
    if 'T8s' in selected_range:
        selected_range.remove('T8s')
        buttonT8s.config(bg = color_suited)
    else:
        selected_range.append('T8s')
        buttonT8s.config(bg = color_suited_selected)

def pressT7s():
    print("T7s")
    if 'T7s' in selected_range:
        selected_range.remove('T7s')
        buttonT7s.config(bg = color_suited)
    else:
        selected_range.append('T7s')
        buttonT7s.config(bg = color_suited_selected)

def pressT6s():
    print("T6s")
    if 'T6s' in selected_range:
        selected_range.remove('T6s')
        buttonT6s.config(bg = color_suited)
    else:
        selected_range.append('T6s')
        buttonT6s.config(bg = color_suited_selected)

def pressT5s():
    print("T5s")
    if 'T5s' in selected_range:
        selected_range.remove('T5s')
        buttonT5s.config(bg = color_suited)
    else:
        selected_range.append('T5s')
        buttonT5s.config(bg = color_suited_selected)

def pressT4s():
    print("T4s")
    if 'T4s' in selected_range:
        selected_range.remove('T4s')
        buttonT4s.config(bg = color_suited)
    else:
        selected_range.append('T4s')
        buttonT4s.config(bg = color_suited_selected)

def pressT3s():
    print("T3s")
    if 'T3s' in selected_range:
        selected_range.remove('T3s')
        buttonT3s.config(bg = color_suited)
    else:
        selected_range.append('T3s')
        buttonT3s.config(bg = color_suited_selected)

def pressT2s():
    print("T2s")
    if 'T2s' in selected_range:
        selected_range.remove('T2s')
        buttonT2s.config(bg = color_suited)
    else:
        selected_range.append('T2s')
        buttonT2s.config(bg = color_suited_selected)

#suited handlers 9

def press98s():
    print("98s")
    if '98s' in selected_range:
        selected_range.remove('98s')
        button98s.config(bg = color_suited)
    else:
        selected_range.append('98s')
        button98s.config(bg = color_suited_selected)

def press97s():
    print("97s")
    if '97s' in selected_range:
        selected_range.remove('97s')
        button97s.config(bg = color_suited)
    else:
        selected_range.append('97s')
        button97s.config(bg = color_suited_selected)

def press96s():
    print("96s")
    if '96s' in selected_range:
        selected_range.remove('96s')
        button96s.config(bg = color_suited)
    else:
        selected_range.append('96s')
        button96s.config(bg = color_suited_selected)

def press95s():
    print("95s")
    if '95s' in selected_range:
        selected_range.remove('95s')
        button95s.config(bg = color_suited)
    else:
        selected_range.append('95s')
        button95s.config(bg = color_suited_selected)

def press94s():
    print("94s")
    if '94s' in selected_range:
        selected_range.remove('94s')
        button94s.config(bg = color_suited)
    else:
        selected_range.append('94s')
        button94s.config(bg = color_suited_selected)

def press93s():
    print("93s")
    if '93s' in selected_range:
        selected_range.remove('93s')
        button93s.config(bg = color_suited)
    else:
        selected_range.append('93s')
        button93s.config(bg = color_suited_selected)

def press92s():
    print("92s")
    if '92s' in selected_range:
        selected_range.remove('92s')
        button92s.config(bg = color_suited)
    else:
        selected_range.append('92s')
        button92s.config(bg = color_suited_selected)

#suited handlers 8

def press87s():
    print("87s")
    if '87s' in selected_range:
        selected_range.remove('87s')
        button87s.config(bg = color_suited)
    else:
        selected_range.append('87s')
        button87s.config(bg = color_suited_selected)

def press86s():
    print("86s")
    if '86s' in selected_range:
        selected_range.remove('86s')
        button86s.config(bg = color_suited)
    else:
        selected_range.append('86s')
        button86s.config(bg = color_suited_selected)

def press85s():
    print("85s")
    if '85s' in selected_range:
        selected_range.remove('85s')
        button85s.config(bg = color_suited)
    else:
        selected_range.append('85s')
        button85s.config(bg = color_suited_selected)

def press84s():
    print("84s")
    if '84s' in selected_range:
        selected_range.remove('84s')
        button84s.config(bg = color_suited)
    else:
        selected_range.append('84s')
        button84s.config(bg = color_suited_selected)

def press83s():
    print("83s")
    if '83s' in selected_range:
        selected_range.remove('83s')
        button83s.config(bg = color_suited)
    else:
        selected_range.append('83s')
        button83s.config(bg = color_suited_selected)

def press82s():
    print("82s")
    if '82s' in selected_range:
        selected_range.remove('82s')
        button82s.config(bg = color_suited)
    else:
        selected_range.append('82s')
        button82s.config(bg = color_suited_selected)

#suited handlers 7

def press76s():
    print("76s")
    if '76s' in selected_range:
        selected_range.remove('76s')
        button76s.config(bg = color_suited)
    else:
        selected_range.append('76s')
        button76s.config(bg = color_suited_selected)

def press75s():
    print("75s")
    if '75s' in selected_range:
        selected_range.remove('75s')
        button75s.config(bg = color_suited)
    else:
        selected_range.append('75s')
        button75s.config(bg = color_suited_selected)

def press74s():
    print("74s")
    if '74s' in selected_range:
        selected_range.remove('74s')
        button74s.config(bg = color_suited)
    else:
        selected_range.append('74s')
        button74s.config(bg = color_suited_selected)

def press73s():
    print("73s")
    if '73s' in selected_range:
        selected_range.remove('73s')
        button73s.config(bg = color_suited)
    else:
        selected_range.append('73s')
        button73s.config(bg = color_suited_selected)

def press72s():
    print("72s")
    if '72s' in selected_range:
        selected_range.remove('72s')
        button72s.config(bg = color_suited)
    else:
        selected_range.append('82s')
        button72s.config(bg = color_suited_selected)

#suited handlers 6

def press65s():
    print("65s")
    if '65s' in selected_range:
        selected_range.remove('65s')
        button65s.config(bg = color_suited)
    else:
        selected_range.append('65s')
        button65s.config(bg = color_suited_selected)

def press64s():
    print("64s")
    if '64s' in selected_range:
        selected_range.remove('64s')
        button64s.config(bg = color_suited)
    else:
        selected_range.append('64s')
        button64s.config(bg = color_suited_selected)

def press63s():
    print("63s")
    if '63s' in selected_range:
        selected_range.remove('63s')
        button63s.config(bg = color_suited)
    else:
        selected_range.append('63s')
        button63s.config(bg = color_suited_selected)

def press62s():
    print("62s")
    if '62s' in selected_range:
        selected_range.remove('62s')
        button62s.config(bg = color_suited)
    else:
        selected_range.append('62s')
        button62s.config(bg = color_suited_selected)

#suited handlers 5

def press54s():
    print("54s")
    if '54s' in selected_range:
        selected_range.remove('54s')
        button54s.config(bg = color_suited)
    else:
        selected_range.append('54s')
        button54s.config(bg = color_suited_selected)

def press53s():
    print("53s")
    if '53s' in selected_range:
        selected_range.remove('53s')
        button53s.config(bg = color_suited)
    else:
        selected_range.append('53s')
        button53s.config(bg = color_suited_selected)

def press52s():
    print("52s")
    if '52s' in selected_range:
        selected_range.remove('52s')
        button52s.config(bg = color_suited)
    else:
        selected_range.append('52s')
        button52s.config(bg = color_suited_selected)

#suited handlers 4

def press43s():
    print("43s")
    if '43s' in selected_range:
        selected_range.remove('43s')
        button43s.config(bg = color_suited)
    else:
        selected_range.append('43s')
        button43s.config(bg = color_suited_selected)

def press42s():
    print("42s")
    if '42s' in selected_range:
        selected_range.remove('42s')
        button42s.config(bg = color_suited)
    else:
        selected_range.append('42s')
        button42s.config(bg = color_suited_selected)

#suited handlers 3

def press32s():
    print("32s")
    if '32s' in selected_range:
        selected_range.remove('32s')
        button32s.config(bg = color_suited)
    else:
        selected_range.append('32s')
        button32s.config(bg = color_suited_selected)

#offsuited handlers

def pressAKo():
    print("AKo")
    if 'AKo' in selected_range:
        buttonAKo.config(bg = color_offsuit)
        selected_range.remove('AKo')
    else:
        buttonAKo.config(bg = color_offsuit_selected)
        selected_range.append('AKo')

def pressAQo():
    print("AQo")
    if 'AQo' in selected_range:
        buttonAQo.config(bg = color_offsuit)
        selected_range.remove('AQo')
    else:
        buttonAQo.config(bg = color_offsuit_selected)
        selected_range.append('AQo')

def pressAJo():
    print("AJo")
    if 'AJo' in selected_range:
        buttonAJo.config(bg = color_offsuit)
        selected_range.remove('AJo')
    else:
        buttonAJo.config(bg = color_offsuit_selected)
        selected_range.append('AJo')

def pressATo():
    print("ATo")
    if 'ATo' in selected_range:
        buttonATo.config(bg = color_offsuit)
        selected_range.remove('ATo')
    else:
        buttonATo.config(bg = color_offsuit_selected)
        selected_range.append('ATo')

def pressA9o():
    print("A9o")
    if 'A9o' in selected_range:
        buttonA9o.config(bg = color_offsuit)
        selected_range.remove('A9o')
    else:
        buttonA9o.config(bg = color_offsuit_selected)
        selected_range.append('A9o')

def pressA8o():
    print("A8o")
    if 'A8o' in selected_range:
        buttonA8o.config(bg = color_offsuit)
        selected_range.remove('A8o')
    else:
        buttonA8o.config(bg = color_offsuit_selected)
        selected_range.append('A8o')

def pressA7o():
    print("A7o")
    if 'A7o' in selected_range:
        buttonA7o.config(bg = color_offsuit)
        selected_range.remove('A7o')
    else:
        buttonA7o.config(bg = color_offsuit_selected)
        selected_range.append('A7o')

def pressA6o():
    print("A6o")
    if 'A6o' in selected_range:
        buttonA6o.config(bg = color_offsuit)
        selected_range.remove('A6o')
    else:
        buttonA6o.config(bg = color_offsuit_selected)
        selected_range.append('A6o')

def pressA5o():
    print("A5o")
    if 'A5o' in selected_range:
        buttonA5o.config(bg = color_offsuit)
        selected_range.remove('A5o')
    else:
        buttonA5o.config(bg = color_offsuit_selected)
        selected_range.append('A5o')

def pressA4o():
    print("A4o")
    if 'A4o' in selected_range:
        buttonA4o.config(bg = color_offsuit)
        selected_range.remove('A4o')
    else:
        buttonA4o.config(bg = color_offsuit_selected)
        selected_range.append('A4o')

def pressA3o():
    print("A3o")
    if 'A3o' in selected_range:
        buttonA3o.config(bg = color_offsuit)
        selected_range.remove('A3o')
    else:
        buttonA3o.config(bg = color_offsuit_selected)
        selected_range.append('A3o')

def pressA2o():
    print("A2o")
    if 'A2o' in selected_range:
        buttonA2o.config(bg = color_offsuit)
        selected_range.remove('A2o')
    else:
        buttonA2o.config(bg = color_offsuit_selected)
        selected_range.append('A2o')

# K

def pressKQo():
    print("KQo")
    if 'KQo' in selected_range:
        buttonKQo.config(bg = color_offsuit)
        selected_range.remove('KQo')
    else:
        buttonKQo.config(bg = color_offsuit_selected)
        selected_range.append('KQo')

def pressKJo():
    print("KJo")
    if 'KJo' in selected_range:
        buttonKJo.config(bg = color_offsuit)
        selected_range.remove('KJo')
    else:
        buttonKJo.config(bg = color_offsuit_selected)
        selected_range.append('KJo')

def pressKTo():
    print("KTo")
    if 'KTo' in selected_range:
        buttonKTo.config(bg = color_offsuit)
        selected_range.remove('KTo')
    else:
        buttonKTo.config(bg = color_offsuit_selected)
        selected_range.append('KTo')

def pressK9o():
    print("K9o")
    if 'K9o' in selected_range:
        buttonK9o.config(bg = color_offsuit)
        selected_range.remove('K9o')
    else:
        buttonK9o.config(bg = color_offsuit_selected)
        selected_range.append('K9o')

def pressK8o():
    print("K8o")
    if 'K8o' in selected_range:
        buttonK8o.config(bg = color_offsuit)
        selected_range.remove('K8o')
    else:
        buttonK8o.config(bg = color_offsuit_selected)
        selected_range.append('K8o')

def pressK7o():
    print("K7o")
    if 'K7o' in selected_range:
        buttonK7o.config(bg = color_offsuit)
        selected_range.remove('K7o')
    else:
        buttonK7o.config(bg = color_offsuit_selected)
        selected_range.append('K7o')

def pressK6o():
    print("K6o")
    if 'K6o' in selected_range:
        buttonK6o.config(bg = color_offsuit)
        selected_range.remove('K6o')
    else:
        buttonK6o.config(bg = color_offsuit_selected)
        selected_range.append('K6o')

def pressK5o():
    print("K5o")
    if 'K5o' in selected_range:
        buttonA5o.config(bg = color_offsuit)
        selected_range.remove('K5o')
    else:
        buttonK5o.config(bg = color_offsuit_selected)
        selected_range.append('K5o')

def pressK4o():
    print("K4o")
    if 'K4o' in selected_range:
        buttonK4o.config(bg = color_offsuit)
        selected_range.remove('K4o')
    else:
        buttonK4o.config(bg = color_offsuit_selected)
        selected_range.append('K4o')

def pressK3o():
    print("K3o")
    if 'K3o' in selected_range:
        buttonK3o.config(bg = color_offsuit)
        selected_range.remove('K3o')
    else:
        buttonK3o.config(bg = color_offsuit_selected)
        selected_range.append('K3o')

def pressK2o():
    print("K2o")
    if 'K2o' in selected_range:
        buttonK2o.config(bg = color_offsuit)
        selected_range.remove('K2o')
    else:
        buttonK2o.config(bg = color_offsuit_selected)
        selected_range.append('K2o') 

# Q

def pressQJo():
    print("QJo")
    if 'QJo' in selected_range:
        buttonQJo.config(bg = color_offsuit)
        selected_range.remove('QJo')
    else:
        buttonQJo.config(bg = color_offsuit_selected)
        selected_range.append('QJo')

def pressQTo():
    print("QTo")
    if 'QTo' in selected_range:
        buttonQTo.config(bg = color_offsuit)
        selected_range.remove('QTo')
    else:
        buttonQTo.config(bg = color_offsuit_selected)
        selected_range.append('QTo')

def pressQ9o():
    print("Q9o")
    if 'Q9o' in selected_range:
        buttonQ9o.config(bg = color_offsuit)
        selected_range.remove('Q9o')
    else:
        buttonQ9o.config(bg = color_offsuit_selected)
        selected_range.append('Q9o')

def pressQ8o():
    print("Q8o")
    if 'Q8o' in selected_range:
        buttonQ8o.config(bg = color_offsuit)
        selected_range.remove('Q8o')
    else:
        buttonQ8o.config(bg = color_offsuit_selected)
        selected_range.append('Q8o')

def pressQ7o():
    print("Q7o")
    if 'Q7o' in selected_range:
        buttonQ7o.config(bg = color_offsuit)
        selected_range.remove('Q7o')
    else:
        buttonQ7o.config(bg = color_offsuit_selected)
        selected_range.append('Q7o')

def pressQ6o():
    print("Q6o")
    if 'Q6o' in selected_range:
        buttonQ6o.config(bg = color_offsuit)
        selected_range.remove('Q6o')
    else:
        buttonQ6o.config(bg = color_offsuit_selected)
        selected_range.append('Q6o')

def pressQ5o():
    print("Q5o")
    if 'Q5o' in selected_range:
        buttonQ5o.config(bg = color_offsuit)
        selected_range.remove('Q5o')
    else:
        buttonQ5o.config(bg = color_offsuit_selected)
        selected_range.append('Q5o')

def pressQ4o():
    print("Q4o")
    if 'Q4o' in selected_range:
        buttonQ4o.config(bg = color_offsuit)
        selected_range.remove('Q4o')
    else:
        buttonQ4o.config(bg = color_offsuit_selected)
        selected_range.append('Q4o')

def pressQ3o():
    print("Q3o")
    if 'Q3o' in selected_range:
        buttonQ3o.config(bg = color_offsuit)
        selected_range.remove('Q3o')
    else:
        buttonQ3o.config(bg = color_offsuit_selected)
        selected_range.append('Q3o')

def pressQ2o():
    print("Q2o")
    if 'Q2o' in selected_range:
        buttonQ2o.config(bg = color_offsuit)
        selected_range.remove('Q2o')
    else:
        buttonQ2o.config(bg = color_offsuit_selected)
        selected_range.append('Q2o')

# J

def pressJTo():
    print("JTo")
    if 'JTo' in selected_range:
        buttonJTo.config(bg = color_offsuit)
        selected_range.remove('JTo')
    else:
        buttonJTo.config(bg = color_offsuit_selected)
        selected_range.append('JTo')

def pressJ9o():
    print("J9o")
    if 'J9o' in selected_range:
        buttonJ9o.config(bg = color_offsuit)
        selected_range.remove('J9o')
    else:
        buttonJ9o.config(bg = color_offsuit_selected)
        selected_range.append('J9o')

def pressJ8o():
    print("J8o")
    if 'J8o' in selected_range:
        buttonJ8o.config(bg = color_offsuit)
        selected_range.remove('J8o')
    else:
        buttonJ8o.config(bg = color_offsuit_selected)
        selected_range.append('J8o')

def pressJ7o():
    print("J7o")
    if 'J7o' in selected_range:
        buttonJ7o.config(bg = color_offsuit)
        selected_range.remove('J7o')
    else:
        buttonJ7o.config(bg = color_offsuit_selected)
        selected_range.append('J7o')

def pressJ6o():
    print("J6o")
    if 'J6o' in selected_range:
        buttonJ6o.config(bg = color_offsuit)
        selected_range.remove('J6o')
    else:
        buttonJ6o.config(bg = color_offsuit_selected)
        selected_range.append('J6o')

def pressJ5o():
    print("J5o")
    if 'J5o' in selected_range:
        buttonJ5o.config(bg = color_offsuit)
        selected_range.remove('J5o')
    else:
        buttonJ5o.config(bg = color_offsuit_selected)
        selected_range.append('J5o')

def pressJ4o():
    print("J4o")
    if 'J4o' in selected_range:
        buttonJ4o.config(bg = color_offsuit)
        selected_range.remove('J4o')
    else:
        buttonJ4o.config(bg = color_offsuit_selected)
        selected_range.append('J4o')

def pressJ3o():
    print("J3o")
    if 'J3o' in selected_range:
        buttonJ3o.config(bg = color_offsuit)
        selected_range.remove('J3o')
    else:
        buttonJ3o.config(bg = color_offsuit_selected)
        selected_range.append('J3o')

def pressJ2o():
    print("J2o")
    if 'J2o' in selected_range:
        buttonJ2o.config(bg = color_offsuit)
        selected_range.remove('J2o')
    else:
        buttonJ2o.config(bg = color_offsuit_selected)
        selected_range.append('J2o')

# T

def pressT9o():
    print("T9o")
    if 'T9o' in selected_range:
        buttonT9o.config(bg = color_offsuit)
        selected_range.remove('T9o')
    else:
        buttonT9o.config(bg = color_offsuit_selected)
        selected_range.append('T9o')

def pressT8o():
    print("T8o")
    if 'T8o' in selected_range:
        buttonT8o.config(bg = color_offsuit)
        selected_range.remove('T8o')
    else:
        buttonT8o.config(bg = color_offsuit_selected)
        selected_range.append('T8o')

def pressT7o():
    print("T7o")
    if 'T7o' in selected_range:
        buttonT7o.config(bg = color_offsuit)
        selected_range.remove('T7o')
    else:
        buttonT7o.config(bg = color_offsuit_selected)
        selected_range.append('T7o')

def pressT6o():
    print("T6o")
    if 'T6o' in selected_range:
        buttonT6o.config(bg = color_offsuit)
        selected_range.remove('T6o')
    else:
        buttonT6o.config(bg = color_offsuit_selected)
        selected_range.append('T6o')

def pressT5o():
    print("T5o")
    if 'T5o' in selected_range:
        buttonT5o.config(bg = color_offsuit)
        selected_range.remove('T5o')
    else:
        buttonT5o.config(bg = color_offsuit_selected)
        selected_range.append('T5o')

def pressT4o():
    print("T4o")
    if 'T4o' in selected_range:
        buttonT4o.config(bg = color_offsuit)
        selected_range.remove('T4o')
    else:
        buttonT4o.config(bg = color_offsuit_selected)
        selected_range.append('T4o')

def pressT3o():
    print("T3o")
    if 'T3o' in selected_range:
        buttonT3o.config(bg = color_offsuit)
        selected_range.remove('T3o')
    else:
        buttonT3o.config(bg = color_offsuit_selected)
        selected_range.append('T3o')

def pressT2o():
    print("T2o")
    if 'T2o' in selected_range:
        buttonT2o.config(bg = color_offsuit)
        selected_range.remove('T2o')
    else:
        buttonT2o.config(bg = color_offsuit_selected)
        selected_range.append('T2o')

# 9

def press98o():
    print("98o")
    if '98o' in selected_range:
        button98o.config(bg = color_offsuit)
        selected_range.remove('98o')
    else:
        button98o.config(bg = color_offsuit_selected)
        selected_range.append('98o')

def press97o():
    print("97o")
    if '97o' in selected_range:
        button97o.config(bg = color_offsuit)
        selected_range.remove('97o')
    else:
        button97o.config(bg = color_offsuit_selected)
        selected_range.append('97o')

def press96o():
    print("96o")
    if '96o' in selected_range:
        button96o.config(bg = color_offsuit)
        selected_range.remove('96o')
    else:
        button96o.config(bg = color_offsuit_selected)
        selected_range.append('96o')

def press95o():
    print("95o")
    if '95o' in selected_range:
        button95o.config(bg = color_offsuit)
        selected_range.remove('95o')
    else:
        button95o.config(bg = color_offsuit_selected)
        selected_range.append('95o')

def press94o():
    print("94o")
    if '94o' in selected_range:
        button94o.config(bg = color_offsuit)
        selected_range.remove('94o')
    else:
        button94o.config(bg = color_offsuit_selected)
        selected_range.append('94o')

def press93o():
    print("93o")
    if '93o' in selected_range:
        button93o.config(bg = color_offsuit)
        selected_range.remove('93o')
    else:
        button93o.config(bg = color_offsuit_selected)
        selected_range.append('93o')

def press92o():
    print("92o")
    if '92o' in selected_range:
        button92o.config(bg = color_offsuit)
        selected_range.remove('92o')
    else:
        button92o.config(bg = color_offsuit_selected)
        selected_range.append('92o')

# 8

def press87o():
    print("87o")
    if '87o' in selected_range:
        button87o.config(bg = color_offsuit)
        selected_range.remove('87o')
    else:
        button87o.config(bg = color_offsuit_selected)
        selected_range.append('87o')

def press86o():
    print("86o")
    if '86o' in selected_range:
        button86o.config(bg = color_offsuit)
        selected_range.remove('86o')
    else:
        button86o.config(bg = color_offsuit_selected)
        selected_range.append('86o')

def press85o():
    print("85o")
    if '85o' in selected_range:
        button85o.config(bg = color_offsuit)
        selected_range.remove('85o')
    else:
        button85o.config(bg = color_offsuit_selected)
        selected_range.append('85o')

def press84o():
    print("84o")
    if '84o' in selected_range:
        button84o.config(bg = color_offsuit)
        selected_range.remove('84o')
    else:
        button84o.config(bg = color_offsuit_selected)
        selected_range.append('84o')

def press83o():
    print("83o")
    if '83o' in selected_range:
        button83o.config(bg = color_offsuit)
        selected_range.remove('83o')
    else:
        button83o.config(bg = color_offsuit_selected)
        selected_range.append('83o')

def press82o():
    print("82o")
    if '82o' in selected_range:
        button82o.config(bg = color_offsuit)
        selected_range.remove('82o')
    else:
        button82o.config(bg = color_offsuit_selected)
        selected_range.append('82o')

# 7
def press76o():
    print("76o")
    if '76o' in selected_range:
        button76o.config(bg = color_offsuit)
        selected_range.remove('76o')
    else:
        button76o.config(bg = color_offsuit_selected)
        selected_range.append('76o')

def press75o():
    print("75o")
    if '75o' in selected_range:
        button75o.config(bg = color_offsuit)
        selected_range.remove('75o')
    else:
        button75o.config(bg = color_offsuit_selected)
        selected_range.append('75o')

def press74o():
    print("74o")
    if '74o' in selected_range:
        button74o.config(bg = color_offsuit)
        selected_range.remove('74o')
    else:
        button74o.config(bg = color_offsuit_selected)
        selected_range.append('74o')

def press73o():
    print("73o")
    if '73o' in selected_range:
        button73o.config(bg = color_offsuit)
        selected_range.remove('73o')
    else:
        button73o.config(bg = color_offsuit_selected)
        selected_range.append('73o')

def press72o():
    print("72o")
    if '72o' in selected_range:
        button72o.config(bg = color_offsuit)
        selected_range.remove('72o')
    else:
        button72o.config(bg = color_offsuit_selected)
        selected_range.append('72o')

# 6
def press65o():
    print("65o")
    if '65o' in selected_range:
        button65o.config(bg = color_offsuit)
        selected_range.remove('65o')
    else:
        button65o.config(bg = color_offsuit_selected)
        selected_range.append('65o')

def press64o():
    print("64o")
    if '64o' in selected_range:
        button64o.config(bg = color_offsuit)
        selected_range.remove('64o')
    else:
        button64o.config(bg = color_offsuit_selected)
        selected_range.append('64o')

def press63o():
    print("63o")
    if '63o' in selected_range:
        button63o.config(bg = color_offsuit)
        selected_range.remove('63o')
    else:
        button63o.config(bg = color_offsuit_selected)
        selected_range.append('63o')

def press62o():
    print("62o")
    if '62o' in selected_range:
        button62o.config(bg = color_offsuit)
        selected_range.remove('62o')
    else:
        button62o.config(bg = color_offsuit_selected)
        selected_range.append('62o')

# 5

def press54o():
    print("54o")
    if '54o' in selected_range:
        button54o.config(bg = color_offsuit)
        selected_range.remove('54o')
    else:
        button54o.config(bg = color_offsuit_selected)
        selected_range.append('54o')

def press53o():
    print("53o")
    if '53o' in selected_range:
        button53o.config(bg = color_offsuit)
        selected_range.remove('53o')
    else:
        button53o.config(bg = color_offsuit_selected)
        selected_range.append('53o')

def press52o():
    print("52o")
    if '52o' in selected_range:
        button52o.config(bg = color_offsuit)
        selected_range.remove('52o')
    else:
        button52o.config(bg = color_offsuit_selected)
        selected_range.append('52o')

# 4

def press43o():
    print("43o")
    if '43o' in selected_range:
        button43o.config(bg = color_offsuit)
        selected_range.remove('43o')
    else:
        button43o.config(bg = color_offsuit_selected)
        selected_range.append('43o')

def press42o():
    print("42o")
    if '42o' in selected_range:
        button42o.config(bg = color_offsuit)
        selected_range.remove('42o')
    else:
        button42o.config(bg = color_offsuit_selected)
        selected_range.append('42o')

# 3

def press32o():
    print("32o")
    if '32o' in selected_range:
        button32o.config(bg = color_offsuit)
        selected_range.remove('32o')
    else:
        button32o.config(bg = color_offsuit_selected)
        selected_range.append('32o')

'''
def textBox():
    print(textb.get())
'''
    
def slideValueSet():
    print (Slider.get())
    if int(Slider.get()) > 1:
        pressAA()



#Button
#row=1
buttonAA = tk.Button(mywindow,text='AA',command=pressAA,bg=color_pp)
buttonAA.grid(row=1,column=0,sticky = "NSEW")
buttonAKs = tk.Button(mywindow,text='AK',command=pressAKs,bg=color_suited)
buttonAKs.grid(row=1,column=1,sticky = "NSEW")
buttonAQs = tk.Button(mywindow,text='AQ',command=pressAQs,bg=color_suited) #,bg='red
buttonAQs.grid(row=1,column=2,sticky = "NSEW")
buttonAJs = tk.Button(mywindow,text='AJ',command=pressAJs,bg=color_suited) #,bg='red
buttonAJs.grid(row=1,column=3,sticky = "NSEW")
buttonATs = tk.Button(mywindow,text='AT',command=pressATs,bg=color_suited) #,bg='red
buttonATs.grid(row=1,column=4,sticky = "NSEW")
buttonA9s = tk.Button(mywindow,text='A9',command=pressA9s,bg=color_suited) #,bg='red
buttonA9s.grid(row=1,column=5,sticky = "NSEW")
buttonA8s = tk.Button(mywindow,text='A8',command=pressA8s,bg=color_suited) #,bg='red
buttonA8s.grid(row=1,column=6,sticky = "NSEW")
buttonA7s = tk.Button(mywindow,text='A7',command=pressA7s,bg=color_suited) #,bg='red
buttonA7s.grid(row=1,column=7,sticky = "NSEW")
buttonA6s = tk.Button(mywindow,text='A6',command=pressA6s,bg=color_suited) #,bg='red
buttonA6s.grid(row=1,column=8,sticky = "NSEW")
buttonA5s = tk.Button(mywindow,text='A5',command=pressA5s,bg=color_suited) #,bg='red
buttonA5s.grid(row=1,column=9,sticky = "NSEW")
buttonA4s = tk.Button(mywindow,text='A4',command=pressA4s,bg=color_suited) #,bg='red
buttonA4s.grid(row=1,column=10,sticky = "NSEW")
buttonA3s = tk.Button(mywindow,text='A3',command=pressA3s,bg=color_suited) #,bg='red
buttonA3s.grid(row=1,column=11,sticky = "NSEW")
buttonA2s = tk.Button(mywindow,text='A2',command=pressA2s,bg=color_suited) #,bg='red
buttonA2s.grid(row=1,column=12, padx=(0,15))

#board cards A
buttonAs = tk.Button(mywindow,text='A' + suit_spade ,command=pressAs,bg=color_spade, fg=color_spade_selected)
buttonAs.grid(row=1,column=13)

buttonAh = tk.Button(mywindow,text='A' + suit_heart,command=pressAh,bg=color_heart, fg = color_heart_selected)
buttonAh.grid(row=1,column=14)

buttonAd = tk.Button(mywindow,text='A' + suit_diamond,command=pressAd,bg=color_diamond, fg=color_diamond_selected)
buttonAd.grid(row=1,column=15)

buttonAc = tk.Button(mywindow,text='A' + suit_club,command=pressAc,bg=color_club, fg=color_club_selected)
buttonAc.grid(row=1,column=16)



#row=2
buttonAKo = tk.Button(mywindow,text='AK',command=pressAKo,bg=color_offsuit)
buttonAKo.grid(row=2,column=0,sticky = "NSEW")
buttonKK = tk.Button(mywindow,text='KK',command=pressKK,bg=color_pp)
buttonKK.grid(row=2,column=1,sticky = "NSEW")

buttonKQs = tk.Button(mywindow,text='KQ',command=pressKQs,bg=color_suited) #,bg='red
buttonKQs.grid(row=2,column=2,sticky = "NSEW")
buttonKJs = tk.Button(mywindow,text='KJ',command=pressKJs,bg=color_suited) #,bg='red
buttonKJs.grid(row=2,column=3,sticky = "NSEW")
buttonKTs = tk.Button(mywindow,text='KT',command=pressKTs,bg=color_suited) #,bg='red
buttonKTs.grid(row=2,column=4,sticky = "NSEW")
buttonK9s = tk.Button(mywindow,text='K9',command=pressK9s,bg=color_suited) #,bg='red
buttonK9s.grid(row=2,column=5,sticky = "NSEW")
buttonK8s = tk.Button(mywindow,text='K8',command=pressK8s,bg=color_suited) #,bg='red
buttonK8s.grid(row=2,column=6,sticky = "NSEW")
buttonK7s = tk.Button(mywindow,text='K7',command=pressK7s,bg=color_suited) #,bg='red
buttonK7s.grid(row=2,column=7,sticky = "NSEW")
buttonK6s = tk.Button(mywindow,text='K6',command=pressK6s,bg=color_suited) #,bg='red
buttonK6s.grid(row=2,column=8,sticky = "NSEW")
buttonK5s = tk.Button(mywindow,text='K5',command=pressK5s,bg=color_suited) #,bg='red
buttonK5s.grid(row=2,column=9,sticky = "NSEW")
buttonK4s = tk.Button(mywindow,text='K4',command=pressK4s,bg=color_suited) #,bg='red
buttonK4s.grid(row=2,column=10,sticky = "NSEW")
buttonK3s = tk.Button(mywindow,text='K3',command=pressK3s,bg=color_suited) #,bg='red
buttonK3s.grid(row=2,column=11,sticky = "NSEW")
buttonK2s = tk.Button(mywindow,text='K2',command=pressK2s,bg=color_suited) #,bg='red
buttonK2s.grid(row=2,column=12,padx=(0,15))

#board cards K
buttonKs = tk.Button(mywindow,text='K' + suit_spade,command=pressKs,bg=color_spade, fg=color_spade_selected)
buttonKs.grid(row=2,column=13)

buttonKh = tk.Button(mywindow,text='K' + suit_heart,command=pressKh,bg=color_heart, fg=color_heart_selected)
buttonKh.grid(row=2,column=14)

buttonKd = tk.Button(mywindow,text='K' + suit_diamond,command=pressKd,bg=color_diamond, fg=color_diamond_selected)
buttonKd.grid(row=2,column=15)

buttonKc = tk.Button(mywindow,text='K' + suit_club,command=pressKc,bg=color_club, fg=color_club_selected)
buttonKc.grid(row=2,column=16)

#row=3
buttonAQo = tk.Button(mywindow,text='AQ',command=pressAQo,bg=color_offsuit)
buttonAQo.grid(row=3,column=0,sticky = "NSEW")
buttonKQo = tk.Button(mywindow,text='KQ',command=pressKQo,bg=color_offsuit)
buttonKQo.grid(row=3,column=1,sticky = "NSEW")
buttonQQ = tk.Button(mywindow,text='QQ',command=pressQQ,bg=color_pp)
buttonQQ.grid(row=3,column=2,sticky = "NSEW")

buttonQJs = tk.Button(mywindow,text='QJ',command=pressQJs,bg=color_suited) #,bg='red
buttonQJs.grid(row=3,column=3,sticky = "NSEW")
buttonQTs = tk.Button(mywindow,text='QT',command=pressQTs,bg=color_suited) #,bg='red
buttonQTs.grid(row=3,column=4,sticky = "NSEW")
buttonQ9s = tk.Button(mywindow,text='Q9',command=pressQ9s,bg=color_suited) #,bg='red
buttonQ9s.grid(row=3,column=5,sticky = "NSEW")
buttonQ8s = tk.Button(mywindow,text='Q8',command=pressQ8s,bg=color_suited) #,bg='red
buttonQ8s.grid(row=3,column=6,sticky = "NSEW")
buttonQ7s = tk.Button(mywindow,text='Q7',command=pressQ7s,bg=color_suited) #,bg='red
buttonQ7s.grid(row=3,column=7,sticky = "NSEW")
buttonQ6s = tk.Button(mywindow,text='Q6',command=pressQ6s,bg=color_suited) #,bg='red
buttonQ6s.grid(row=3,column=8,sticky = "NSEW")
buttonQ5s = tk.Button(mywindow,text='Q5',command=pressQ5s,bg=color_suited) #,bg='red
buttonQ5s.grid(row=3,column=9,sticky = "NSEW")
buttonQ4s = tk.Button(mywindow,text='Q4',command=pressQ4s,bg=color_suited) #,bg='red
buttonQ4s.grid(row=3,column=10,sticky = "NSEW")
buttonQ3s = tk.Button(mywindow,text='Q3',command=pressQ3s,bg=color_suited) #,bg='red
buttonQ3s.grid(row=3,column=11,sticky = "NSEW")
buttonQ2s = tk.Button(mywindow,text='Q2',command=pressQ2s,bg=color_suited) #,bg='red
buttonQ2s.grid(row=3,column=12,padx=(0,15))

#board cards Q
buttonQs = tk.Button(mywindow,text='Q' + suit_spade ,command=pressQs,bg=color_spade, fg=color_spade_selected)
buttonQs.grid(row=3,column=13)

buttonQh = tk.Button(mywindow,text='Q' + suit_heart,command=pressQh,bg=color_heart, fg = color_heart_selected)
buttonQh.grid(row=3,column=14)

buttonQd = tk.Button(mywindow,text='Q' + suit_diamond,command=pressQd,bg=color_diamond, fg=color_diamond_selected)
buttonQd.grid(row=3,column=15)

buttonQc = tk.Button(mywindow,text='Q' + suit_club,command=pressQc,bg=color_club, fg=color_club_selected)
buttonQc.grid(row=3,column=16)

#row=4
buttonAJo = tk.Button(mywindow,text='AJ',command=pressAJo,bg=color_offsuit)
buttonAJo.grid(row=4,column=0,sticky = "NSEW")
buttonKJo = tk.Button(mywindow,text='KJ',command=pressKJo,bg=color_offsuit)
buttonKJo.grid(row=4,column=1,sticky = "NSEW")
buttonQJo = tk.Button(mywindow,text='QJ',command=pressQJo,bg=color_offsuit)
buttonQJo.grid(row=4,column=2,sticky = "NSEW")

buttonJJ = tk.Button(mywindow,text='JJ',command=pressJJ,bg=color_pp) #,bg='red
buttonJJ.grid(row=4,column=3,sticky = "NSEW")
buttonJTs = tk.Button(mywindow,text='JT',command=pressJTs,bg=color_suited) #,bg='red
buttonJTs.grid(row=4,column=4,sticky = "NSEW")
buttonJ9s = tk.Button(mywindow,text='J9',command=pressJ9s,bg=color_suited) #,bg='red
buttonJ9s.grid(row=4,column=5,sticky = "NSEW")
buttonJ8s = tk.Button(mywindow,text='J8',command=pressJ8s,bg=color_suited) #,bg='red
buttonJ8s.grid(row=4,column=6,sticky = "NSEW")
buttonJ7s = tk.Button(mywindow,text='J7',command=pressJ7s,bg=color_suited) #,bg='red
buttonJ7s.grid(row=4,column=7,sticky = "NSEW")
buttonJ6s = tk.Button(mywindow,text='J6',command=pressJ6s,bg=color_suited) #,bg='red
buttonJ6s.grid(row=4,column=8,sticky = "NSEW")
buttonJ5s = tk.Button(mywindow,text='J5',command=pressJ5s,bg=color_suited) #,bg='red
buttonJ5s.grid(row=4,column=9,sticky = "NSEW")
buttonJ4s = tk.Button(mywindow,text='J4',command=pressJ4s,bg=color_suited) #,bg='red
buttonJ4s.grid(row=4,column=10,sticky = "NSEW")
buttonJ3s = tk.Button(mywindow,text='J3',command=pressJ3s,bg=color_suited) #,bg='red
buttonJ3s.grid(row=4,column=11,sticky = "NSEW")
buttonJ2s = tk.Button(mywindow,text='J2',command=pressJ2s,bg=color_suited) #,bg='red
buttonJ2s.grid(row=4,column=12,padx=(0,15))

#board cards J
buttonJs = tk.Button(mywindow,text='J' + suit_spade ,command=pressJs,bg=color_spade, fg=color_spade_selected)
buttonJs.grid(row=4,column=13,sticky = "NSEW")

buttonJh = tk.Button(mywindow,text='J' + suit_heart,command=pressJh,bg=color_heart, fg = color_heart_selected)
buttonJh.grid(row=4,column=14,sticky = "NSEW")

buttonJd = tk.Button(mywindow,text='J' + suit_diamond,command=pressJd,bg=color_diamond, fg=color_diamond_selected)
buttonJd.grid(row=4,column=15,sticky = "NSEW")

buttonJc = tk.Button(mywindow,text='J' + suit_club,command=pressJc,bg=color_club, fg=color_club_selected)
buttonJc.grid(row=4,column=16,sticky = "NSEW")

#row=5

buttonATo = tk.Button(mywindow,text='AT',command=pressATo,bg=color_offsuit)
buttonATo.grid(row=5,column=0,sticky = "NSEW")
buttonKTo = tk.Button(mywindow,text='KT',command=pressKTo,bg=color_offsuit)
buttonKTo.grid(row=5,column=1,sticky = "NSEW")
buttonQTo = tk.Button(mywindow,text='QT',command=pressQTo,bg=color_offsuit)
buttonQTo.grid(row=5,column=2,sticky = "NSEW")
buttonJTo = tk.Button(mywindow,text='JT',command=pressJTo,bg=color_offsuit) #,bg='red
buttonJTo.grid(row=5,column=3,sticky = "NSEW")
buttonTT = tk.Button(mywindow,text='TT',command=pressTT,bg=color_pp) #,bg='red
buttonTT.grid(row=5,column=4,sticky = "NSEW")
buttonT9s = tk.Button(mywindow,text='T9',command=pressT9s,bg=color_suited) #,bg='red
buttonT9s.grid(row=5,column=5,sticky = "NSEW")
buttonT8s = tk.Button(mywindow,text='T8',command=pressT8s,bg=color_suited) #,bg='red
buttonT8s.grid(row=5,column=6,sticky = "NSEW")
buttonT7s = tk.Button(mywindow,text='T7',command=pressT7s,bg=color_suited) #,bg='red
buttonT7s.grid(row=5,column=7,sticky = "NSEW")
buttonT6s = tk.Button(mywindow,text='T6',command=pressT6s,bg=color_suited) #,bg='red
buttonT6s.grid(row=5,column=8,sticky = "NSEW")
buttonT5s = tk.Button(mywindow,text='T5',command=pressT5s,bg=color_suited) #,bg='red
buttonT5s.grid(row=5,column=9,sticky = "NSEW")
buttonT4s = tk.Button(mywindow,text='T4',command=pressT4s,bg=color_suited) #,bg='red
buttonT4s.grid(row=5,column=10,sticky = "NSEW")
buttonT3s = tk.Button(mywindow,text='T3',command=pressT3s,bg=color_suited) #,bg='red
buttonT3s.grid(row=5,column=11,sticky = "NSEW")
buttonT2s = tk.Button(mywindow,text='T2',command=pressT2s,bg=color_suited) #,bg='red
buttonT2s.grid(row=5,column=12,padx=(0,15))

#board cards T
buttonTs = tk.Button(mywindow,text='T' + suit_spade ,command=pressTs,bg=color_spade, fg=color_spade_selected)
buttonTs.grid(row=5,column=13,sticky = "NSEW")

buttonTh = tk.Button(mywindow,text='T' + suit_heart,command=pressTh,bg=color_heart, fg = color_heart_selected)
buttonTh.grid(row=5,column=14,sticky = "NSEW")

buttonTd = tk.Button(mywindow,text='T' + suit_diamond,command=pressTd,bg=color_diamond, fg=color_diamond_selected)
buttonTd.grid(row=5,column=15,sticky = "NSEW")

buttonTc = tk.Button(mywindow,text='T' + suit_club,command=pressTc,bg=color_club, fg=color_club_selected)
buttonTc.grid(row=5,column=16,sticky = "NSEW")

#row=6

buttonA9o = tk.Button(mywindow,text='A9',command=pressA9o,bg=color_offsuit)
buttonA9o.grid(row=6,column=0,sticky = "NSEW")
buttonK9o = tk.Button(mywindow,text='K9',command=pressK9o,bg=color_offsuit)
buttonK9o.grid(row=6,column=1,sticky = "NSEW")
buttonQ9o = tk.Button(mywindow,text='Q9',command=pressQ9o,bg=color_offsuit)
buttonQ9o.grid(row=6,column=2,sticky = "NSEW")
buttonJ9o = tk.Button(mywindow,text='J9',command=pressJ9o,bg=color_offsuit) #,bg='red
buttonJ9o.grid(row=6,column=3,sticky = "NSEW")
buttonT9o = tk.Button(mywindow,text='T9',command=pressT9o,bg=color_offsuit) #,bg='red
buttonT9o.grid(row=6,column=4,sticky = "NSEW")
button99 = tk.Button(mywindow,text='99',command=press99,bg=color_pp) #,bg='red
button99.grid(row=6,column=5,sticky = "NSEW")
button98s = tk.Button(mywindow,text='98',command=press98s,bg=color_suited) #,bg='red
button98s.grid(row=6,column=6,sticky = "NSEW")
button97s = tk.Button(mywindow,text='97',command=press97s,bg=color_suited) #,bg='red
button97s.grid(row=6,column=7,sticky = "NSEW")
button96s = tk.Button(mywindow,text='96',command=press96s,bg=color_suited) #,bg='red
button96s.grid(row=6,column=8,sticky = "NSEW")
button95s = tk.Button(mywindow,text='95',command=press95s,bg=color_suited) #,bg='red
button95s.grid(row=6,column=9,sticky = "NSEW")
button94s = tk.Button(mywindow,text='94',command=press94s,bg=color_suited) #,bg='red
button94s.grid(row=6,column=10,sticky = "NSEW")
button93s = tk.Button(mywindow,text='93',command=press93s,bg=color_suited) #,bg='red
button93s.grid(row=6,column=11,sticky = "NSEW")
button92s = tk.Button(mywindow,text='92',command=press92s,bg=color_suited) #,bg='red
button92s.grid(row=6,column=12,padx=(0,15))

#board cards 9
button9s = tk.Button(mywindow,text='9' + suit_spade ,command=press9s,bg=color_spade, fg=color_spade_selected)
button9s.grid(row=6,column=13,sticky = "NSEW")

button9h = tk.Button(mywindow,text='9' + suit_heart,command=press9h,bg=color_heart, fg = color_heart_selected)
button9h.grid(row=6,column=14,sticky = "NSEW")

button9d = tk.Button(mywindow,text='9' + suit_diamond,command=press9d,bg=color_diamond, fg=color_diamond_selected)
button9d.grid(row=6,column=15,sticky = "NSEW")

button9c = tk.Button(mywindow,text='9' + suit_club,command=press9c,bg=color_club, fg=color_club_selected)
button9c.grid(row=6,column=16,sticky = "NSEW")

#row=7

buttonA8o = tk.Button(mywindow,text='A8',command=pressA8o,bg=color_offsuit)
buttonA8o.grid(row=7,column=0,sticky = "NSEW")
buttonK8o = tk.Button(mywindow,text='K8',command=pressK8o,bg=color_offsuit)
buttonK8o.grid(row=7,column=1,sticky = "NSEW")
buttonQ8o = tk.Button(mywindow,text='Q8',command=pressQ8o,bg=color_offsuit)
buttonQ8o.grid(row=7,column=2,sticky = "NSEW")
buttonJ8o = tk.Button(mywindow,text='J8',command=pressJ8o,bg=color_offsuit) #,bg='red
buttonJ8o.grid(row=7,column=3,sticky = "NSEW")
buttonT8o = tk.Button(mywindow,text='T8',command=pressT8o,bg=color_offsuit) #,bg='red
buttonT8o.grid(row=7,column=4,sticky = "NSEW")
button98o = tk.Button(mywindow,text='98',command=press98o,bg=color_offsuit) #,bg='red
button98o.grid(row=7,column=5,sticky = "NSEW")
button88 = tk.Button(mywindow,text='88',command=press88,bg=color_pp) #,bg='red
button88.grid(row=7,column=6,sticky = "NSEW")
button87s = tk.Button(mywindow,text='87',command=press87s,bg=color_suited) #,bg='red
button87s.grid(row=7,column=7,sticky = "NSEW")
button86s = tk.Button(mywindow,text='86',command=press86s,bg=color_suited) #,bg='red
button86s.grid(row=7,column=8,sticky = "NSEW")
button85s = tk.Button(mywindow,text='85',command=press85s,bg=color_suited) #,bg='red
button85s.grid(row=7,column=9,sticky = "NSEW")
button84s = tk.Button(mywindow,text='84',command=press84s,bg=color_suited) #,bg='red
button84s.grid(row=7,column=10,sticky = "NSEW")
button83s = tk.Button(mywindow,text='83',command=press83s,bg=color_suited) #,bg='red
button83s.grid(row=7,column=11,sticky = "NSEW")
button82s = tk.Button(mywindow,text='82',command=press82s,bg=color_suited) #,bg='red
button82s.grid(row=7,column=12,padx=(0,15))

#board cards 8
button8s = tk.Button(mywindow,text='8' + suit_spade ,command=press8s,bg=color_spade, fg=color_spade_selected)
button8s.grid(row=7,column=13,sticky = "NSEW")

button8h = tk.Button(mywindow,text='8' + suit_heart,command=press8h,bg=color_heart, fg = color_heart_selected)
button8h.grid(row=7,column=14,sticky = "NSEW")

button8d = tk.Button(mywindow,text='8' + suit_diamond,command=press8d,bg=color_diamond, fg=color_diamond_selected)
button8d.grid(row=7,column=15,sticky = "NSEW")

button8c = tk.Button(mywindow,text='8' + suit_club,command=press8c,bg=color_club, fg=color_club_selected)
button8c.grid(row=7,column=16,sticky = "NSEW")

#row=8

buttonA7o = tk.Button(mywindow,text='A7',command=pressA7o,bg=color_offsuit)
buttonA7o.grid(row=8,column=0,sticky = "NSEW")
buttonK7o = tk.Button(mywindow,text='K7',command=pressK7o,bg=color_offsuit)
buttonK7o.grid(row=8,column=1,sticky = "NSEW")
buttonQ7o = tk.Button(mywindow,text='Q7',command=pressQ7o,bg=color_offsuit)
buttonQ7o.grid(row=8,column=2,sticky = "NSEW")
buttonJ7o = tk.Button(mywindow,text='J7',command=pressJ7o,bg=color_offsuit) #,bg='red
buttonJ7o.grid(row=8,column=3,sticky = "NSEW")
buttonT7o = tk.Button(mywindow,text='T7',command=pressT7o,bg=color_offsuit) #,bg='red
buttonT7o.grid(row=8,column=4,sticky = "NSEW")
button97o = tk.Button(mywindow,text='97',command=press97o,bg=color_offsuit) #,bg='red
button97o.grid(row=8,column=5,sticky = "NSEW")
button87o = tk.Button(mywindow,text='87',command=press87o,bg=color_offsuit) #,bg='red
button87o.grid(row=8,column=6,sticky = "NSEW")
button77 = tk.Button(mywindow,text='77',command=press77,bg=color_pp) #,bg='red
button77.grid(row=8,column=7,sticky = "NSEW")
button76s = tk.Button(mywindow,text='76',command=press76s,bg=color_suited) #,bg='red
button76s.grid(row=8,column=8,sticky = "NSEW")
button75s = tk.Button(mywindow,text='75',command=press75s,bg=color_suited) #,bg='red
button75s.grid(row=8,column=9,sticky = "NSEW")
button74s = tk.Button(mywindow,text='74',command=press74s,bg=color_suited) #,bg='red
button74s.grid(row=8,column=10,sticky = "NSEW")
button73s = tk.Button(mywindow,text='73',command=press73s,bg=color_suited) #,bg='red
button73s.grid(row=8,column=11,sticky = "NSEW")
button72s = tk.Button(mywindow,text='72',command=press72s,bg=color_suited) #,bg='red
button72s.grid(row=8,column=12,padx=(0,15))

#board cards 7
button7s = tk.Button(mywindow,text='7' + suit_spade ,command=press7s,bg=color_spade, fg=color_spade_selected)
button7s.grid(row=8,column=13,sticky = "NSEW")

button7h = tk.Button(mywindow,text='7' + suit_heart,command=press7h,bg=color_heart, fg = color_heart_selected)
button7h.grid(row=8,column=14,sticky = "NSEW")

button7d = tk.Button(mywindow,text='7' + suit_diamond,command=press7d,bg=color_diamond, fg=color_diamond_selected)
button7d.grid(row=8,column=15,sticky = "NSEW")

button7c = tk.Button(mywindow,text='7' + suit_club,command=press7c,bg=color_club, fg=color_club_selected)
button7c.grid(row=8,column=16,sticky = "NSEW")

#row=9

buttonA6o = tk.Button(mywindow,text='A6',command=pressA6o,bg=color_offsuit)
buttonA6o.grid(row=9,column=0,sticky = "NSEW")
buttonK6o = tk.Button(mywindow,text='K6',command=pressK6o,bg=color_offsuit)
buttonK6o.grid(row=9,column=1,sticky = "NSEW")
buttonQ6o = tk.Button(mywindow,text='Q6',command=pressQ6o,bg=color_offsuit)
buttonQ6o.grid(row=9,column=2,sticky = "NSEW")
buttonJ6o = tk.Button(mywindow,text='J6',command=pressJ6o,bg=color_offsuit) #,bg='red
buttonJ6o.grid(row=9,column=3,sticky = "NSEW")
buttonT6o = tk.Button(mywindow,text='T6',command=pressT6o,bg=color_offsuit) #,bg='red
buttonT6o.grid(row=9,column=4,sticky = "NSEW")
button96o = tk.Button(mywindow,text='96',command=press96o,bg=color_offsuit) #,bg='red
button96o.grid(row=9,column=5,sticky = "NSEW")
button86o = tk.Button(mywindow,text='86',command=press86o,bg=color_offsuit) #,bg='red
button86o.grid(row=9,column=6,sticky = "NSEW")
button76o = tk.Button(mywindow,text='76',command=press76o,bg=color_offsuit) #,bg='red
button76o.grid(row=9,column=7,sticky = "NSEW")
button66 = tk.Button(mywindow,text='66',command=press66,bg=color_pp) #,bg='red
button66.grid(row=9,column=8,sticky = "NSEW")
button65s = tk.Button(mywindow,text='65',command=press65s,bg=color_suited) #,bg='red
button65s.grid(row=9,column=9,sticky = "NSEW")
button64s = tk.Button(mywindow,text='64',command=press64s,bg=color_suited) #,bg='red
button64s.grid(row=9,column=10,sticky = "NSEW")
button63s = tk.Button(mywindow,text='63',command=press63s,bg=color_suited) #,bg='red
button63s.grid(row=9,column=11,sticky = "NSEW")
button62s = tk.Button(mywindow,text='62',command=press62s,bg=color_suited) #,bg='red
button62s.grid(row=9,column=12,padx=(0,15))

#board cards 6
button6s = tk.Button(mywindow,text='6' + suit_spade ,command=press6s,bg=color_spade, fg=color_spade_selected)
button6s.grid(row=9,column=13,sticky = "NSEW")

button6h = tk.Button(mywindow,text='6' + suit_heart,command=press6h,bg=color_heart, fg = color_heart_selected)
button6h.grid(row=9,column=14,sticky = "NSEW")

button6d = tk.Button(mywindow,text='6' + suit_diamond,command=press6d,bg=color_diamond, fg=color_diamond_selected)
button6d.grid(row=9,column=15,sticky = "NSEW")

button6c = tk.Button(mywindow,text='6' + suit_club,command=press6c,bg=color_club, fg=color_club_selected)
button6c.grid(row=9,column=16,sticky = "NSEW")

#row=10

buttonA5o = tk.Button(mywindow,text='A5',command=pressA5o,bg=color_offsuit)
buttonA5o.grid(row=10,column=0,sticky = "NSEW")
buttonK5o = tk.Button(mywindow,text='K5',command=pressK5o,bg=color_offsuit)
buttonK5o.grid(row=10,column=1,sticky = "NSEW")
buttonQ5o = tk.Button(mywindow,text='Q5',command=pressQ5o,bg=color_offsuit)
buttonQ5o.grid(row=10,column=2,sticky = "NSEW")
buttonJ5o = tk.Button(mywindow,text='J5',command=pressJ5o,bg=color_offsuit) #,bg='red
buttonJ5o.grid(row=10,column=3,sticky = "NSEW")
buttonT5o = tk.Button(mywindow,text='T5',command=pressT5o,bg=color_offsuit) #,bg='red
buttonT5o.grid(row=10,column=4,sticky = "NSEW")
button95o = tk.Button(mywindow,text='95',command=press95o,bg=color_offsuit) #,bg='red
button95o.grid(row=10,column=5,sticky = "NSEW")
button85o = tk.Button(mywindow,text='85',command=press85o,bg=color_offsuit) #,bg='red
button85o.grid(row=10,column=6,sticky = "NSEW")
button75o = tk.Button(mywindow,text='75',command=press75o,bg=color_offsuit) #,bg='red
button75o.grid(row=10,column=7,sticky = "NSEW")
button65o = tk.Button(mywindow,text='65',command=press65o,bg=color_offsuit) #,bg='red
button65o.grid(row=10,column=8,sticky = "NSEW")
button55 = tk.Button(mywindow,text='55',command=press55,bg=color_pp) #,bg='red
button55.grid(row=10,column=9,sticky = "NSEW")
button54s = tk.Button(mywindow,text='54',command=press54s,bg=color_suited) #,bg='red
button54s.grid(row=10,column=10,sticky = "NSEW")
button53s = tk.Button(mywindow,text='53',command=press53s,bg=color_suited) #,bg='red
button53s.grid(row=10,column=11,sticky = "NSEW")
button52s = tk.Button(mywindow,text='52',command=press52s,bg=color_suited) #,bg='red
button52s.grid(row=10,column=12,padx=(0,15))

#board cards 5
button5s = tk.Button(mywindow,text='5' + suit_spade ,command=press5s,bg=color_spade, fg=color_spade_selected)
button5s.grid(row=10,column=13,sticky = "NSEW")

button5h = tk.Button(mywindow,text='5' + suit_heart,command=press5h,bg=color_heart, fg = color_heart_selected)
button5h.grid(row=10,column=14,sticky = "NSEW")

button5d = tk.Button(mywindow,text='5' + suit_diamond,command=press5d,bg=color_diamond, fg=color_diamond_selected)
button5d.grid(row=10,column=15,sticky = "NSEW")

button5c = tk.Button(mywindow,text='5' + suit_club,command=press5c,bg=color_club, fg=color_club_selected)
button5c.grid(row=10,column=16,sticky = "NSEW")

#row=11

buttonA4o = tk.Button(mywindow,text='A4',command=pressA4o,bg=color_offsuit)
buttonA4o.grid(row=11,column=0,sticky = "NSEW")
buttonK4o = tk.Button(mywindow,text='K4',command=pressK4o,bg=color_offsuit)
buttonK4o.grid(row=11,column=1,sticky = "NSEW")
buttonQ4o = tk.Button(mywindow,text='Q4',command=pressQ4o,bg=color_offsuit)
buttonQ4o.grid(row=11,column=2,sticky = "NSEW")
buttonJ4o = tk.Button(mywindow,text='J4',command=pressJ4o,bg=color_offsuit) #,bg='red
buttonJ4o.grid(row=11,column=3,sticky = "NSEW")
buttonT4o = tk.Button(mywindow,text='T4',command=pressT4o,bg=color_offsuit) #,bg='red
buttonT4o.grid(row=11,column=4,sticky = "NSEW")
button94o = tk.Button(mywindow,text='94',command=press94o,bg=color_offsuit) #,bg='red
button94o.grid(row=11,column=5,sticky = "NSEW")
button84o = tk.Button(mywindow,text='84',command=press84o,bg=color_offsuit) #,bg='red
button84o.grid(row=11,column=6,sticky = "NSEW")
button74o = tk.Button(mywindow,text='74',command=press74o,bg=color_offsuit) #,bg='red
button74o.grid(row=11,column=7,sticky = "NSEW")
button64o = tk.Button(mywindow,text='64',command=press64o,bg=color_offsuit) #,bg='red
button64o.grid(row=11,column=8,sticky = "NSEW")
button54o = tk.Button(mywindow,text='54',command=press54o,bg=color_offsuit) #,bg='red
button54o.grid(row=11,column=9,sticky = "NSEW")
button44 = tk.Button(mywindow,text='44',command=press44,bg=color_pp) #,bg='red
button44.grid(row=11,column=10,sticky = "NSEW")
button43s = tk.Button(mywindow,text='43',command=press43s,bg=color_suited) #,bg='red
button43s.grid(row=11,column=11,sticky = "NSEW")
button42s = tk.Button(mywindow,text='42',command=press42s,bg=color_suited) #,bg='red
button42s.grid(row=11,column=12,padx=(0,15))

#board cards 4
button4s = tk.Button(mywindow,text='4' + suit_spade ,command=press4s,bg=color_spade, fg=color_spade_selected)
button4s.grid(row=11,column=13,sticky = "NSEW")

button4h = tk.Button(mywindow,text='4' + suit_heart,command=press4h,bg=color_heart, fg = color_heart_selected)
button4h.grid(row=11,column=14,sticky = "NSEW")

button4d = tk.Button(mywindow,text='4' + suit_diamond,command=press4d,bg=color_diamond, fg=color_diamond_selected)
button4d.grid(row=11,column=15,sticky = "NSEW")

button4c = tk.Button(mywindow,text='4' + suit_club,command=press4c,bg=color_club, fg=color_club_selected)
button4c.grid(row=11,column=16,sticky = "NSEW")

#row=12

buttonA3o = tk.Button(mywindow,text='A3',command=pressA3o,bg=color_offsuit)
buttonA3o.grid(row=12,column=0,sticky = "NSEW")
buttonK3o = tk.Button(mywindow,text='K3',command=pressK3o,bg=color_offsuit)
buttonK3o.grid(row=12,column=1,sticky = "NSEW")
buttonQ3o = tk.Button(mywindow,text='Q3',command=pressQ3o,bg=color_offsuit)
buttonQ3o.grid(row=12,column=2,sticky = "NSEW")
buttonJ3o = tk.Button(mywindow,text='J3',command=pressJ3o,bg=color_offsuit) #,bg='red
buttonJ3o.grid(row=12,column=3,sticky = "NSEW")
buttonT3o = tk.Button(mywindow,text='T3',command=pressT3o,bg=color_offsuit) #,bg='red
buttonT3o.grid(row=12,column=4,sticky = "NSEW")
button93o = tk.Button(mywindow,text='93',command=press93o,bg=color_offsuit) #,bg='red
button93o.grid(row=12,column=5,sticky = "NSEW")
button83o = tk.Button(mywindow,text='83',command=press83o,bg=color_offsuit) #,bg='red
button83o.grid(row=12,column=6,sticky = "NSEW")
button73o = tk.Button(mywindow,text='73',command=press73o,bg=color_offsuit) #,bg='red
button73o.grid(row=12,column=7,sticky = "NSEW")
button63o = tk.Button(mywindow,text='63',command=press63o,bg=color_offsuit) #,bg='red
button63o.grid(row=12,column=8,sticky = "NSEW")
button53o = tk.Button(mywindow,text='53',command=press53o,bg=color_offsuit) #,bg='red
button53o.grid(row=12,column=9,sticky = "NSEW")
button43o = tk.Button(mywindow,text='43',command=press43o,bg=color_offsuit) #,bg='red
button43o.grid(row=12,column=10,sticky = "NSEW")
button33 = tk.Button(mywindow,text='33',command=press33,bg=color_pp) #,bg='red
button33.grid(row=12,column=11,sticky = "NSEW")
button32s = tk.Button(mywindow,text='32',command=press32s,bg=color_suited) #,bg='red
button32s.grid(row=12,column=12,padx=(0,15))

#board cards 3
button3s = tk.Button(mywindow,text='3' + suit_spade ,command=press3s,bg=color_spade, fg=color_spade_selected)
button3s.grid(row=12,column=13,sticky = "NSEW")

button3h = tk.Button(mywindow,text='3' + suit_heart,command=press3h,bg=color_heart, fg = color_heart_selected)
button3h.grid(row=12,column=14,sticky = "NSEW")

button3d = tk.Button(mywindow,text='3' + suit_diamond,command=press3d,bg=color_diamond, fg=color_diamond_selected)
button3d.grid(row=12,column=15,sticky = "NSEW")

button3c = tk.Button(mywindow,text='3' + suit_club,command=press3c,bg=color_club, fg=color_club_selected)
button3c.grid(row=12,column=16,sticky = "NSEW")

#row=13

buttonA2o = tk.Button(mywindow,text='A2',command=pressA2o,bg=color_offsuit)
buttonA2o.grid(row=13,column=0,sticky = "NSEW")
buttonK2o = tk.Button(mywindow,text='K2',command=pressK2o,bg=color_offsuit)
buttonK2o.grid(row=13,column=1,sticky = "NSEW")
buttonQ2o = tk.Button(mywindow,text='Q2',command=pressQ2o,bg=color_offsuit)
buttonQ2o.grid(row=13,column=2,sticky = "NSEW")
buttonJ2o = tk.Button(mywindow,text='J2',command=pressJ2o,bg=color_offsuit) #,bg='red
buttonJ2o.grid(row=13,column=3,sticky = "NSEW")
buttonT2o = tk.Button(mywindow,text='T2',command=pressT2o,bg=color_offsuit) #,bg='red
buttonT2o.grid(row=13,column=4,sticky = "NSEW")
button92o = tk.Button(mywindow,text='92',command=press92o,bg=color_offsuit) #,bg='red
button92o.grid(row=13,column=5,sticky = "NSEW")
button82o = tk.Button(mywindow,text='82',command=press82o,bg=color_offsuit) #,bg='red
button82o.grid(row=13,column=6,sticky = "NSEW")
button72o = tk.Button(mywindow,text='72',command=press72o,bg=color_offsuit) #,bg='red
button72o.grid(row=13,column=7,sticky = "NSEW")
button62o = tk.Button(mywindow,text='62',command=press62o,bg=color_offsuit) #,bg='red
button62o.grid(row=13,column=8,sticky = "NSEW")
button52o = tk.Button(mywindow,text='52',command=press52o,bg=color_offsuit) #,bg='red
button52o.grid(row=13,column=9,sticky = "NSEW")
button42o = tk.Button(mywindow,text='42',command=press42o,bg=color_offsuit) #,bg='red
button42o.grid(row=13,column=10,sticky = "NSEW")
button32o = tk.Button(mywindow,text='32',command=press32o,bg=color_offsuit) #,bg='red
button32o.grid(row=13,column=11,sticky = "NSEW")
button22 = tk.Button(mywindow,text='22',command=press22,bg=color_pp) #,bg='red
button22.grid(row=13,column=12,padx=(0,15))

#board cards 2
button2s = tk.Button(mywindow,text='2' + suit_spade ,command=press2s,bg=color_spade, fg=color_spade_selected)
button2s.grid(row=13,column=13,sticky = "NSEW")

button2h = tk.Button(mywindow,text='2' + suit_heart,command=press2h,bg=color_heart, fg = color_heart_selected)
button2h.grid(row=13,column=14,sticky = "NSEW")

button2d = tk.Button(mywindow,text='2' + suit_diamond,command=press2d,bg=color_diamond, fg=color_diamond_selected)
button2d.grid(row=13,column=15,sticky = "NSEW")

button2c = tk.Button(mywindow,text='2' + suit_club,command=press2c,bg=color_club, fg=color_club_selected)
button2c.grid(row=13,column=16,sticky = "NSEW")

#Button
buttonExpand = tk.Button(mywindow,text='=',command=buttonPress)
buttonExpand.grid(row=15,column=15)

'''
#Textbox
textb = tk.Entry(mywindow,text="Entry")
textbutton = tk.Button(mywindow,text="Text Box",command=textBox)
textb.grid(row=3,column=0, sticky = tk.W+tk.E, columnspan=4)
textbutton.grid(row=3,column=2)
'''

#Slider
Slider = (tk.Scale(mywindow,variable=0,orient="horizontal", length=200))
SliderButton = (tk.Button(mywindow,text='Set',command=slideValueSet))
Slider.grid(row=15,column=0, columnspan=12)
SliderButton.grid(row=15,column=13)


mywindow.mainloop()