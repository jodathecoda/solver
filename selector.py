import tkinter as tk

import expander
import slider_control

mywindow = tk.Tk()
mywindow.geometry("500x400")

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

def setRange(per):
    print("setRange: " + str(per))
    press22(1)


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

def pressAA(par):
    # par = 0 clear
    # par = 1 set
    # par = 2 toggle
    if par == 0:
        if 'AA' in selected_range:
            selected_range.remove('AA')
            buttonAA.config(bg = color_pp)
    elif par == 1:
        if 'AA' not in selected_range:
            selected_range.append('AA')
            buttonAA.config(bg = color_pp_selected)
    else: 
        # par = 2 toggle
        if 'AA' in selected_range:
            selected_range.remove('AA')
            buttonAA.config(bg = color_pp)
        else:
            selected_range.append('AA')
            buttonAA.config(bg = color_pp_selected)
            #open_secondary_window()

def pressKK(par):
    if par == 0:
        if 'KK' in selected_range:
            selected_range.remove('KK')
            buttonKK.config(bg = color_pp)
    elif par == 1:
        if 'KK' not in selected_range:
            selected_range.append('KK')
            buttonKK.config(bg = color_pp_selected)
    else: 
        # par = 2 toggle
        if 'KK' in selected_range:
            selected_range.remove('KK')
            buttonKK.config(bg = color_pp)
        else:
            selected_range.append('KK')
            buttonKK.config(bg = color_pp_selected)

def pressQQ(par):
    if par == 0:
        if 'QQ' in selected_range:
            selected_range.remove('QQ')
            buttonQQ.config(bg = color_pp)
    elif par == 1:
        if 'QQ' not in selected_range:
            selected_range.append('QQ')
            buttonQQ.config(bg = color_pp_selected)
    else: 
        # par = 2 toggle
        if 'QQ' in selected_range:
            selected_range.remove('QQ')
            buttonQQ.config(bg = color_pp)
        else:
            selected_range.append('QQ')
            buttonQQ.config(bg = color_pp_selected)

def pressJJ(par):
    if par == 0:
        if 'JJ' in selected_range:
            selected_range.remove('JJ')
            buttonJJ.config(bg = color_pp)
    elif par == 1:
        if 'JJ' not in selected_range:
            selected_range.append('JJ')
            buttonJJ.config(bg = color_pp_selected)
    else: 
        # par = 2 toggle
        if 'JJ' in selected_range:
            selected_range.remove('JJ')
            buttonJJ.config(bg = color_pp)
        else:
            selected_range.append('JJ')
            buttonJJ.config(bg = color_pp_selected)

def pressTT(par):
    if par == 0:
        if 'TT' in selected_range:
            selected_range.remove('TT')
            buttonTT.config(bg = color_pp)
    elif par == 1:
        if 'TT' not in selected_range:
            selected_range.append('TT')
            buttonTT.config(bg = color_pp_selected)
    else: 
        # par = 2 toggle
        if 'TT' in selected_range:
            selected_range.remove('TT')
            buttonTT.config(bg = color_pp)
        else:
            selected_range.append('TT')
            buttonTT.config(bg = color_pp_selected)

def press99(par):
    if par == 0:
        if '99' in selected_range:
            selected_range.remove('99')
            button99.config(bg = color_pp)
    elif par == 1:
        if '99' not in selected_range:
            selected_range.append('99')
            button99.config(bg = color_pp_selected)
    else: #toggle
        if '99' in selected_range:
            selected_range.remove('99')
            button99.config(bg = color_pp)
        else:
            selected_range.append('99')
            button99.config(bg = color_pp_selected)

def press88(par):
    if par == 0:
        if '88' in selected_range:
            selected_range.remove('88')
            button88.config(bg = color_pp)
    elif par == 1:
        if '88' not in selected_range:
            selected_range.append('88')
            button88.config(bg = color_pp_selected)
    else: #toggle
        if '88' in selected_range:
            selected_range.remove('88')
            button88.config(bg = color_pp)
        else:
            selected_range.append('88')
            button88.config(bg = color_pp_selected)

def press77(par):
    if par == 0:
        if '77' in selected_range:
            selected_range.remove('77')
            button77.config(bg = color_pp)
    elif par == 1:
        if '77' not in selected_range:
            selected_range.append('77')
            button77.config(bg = color_pp_selected)
    else: #toggle
        if '77' in selected_range:
            selected_range.remove('77')
            button77.config(bg = color_pp)
        else:
            selected_range.append('77')
            button77.config(bg = color_pp_selected)

def press66(par):
    if par == 0:
        if '66' in selected_range:
            selected_range.remove('66')
            button66.config(bg = color_pp)
    elif par == 1:
        if '66' not in selected_range:
            selected_range.append('66')
            button66.config(bg = color_pp_selected)
    else: #toggle
        if '66' in selected_range:
            selected_range.remove('66')
            button66.config(bg = color_pp)
        else:
            selected_range.append('66')
            button66.config(bg = color_pp_selected)

def press55(par):
    if par == 0:
        if '55' in selected_range:
            selected_range.remove('55')
            button55.config(bg = color_pp)
    elif par == 1:
        if '55' not in selected_range:
            selected_range.append('55')
            button55.config(bg = color_pp_selected)
    else: #toggle
        if '55' in selected_range:
            selected_range.remove('55')
            button55.config(bg = color_pp)
        else:
            selected_range.append('55')
            button55.config(bg = color_pp_selected)

def press44(par):
    if par == 0:
        if '44' in selected_range:
            selected_range.remove('44')
            button44.config(bg = color_pp)
    elif par == 1:
        if '44' not in selected_range:
            selected_range.append('44')
            button44.config(bg = color_pp_selected)
    else: #toggle
        if '44' in selected_range:
            selected_range.remove('44')
            button44.config(bg = color_pp)
        else:
            selected_range.append('44')
            button44.config(bg = color_pp_selected)

def press33(par):
    if par == 0:
        if '33' in selected_range:
            selected_range.remove('33')
            button33.config(bg = color_pp)
    elif par == 1:
        if '33' not in selected_range:
            selected_range.append('33')
            button33.config(bg = color_pp_selected)
    else: #toggle
        if '33' in selected_range:
            selected_range.remove('33')
            button33.config(bg = color_pp)
        else:
            selected_range.append('33')
            button33.config(bg = color_pp_selected)

def press22(par):
    if par == 0:
        if '22' in selected_range:
            selected_range.remove('22')
            button22.config(bg = color_pp)
    elif par == 1:
        if '22' not in selected_range:
            selected_range.append('22')
            button22.config(bg = color_pp_selected)
    else: #toggle
        if '22' in selected_range:
            selected_range.remove('22')
            button22.config(bg = color_pp)
        else:
            selected_range.append('22')
            button22.config(bg = color_pp_selected)

#suited handlers A
def pressAKs(par):
    if par == 0:
        if 'AKs' in selected_range:
            buttonAKs.config(bg = color_suited)
            selected_range.remove('AKs')
    elif par == 1:
        if 'AKs' not in selected_range:
            buttonAKs.config(bg = color_suited_selected)
            selected_range.append('AKs')
    else: #toggle
        if 'AKs' in selected_range:
            buttonAKs.config(bg = color_suited)
            selected_range.remove('AKs')
        else:
            buttonAKs.config(bg = color_suited_selected)
            selected_range.append('AKs')       

def pressAQs(par):
    if par == 0:
        if 'AQs' in selected_range:
            buttonAQs.config(bg = color_suited)
            selected_range.remove('AQs')
    elif par == 1:
        if 'AQs' not in selected_range:
            buttonAQs.config(bg = color_suited_selected)
            selected_range.append('AQs')
    else: #toggle
        if 'AQs' in selected_range:
            buttonAQs.config(bg = color_suited)
            selected_range.remove('AQs')
        else:
            buttonAQs.config(bg = color_suited_selected)
            selected_range.append('AQs')

def pressAJs(par):
    if par == 0:
        if 'AJs' in selected_range:
            buttonAJs.config(bg = color_suited)
            selected_range.remove('AJs')
    elif par == 1:
        if 'AJs' not in selected_range:
            buttonAJs.config(bg = color_suited_selected)
            selected_range.append('AJs')
    else: #toggle
        if 'AJs' in selected_range:
            buttonAJs.config(bg = color_suited)
            selected_range.remove('AJs')
        else:
            buttonAJs.config(bg = color_suited_selected)
            selected_range.append('AJs')

def pressATs(par):
    if par == 0:
        if 'ATs' in selected_range:
            buttonATs.config(bg = color_suited)
            selected_range.remove('ATs')
    elif par == 1:
        if 'ATs' not in selected_range:
            buttonATs.config(bg = color_suited_selected)
            selected_range.append('ATs')
    else: #toggle
        if 'ATs' in selected_range:
            buttonATs.config(bg = color_suited)
            selected_range.remove('ATs')
        else:
            buttonATs.config(bg = color_suited_selected)
            selected_range.append('ATs')

def pressA9s(par):
    if par == 0:
        if 'A9s' in selected_range:
            buttonA9s.config(bg = color_suited)
            selected_range.remove('A9s')
    elif par == 1:
        if 'A9s' not in selected_range:
            buttonA9s.config(bg = color_suited_selected)
            selected_range.append('A9s')
    else: #toggle
        if 'A9s' in selected_range:
            buttonA9s.config(bg = color_suited)
            selected_range.remove('A9s')
        else:
            buttonA9s.config(bg = color_suited_selected)
            selected_range.append('A9s')

def pressA8s(par):
    if par == 0:
        if 'A8s' in selected_range:
            buttonA8s.config(bg = color_suited)
            selected_range.remove('A8s')
    elif par == 1:
        if 'A8s' not in selected_range:
            buttonA8s.config(bg = color_suited_selected)
            selected_range.append('A8s')
    else: #toggle
        if 'A8s' in selected_range:
            buttonA8s.config(bg = color_suited)
            selected_range.remove('A8s')
        else:
            buttonA8s.config(bg = color_suited_selected)
            selected_range.append('A8s')

def pressA7s(par):
    if par == 0:
        if 'A7s' in selected_range:
            buttonA7s.config(bg = color_suited)
            selected_range.remove('A7s')
    elif par == 1:
        if 'A7s' not in selected_range:
            buttonA7s.config(bg = color_suited_selected)
            selected_range.append('A7s')
    else: #toggle
        if 'A7s' in selected_range:
            buttonA7s.config(bg = color_suited)
            selected_range.remove('A7s')
        else:
            buttonA7s.config(bg = color_suited_selected)
            selected_range.append('A7s')

def pressA6s(par):
    if par == 0:
        if 'A6s' in selected_range:
            buttonA6s.config(bg = color_suited)
            selected_range.remove('A6s')
    elif par == 1:
        if 'A6s' not in selected_range:
            buttonA6s.config(bg = color_suited_selected)
            selected_range.append('A6s')
    else: #toggle
        if 'A6s' in selected_range:
            buttonA6s.config(bg = color_suited)
            selected_range.remove('A6s')
        else:
            buttonA6s.config(bg = color_suited_selected)
            selected_range.append('A6s')

def pressA5s(par):
    if par == 0:
        if 'A5s' in selected_range:
            buttonA5s.config(bg = color_suited)
            selected_range.remove('A5s')
    elif par == 1:
        if 'A5s' not in selected_range:
            buttonA5s.config(bg = color_suited_selected)
            selected_range.append('A5s')
    else: #toggle
        if 'A5s' in selected_range:
            buttonA5s.config(bg = color_suited)
            selected_range.remove('A5s')
        else:
            buttonA5s.config(bg = color_suited_selected)
            selected_range.append('A5s')

def pressA4s(par):
    if par == 0:
        if 'A4s' in selected_range:
            buttonA4s.config(bg = color_suited)
            selected_range.remove('A4s')
    elif par == 1:
        if 'A4s' not in selected_range:
            buttonA4s.config(bg = color_suited_selected)
            selected_range.append('A4s')
    else: #toggle
        if 'A4s' in selected_range:
            buttonA4s.config(bg = color_suited)
            selected_range.remove('A4s')
        else:
            buttonA4s.config(bg = color_suited_selected)
            selected_range.append('A4s')

def pressA3s(par):
    if par == 0:
        if 'A3s' in selected_range:
            buttonA3s.config(bg = color_suited)
            selected_range.remove('A3s')
    elif par == 1:
        if 'A3s' not in selected_range:
            buttonA3s.config(bg = color_suited_selected)
            selected_range.append('A3s')
    else: #toggle
        if 'A3s' in selected_range:
            buttonA3s.config(bg = color_suited)
            selected_range.remove('A3s')
        else:
            buttonA3s.config(bg = color_suited_selected)
            selected_range.append('A3s')

def pressA2s(par):
    if par == 0:
        if 'A2s' in selected_range:
            buttonA2s.config(bg = color_suited)
            selected_range.remove('A2s')
    elif par == 1:
        if 'A2s' not in selected_range:
            buttonA2s.config(bg = color_suited_selected)
            selected_range.append('A2s')
    else: #toggle
        if 'A2s' in selected_range:
            buttonA2s.config(bg = color_suited)
            selected_range.remove('A2s')
        else:
            buttonA2s.config(bg = color_suited_selected)
            selected_range.append('A2s')

#suited handlers K
    
def pressKQs(par):
    if par == 0:
        if 'KQs' in selected_range:
            buttonKQs.config(bg = color_suited)
            selected_range.remove('KQs')
    elif par == 1:
        if 'KQs' not in selected_range:
            buttonKQs.config(bg = color_suited_selected)
            selected_range.append('KQs')
    else: #toggle
        if 'KQs' in selected_range:
            buttonKQs.config(bg = color_suited)
            selected_range.remove('KQs')
        else:
            buttonKQs.config(bg = color_suited_selected)
            selected_range.append('KQs')

def pressKJs(par):
    if par == 0:
        if 'KJs' in selected_range:
            buttonKJs.config(bg = color_suited)
            selected_range.remove('KJs')
    elif par == 1:
        if 'KJs' not in selected_range:
            buttonKJs.config(bg = color_suited_selected)
            selected_range.append('KJs')
    else: #toggle
        if 'KJs' in selected_range:
            buttonKJs.config(bg = color_suited)
            selected_range.remove('KJs')
        else:
            buttonKJs.config(bg = color_suited_selected)
            selected_range.append('KJs')

def pressKTs(par):
    if par == 0:
        if 'KTs' in selected_range:
            buttonKTs.config(bg = color_suited)
            selected_range.remove('KTs')
    elif par == 1:
        if 'KTs' not in selected_range:
            buttonKTs.config(bg = color_suited_selected)
            selected_range.append('KTs')
    else: #toggle
        if 'KTs' in selected_range:
            buttonKTs.config(bg = color_suited)
            selected_range.remove('KTs')
        else:
            buttonKTs.config(bg = color_suited_selected)
            selected_range.append('KTs')

def pressK9s(par):
    if par == 0:
        if 'K9s' in selected_range:
            buttonK9s.config(bg = color_suited)
            selected_range.remove('K9s')
    elif par == 1:
        if 'K9s' not in selected_range:
            buttonK9s.config(bg = color_suited_selected)
            selected_range.append('K9s')
    else: #toggle
        if 'K9s' in selected_range:
            buttonK9s.config(bg = color_suited)
            selected_range.remove('K9s')
        else:
            buttonK9s.config(bg = color_suited_selected)
            selected_range.append('K9s')

def pressK8s(par):
    if par == 0:
        if 'K8s' in selected_range:
            buttonK8s.config(bg = color_suited)
            selected_range.remove('K8s')
    elif par == 1:
        if 'K8s' not in selected_range:
            buttonK8s.config(bg = color_suited_selected)
            selected_range.append('K8s')
    else: #toggle
        if 'K8s' in selected_range:
            buttonK8s.config(bg = color_suited)
            selected_range.remove('K8s')
        else:
            buttonK8s.config(bg = color_suited_selected)
            selected_range.append('K8s')

def pressK7s(par):
    if par == 0:
        if 'K7s' in selected_range:
            buttonK7s.config(bg = color_suited)
            selected_range.remove('K7s')
    elif par == 1:
        if 'K7s' not in selected_range:
            buttonK7s.config(bg = color_suited_selected)
            selected_range.append('K7s')
    else: #toggle
        if 'K7s' in selected_range:
            buttonK7s.config(bg = color_suited)
            selected_range.remove('K7s')
        else:
            buttonK7s.config(bg = color_suited_selected)
            selected_range.append('K7s')

def pressK6s(par):
    if par == 0:
        if 'K6s' in selected_range:
            buttonK6s.config(bg = color_suited)
            selected_range.remove('K6s')
    elif par == 1:
        if 'K6s' not in selected_range:
            buttonK6s.config(bg = color_suited_selected)
            selected_range.append('K6s')
    else: #toggle
        if 'K6s' in selected_range:
            buttonK6s.config(bg = color_suited)
            selected_range.remove('K6s')
        else:
            buttonK6s.config(bg = color_suited_selected)
            selected_range.append('K6s')

def pressK5s(par):
    if par == 0:
        if 'K5s' in selected_range:
            buttonK5s.config(bg = color_suited)
            selected_range.remove('K5s')
    elif par == 1:
        if 'K5s' not in selected_range:
            buttonK5s.config(bg = color_suited_selected)
            selected_range.append('K5s')
    else: #toggle
        if 'K5s' in selected_range:
            buttonK5s.config(bg = color_suited)
            selected_range.remove('K5s')
        else:
            buttonK5s.config(bg = color_suited_selected)
            selected_range.append('K5s')

def pressK4s(par):
    if par == 0:
        if 'K4s' in selected_range:
            buttonK4s.config(bg = color_suited)
            selected_range.remove('K4s')
    elif par == 1:
        if 'K4s' not in selected_range:
            buttonK4s.config(bg = color_suited_selected)
            selected_range.append('K4s')
    else: #toggle
        if 'K4s' in selected_range:
            buttonK4s.config(bg = color_suited)
            selected_range.remove('K4s')
        else:
            buttonK4s.config(bg = color_suited_selected)
            selected_range.append('K4s')

def pressK3s(par):
    if par == 0:
        if 'K3s' in selected_range:
            buttonK3s.config(bg = color_suited)
            selected_range.remove('K3s')
    elif par == 1:
        if 'K3s' not in selected_range:
            buttonK3s.config(bg = color_suited_selected)
            selected_range.append('K3s')
    else: #toggle
        if 'K3s' in selected_range:
            buttonK3s.config(bg = color_suited)
            selected_range.remove('K3s')
        else:
            buttonK3s.config(bg = color_suited_selected)
            selected_range.append('K3s')

def pressK2s(par):
    if par == 0:
        if 'K2s' in selected_range:
            buttonK2s.config(bg = color_suited)
            selected_range.remove('K2s')
    elif par == 1:
        if 'K2s' not in selected_range:
            buttonK2s.config(bg = color_suited_selected)
            selected_range.append('K2s')
    else: #toggle
        if 'K2s' in selected_range:
            buttonK2s.config(bg = color_suited)
            selected_range.remove('K2s')
        else:
            buttonK2s.config(bg = color_suited_selected)
            selected_range.append('K2s')

#suited handlers Q

def pressQJs(par):
    if par == 0:
        if 'QJs' in selected_range:
            buttonQJs.config(bg = color_suited)
            selected_range.remove('QJs')
    elif par == 1:
        if 'QJs' not in selected_range:
            buttonQJs.config(bg = color_suited_selected)
            selected_range.append('QJs')
    else: #toggle
        if 'QJs' in selected_range:
            buttonQJs.config(bg = color_suited)
            selected_range.remove('QJs')
        else:
            buttonQJs.config(bg = color_suited_selected)
            selected_range.append('QJs')

def pressQTs(par):
    if par == 0:
        if 'QTs' in selected_range:
            buttonQTs.config(bg = color_suited)
            selected_range.remove('QTs')
    elif par == 1:
        if 'QTs' not in selected_range:
            buttonQTs.config(bg = color_suited_selected)
            selected_range.append('QTs')
    else: #toggle
        if 'QTs' in selected_range:
            buttonQTs.config(bg = color_suited)
            selected_range.remove('QTs')
        else:
            buttonQTs.config(bg = color_suited_selected)
            selected_range.append('QTs')

def pressQ9s(par):
    if par == 0:
        if 'Q9s' in selected_range:
            buttonQ9s.config(bg = color_suited)
            selected_range.remove('Q9s')
    elif par == 1:
        if 'Q9s' not in selected_range:
            buttonQ9s.config(bg = color_suited_selected)
            selected_range.append('Q9s')
    else: #toggle
        if 'Q9s' in selected_range:
            buttonQ9s.config(bg = color_suited)
            selected_range.remove('Q9s')
        else:
            buttonQ9s.config(bg = color_suited_selected)
            selected_range.append('Q9s')

def pressQ8s(par):
    if par == 0:
        if 'Q8s' in selected_range:
            buttonQ8s.config(bg = color_suited)
            selected_range.remove('Q8s')
    elif par == 1:
        if 'Q8s' not in selected_range:
            buttonQ8s.config(bg = color_suited_selected)
            selected_range.append('Q8s')
    else: #toggle
        if 'Q8s' in selected_range:
            buttonQ8s.config(bg = color_suited)
            selected_range.remove('Q8s')
        else:
            buttonQ8s.config(bg = color_suited_selected)
            selected_range.append('Q8s')

def pressQ7s(par):
    if par == 0:
        if 'Q7s' in selected_range:
            buttonQ7s.config(bg = color_suited)
            selected_range.remove('Q7s')
    elif par == 1:
        if 'Q7s' not in selected_range:
            buttonQ7s.config(bg = color_suited_selected)
            selected_range.append('Q7s')
    else: #toggle
        if 'Q7s' in selected_range:
            buttonQ7s.config(bg = color_suited)
            selected_range.remove('Q7s')
        else:
            buttonQ7s.config(bg = color_suited_selected)
            selected_range.append('Q7s')

def pressQ6s(par):
    if par == 0:
        if 'Q6s' in selected_range:
            buttonQ6s.config(bg = color_suited)
            selected_range.remove('Q6s')
    elif par == 1:
        if 'Q6s' not in selected_range:
            buttonQ6s.config(bg = color_suited_selected)
            selected_range.append('Q6s')
    else: #toggle
        if 'Q6s' in selected_range:
            buttonQ6s.config(bg = color_suited)
            selected_range.remove('Q6s')
        else:
            buttonQ6s.config(bg = color_suited_selected)
            selected_range.append('Q6s')

def pressQ5s(par):
    if par == 0:
        if 'Q5s' in selected_range:
            buttonQ5s.config(bg = color_suited)
            selected_range.remove('Q5s')
    elif par == 1:
        if 'Q5s' not in selected_range:
            buttonQ5s.config(bg = color_suited_selected)
            selected_range.append('Q5s')
    else: #toggle
        if 'Q5s' in selected_range:
            buttonQ5s.config(bg = color_suited)
            selected_range.remove('Q5s')
        else:
            buttonQ5s.config(bg = color_suited_selected)
            selected_range.append('Q5s')

def pressQ4s(par):
    if par == 0:
        if 'Q4s' in selected_range:
            buttonQ4s.config(bg = color_suited)
            selected_range.remove('Q4s')
    elif par == 1:
        if 'Q4s' not in selected_range:
            buttonQ4s.config(bg = color_suited_selected)
            selected_range.append('Q4s')
    else: #toggle
        if 'Q4s' in selected_range:
            buttonQ4s.config(bg = color_suited)
            selected_range.remove('Q4s')
        else:
            buttonQ4s.config(bg = color_suited_selected)
            selected_range.append('Q4s')

def pressQ3s(par):
    if par == 0:
        if 'Q3s' in selected_range:
            buttonQ3s.config(bg = color_suited)
            selected_range.remove('Q3s')
    elif par == 1:
        if 'Q3s' not in selected_range:
            buttonQ3s.config(bg = color_suited_selected)
            selected_range.append('Q3s')
    else: #toggle
        if 'Q3s' in selected_range:
            buttonQ3s.config(bg = color_suited)
            selected_range.remove('Q3s')
        else:
            buttonQ3s.config(bg = color_suited_selected)
            selected_range.append('Q3s')

def pressQ2s(par):
    if par == 0:
        if 'Q2s' in selected_range:
            buttonQ2s.config(bg = color_suited)
            selected_range.remove('Q2s')
    elif par == 1:
        if 'Q2s' not in selected_range:
            buttonQ2s.config(bg = color_suited_selected)
            selected_range.append('Q2s')
    else: #toggle
        if 'Q2s' in selected_range:
            buttonQ2s.config(bg = color_suited)
            selected_range.remove('Q2s')
        else:
            buttonQ2s.config(bg = color_suited_selected)
            selected_range.append('Q2s')

#suited handlers J

def pressJTs(par):
    if par == 0:
        if 'JTs' in selected_range:
            buttonJTs.config(bg = color_suited)
            selected_range.remove('JTs')
    elif par == 1:
        if 'JTs' not in selected_range:
            buttonJTs.config(bg = color_suited_selected)
            selected_range.append('JTs')
    else: #toggle
        if 'JTs' in selected_range:
            buttonJTs.config(bg = color_suited)
            selected_range.remove('JTs')
        else:
            buttonJTs.config(bg = color_suited_selected)
            selected_range.append('JTs')

def pressJ9s(par):
    if par == 0:
        if 'J9s' in selected_range:
            buttonJ9s.config(bg = color_suited)
            selected_range.remove('J9s')
    elif par == 1:
        if 'J9s' not in selected_range:
            buttonJ9s.config(bg = color_suited_selected)
            selected_range.append('J9s')
    else: #toggle
        if 'J9s' in selected_range:
            buttonJ9s.config(bg = color_suited)
            selected_range.remove('J9s')
        else:
            buttonJ9s.config(bg = color_suited_selected)
            selected_range.append('J9s')

def pressJ8s(par):
    if par == 0:
        if 'J8s' in selected_range:
            buttonJ8s.config(bg = color_suited)
            selected_range.remove('J8s')
    elif par == 1:
        if 'J8s' not in selected_range:
            buttonJ8s.config(bg = color_suited_selected)
            selected_range.append('J8s')
    else: #toggle
        if 'J8s' in selected_range:
            buttonJ8s.config(bg = color_suited)
            selected_range.remove('J8s')
        else:
            buttonJ8s.config(bg = color_suited_selected)
            selected_range.append('J8s')

def pressJ7s(par):
    if par == 0:
        if 'J7s' in selected_range:
            buttonJ7s.config(bg = color_suited)
            selected_range.remove('J7s')
    elif par == 1:
        if 'J7s' not in selected_range:
            buttonJ7s.config(bg = color_suited_selected)
            selected_range.append('J7s')
    else: #toggle
        if 'J7s' in selected_range:
            buttonJ7s.config(bg = color_suited)
            selected_range.remove('J7s')
        else:
            buttonJ7s.config(bg = color_suited_selected)
            selected_range.append('J7s')

def pressJ6s(par):
    if par == 0:
        if 'J6s' in selected_range:
            buttonJ6s.config(bg = color_suited)
            selected_range.remove('J6s')
    elif par == 1:
        if 'J6s' not in selected_range:
            buttonJ6s.config(bg = color_suited_selected)
            selected_range.append('J6s')
    else: #toggle
        if 'J6s' in selected_range:
            buttonJ6s.config(bg = color_suited)
            selected_range.remove('J6s')
        else:
            buttonJ6s.config(bg = color_suited_selected)
            selected_range.append('J6s')

def pressJ5s(par):
    if par == 0:
        if 'J5s' in selected_range:
            buttonJ5s.config(bg = color_suited)
            selected_range.remove('J5s')
    elif par == 1:
        if 'J5s' not in selected_range:
            buttonJ5s.config(bg = color_suited_selected)
            selected_range.append('J5s')
    else: #toggle
        if 'J5s' in selected_range:
            buttonJ5s.config(bg = color_suited)
            selected_range.remove('J5s')
        else:
            buttonJ5s.config(bg = color_suited_selected)
            selected_range.append('J5s')

def pressJ4s(par):
    if par == 0:
        if 'J4s' in selected_range:
            buttonJ4s.config(bg = color_suited)
            selected_range.remove('J4s')
    elif par == 1:
        if 'J4s' not in selected_range:
            buttonJ4s.config(bg = color_suited_selected)
            selected_range.append('J4s')
    else: #toggle
        if 'J4s' in selected_range:
            buttonJ4s.config(bg = color_suited)
            selected_range.remove('J4s')
        else:
            buttonJ4s.config(bg = color_suited_selected)
            selected_range.append('J4s')

def pressJ3s(par):
    if par == 0:
        if 'J3s' in selected_range:
            buttonJ3s.config(bg = color_suited)
            selected_range.remove('J3s')
    elif par == 1:
        if 'J3s' not in selected_range:
            buttonJ3s.config(bg = color_suited_selected)
            selected_range.append('J3s')
    else: #toggle
        if 'J3s' in selected_range:
            buttonJ3s.config(bg = color_suited)
            selected_range.remove('J3s')
        else:
            buttonJ3s.config(bg = color_suited_selected)
            selected_range.append('J3s')

def pressJ2s(par):
    if par == 0:
        if 'J2s' in selected_range:
            buttonJ2s.config(bg = color_suited)
            selected_range.remove('J2s')
    elif par == 1:
        if 'J2s' not in selected_range:
            buttonJ2s.config(bg = color_suited_selected)
            selected_range.append('J2s')
    else: #toggle
        if 'J2s' in selected_range:
            buttonJ2s.config(bg = color_suited)
            selected_range.remove('J2s')
        else:
            buttonJ2s.config(bg = color_suited_selected)
            selected_range.append('J2s')

#suited handlers T

def pressT9s(par):
    if par == 0:
        if 'T9s' in selected_range:
            buttonT9s.config(bg = color_suited)
            selected_range.remove('T9s')
    elif par == 1:
        if 'T9s' not in selected_range:
            buttonT9s.config(bg = color_suited_selected)
            selected_range.append('T9s')
    else: #toggle
        if 'T9s' in selected_range:
            buttonT9s.config(bg = color_suited)
            selected_range.remove('T9s')
        else:
            buttonT9s.config(bg = color_suited_selected)
            selected_range.append('T9s')

def pressT8s(par):
    if par == 0:
        if 'T8s' in selected_range:
            buttonT8s.config(bg = color_suited)
            selected_range.remove('T8s')
    elif par == 1:
        if 'T8s' not in selected_range:
            buttonT8s.config(bg = color_suited_selected)
            selected_range.append('T8s')
    else: #toggle
        if 'T8s' in selected_range:
            buttonT8s.config(bg = color_suited)
            selected_range.remove('T8s')
        else:
            buttonT8s.config(bg = color_suited_selected)
            selected_range.append('T8s')

def pressT7s(par):
    if par == 0:
        if 'T7s' in selected_range:
            buttonT7s.config(bg = color_suited)
            selected_range.remove('T7s')
    elif par == 1:
        if 'T7s' not in selected_range:
            buttonT7s.config(bg = color_suited_selected)
            selected_range.append('T7s')
    else: #toggle
        if 'T7s' in selected_range:
            buttonT7s.config(bg = color_suited)
            selected_range.remove('T7s')
        else:
            buttonT7s.config(bg = color_suited_selected)
            selected_range.append('T7s')

def pressT6s(par):
    if par == 0:
        if 'T6s' in selected_range:
            buttonT6s.config(bg = color_suited)
            selected_range.remove('T6s')
    elif par == 1:
        if 'T6s' not in selected_range:
            buttonT6s.config(bg = color_suited_selected)
            selected_range.append('T6s')
    else: #toggle
        if 'T6s' in selected_range:
            buttonT6s.config(bg = color_suited)
            selected_range.remove('T6s')
        else:
            buttonT6s.config(bg = color_suited_selected)
            selected_range.append('T6s')

def pressT5s(par):
    if par == 0:
        if 'T5s' in selected_range:
            buttonT5s.config(bg = color_suited)
            selected_range.remove('T5s')
    elif par == 1:
        if 'T5s' not in selected_range:
            buttonT5s.config(bg = color_suited_selected)
            selected_range.append('T5s')
    else: #toggle
        if 'T5s' in selected_range:
            buttonT5s.config(bg = color_suited)
            selected_range.remove('T5s')
        else:
            buttonT5s.config(bg = color_suited_selected)
            selected_range.append('T5s')

def pressT4s(par):
    if par == 0:
        if 'T4s' in selected_range:
            buttonT4s.config(bg = color_suited)
            selected_range.remove('T4s')
    elif par == 1:
        if 'T4s' not in selected_range:
            buttonT4s.config(bg = color_suited_selected)
            selected_range.append('T4s')
    else: #toggle
        if 'T4s' in selected_range:
            buttonT4s.config(bg = color_suited)
            selected_range.remove('T4s')
        else:
            buttonT4s.config(bg = color_suited_selected)
            selected_range.append('T4s')

def pressT3s(par):
    if par == 0:
        if 'T3s' in selected_range:
            buttonT3s.config(bg = color_suited)
            selected_range.remove('T3s')
    elif par == 1:
        if 'T3s' not in selected_range:
            buttonT3s.config(bg = color_suited_selected)
            selected_range.append('T3s')
    else: #toggle
        if 'T3s' in selected_range:
            buttonT3s.config(bg = color_suited)
            selected_range.remove('T3s')
        else:
            buttonT3s.config(bg = color_suited_selected)
            selected_range.append('T3s')

def pressT2s(par):
    if par == 0:
        if 'T2s' in selected_range:
            buttonT2s.config(bg = color_suited)
            selected_range.remove('T2s')
    elif par == 1:
        if 'T2s' not in selected_range:
            buttonT2s.config(bg = color_suited_selected)
            selected_range.append('T2s')
    else: #toggle
        if 'T2s' in selected_range:
            buttonT2s.config(bg = color_suited)
            selected_range.remove('T2s')
        else:
            buttonT2s.config(bg = color_suited_selected)
            selected_range.append('T2s')

#suited handlers 9

def press98s(par):
    if par == 0:
        if '98s' in selected_range:
            button98s.config(bg = color_suited)
            selected_range.remove('98s')
    elif par == 1:
        if '98s' not in selected_range:
            button98s.config(bg = color_suited_selected)
            selected_range.append('98s')
    else: #toggle
        if '98s' in selected_range:
            button98s.config(bg = color_suited)
            selected_range.remove('98s')
        else:
            button98s.config(bg = color_suited_selected)
            selected_range.append('98s')

def press97s(par):
    if par == 0:
        if '97s' in selected_range:
            button97s.config(bg = color_suited)
            selected_range.remove('97s')
    elif par == 1:
        if '97s' not in selected_range:
            button97s.config(bg = color_suited_selected)
            selected_range.append('97s')
    else: #toggle
        if '97s' in selected_range:
            button97s.config(bg = color_suited)
            selected_range.remove('97s')
        else:
            button97s.config(bg = color_suited_selected)
            selected_range.append('97s')

def press96s(par):
    if par == 0:
        if '96s' in selected_range:
            button96s.config(bg = color_suited)
            selected_range.remove('96s')
    elif par == 1:
        if '96s' not in selected_range:
            button96s.config(bg = color_suited_selected)
            selected_range.append('96s')
    else: #toggle
        if '96s' in selected_range:
            button96s.config(bg = color_suited)
            selected_range.remove('96s')
        else:
            button96s.config(bg = color_suited_selected)
            selected_range.append('96s')

def press95s(par):
    if par == 0:
        if '95s' in selected_range:
            button95s.config(bg = color_suited)
            selected_range.remove('95s')
    elif par == 1:
        if '95s' not in selected_range:
            button95s.config(bg = color_suited_selected)
            selected_range.append('95s')
    else: #toggle
        if '95s' in selected_range:
            button95s.config(bg = color_suited)
            selected_range.remove('95s')
        else:
            button95s.config(bg = color_suited_selected)
            selected_range.append('95s')

def press94s(par):
    if par == 0:
        if '94s' in selected_range:
            button94s.config(bg = color_suited)
            selected_range.remove('94s')
    elif par == 1:
        if '94s' not in selected_range:
            button94s.config(bg = color_suited_selected)
            selected_range.append('94s')
    else: #toggle
        if '94s' in selected_range:
            button94s.config(bg = color_suited)
            selected_range.remove('94s')
        else:
            button94s.config(bg = color_suited_selected)
            selected_range.append('94s')

def press93s(par):
    if par == 0:
        if '93s' in selected_range:
            button93s.config(bg = color_suited)
            selected_range.remove('93s')
    elif par == 1:
        if '93s' not in selected_range:
            button93s.config(bg = color_suited_selected)
            selected_range.append('93s')
    else: #toggle
        if '93s' in selected_range:
            button93s.config(bg = color_suited)
            selected_range.remove('93s')
        else:
            button93s.config(bg = color_suited_selected)
            selected_range.append('93s')

def press92s(par):
    if par == 0:
        if '92s' in selected_range:
            button92s.config(bg = color_suited)
            selected_range.remove('92s')
    elif par == 1:
        if '92s' not in selected_range:
            button92s.config(bg = color_suited_selected)
            selected_range.append('92s')
    else: #toggle
        if '92s' in selected_range:
            button92s.config(bg = color_suited)
            selected_range.remove('92s')
        else:
            button92s.config(bg = color_suited_selected)
            selected_range.append('92s')

#suited handlers 8

def press87s(par):
    if par == 0:
        if '87s' in selected_range:
            button87s.config(bg = color_suited)
            selected_range.remove('87s')
    elif par == 1:
        if '87s' not in selected_range:
            button87s.config(bg = color_suited_selected)
            selected_range.append('87s')
    else: #toggle
        if '87s' in selected_range:
            button87s.config(bg = color_suited)
            selected_range.remove('87s')
        else:
            button87s.config(bg = color_suited_selected)
            selected_range.append('87s')

def press86s(par):
    if par == 0:
        if '86s' in selected_range:
            button86s.config(bg = color_suited)
            selected_range.remove('86s')
    elif par == 1:
        if '86s' not in selected_range:
            button86s.config(bg = color_suited_selected)
            selected_range.append('86s')
    else: #toggle
        if '86s' in selected_range:
            button86s.config(bg = color_suited)
            selected_range.remove('86s')
        else:
            button86s.config(bg = color_suited_selected)
            selected_range.append('86s')

def press85s(par):
    if par == 0:
        if '85s' in selected_range:
            button85s.config(bg = color_suited)
            selected_range.remove('85s')
    elif par == 1:
        if '85s' not in selected_range:
            button85s.config(bg = color_suited_selected)
            selected_range.append('85s')
    else: #toggle
        if '85s' in selected_range:
            button85s.config(bg = color_suited)
            selected_range.remove('85s')
        else:
            button85s.config(bg = color_suited_selected)
            selected_range.append('85s')

def press84s(par):
    if par == 0:
        if '84s' in selected_range:
            button84s.config(bg = color_suited)
            selected_range.remove('84s')
    elif par == 1:
        if '84s' not in selected_range:
            button84s.config(bg = color_suited_selected)
            selected_range.append('84s')
    else: #toggle
        if '84s' in selected_range:
            button84s.config(bg = color_suited)
            selected_range.remove('84s')
        else:
            button84s.config(bg = color_suited_selected)
            selected_range.append('84s')

def press83s(par):
    if par == 0:
        if '83s' in selected_range:
            button83s.config(bg = color_suited)
            selected_range.remove('83s')
    elif par == 1:
        if '83s' not in selected_range:
            button83s.config(bg = color_suited_selected)
            selected_range.append('83s')
    else: #toggle
        if '83s' in selected_range:
            button83s.config(bg = color_suited)
            selected_range.remove('83s')
        else:
            button83s.config(bg = color_suited_selected)
            selected_range.append('83s')

def press82s(par):
    if par == 0:
        if '82s' in selected_range:
            button82s.config(bg = color_suited)
            selected_range.remove('82s')
    elif par == 1:
        if '82s' not in selected_range:
            button82s.config(bg = color_suited_selected)
            selected_range.append('82s')
    else: #toggle
        if '82s' in selected_range:
            button82s.config(bg = color_suited)
            selected_range.remove('82s')
        else:
            button82s.config(bg = color_suited_selected)
            selected_range.append('82s')

#suited handlers 7

def press76s(par):
    if par == 0:
        if '76s' in selected_range:
            button76s.config(bg = color_suited)
            selected_range.remove('76s')
    elif par == 1:
        if '76s' not in selected_range:
            button76s.config(bg = color_suited_selected)
            selected_range.append('76s')
    else: #toggle
        if '76s' in selected_range:
            button76s.config(bg = color_suited)
            selected_range.remove('76s')
        else:
            button76s.config(bg = color_suited_selected)
            selected_range.append('76s')

def press75s(par):
    if par == 0:
        if '75s' in selected_range:
            button75s.config(bg = color_suited)
            selected_range.remove('75s')
    elif par == 1:
        if '75s' not in selected_range:
            button75s.config(bg = color_suited_selected)
            selected_range.append('75s')
    else: #toggle
        if '75s' in selected_range:
            button75s.config(bg = color_suited)
            selected_range.remove('75s')
        else:
            button75s.config(bg = color_suited_selected)
            selected_range.append('75s')

def press74s(par):
    if par == 0:
        if '74s' in selected_range:
            button74s.config(bg = color_suited)
            selected_range.remove('74s')
    elif par == 1:
        if '74s' not in selected_range:
            button74s.config(bg = color_suited_selected)
            selected_range.append('74s')
    else: #toggle
        if '74s' in selected_range:
            button74s.config(bg = color_suited)
            selected_range.remove('74s')
        else:
            button74s.config(bg = color_suited_selected)
            selected_range.append('74s')

def press73s(par):
    if par == 0:
        if '73s' in selected_range:
            button73s.config(bg = color_suited)
            selected_range.remove('73s')
    elif par == 1:
        if '73s' not in selected_range:
            button73s.config(bg = color_suited_selected)
            selected_range.append('73s')
    else: #toggle
        if '73s' in selected_range:
            button73s.config(bg = color_suited)
            selected_range.remove('73s')
        else:
            button73s.config(bg = color_suited_selected)
            selected_range.append('73s')

def press72s(par):
    if par == 0:
        if '72s' in selected_range:
            button72s.config(bg = color_suited)
            selected_range.remove('72s')
    elif par == 1:
        if '72s' not in selected_range:
            button72s.config(bg = color_suited_selected)
            selected_range.append('72s')
    else: #toggle
        if '72s' in selected_range:
            button72s.config(bg = color_suited)
            selected_range.remove('72s')
        else:
            button72s.config(bg = color_suited_selected)
            selected_range.append('72s')

#suited handlers 6

def press65s(par):
    if par == 0:
        if '65s' in selected_range:
            button65s.config(bg = color_suited)
            selected_range.remove('65s')
    elif par == 1:
        if '65s' not in selected_range:
            button65s.config(bg = color_suited_selected)
            selected_range.append('65s')
    else: #toggle
        if '65s' in selected_range:
            button65s.config(bg = color_suited)
            selected_range.remove('65s')
        else:
            button65s.config(bg = color_suited_selected)
            selected_range.append('65s')

def press64s(par):
    if par == 0:
        if '64s' in selected_range:
            button64s.config(bg = color_suited)
            selected_range.remove('64s')
    elif par == 1:
        if '64s' not in selected_range:
            button64s.config(bg = color_suited_selected)
            selected_range.append('64s')
    else: #toggle
        if '64s' in selected_range:
            button64s.config(bg = color_suited)
            selected_range.remove('64s')
        else:
            button64s.config(bg = color_suited_selected)
            selected_range.append('64s')

def press63s(par):
    if par == 0:
        if '63s' in selected_range:
            button63s.config(bg = color_suited)
            selected_range.remove('63s')
    elif par == 1:
        if '63s' not in selected_range:
            button63s.config(bg = color_suited_selected)
            selected_range.append('63s')
    else: #toggle
        if '63s' in selected_range:
            button63s.config(bg = color_suited)
            selected_range.remove('63s')
        else:
            button63s.config(bg = color_suited_selected)
            selected_range.append('63s')

def press62s(par):
    if par == 0:
        if '62s' in selected_range:
            button62s.config(bg = color_suited)
            selected_range.remove('62s')
    elif par == 1:
        if '62s' not in selected_range:
            button62s.config(bg = color_suited_selected)
            selected_range.append('62s')
    else: #toggle
        if '62s' in selected_range:
            button62s.config(bg = color_suited)
            selected_range.remove('62s')
        else:
            button62s.config(bg = color_suited_selected)
            selected_range.append('62s')

#suited handlers 5

def press54s(par):
    if par == 0:
        if '54s' in selected_range:
            button54s.config(bg = color_suited)
            selected_range.remove('54s')
    elif par == 1:
        if '54s' not in selected_range:
            button54s.config(bg = color_suited_selected)
            selected_range.append('54s')
    else: #toggle
        if '54s' in selected_range:
            button54s.config(bg = color_suited)
            selected_range.remove('54s')
        else:
            button54s.config(bg = color_suited_selected)
            selected_range.append('54s')

def press53s(par):
    if par == 0:
        if '53s' in selected_range:
            button53s.config(bg = color_suited)
            selected_range.remove('53s')
    elif par == 1:
        if '53s' not in selected_range:
            button53s.config(bg = color_suited_selected)
            selected_range.append('53s')
    else: #toggle
        if '53s' in selected_range:
            button53s.config(bg = color_suited)
            selected_range.remove('53s')
        else:
            button53s.config(bg = color_suited_selected)
            selected_range.append('53s')

def press52s(par):
    if par == 0:
        if '52s' in selected_range:
            button52s.config(bg = color_suited)
            selected_range.remove('52s')
    elif par == 1:
        if '52s' not in selected_range:
            button52s.config(bg = color_suited_selected)
            selected_range.append('52s')
    else: #toggle
        if '52s' in selected_range:
            button52s.config(bg = color_suited)
            selected_range.remove('52s')
        else:
            button52s.config(bg = color_suited_selected)
            selected_range.append('52s')

#suited handlers 4

def press43s(par):
    if par == 0:
        if '43s' in selected_range:
            button43s.config(bg = color_suited)
            selected_range.remove('43s')
    elif par == 1:
        if '43s' not in selected_range:
            button43s.config(bg = color_suited_selected)
            selected_range.append('43s')
    else: #toggle
        if '43s' in selected_range:
            button43s.config(bg = color_suited)
            selected_range.remove('43s')
        else:
            button43s.config(bg = color_suited_selected)
            selected_range.append('43s')

def press42s(par):
    if par == 0:
        if '42s' in selected_range:
            button42s.config(bg = color_suited)
            selected_range.remove('42s')
    elif par == 1:
        if '42s' not in selected_range:
            button42s.config(bg = color_suited_selected)
            selected_range.append('42s')
    else: #toggle
        if '42s' in selected_range:
            button42s.config(bg = color_suited)
            selected_range.remove('42s')
        else:
            button42s.config(bg = color_suited_selected)
            selected_range.append('42s')

#suited handlers 3

def press32s(par):
    if par == 0:
        if '32s' in selected_range:
            button32s.config(bg = color_suited)
            selected_range.remove('32s')
    elif par == 1:
        if '32s' not in selected_range:
            button32s.config(bg = color_suited_selected)
            selected_range.append('32s')
    else: #toggle
        if '32s' in selected_range:
            button32s.config(bg = color_suited)
            selected_range.remove('32s')
        else:
            button32s.config(bg = color_suited_selected)
            selected_range.append('32s')

#offsuited handlers

def pressAKo(par):
    if par == 0:
        if 'AKo' in selected_range:
            buttonAKo.config(bg = color_offsuit)
            selected_range.remove('AKo')
    elif par == 1:
        if 'AKo' not in selected_range:
            buttonAKo.config(bg = color_offsuit_selected)
            selected_range.append('AKo')
    else: #toggle
        if 'AKo' in selected_range:
            buttonAKo.config(bg = color_offsuit)
            selected_range.remove('AKo')
        else:
            buttonAKo.config(bg = color_offsuit_selected)
            selected_range.append('AKo')

def pressAQo(par):
    if par == 0:
        if 'AQo' in selected_range:
            buttonAQo.config(bg = color_offsuit)
            selected_range.remove('AQo')
    elif par == 1:
        if 'AQo' not in selected_range:
            buttonAQo.config(bg = color_offsuit_selected)
            selected_range.append('AQo')
    else: #toggle
        if 'AQo' in selected_range:
            buttonAQo.config(bg = color_offsuit)
            selected_range.remove('AQo')
        else:
            buttonAQo.config(bg = color_offsuit_selected)
            selected_range.append('AQo')

def pressAJo(par):
    if par == 0:
        if 'AJo' in selected_range:
            buttonAJo.config(bg = color_offsuit)
            selected_range.remove('AJo')
    elif par == 1:
        if 'AJo' not in selected_range:
            buttonAJo.config(bg = color_offsuit_selected)
            selected_range.append('AJo')
    else: #toggle
        if 'AJo' in selected_range:
            buttonAJo.config(bg = color_offsuit)
            selected_range.remove('AJo')
        else:
            buttonAJo.config(bg = color_offsuit_selected)
            selected_range.append('AJo')

def pressATo(par):
    if par == 0:
        if 'ATo' in selected_range:
            buttonATo.config(bg = color_offsuit)
            selected_range.remove('ATo')
    elif par == 1:
        if 'ATo' not in selected_range:
            buttonATo.config(bg = color_offsuit_selected)
            selected_range.append('ATo')
    else: #toggle
        if 'ATo' in selected_range:
            buttonATo.config(bg = color_offsuit)
            selected_range.remove('ATo')
        else:
            buttonATo.config(bg = color_offsuit_selected)
            selected_range.append('ATo')

def pressA9o(par):
    if par == 0:
        if 'A9o' in selected_range:
            buttonA9o.config(bg = color_offsuit)
            selected_range.remove('A9o')
    elif par == 1:
        if 'A9o' not in selected_range:
            buttonA9o.config(bg = color_offsuit_selected)
            selected_range.append('A9o')
    else: #toggle
        if 'A9o' in selected_range:
            buttonA9o.config(bg = color_offsuit)
            selected_range.remove('A9o')
        else:
            buttonA9o.config(bg = color_offsuit_selected)
            selected_range.append('A9o')

def pressA8o(par):
    if par == 0:
        if 'A8o' in selected_range:
            buttonA8o.config(bg = color_offsuit)
            selected_range.remove('A8o')
    elif par == 1:
        if 'A8o' not in selected_range:
            buttonA8o.config(bg = color_offsuit_selected)
            selected_range.append('A8o')
    else: #toggle
        if 'A8o' in selected_range:
            buttonA8o.config(bg = color_offsuit)
            selected_range.remove('A8o')
        else:
            buttonA8o.config(bg = color_offsuit_selected)
            selected_range.append('A8o')

def pressA7o(par):
    if par == 0:
        if 'A7o' in selected_range:
            buttonA7o.config(bg = color_offsuit)
            selected_range.remove('A7o')
    elif par == 1:
        if 'A7o' not in selected_range:
            buttonA7o.config(bg = color_offsuit_selected)
            selected_range.append('A7o')
    else: #toggle
        if 'A7o' in selected_range:
            buttonA7o.config(bg = color_offsuit)
            selected_range.remove('A7o')
        else:
            buttonA7o.config(bg = color_offsuit_selected)
            selected_range.append('A7o')

def pressA6o(par):
    if par == 0:
        if 'A6o' in selected_range:
            buttonA6o.config(bg = color_offsuit)
            selected_range.remove('A6o')
    elif par == 1:
        if 'A6o' not in selected_range:
            buttonA6o.config(bg = color_offsuit_selected)
            selected_range.append('A6o')
    else: #toggle
        if 'A6o' in selected_range:
            buttonA6o.config(bg = color_offsuit)
            selected_range.remove('A6o')
        else:
            buttonA6o.config(bg = color_offsuit_selected)
            selected_range.append('A6o')

def pressA5o(par):
    if par == 0:
        if 'A5o' in selected_range:
            buttonA5o.config(bg = color_offsuit)
            selected_range.remove('A5o')
    elif par == 1:
        if 'A5o' not in selected_range:
            buttonA5o.config(bg = color_offsuit_selected)
            selected_range.append('A5o')
    else: #toggle
        if 'A5o' in selected_range:
            buttonA5o.config(bg = color_offsuit)
            selected_range.remove('A5o')
        else:
            buttonA5o.config(bg = color_offsuit_selected)
            selected_range.append('A5o')

def pressA4o(par):
    if par == 0:
        if 'A4o' in selected_range:
            buttonA4o.config(bg = color_offsuit)
            selected_range.remove('A4o')
    elif par == 1:
        if 'A4o' not in selected_range:
            buttonA4o.config(bg = color_offsuit_selected)
            selected_range.append('A4o')
    else: #toggle
        if 'A4o' in selected_range:
            buttonA4o.config(bg = color_offsuit)
            selected_range.remove('A4o')
        else:
            buttonA4o.config(bg = color_offsuit_selected)
            selected_range.append('A4o')

def pressA3o(par):
    if par == 0:
        if 'A3o' in selected_range:
            buttonA3o.config(bg = color_offsuit)
            selected_range.remove('A3o')
    elif par == 1:
        if 'A3o' not in selected_range:
            buttonA3o.config(bg = color_offsuit_selected)
            selected_range.append('A3o')
    else: #toggle
        if 'A3o' in selected_range:
            buttonA3o.config(bg = color_offsuit)
            selected_range.remove('A3o')
        else:
            buttonA3o.config(bg = color_offsuit_selected)
            selected_range.append('A3o')

def pressA2o(par):
    if par == 0:
        if 'A2o' in selected_range:
            buttonA2o.config(bg = color_offsuit)
            selected_range.remove('A2o')
    elif par == 1:
        if 'A2o' not in selected_range:
            buttonA2o.config(bg = color_offsuit_selected)
            selected_range.append('A2o')
    else: #toggle
        if 'A2o' in selected_range:
            buttonA2o.config(bg = color_offsuit)
            selected_range.remove('A2o')
        else:
            buttonA2o.config(bg = color_offsuit_selected)
            selected_range.append('A2o')

# K

def pressKQo(par):
    if par == 0:
        if 'KQo' in selected_range:
            buttonKQo.config(bg = color_offsuit)
            selected_range.remove('KQo')
    elif par == 1:
        if 'KQo' not in selected_range:
            buttonKQo.config(bg = color_offsuit_selected)
            selected_range.append('KQo')
    else: #toggle
        if 'KQo' in selected_range:
            buttonKQo.config(bg = color_offsuit)
            selected_range.remove('KQo')
        else:
            buttonKQo.config(bg = color_offsuit_selected)
            selected_range.append('KQo')

def pressKJo(par):
    if par == 0:
        if 'KJo' in selected_range:
            buttonKJo.config(bg = color_offsuit)
            selected_range.remove('KJo')
    elif par == 1:
        if 'KJo' not in selected_range:
            buttonKJo.config(bg = color_offsuit_selected)
            selected_range.append('KJo')
    else: #toggle
        if 'KJo' in selected_range:
            buttonKJo.config(bg = color_offsuit)
            selected_range.remove('KJo')
        else:
            buttonKJo.config(bg = color_offsuit_selected)
            selected_range.append('KJo')

def pressKTo(par):
    if par == 0:
        if 'KTo' in selected_range:
            buttonKTo.config(bg = color_offsuit)
            selected_range.remove('KTo')
    elif par == 1:
        if 'KTo' not in selected_range:
            buttonKTo.config(bg = color_offsuit_selected)
            selected_range.append('KTo')
    else: #toggle
        if 'KTo' in selected_range:
            buttonKTo.config(bg = color_offsuit)
            selected_range.remove('KTo')
        else:
            buttonKTo.config(bg = color_offsuit_selected)
            selected_range.append('KTo')

def pressK9o(par):
    if par == 0:
        if 'K9o' in selected_range:
            buttonK9o.config(bg = color_offsuit)
            selected_range.remove('K9o')
    elif par == 1:
        if 'K9o' not in selected_range:
            buttonK9o.config(bg = color_offsuit_selected)
            selected_range.append('K9o')
    else: #toggle
        if 'K9o' in selected_range:
            buttonK9o.config(bg = color_offsuit)
            selected_range.remove('K9o')
        else:
            buttonK9o.config(bg = color_offsuit_selected)
            selected_range.append('K9o')

def pressK8o(par):
    if par == 0:
        if 'K8o' in selected_range:
            buttonK8o.config(bg = color_offsuit)
            selected_range.remove('K8o')
    elif par == 1:
        if 'K8o' not in selected_range:
            buttonK8o.config(bg = color_offsuit_selected)
            selected_range.append('K8o')
    else: #toggle
        if 'K8o' in selected_range:
            buttonK8o.config(bg = color_offsuit)
            selected_range.remove('K8o')
        else:
            buttonK8o.config(bg = color_offsuit_selected)
            selected_range.append('K8o')

def pressK7o(par):
    if par == 0:
        if 'K7o' in selected_range:
            buttonK7o.config(bg = color_offsuit)
            selected_range.remove('K7o')
    elif par == 1:
        if 'K7o' not in selected_range:
            buttonK7o.config(bg = color_offsuit_selected)
            selected_range.append('K7o')
    else: #toggle
        if 'K7o' in selected_range:
            buttonK7o.config(bg = color_offsuit)
            selected_range.remove('K7o')
        else:
            buttonK7o.config(bg = color_offsuit_selected)
            selected_range.append('K7o')

def pressK6o(par):
    if par == 0:
        if 'K6o' in selected_range:
            buttonK6o.config(bg = color_offsuit)
            selected_range.remove('K6o')
    elif par == 1:
        if 'K6o' not in selected_range:
            buttonK6o.config(bg = color_offsuit_selected)
            selected_range.append('K6o')
    else: #toggle
        if 'K6o' in selected_range:
            buttonK6o.config(bg = color_offsuit)
            selected_range.remove('K6o')
        else:
            buttonK6o.config(bg = color_offsuit_selected)
            selected_range.append('K6o')

def pressK5o(par):
    if par == 0:
        if 'K5o' in selected_range:
            buttonK5o.config(bg = color_offsuit)
            selected_range.remove('K5o')
    elif par == 1:
        if 'K5o' not in selected_range:
            buttonK5o.config(bg = color_offsuit_selected)
            selected_range.append('K5o')
    else: #toggle
        if 'K5o' in selected_range:
            buttonK5o.config(bg = color_offsuit)
            selected_range.remove('K5o')
        else:
            buttonK5o.config(bg = color_offsuit_selected)
            selected_range.append('K5o')

def pressK4o(par):
    if par == 0:
        if 'K4o' in selected_range:
            buttonK4o.config(bg = color_offsuit)
            selected_range.remove('K4o')
    elif par == 1:
        if 'K4o' not in selected_range:
            buttonK4o.config(bg = color_offsuit_selected)
            selected_range.append('K4o')
    else: #toggle
        if 'K4o' in selected_range:
            buttonK4o.config(bg = color_offsuit)
            selected_range.remove('K4o')
        else:
            buttonK4o.config(bg = color_offsuit_selected)
            selected_range.append('K4o')

def pressK3o(par):
    if par == 0:
        if 'K3o' in selected_range:
            buttonK3o.config(bg = color_offsuit)
            selected_range.remove('K3o')
    elif par == 1:
        if 'K3o' not in selected_range:
            buttonK3o.config(bg = color_offsuit_selected)
            selected_range.append('K3o')
    else: #toggle
        if 'K3o' in selected_range:
            buttonK3o.config(bg = color_offsuit)
            selected_range.remove('K3o')
        else:
            buttonK3o.config(bg = color_offsuit_selected)
            selected_range.append('K3o')

def pressK2o(par):
    if par == 0:
        if 'K2o' in selected_range:
            buttonK2o.config(bg = color_offsuit)
            selected_range.remove('K2o')
    elif par == 1:
        if 'K2o' not in selected_range:
            buttonK2o.config(bg = color_offsuit_selected)
            selected_range.append('K2o')
    else: #toggle
        if 'K2o' in selected_range:
            buttonK2o.config(bg = color_offsuit)
            selected_range.remove('K2o')
        else:
            buttonK2o.config(bg = color_offsuit_selected)
            selected_range.append('K2o') 

# Q

def pressQJo(par):
    if par == 0:
        if 'QJo' in selected_range:
            buttonQJo.config(bg = color_offsuit)
            selected_range.remove('QJo')
    elif par == 1:
        if 'QJo' not in selected_range:
            buttonQJo.config(bg = color_offsuit_selected)
            selected_range.append('QJo')
    else: #toggle
        if 'QJo' in selected_range:
            buttonQJo.config(bg = color_offsuit)
            selected_range.remove('QJo')
        else:
            buttonQJo.config(bg = color_offsuit_selected)
            selected_range.append('QJo')

def pressQTo(par):
    if par == 0:
        if 'QTo' in selected_range:
            buttonQTo.config(bg = color_offsuit)
            selected_range.remove('QTo')
    elif par == 1:
        if 'QTo' not in selected_range:
            buttonQTo.config(bg = color_offsuit_selected)
            selected_range.append('QTo')
    else: #toggle
        if 'QTo' in selected_range:
            buttonQTo.config(bg = color_offsuit)
            selected_range.remove('QTo')
        else:
            buttonQTo.config(bg = color_offsuit_selected)
            selected_range.append('QTo')

def pressQ9o(par):
    if par == 0:
        if 'Q9o' in selected_range:
            buttonQ9o.config(bg = color_offsuit)
            selected_range.remove('Q9o')
    elif par == 1:
        if 'Q9o' not in selected_range:
            buttonQ9o.config(bg = color_offsuit_selected)
            selected_range.append('Q9o')
    else: #toggle
        if 'Q9o' in selected_range:
            buttonQ9o.config(bg = color_offsuit)
            selected_range.remove('Q9o')
        else:
            buttonQ9o.config(bg = color_offsuit_selected)
            selected_range.append('Q9o')

def pressQ8o(par):
    if par == 0:
        if 'Q8o' in selected_range:
            buttonQ8o.config(bg = color_offsuit)
            selected_range.remove('Q8o')
    elif par == 1:
        if 'Q8o' not in selected_range:
            buttonQ8o.config(bg = color_offsuit_selected)
            selected_range.append('Q8o')
    else: #toggle
        if 'Q8o' in selected_range:
            buttonQ8o.config(bg = color_offsuit)
            selected_range.remove('Q8o')
        else:
            buttonQ8o.config(bg = color_offsuit_selected)
            selected_range.append('Q8o')

def pressQ7o(par):
    if par == 0:
        if 'Q7o' in selected_range:
            buttonQ7o.config(bg = color_offsuit)
            selected_range.remove('Q7o')
    elif par == 1:
        if 'Q7o' not in selected_range:
            buttonQ7o.config(bg = color_offsuit_selected)
            selected_range.append('Q7o')
    else: #toggle
        if 'Q7o' in selected_range:
            buttonQ7o.config(bg = color_offsuit)
            selected_range.remove('Q7o')
        else:
            buttonQ7o.config(bg = color_offsuit_selected)
            selected_range.append('Q7o')

def pressQ6o(par):
    if par == 0:
        if 'Q6o' in selected_range:
            buttonQ6o.config(bg = color_offsuit)
            selected_range.remove('Q6o')
    elif par == 1:
        if 'Q6o' not in selected_range:
            buttonQ6o.config(bg = color_offsuit_selected)
            selected_range.append('Q6o')
    else: #toggle
        if 'Q6o' in selected_range:
            buttonQ6o.config(bg = color_offsuit)
            selected_range.remove('Q6o')
        else:
            buttonQ6o.config(bg = color_offsuit_selected)
            selected_range.append('Q6o')

def pressQ5o(par):
    if par == 0:
        if 'Q5o' in selected_range:
            buttonQ5o.config(bg = color_offsuit)
            selected_range.remove('Q5o')
    elif par == 1:
        if 'Q5o' not in selected_range:
            buttonQ5o.config(bg = color_offsuit_selected)
            selected_range.append('Q5o')
    else: #toggle
        if 'Q5o' in selected_range:
            buttonQ5o.config(bg = color_offsuit)
            selected_range.remove('Q5o')
        else:
            buttonQ5o.config(bg = color_offsuit_selected)
            selected_range.append('Q5o')

def pressQ4o(par):
    if par == 0:
        if 'Q4o' in selected_range:
            buttonQ4o.config(bg = color_offsuit)
            selected_range.remove('Q4o')
    elif par == 1:
        if 'Q4o' not in selected_range:
            buttonQ4o.config(bg = color_offsuit_selected)
            selected_range.append('Q4o')
    else: #toggle
        if 'Q4o' in selected_range:
            buttonQ4o.config(bg = color_offsuit)
            selected_range.remove('Q4o')
        else:
            buttonQ4o.config(bg = color_offsuit_selected)
            selected_range.append('Q4o')

def pressQ3o(par):
    if par == 0:
        if 'Q3o' in selected_range:
            buttonQ3o.config(bg = color_offsuit)
            selected_range.remove('Q3o')
    elif par == 1:
        if 'Q3o' not in selected_range:
            buttonQ3o.config(bg = color_offsuit_selected)
            selected_range.append('Q3o')
    else: #toggle
        if 'Q3o' in selected_range:
            buttonQ3o.config(bg = color_offsuit)
            selected_range.remove('Q3o')
        else:
            buttonQ3o.config(bg = color_offsuit_selected)
            selected_range.append('Q3o')

def pressQ2o(par):
    if par == 0:
        if 'Q2o' in selected_range:
            buttonQ2o.config(bg = color_offsuit)
            selected_range.remove('Q2o')
    elif par == 1:
        if 'Q2o' not in selected_range:
            buttonQ2o.config(bg = color_offsuit_selected)
            selected_range.append('Q2o')
    else: #toggle
        if 'Q2o' in selected_range:
            buttonQ2o.config(bg = color_offsuit)
            selected_range.remove('Q2o')
        else:
            buttonQ2o.config(bg = color_offsuit_selected)
            selected_range.append('Q2o')

# J

def pressJTo(par):
    if par == 0:
        if 'JTo' in selected_range:
            buttonJTo.config(bg = color_offsuit)
            selected_range.remove('JTo')
    elif par == 1:
        if 'JTo' not in selected_range:
            buttonJTo.config(bg = color_offsuit_selected)
            selected_range.append('JTo')
    else: #toggle
        if 'JTo' in selected_range:
            buttonJTo.config(bg = color_offsuit)
            selected_range.remove('JTo')
        else:
            buttonJTo.config(bg = color_offsuit_selected)
            selected_range.append('JTo')

def pressJ9o(par):
    if par == 0:
        if 'J9o' in selected_range:
            buttonJ9o.config(bg = color_offsuit)
            selected_range.remove('J9o')
    elif par == 1:
        if 'J9o' not in selected_range:
            buttonJ9o.config(bg = color_offsuit_selected)
            selected_range.append('J9o')
    else: #toggle
        if 'J9o' in selected_range:
            buttonJ9o.config(bg = color_offsuit)
            selected_range.remove('J9o')
        else:
            buttonJ9o.config(bg = color_offsuit_selected)
            selected_range.append('J9o')

def pressJ8o(par):
    if par == 0:
        if 'J8o' in selected_range:
            buttonJ8o.config(bg = color_offsuit)
            selected_range.remove('J8o')
    elif par == 1:
        if 'J8o' not in selected_range:
            buttonJ8o.config(bg = color_offsuit_selected)
            selected_range.append('J8o')
    else: #toggle
        if 'J8o' in selected_range:
            buttonJ8o.config(bg = color_offsuit)
            selected_range.remove('J8o')
        else:
            buttonJ8o.config(bg = color_offsuit_selected)
            selected_range.append('J8o')

def pressJ7o(par):
    if par == 0:
        if 'J7o' in selected_range:
            buttonJ7o.config(bg = color_offsuit)
            selected_range.remove('J7o')
    elif par == 1:
        if 'J7o' not in selected_range:
            buttonJ7o.config(bg = color_offsuit_selected)
            selected_range.append('J7o')
    else: #toggle
        if 'J7o' in selected_range:
            buttonJ7o.config(bg = color_offsuit)
            selected_range.remove('J7o')
        else:
            buttonJ7o.config(bg = color_offsuit_selected)
            selected_range.append('J7o')

def pressJ6o(par):
    if par == 0:
        if 'J6o' in selected_range:
            buttonJ6o.config(bg = color_offsuit)
            selected_range.remove('J6o')
    elif par == 1:
        if 'J6o' not in selected_range:
            buttonJ6o.config(bg = color_offsuit_selected)
            selected_range.append('J6o')
    else: #toggle
        if 'J6o' in selected_range:
            buttonJ6o.config(bg = color_offsuit)
            selected_range.remove('J6o')
        else:
            buttonJ6o.config(bg = color_offsuit_selected)
            selected_range.append('J6o')

def pressJ5o(par):
    if par == 0:
        if 'J5o' in selected_range:
            buttonJ5o.config(bg = color_offsuit)
            selected_range.remove('J5o')
    elif par == 1:
        if 'J5o' not in selected_range:
            buttonJ5o.config(bg = color_offsuit_selected)
            selected_range.append('J5o')
    else: #toggle
        if 'J5o' in selected_range:
            buttonJ5o.config(bg = color_offsuit)
            selected_range.remove('J5o')
        else:
            buttonJ5o.config(bg = color_offsuit_selected)
            selected_range.append('J5o')

def pressJ4o(par):
    if par == 0:
        if 'J4o' in selected_range:
            buttonJ4o.config(bg = color_offsuit)
            selected_range.remove('J4o')
    elif par == 1:
        if 'J4o' not in selected_range:
            buttonJ4o.config(bg = color_offsuit_selected)
            selected_range.append('J4o')
    else: #toggle
        if 'J4o' in selected_range:
            buttonJ4o.config(bg = color_offsuit)
            selected_range.remove('J4o')
        else:
            buttonJ4o.config(bg = color_offsuit_selected)
            selected_range.append('J4o')

def pressJ3o(par):
    if par == 0:
        if 'J3o' in selected_range:
            buttonJ3o.config(bg = color_offsuit)
            selected_range.remove('J3o')
    elif par == 1:
        if 'J3o' not in selected_range:
            buttonJ3o.config(bg = color_offsuit_selected)
            selected_range.append('J3o')
    else: #toggle
        if 'J3o' in selected_range:
            buttonJ3o.config(bg = color_offsuit)
            selected_range.remove('J3o')
        else:
            buttonJ3o.config(bg = color_offsuit_selected)
            selected_range.append('J3o')

def pressJ2o(par):
    if par == 0:
        if 'J2o' in selected_range:
            buttonJ2o.config(bg = color_offsuit)
            selected_range.remove('J2o')
    elif par == 1:
        if 'J2o' not in selected_range:
            buttonJ2o.config(bg = color_offsuit_selected)
            selected_range.append('J2o')
    else: #toggle
        if 'J2o' in selected_range:
            buttonJ2o.config(bg = color_offsuit)
            selected_range.remove('J2o')
        else:
            buttonJ2o.config(bg = color_offsuit_selected)
            selected_range.append('J2o')

# T

def pressT9o(par):
    if par == 0:
        if 'T9o' in selected_range:
            buttonT9o.config(bg = color_offsuit)
            selected_range.remove('T9o')
    elif par == 1:
        if 'T9o' not in selected_range:
            buttonT9o.config(bg = color_offsuit_selected)
            selected_range.append('T9o')
    else: #toggle
        if 'T9o' in selected_range:
            buttonT9o.config(bg = color_offsuit)
            selected_range.remove('T9o')
        else:
            buttonT9o.config(bg = color_offsuit_selected)
            selected_range.append('T9o')

def pressT8o(par):
    if par == 0:
        if 'T8o' in selected_range:
            buttonT8o.config(bg = color_offsuit)
            selected_range.remove('T8o')
    elif par == 1:
        if 'T8o' not in selected_range:
            buttonT8o.config(bg = color_offsuit_selected)
            selected_range.append('T8o')
    else: #toggle
        if 'T8o' in selected_range:
            buttonT8o.config(bg = color_offsuit)
            selected_range.remove('T8o')
        else:
            buttonT8o.config(bg = color_offsuit_selected)
            selected_range.append('T8o')

def pressT7o(par):
    if par == 0:
        if 'T7o' in selected_range:
            buttonT7o.config(bg = color_offsuit)
            selected_range.remove('T7o')
    elif par == 1:
        if 'T7o' not in selected_range:
            buttonT7o.config(bg = color_offsuit_selected)
            selected_range.append('T7o')
    else: #toggle
        if 'T7o' in selected_range:
            buttonT7o.config(bg = color_offsuit)
            selected_range.remove('T7o')
        else:
            buttonT7o.config(bg = color_offsuit_selected)
            selected_range.append('T7o')

def pressT6o(par):
    if par == 0:
        if 'T6o' in selected_range:
            buttonT6o.config(bg = color_offsuit)
            selected_range.remove('T6o')
    elif par == 1:
        if 'T6o' not in selected_range:
            buttonT6o.config(bg = color_offsuit_selected)
            selected_range.append('T6o')
    else: #toggle
        if 'T6o' in selected_range:
            buttonT6o.config(bg = color_offsuit)
            selected_range.remove('T6o')
        else:
            buttonT6o.config(bg = color_offsuit_selected)
            selected_range.append('T6o')

def pressT5o(par):
    if par == 0:
        if 'T5o' in selected_range:
            buttonT5o.config(bg = color_offsuit)
            selected_range.remove('T5o')
    elif par == 1:
        if 'T5o' not in selected_range:
            buttonT5o.config(bg = color_offsuit_selected)
            selected_range.append('T5o')
    else: #toggle
        if 'T5o' in selected_range:
            buttonT5o.config(bg = color_offsuit)
            selected_range.remove('T5o')
        else:
            buttonT5o.config(bg = color_offsuit_selected)
            selected_range.append('T5o')

def pressT4o(par):
    if par == 0:
        if 'T4o' in selected_range:
            buttonT4o.config(bg = color_offsuit)
            selected_range.remove('T4o')
    elif par == 1:
        if 'T4o' not in selected_range:
            buttonT4o.config(bg = color_offsuit_selected)
            selected_range.append('T4o')
    else: #toggle
        if 'T4o' in selected_range:
            buttonT4o.config(bg = color_offsuit)
            selected_range.remove('T4o')
        else:
            buttonT4o.config(bg = color_offsuit_selected)
            selected_range.append('T4o')

def pressT3o(par):
    if par == 0:
        if 'T3o' in selected_range:
            buttonT3o.config(bg = color_offsuit)
            selected_range.remove('T3o')
    elif par == 1:
        if 'T3o' not in selected_range:
            buttonT3o.config(bg = color_offsuit_selected)
            selected_range.append('T3o')
    else: #toggle
        if 'T3o' in selected_range:
            buttonT3o.config(bg = color_offsuit)
            selected_range.remove('T3o')
        else:
            buttonT3o.config(bg = color_offsuit_selected)
            selected_range.append('T3o')

def pressT2o(par):
    if par == 0:
        if 'T2o' in selected_range:
            buttonT2o.config(bg = color_offsuit)
            selected_range.remove('T2o')
    elif par == 1:
        if 'T2o' not in selected_range:
            buttonT2o.config(bg = color_offsuit_selected)
            selected_range.append('T2o')
    else: #toggle
        if 'T2o' in selected_range:
            buttonT2o.config(bg = color_offsuit)
            selected_range.remove('T2o')
        else:
            buttonT2o.config(bg = color_offsuit_selected)
            selected_range.append('T2o')

# 9

def press98o(par):
    if par == 0:
        if '98o' in selected_range:
            button98o.config(bg = color_offsuit)
            selected_range.remove('98o')
    elif par == 1:
        if '98o' not in selected_range:
            button98o.config(bg = color_offsuit_selected)
            selected_range.append('98o')
    else: #toggle
        if '98o' in selected_range:
            button98o.config(bg = color_offsuit)
            selected_range.remove('98o')
        else:
            button98o.config(bg = color_offsuit_selected)
            selected_range.append('98o')

def press97o(par):
    if par == 0:
        if '97o' in selected_range:
            button97o.config(bg = color_offsuit)
            selected_range.remove('97o')
    elif par == 1:
        if '97o' not in selected_range:
            button97o.config(bg = color_offsuit_selected)
            selected_range.append('97o')
    else: #toggle
        if '97o' in selected_range:
            button97o.config(bg = color_offsuit)
            selected_range.remove('97o')
        else:
            button97o.config(bg = color_offsuit_selected)
            selected_range.append('97o')

def press96o(par):
    if par == 0:
        if '96o' in selected_range:
            button96o.config(bg = color_offsuit)
            selected_range.remove('96o')
    elif par == 1:
        if '96o' not in selected_range:
            button96o.config(bg = color_offsuit_selected)
            selected_range.append('96o')
    else: #toggle
        if '96o' in selected_range:
            button96o.config(bg = color_offsuit)
            selected_range.remove('96o')
        else:
            button96o.config(bg = color_offsuit_selected)
            selected_range.append('96o')

def press95o(par):
    if par == 0:
        if '95o' in selected_range:
            button95o.config(bg = color_offsuit)
            selected_range.remove('95o')
    elif par == 1:
        if '95o' not in selected_range:
            button95o.config(bg = color_offsuit_selected)
            selected_range.append('95o')
    else: #toggle
        if '95o' in selected_range:
            button95o.config(bg = color_offsuit)
            selected_range.remove('95o')
        else:
            button95o.config(bg = color_offsuit_selected)
            selected_range.append('95o')

def press94o(par):
    if par == 0:
        if '94o' in selected_range:
            button94o.config(bg = color_offsuit)
            selected_range.remove('94o')
    elif par == 1:
        if '94o' not in selected_range:
            button94o.config(bg = color_offsuit_selected)
            selected_range.append('94o')
    else: #toggle
        if '94o' in selected_range:
            button94o.config(bg = color_offsuit)
            selected_range.remove('94o')
        else:
            button94o.config(bg = color_offsuit_selected)
            selected_range.append('94o')

def press93o(par):
    if par == 0:
        if '93o' in selected_range:
            button93o.config(bg = color_offsuit)
            selected_range.remove('93o')
    elif par == 1:
        if '93o' not in selected_range:
            button93o.config(bg = color_offsuit_selected)
            selected_range.append('93o')
    else: #toggle
        if '93o' in selected_range:
            button93o.config(bg = color_offsuit)
            selected_range.remove('93o')
        else:
            button93o.config(bg = color_offsuit_selected)
            selected_range.append('93o')

def press92o(par):
    if par == 0:
        if '92o' in selected_range:
            button92o.config(bg = color_offsuit)
            selected_range.remove('92o')
    elif par == 1:
        if '92o' not in selected_range:
            button92o.config(bg = color_offsuit_selected)
            selected_range.append('92o')
    else: #toggle
        if '92o' in selected_range:
            button92o.config(bg = color_offsuit)
            selected_range.remove('92o')
        else:
            button92o.config(bg = color_offsuit_selected)
            selected_range.append('92o')

# 8

def press87o(par):
    if par == 0:
        if '87o' in selected_range:
            button87o.config(bg = color_offsuit)
            selected_range.remove('87o')
    elif par == 1:
        if '87o' not in selected_range:
            button87o.config(bg = color_offsuit_selected)
            selected_range.append('87o')
    else: #toggle
        if '87o' in selected_range:
            button87o.config(bg = color_offsuit)
            selected_range.remove('87o')
        else:
            button87o.config(bg = color_offsuit_selected)
            selected_range.append('87o')

def press86o(par):
    if par == 0:
        if '86o' in selected_range:
            button86o.config(bg = color_offsuit)
            selected_range.remove('86o')
    elif par == 1:
        if '86o' not in selected_range:
            button86o.config(bg = color_offsuit_selected)
            selected_range.append('86o')
    else: #toggle
        if '86o' in selected_range:
            button86o.config(bg = color_offsuit)
            selected_range.remove('86o')
        else:
            button86o.config(bg = color_offsuit_selected)
            selected_range.append('86o')

def press85o(par):
    if par == 0:
        if '85o' in selected_range:
            button85o.config(bg = color_offsuit)
            selected_range.remove('85o')
    elif par == 1:
        if '85o' not in selected_range:
            button85o.config(bg = color_offsuit_selected)
            selected_range.append('85o')
    else: #toggle
        if '85o' in selected_range:
            button85o.config(bg = color_offsuit)
            selected_range.remove('85o')
        else:
            button85o.config(bg = color_offsuit_selected)
            selected_range.append('85o')

def press84o(par):
    if par == 0:
        if '84o' in selected_range:
            button84o.config(bg = color_offsuit)
            selected_range.remove('84o')
    elif par == 1:
        if '84o' not in selected_range:
            button84o.config(bg = color_offsuit_selected)
            selected_range.append('84o')
    else: #toggle
        if '84o' in selected_range:
            button84o.config(bg = color_offsuit)
            selected_range.remove('84o')
        else:
            button84o.config(bg = color_offsuit_selected)
            selected_range.append('84o')

def press83o(par):
    if par == 0:
        if '83o' in selected_range:
            button83o.config(bg = color_offsuit)
            selected_range.remove('83o')
    elif par == 1:
        if '83o' not in selected_range:
            button83o.config(bg = color_offsuit_selected)
            selected_range.append('83o')
    else: #toggle
        if '83o' in selected_range:
            button83o.config(bg = color_offsuit)
            selected_range.remove('83o')
        else:
            button83o.config(bg = color_offsuit_selected)
            selected_range.append('83o')

def press82o(par):
    if par == 0:
        if '82o' in selected_range:
            button82o.config(bg = color_offsuit)
            selected_range.remove('82o')
    elif par == 1:
        if '82o' not in selected_range:
            button82o.config(bg = color_offsuit_selected)
            selected_range.append('82o')
    else: #toggle
        if '82o' in selected_range:
            button82o.config(bg = color_offsuit)
            selected_range.remove('82o')
        else:
            button82o.config(bg = color_offsuit_selected)
            selected_range.append('82o')

# 7
def press76o(par):
    if par == 0:
        if '76o' in selected_range:
            button76o.config(bg = color_offsuit)
            selected_range.remove('76o')
    elif par == 1:
        if '76o' not in selected_range:
            button76o.config(bg = color_offsuit_selected)
            selected_range.append('76o')
    else: #toggle
        if '76o' in selected_range:
            button76o.config(bg = color_offsuit)
            selected_range.remove('76o')
        else:
            button76o.config(bg = color_offsuit_selected)
            selected_range.append('76o')

def press75o(par):
    if par == 0:
        if '75o' in selected_range:
            button75o.config(bg = color_offsuit)
            selected_range.remove('75o')
    elif par == 1:
        if '75o' not in selected_range:
            button75o.config(bg = color_offsuit_selected)
            selected_range.append('75o')
    else: #toggle
        if '75o' in selected_range:
            button75o.config(bg = color_offsuit)
            selected_range.remove('75o')
        else:
            button75o.config(bg = color_offsuit_selected)
            selected_range.append('75o')

def press74o(par):
    if par == 0:
        if '74o' in selected_range:
            button74o.config(bg = color_offsuit)
            selected_range.remove('74o')
    elif par == 1:
        if '74o' not in selected_range:
            button74o.config(bg = color_offsuit_selected)
            selected_range.append('74o')
    else: #toggle
        if '74o' in selected_range:
            button74o.config(bg = color_offsuit)
            selected_range.remove('74o')
        else:
            button74o.config(bg = color_offsuit_selected)
            selected_range.append('74o')

def press73o(par):
    if par == 0:
        if '73o' in selected_range:
            button73o.config(bg = color_offsuit)
            selected_range.remove('73o')
    elif par == 1:
        if '73o' not in selected_range:
            button73o.config(bg = color_offsuit_selected)
            selected_range.append('73o')
    else: #toggle
        if '73o' in selected_range:
            button73o.config(bg = color_offsuit)
            selected_range.remove('73o')
        else:
            button73o.config(bg = color_offsuit_selected)
            selected_range.append('73o')

def press72o(par):
    if par == 0:
        if '72o' in selected_range:
            button72o.config(bg = color_offsuit)
            selected_range.remove('72o')
    elif par == 1:
        if '72o' not in selected_range:
            button72o.config(bg = color_offsuit_selected)
            selected_range.append('72o')
    else: #toggle
        if '72o' in selected_range:
            button72o.config(bg = color_offsuit)
            selected_range.remove('72o')
        else:
            button72o.config(bg = color_offsuit_selected)
            selected_range.append('72o')

# 6
def press65o(par):
    if par == 0:
        if '65o' in selected_range:
            button65o.config(bg = color_offsuit)
            selected_range.remove('65o')
    elif par == 1:
        if '65o' not in selected_range:
            button65o.config(bg = color_offsuit_selected)
            selected_range.append('65o')
    else: #toggle
        if '65o' in selected_range:
            button65o.config(bg = color_offsuit)
            selected_range.remove('65o')
        else:
            button65o.config(bg = color_offsuit_selected)
            selected_range.append('65o')

def press64o(par):
    if par == 0:
        if '64o' in selected_range:
            button64o.config(bg = color_offsuit)
            selected_range.remove('64o')
    elif par == 1:
        if '64o' not in selected_range:
            button64o.config(bg = color_offsuit_selected)
            selected_range.append('64o')
    else: #toggle
        if '64o' in selected_range:
            button64o.config(bg = color_offsuit)
            selected_range.remove('64o')
        else:
            button64o.config(bg = color_offsuit_selected)
            selected_range.append('64o')

def press63o(par):
    if par == 0:
        if '63o' in selected_range:
            button63o.config(bg = color_offsuit)
            selected_range.remove('63o')
    elif par == 1:
        if '63o' not in selected_range:
            button63o.config(bg = color_offsuit_selected)
            selected_range.append('63o')
    else: #toggle
        if '63o' in selected_range:
            button63o.config(bg = color_offsuit)
            selected_range.remove('63o')
        else:
            button63o.config(bg = color_offsuit_selected)
            selected_range.append('63o')

def press62o(par):
    if par == 0:
        if '62o' in selected_range:
            button62o.config(bg = color_offsuit)
            selected_range.remove('62o')
    elif par == 1:
        if '62o' not in selected_range:
            button62o.config(bg = color_offsuit_selected)
            selected_range.append('62o')
    else: #toggle
        if '62o' in selected_range:
            button62o.config(bg = color_offsuit)
            selected_range.remove('62o')
        else:
            button62o.config(bg = color_offsuit_selected)
            selected_range.append('62o')

# 5

def press54o(par):
    if par == 0:
        if '54o' in selected_range:
            button54o.config(bg = color_offsuit)
            selected_range.remove('54o')
    elif par == 1:
        if '54o' not in selected_range:
            button54o.config(bg = color_offsuit_selected)
            selected_range.append('54o')
    else: #toggle
        if '54o' in selected_range:
            button54o.config(bg = color_offsuit)
            selected_range.remove('54o')
        else:
            button54o.config(bg = color_offsuit_selected)
            selected_range.append('54o')

def press53o(par):
    if par == 0:
        if '53o' in selected_range:
            button53o.config(bg = color_offsuit)
            selected_range.remove('53o')
    elif par == 1:
        if '53o' not in selected_range:
            button53o.config(bg = color_offsuit_selected)
            selected_range.append('53o')
    else: #toggle
        if '53o' in selected_range:
            button53o.config(bg = color_offsuit)
            selected_range.remove('53o')
        else:
            button53o.config(bg = color_offsuit_selected)
            selected_range.append('53o')

def press52o(par):
    if par == 0:
        if '52o' in selected_range:
            button52o.config(bg = color_offsuit)
            selected_range.remove('52o')
    elif par == 1:
        if '52o' not in selected_range:
            button52o.config(bg = color_offsuit_selected)
            selected_range.append('52o')
    else: #toggle
        if '52o' in selected_range:
            button52o.config(bg = color_offsuit)
            selected_range.remove('52o')
        else:
            button52o.config(bg = color_offsuit_selected)
            selected_range.append('52o')

# 4

def press43o(par):
    if par == 0:
        if '43o' in selected_range:
            button43o.config(bg = color_offsuit)
            selected_range.remove('43o')
    elif par == 1:
        if '43o' not in selected_range:
            button43o.config(bg = color_offsuit_selected)
            selected_range.append('43o')
    else: #toggle
        if '43o' in selected_range:
            button43o.config(bg = color_offsuit)
            selected_range.remove('43o')
        else:
            button43o.config(bg = color_offsuit_selected)
            selected_range.append('43o')

def press42o(par):
    if par == 0:
        if '42o' in selected_range:
            button42o.config(bg = color_offsuit)
            selected_range.remove('42o')
    elif par == 1:
        if '42o' not in selected_range:
            button42o.config(bg = color_offsuit_selected)
            selected_range.append('42o')
    else: #toggle
        if '42o' in selected_range:
            button42o.config(bg = color_offsuit)
            selected_range.remove('42o')
        else:
            button42o.config(bg = color_offsuit_selected)
            selected_range.append('42o')

# 3

def press32o(par):
    if par == 0:
        if '32o' in selected_range:
            button32o.config(bg = color_offsuit)
            selected_range.remove('32o')
    elif par == 1:
        if '32o' not in selected_range:
            button32o.config(bg = color_offsuit_selected)
            selected_range.append('32o')
    else: #toggle
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
    #clear all
    procent = int(Slider.get())
    print (Slider.get())
    #clear row #1
    pressAA(0)
    pressAKs(0)
    pressAQs(0)
    pressAJs(0)
    pressATs(0)
    pressA9s(0)
    pressA8s(0)
    pressA7s(0)
    pressA6s(0)
    pressA5s(0)
    pressA4s(0)
    pressA3s(0)
    pressA2s(0)
    #clear row 2
    pressAKo(0)
    pressKK(0)
    pressKQs(0)
    pressKJs(0)
    pressKTs(0)
    pressK9s(0)
    pressK8s(0)
    pressK7s(0)
    pressK6s(0)
    pressK5s(0)
    pressK4s(0)
    pressK3s(0)
    pressK2s(0)
    #clear row 3
    pressAQo(0)
    pressKQo(0)
    pressQQ(0)
    pressQJs(0)
    pressQTs(0)
    pressQ9s(0)
    pressQ8s(0)
    pressQ7s(0)
    pressQ6s(0)
    pressQ5s(0)
    pressQ4s(0)
    pressQ3s(0)
    pressQ2s(0)
    #clear row 4
    pressAJo(0)
    pressKJo(0)
    pressQJo(0)
    pressJJ(0)
    pressJTs(0)
    pressJ9s(0)
    pressJ8s(0)
    pressJ7s(0)
    pressJ6s(0)
    pressJ5s(0)
    pressJ4s(0)
    pressJ3s(0)
    pressJ2s(0)
    #clear row 5
    pressATo(0)
    pressKTo(0)
    pressQTo(0)
    pressJTo(0)
    pressTT(0)
    pressT9s(0)
    pressT8s(0)
    pressT7s(0)
    pressT6s(0)
    pressT5s(0)
    pressT4s(0)
    pressT3s(0)
    pressT2s(0)
    #clear row 6
    pressA9o(0)
    pressK9o(0)
    pressQ9o(0)
    pressJ9o(0)
    pressT9o(0)
    press99(0)
    press98s(0)
    press97s(0)
    press96s(0)
    press95s(0)
    press94s(0)
    press93s(0)
    press92s(0)
    #clear row 7
    pressA8o(0)
    pressK8o(0)
    pressQ8o(0)
    pressJ8o(0)
    pressT8o(0)
    press98o(0)
    press88(0)
    press87s(0)
    press86s(0)
    press85s(0)
    press84s(0)
    press83s(0)
    press82s(0)
    #clear row 8
    pressA7o(0)
    pressK7o(0)
    pressQ7o(0)
    pressJ7o(0)
    pressT7o(0)
    press97o(0)
    press87o(0)
    press77(0)
    press76s(0)
    press75s(0)
    press74s(0)
    press73s(0)
    press72s(0)
    #clear row 9
    pressA6o(0)
    pressK6o(0)
    pressQ6o(0)
    pressJ6o(0)
    pressT6o(0)
    press96o(0)
    press86o(0)
    press76o(0)
    press66(0)
    press65s(0)
    press64s(0)
    press63s(0)
    press62s(0)
    #clear row 10
    pressA5o(0)
    pressK5o(0)
    pressQ5o(0)
    pressJ5o(0)
    pressT5o(0)
    press95o(0)
    press85o(0)
    press75o(0)
    press65o(0)
    press55(0)
    press54s(0)
    press53s(0)
    press52s(0)
    #clear row 11
    pressA4o(0)
    pressK4o(0)
    pressQ4o(0)
    pressJ4o(0)
    pressT4o(0)
    press94o(0)
    press84o(0)
    press74o(0)
    press64o(0)
    press54o(0)
    press44(0)
    press43s(0)
    press42s(0)
    #clear row 12
    pressA3o(0)
    pressK3o(0)
    pressQ3o(0)
    pressJ3o(0)
    pressT3o(0)
    press93o(0)
    press83o(0)
    press73o(0)
    press63o(0)
    press53o(0)
    press43o(0)
    press33(0)
    press32s(0)
    #clear row 13
    pressA2o(0)
    pressK2o(0)
    pressQ2o(0)
    pressJ2o(0)
    pressT2o(0)
    press92o(0)
    press82o(0)
    press72o(0)
    press62o(0)
    press52o(0)
    press42o(0)
    press32o(0)
    press22(0)

    #slider control set hands based on integer %
    #setRange(procent)
    if procent < 1:
        pass
    elif procent < 2:
        pressAA(1), pressKK(1), pressQQ(1)
    elif procent < 3:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
    elif procent < 4:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
    elif procent < 5:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
    elif procent < 6:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
    elif procent < 7:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
    elif procent < 8:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
    elif procent < 9:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
    elif procent < 10:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
    elif procent < 11:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
    elif procent < 12:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
    elif procent < 13:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
    elif procent < 14:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
    elif procent < 15:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
    elif procent < 16:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
    elif procent < 17:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
    elif procent < 18:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
    elif procent < 19:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
    elif procent < 20:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
    elif procent < 21:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
        pressA6s(1), pressA5s(1), pressQ9s(1)
    elif procent < 22:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
        pressA6s(1), pressA5s(1), pressQ9s(1)
        pressA4s(1), pressJ9s(1)
    elif procent < 23:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
        pressA6s(1), pressA5s(1), pressQ9s(1)
        pressA4s(1), pressJ9s(1)
        pressA9o(1), press98s(1)
    elif procent < 24:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
        pressA6s(1), pressA5s(1), pressQ9s(1)
        pressA4s(1), pressJ9s(1)
        pressA9o(1), press98s(1)
        press87s(1), press76s(1), press65s(1)
    elif procent < 25:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
        pressA6s(1), pressA5s(1), pressQ9s(1)
        pressA4s(1), pressJ9s(1)
        pressA9o(1), press98s(1)
        press87s(1), press76s(1), press65s(1)
        pressT9o(1), press54s(1)
    elif procent < 26:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
        pressA6s(1), pressA5s(1), pressQ9s(1)
        pressA4s(1), pressJ9s(1)
        pressA9o(1), press98s(1)
        press87s(1), press76s(1), press65s(1)
        pressT9o(1), press54s(1)
        pressK9o(1), pressJ9o(1)
    elif procent < 27:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
        pressA6s(1), pressA5s(1), pressQ9s(1)
        pressA4s(1), pressJ9s(1)
        pressA9o(1), press98s(1)
        press87s(1), press76s(1), press65s(1)
        pressT9o(1), press54s(1)
        pressK9o(1), pressJ9o(1)
        pressQ9o(1)
    elif procent < 28:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
        pressA6s(1), pressA5s(1), pressQ9s(1)
        pressA4s(1), pressJ9s(1)
        pressA9o(1), press98s(1)
        press87s(1), press76s(1), press65s(1)
        pressT9o(1), press54s(1)
        pressK9o(1), pressJ9o(1)
        pressQ9o(1)
        pressK8s(1)
    elif procent < 29:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
        pressA6s(1), pressA5s(1), pressQ9s(1)
        pressA4s(1), pressJ9s(1)
        pressA9o(1), press98s(1)
        press87s(1), press76s(1), press65s(1)
        pressT9o(1), press54s(1)
        pressK9o(1), pressJ9o(1)
        pressQ9o(1)
        pressK8s(1)
        pressA8o(1), pressK7s(1), pressA3s(1)
    elif procent < 30:
        pressAA(1), pressKK(1), pressQQ(1)
        pressJJ(1), pressAKs(1)
        pressAKo(1)
        pressAQs(1), pressTT(1), pressAQo(1)
        pressAJs(1)
        pressAJo(1), pressKQs(1)
        pressATs(1), pressKQo(1)
        press99(1), press88(1)
        pressA9s(1), pressATo(1)
        pressKJs(1), pressQJs(1), press77(1)
        press66(1), press55(1), press44(1)
        press33(1), press22(1)
        pressKJo(1)
        pressQJo(1), pressKTs(1), pressQTs(1), pressJTs(1)
        pressA9s(1), pressATo(1)
        pressQTo(1)
        pressJTo(1)
        pressKTo(1), pressT9s(1)
        pressA8s(1), pressA7s(1), pressK9s(1)
        pressA6s(1), pressA5s(1), pressQ9s(1)
        pressA4s(1), pressJ9s(1)
        pressA9o(1), press98s(1)
        press87s(1), press76s(1), press65s(1)
        pressT9o(1), press54s(1)
        pressK9o(1), pressJ9o(1)
        pressQ9o(1)
        pressK8s(1)
        pressA8o(1), pressK7s(1), pressA3s(1)
        pressA2s(1), pressT8s(1)




#Button
#row=1
#buttonAA = tk.Button(mywindow,text='AA',command=pressAA(2),bg=color_pp)
buttonAA = tk.Button(mywindow,text='AA',command = lambda: pressAA(2),bg=color_pp)
buttonAA.grid(row=1,column=0,sticky = "NSEW")
buttonAKs = tk.Button(mywindow,text='AK',command = lambda: pressAKs(2),bg=color_suited)
buttonAKs.grid(row=1,column=1,sticky = "NSEW")
buttonAQs = tk.Button(mywindow,text='AQ',command = lambda: pressAQs(2),bg=color_suited) #,bg='red
buttonAQs.grid(row=1,column=2,sticky = "NSEW")
buttonAJs = tk.Button(mywindow,text='AJ',command = lambda: pressAJs(2),bg=color_suited) #,bg='red
buttonAJs.grid(row=1,column=3,sticky = "NSEW")
buttonATs = tk.Button(mywindow,text='AT',command = lambda: pressATs(2),bg=color_suited) #,bg='red
buttonATs.grid(row=1,column=4,sticky = "NSEW")
buttonA9s = tk.Button(mywindow,text='A9',command = lambda: pressA9s(2),bg=color_suited) #,bg='red
buttonA9s.grid(row=1,column=5,sticky = "NSEW")
buttonA8s = tk.Button(mywindow,text='A8',command = lambda: pressA8s(2),bg=color_suited) #,bg='red
buttonA8s.grid(row=1,column=6,sticky = "NSEW")
buttonA7s = tk.Button(mywindow,text='A7',command = lambda: pressA7s(2),bg=color_suited) #,bg='red
buttonA7s.grid(row=1,column=7,sticky = "NSEW")
buttonA6s = tk.Button(mywindow,text='A6',command = lambda: pressA6s(2),bg=color_suited) #,bg='red
buttonA6s.grid(row=1,column=8,sticky = "NSEW")
buttonA5s = tk.Button(mywindow,text='A5',command = lambda: pressA5s(2),bg=color_suited) #,bg='red
buttonA5s.grid(row=1,column=9,sticky = "NSEW")
buttonA4s = tk.Button(mywindow,text='A4',command = lambda: pressA4s(2),bg=color_suited) #,bg='red
buttonA4s.grid(row=1,column=10,sticky = "NSEW")
buttonA3s = tk.Button(mywindow,text='A3',command = lambda: pressA3s(2),bg=color_suited) #,bg='red
buttonA3s.grid(row=1,column=11,sticky = "NSEW")
buttonA2s = tk.Button(mywindow,text='A2',command = lambda: pressA2s(2),bg=color_suited) #,bg='red
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
buttonAKo = tk.Button(mywindow,text='AK',command = lambda: pressAKo(2),bg=color_offsuit)
buttonAKo.grid(row=2,column=0,sticky = "NSEW")
buttonKK = tk.Button(mywindow,text='KK',command = lambda: pressKK(2),bg=color_pp)
buttonKK.grid(row=2,column=1,sticky = "NSEW")

buttonKQs = tk.Button(mywindow,text='KQ',command = lambda: pressKQs(2),bg=color_suited)
buttonKQs.grid(row=2,column=2,sticky = "NSEW")
buttonKJs = tk.Button(mywindow,text='KJ',command = lambda: pressKJs(2),bg=color_suited)
buttonKJs.grid(row=2,column=3,sticky = "NSEW")
buttonKTs = tk.Button(mywindow,text='KT',command = lambda: pressKTs(2),bg=color_suited)
buttonKTs.grid(row=2,column=4,sticky = "NSEW")
buttonK9s = tk.Button(mywindow,text='K9',command = lambda: pressK9s(2),bg=color_suited)
buttonK9s.grid(row=2,column=5,sticky = "NSEW")
buttonK8s = tk.Button(mywindow,text='K8',command = lambda: pressK8s(2),bg=color_suited)
buttonK8s.grid(row=2,column=6,sticky = "NSEW")
buttonK7s = tk.Button(mywindow,text='K7',command = lambda: pressK7s(2),bg=color_suited)
buttonK7s.grid(row=2,column=7,sticky = "NSEW")
buttonK6s = tk.Button(mywindow,text='K6',command = lambda: pressK6s(2),bg=color_suited)
buttonK6s.grid(row=2,column=8,sticky = "NSEW")
buttonK5s = tk.Button(mywindow,text='K5',command = lambda: pressK5s(2),bg=color_suited)
buttonK5s.grid(row=2,column=9,sticky = "NSEW")
buttonK4s = tk.Button(mywindow,text='K4',command = lambda: pressK4s(2),bg=color_suited)
buttonK4s.grid(row=2,column=10,sticky = "NSEW")
buttonK3s = tk.Button(mywindow,text='K3',command = lambda: pressK3s(2),bg=color_suited)
buttonK3s.grid(row=2,column=11,sticky = "NSEW")
buttonK2s = tk.Button(mywindow,text='K2',command = lambda: pressK2s(2),bg=color_suited)
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
buttonAQo = tk.Button(mywindow,text='AQ',command = lambda: pressAQo(2),bg=color_offsuit)
buttonAQo.grid(row=3,column=0,sticky = "NSEW")
buttonKQo = tk.Button(mywindow,text='KQ',command = lambda: pressKQo(2),bg=color_offsuit)
buttonKQo.grid(row=3,column=1,sticky = "NSEW")
buttonQQ = tk.Button(mywindow,text='QQ',command = lambda: pressQQ(2),bg=color_pp)
buttonQQ.grid(row=3,column=2,sticky = "NSEW")

buttonQJs = tk.Button(mywindow,text='QJ',command = lambda: pressQJs(2),bg=color_suited)
buttonQJs.grid(row=3,column=3,sticky = "NSEW")
buttonQTs = tk.Button(mywindow,text='QT',command = lambda: pressQTs(2),bg=color_suited)
buttonQTs.grid(row=3,column=4,sticky = "NSEW")
buttonQ9s = tk.Button(mywindow,text='Q9',command = lambda: pressQ9s(2),bg=color_suited)
buttonQ9s.grid(row=3,column=5,sticky = "NSEW")
buttonQ8s = tk.Button(mywindow,text='Q8',command = lambda: pressQ8s(2),bg=color_suited)
buttonQ8s.grid(row=3,column=6,sticky = "NSEW")
buttonQ7s = tk.Button(mywindow,text='Q7',command = lambda: pressQ7s(2),bg=color_suited)
buttonQ7s.grid(row=3,column=7,sticky = "NSEW")
buttonQ6s = tk.Button(mywindow,text='Q6',command = lambda: pressQ6s(2),bg=color_suited)
buttonQ6s.grid(row=3,column=8,sticky = "NSEW")
buttonQ5s = tk.Button(mywindow,text='Q5',command = lambda: pressQ5s(2),bg=color_suited)
buttonQ5s.grid(row=3,column=9,sticky = "NSEW")
buttonQ4s = tk.Button(mywindow,text='Q4',command = lambda: pressQ4s(2),bg=color_suited)
buttonQ4s.grid(row=3,column=10,sticky = "NSEW")
buttonQ3s = tk.Button(mywindow,text='Q3',command = lambda: pressQ3s(2),bg=color_suited)
buttonQ3s.grid(row=3,column=11,sticky = "NSEW")
buttonQ2s = tk.Button(mywindow,text='Q2',command = lambda: pressQ2s(2),bg=color_suited)
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
buttonAJo = tk.Button(mywindow,text='AJ',command = lambda: pressAJo(2),bg=color_offsuit)
buttonAJo.grid(row=4,column=0,sticky = "NSEW")
buttonKJo = tk.Button(mywindow,text='KJ',command = lambda: pressKJo(2),bg=color_offsuit)
buttonKJo.grid(row=4,column=1,sticky = "NSEW")
buttonQJo = tk.Button(mywindow,text='QJ',command = lambda: pressQJo(2),bg=color_offsuit)
buttonQJo.grid(row=4,column=2,sticky = "NSEW")

buttonJJ = tk.Button(mywindow,text='JJ',command = lambda: pressJJ(2),bg=color_pp)
buttonJJ.grid(row=4,column=3,sticky = "NSEW")
buttonJTs = tk.Button(mywindow,text='JT',command = lambda: pressJTs(2),bg=color_suited)
buttonJTs.grid(row=4,column=4,sticky = "NSEW")
buttonJ9s = tk.Button(mywindow,text='J9',command = lambda: pressJ9s(2),bg=color_suited)
buttonJ9s.grid(row=4,column=5,sticky = "NSEW")
buttonJ8s = tk.Button(mywindow,text='J8',command = lambda: pressJ8s(2),bg=color_suited)
buttonJ8s.grid(row=4,column=6,sticky = "NSEW")
buttonJ7s = tk.Button(mywindow,text='J7',command = lambda: pressJ7s(2),bg=color_suited)
buttonJ7s.grid(row=4,column=7,sticky = "NSEW")
buttonJ6s = tk.Button(mywindow,text='J6',command = lambda: pressJ6s(2),bg=color_suited)
buttonJ6s.grid(row=4,column=8,sticky = "NSEW")
buttonJ5s = tk.Button(mywindow,text='J5',command = lambda: pressJ5s(2),bg=color_suited)
buttonJ5s.grid(row=4,column=9,sticky = "NSEW")
buttonJ4s = tk.Button(mywindow,text='J4',command = lambda: pressJ4s(2),bg=color_suited)
buttonJ4s.grid(row=4,column=10,sticky = "NSEW")
buttonJ3s = tk.Button(mywindow,text='J3',command = lambda: pressJ3s(2),bg=color_suited)
buttonJ3s.grid(row=4,column=11,sticky = "NSEW")
buttonJ2s = tk.Button(mywindow,text='J2',command = lambda: pressJ2s(2),bg=color_suited)
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

buttonATo = tk.Button(mywindow,text='AT',command = lambda: pressATo(2),bg=color_offsuit)
buttonATo.grid(row=5,column=0,sticky = "NSEW")
buttonKTo = tk.Button(mywindow,text='KT',command = lambda: pressKTo(2),bg=color_offsuit)
buttonKTo.grid(row=5,column=1,sticky = "NSEW")
buttonQTo = tk.Button(mywindow,text='QT',command = lambda: pressQTo(2),bg=color_offsuit)
buttonQTo.grid(row=5,column=2,sticky = "NSEW")
buttonJTo = tk.Button(mywindow,text='JT',command = lambda: pressJTo(2),bg=color_offsuit)
buttonJTo.grid(row=5,column=3,sticky = "NSEW")
buttonTT = tk.Button(mywindow,text='TT',command = lambda: pressTT(2),bg=color_pp)
buttonTT.grid(row=5,column=4,sticky = "NSEW")
buttonT9s = tk.Button(mywindow,text='T9',command = lambda: pressT9s(2),bg=color_suited)
buttonT9s.grid(row=5,column=5,sticky = "NSEW")
buttonT8s = tk.Button(mywindow,text='T8',command = lambda: pressT8s(2),bg=color_suited)
buttonT8s.grid(row=5,column=6,sticky = "NSEW")
buttonT7s = tk.Button(mywindow,text='T7',command = lambda: pressT7s(2),bg=color_suited)
buttonT7s.grid(row=5,column=7,sticky = "NSEW")
buttonT6s = tk.Button(mywindow,text='T6',command = lambda: pressT6s(2),bg=color_suited)
buttonT6s.grid(row=5,column=8,sticky = "NSEW")
buttonT5s = tk.Button(mywindow,text='T5',command = lambda: pressT5s(2),bg=color_suited)
buttonT5s.grid(row=5,column=9,sticky = "NSEW")
buttonT4s = tk.Button(mywindow,text='T4',command = lambda: pressT4s(2),bg=color_suited)
buttonT4s.grid(row=5,column=10,sticky = "NSEW")
buttonT3s = tk.Button(mywindow,text='T3',command = lambda: pressT3s(2),bg=color_suited)
buttonT3s.grid(row=5,column=11,sticky = "NSEW")
buttonT2s = tk.Button(mywindow,text='T2',command = lambda: pressT2s(2),bg=color_suited)
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

buttonA9o = tk.Button(mywindow,text='A9',command = lambda: pressA9o(2),bg=color_offsuit)
buttonA9o.grid(row=6,column=0,sticky = "NSEW")
buttonK9o = tk.Button(mywindow,text='K9',command = lambda: pressK9o(2),bg=color_offsuit)
buttonK9o.grid(row=6,column=1,sticky = "NSEW")
buttonQ9o = tk.Button(mywindow,text='Q9',command = lambda: pressQ9o(2),bg=color_offsuit)
buttonQ9o.grid(row=6,column=2,sticky = "NSEW")
buttonJ9o = tk.Button(mywindow,text='J9',command = lambda: pressJ9o(2),bg=color_offsuit)
buttonJ9o.grid(row=6,column=3,sticky = "NSEW")
buttonT9o = tk.Button(mywindow,text='T9',command = lambda: pressT9o(2),bg=color_offsuit)
buttonT9o.grid(row=6,column=4,sticky = "NSEW")
button99 = tk.Button(mywindow,text='99',command = lambda: press99(2),bg=color_pp)
button99.grid(row=6,column=5,sticky = "NSEW")
button98s = tk.Button(mywindow,text='98',command = lambda: press98s(2),bg=color_suited)
button98s.grid(row=6,column=6,sticky = "NSEW")
button97s = tk.Button(mywindow,text='97',command = lambda: press97s(2),bg=color_suited)
button97s.grid(row=6,column=7,sticky = "NSEW")
button96s = tk.Button(mywindow,text='96',command = lambda: press96s(2),bg=color_suited)
button96s.grid(row=6,column=8,sticky = "NSEW")
button95s = tk.Button(mywindow,text='95',command = lambda: press95s(2),bg=color_suited)
button95s.grid(row=6,column=9,sticky = "NSEW")
button94s = tk.Button(mywindow,text='94',command = lambda: press94s(2),bg=color_suited)
button94s.grid(row=6,column=10,sticky = "NSEW")
button93s = tk.Button(mywindow,text='93',command = lambda: press93s(2),bg=color_suited)
button93s.grid(row=6,column=11,sticky = "NSEW")
button92s = tk.Button(mywindow,text='92',command = lambda: press92s(2),bg=color_suited)
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

buttonA8o = tk.Button(mywindow,text='A8',command = lambda: pressA8o(2),bg=color_offsuit)
buttonA8o.grid(row=7,column=0,sticky = "NSEW")
buttonK8o = tk.Button(mywindow,text='K8',command = lambda: pressK8o(2),bg=color_offsuit)
buttonK8o.grid(row=7,column=1,sticky = "NSEW")
buttonQ8o = tk.Button(mywindow,text='Q8',command = lambda: pressQ8o(2),bg=color_offsuit)
buttonQ8o.grid(row=7,column=2,sticky = "NSEW")
buttonJ8o = tk.Button(mywindow,text='J8',command = lambda: pressJ8o(2),bg=color_offsuit)
buttonJ8o.grid(row=7,column=3,sticky = "NSEW")
buttonT8o = tk.Button(mywindow,text='T8',command = lambda: pressT8o(2),bg=color_offsuit)
buttonT8o.grid(row=7,column=4,sticky = "NSEW")
button98o = tk.Button(mywindow,text='98',command = lambda: press98o(2),bg=color_offsuit)
button98o.grid(row=7,column=5,sticky = "NSEW")
button88 = tk.Button(mywindow,text='88',command = lambda: press88(2),bg=color_pp)
button88.grid(row=7,column=6,sticky = "NSEW")
button87s = tk.Button(mywindow,text='87',command = lambda: press87s(2),bg=color_suited)
button87s.grid(row=7,column=7,sticky = "NSEW")
button86s = tk.Button(mywindow,text='86',command = lambda: press86s(2),bg=color_suited)
button86s.grid(row=7,column=8,sticky = "NSEW")
button85s = tk.Button(mywindow,text='85',command = lambda: press85s(2),bg=color_suited)
button85s.grid(row=7,column=9,sticky = "NSEW")
button84s = tk.Button(mywindow,text='84',command = lambda: press84s(2),bg=color_suited)
button84s.grid(row=7,column=10,sticky = "NSEW")
button83s = tk.Button(mywindow,text='83',command = lambda: press83s(2),bg=color_suited)
button83s.grid(row=7,column=11,sticky = "NSEW")
button82s = tk.Button(mywindow,text='82',command = lambda: press82s(2),bg=color_suited)
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

buttonA7o = tk.Button(mywindow,text='A7',command = lambda: pressA7o(2),bg=color_offsuit)
buttonA7o.grid(row=8,column=0,sticky = "NSEW")
buttonK7o = tk.Button(mywindow,text='K7',command = lambda: pressK7o(2),bg=color_offsuit)
buttonK7o.grid(row=8,column=1,sticky = "NSEW")
buttonQ7o = tk.Button(mywindow,text='Q7',command = lambda: pressQ7o(2),bg=color_offsuit)
buttonQ7o.grid(row=8,column=2,sticky = "NSEW")
buttonJ7o = tk.Button(mywindow,text='J7',command = lambda: pressJ7o(2),bg=color_offsuit)
buttonJ7o.grid(row=8,column=3,sticky = "NSEW")
buttonT7o = tk.Button(mywindow,text='T7',command = lambda: pressT7o(2),bg=color_offsuit)
buttonT7o.grid(row=8,column=4,sticky = "NSEW")
button97o = tk.Button(mywindow,text='97',command = lambda: press97o(2),bg=color_offsuit)
button97o.grid(row=8,column=5,sticky = "NSEW")
button87o = tk.Button(mywindow,text='87',command = lambda: press87o(2),bg=color_offsuit)
button87o.grid(row=8,column=6,sticky = "NSEW")
button77 = tk.Button(mywindow,text='77',command = lambda: press77(2),bg=color_pp)
button77.grid(row=8,column=7,sticky = "NSEW")
button76s = tk.Button(mywindow,text='76',command = lambda: press76s(2),bg=color_suited)
button76s.grid(row=8,column=8,sticky = "NSEW")
button75s = tk.Button(mywindow,text='75',command = lambda: press75s(2),bg=color_suited)
button75s.grid(row=8,column=9,sticky = "NSEW")
button74s = tk.Button(mywindow,text='74',command = lambda: press74s(2),bg=color_suited)
button74s.grid(row=8,column=10,sticky = "NSEW")
button73s = tk.Button(mywindow,text='73',command = lambda: press73s(2),bg=color_suited)
button73s.grid(row=8,column=11,sticky = "NSEW")
button72s = tk.Button(mywindow,text='72',command = lambda: press72s(2),bg=color_suited)
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

buttonA6o = tk.Button(mywindow,text='A6',command = lambda: pressA6o(2),bg=color_offsuit)
buttonA6o.grid(row=9,column=0,sticky = "NSEW")
buttonK6o = tk.Button(mywindow,text='K6',command = lambda: pressK6o(2),bg=color_offsuit)
buttonK6o.grid(row=9,column=1,sticky = "NSEW")
buttonQ6o = tk.Button(mywindow,text='Q6',command = lambda: pressQ6o(2),bg=color_offsuit)
buttonQ6o.grid(row=9,column=2,sticky = "NSEW")
buttonJ6o = tk.Button(mywindow,text='J6',command = lambda: pressJ6o(2),bg=color_offsuit)
buttonJ6o.grid(row=9,column=3,sticky = "NSEW")
buttonT6o = tk.Button(mywindow,text='T6',command = lambda: pressT6o(2),bg=color_offsuit)
buttonT6o.grid(row=9,column=4,sticky = "NSEW")
button96o = tk.Button(mywindow,text='96',command = lambda: press96o(2),bg=color_offsuit)
button96o.grid(row=9,column=5,sticky = "NSEW")
button86o = tk.Button(mywindow,text='86',command = lambda: press86o(2),bg=color_offsuit)
button86o.grid(row=9,column=6,sticky = "NSEW")
button76o = tk.Button(mywindow,text='76',command = lambda: press76o(2),bg=color_offsuit)
button76o.grid(row=9,column=7,sticky = "NSEW")
button66 = tk.Button(mywindow,text='66',command = lambda: press66(2),bg=color_pp)
button66.grid(row=9,column=8,sticky = "NSEW")
button65s = tk.Button(mywindow,text='65',command = lambda: press65s(2),bg=color_suited)
button65s.grid(row=9,column=9,sticky = "NSEW")
button64s = tk.Button(mywindow,text='64',command = lambda: press64s(2),bg=color_suited)
button64s.grid(row=9,column=10,sticky = "NSEW")
button63s = tk.Button(mywindow,text='63',command = lambda: press63s(2),bg=color_suited)
button63s.grid(row=9,column=11,sticky = "NSEW")
button62s = tk.Button(mywindow,text='62',command = lambda: press62s(2),bg=color_suited)
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

buttonA5o = tk.Button(mywindow,text='A5',command = lambda: pressA5o(2),bg=color_offsuit)
buttonA5o.grid(row=10,column=0,sticky = "NSEW")
buttonK5o = tk.Button(mywindow,text='K5',command = lambda: pressK5o(2),bg=color_offsuit)
buttonK5o.grid(row=10,column=1,sticky = "NSEW")
buttonQ5o = tk.Button(mywindow,text='Q5',command = lambda: pressQ5o(2),bg=color_offsuit)
buttonQ5o.grid(row=10,column=2,sticky = "NSEW")
buttonJ5o = tk.Button(mywindow,text='J5',command = lambda: pressJ5o(2),bg=color_offsuit)
buttonJ5o.grid(row=10,column=3,sticky = "NSEW")
buttonT5o = tk.Button(mywindow,text='T5',command = lambda: pressT5o(2),bg=color_offsuit)
buttonT5o.grid(row=10,column=4,sticky = "NSEW")
button95o = tk.Button(mywindow,text='95',command = lambda: press95o(2),bg=color_offsuit)
button95o.grid(row=10,column=5,sticky = "NSEW")
button85o = tk.Button(mywindow,text='85',command = lambda: press85o(2),bg=color_offsuit)
button85o.grid(row=10,column=6,sticky = "NSEW")
button75o = tk.Button(mywindow,text='75',command = lambda: press75o(2),bg=color_offsuit)
button75o.grid(row=10,column=7,sticky = "NSEW")
button65o = tk.Button(mywindow,text='65',command = lambda: press65o(2),bg=color_offsuit)
button65o.grid(row=10,column=8,sticky = "NSEW")
button55 = tk.Button(mywindow,text='55',command = lambda: press55(2),bg=color_pp)
button55.grid(row=10,column=9,sticky = "NSEW")
button54s = tk.Button(mywindow,text='54',command = lambda: press54s(2),bg=color_suited)
button54s.grid(row=10,column=10,sticky = "NSEW")
button53s = tk.Button(mywindow,text='53',command = lambda: press53s(2),bg=color_suited)
button53s.grid(row=10,column=11,sticky = "NSEW")
button52s = tk.Button(mywindow,text='52',command = lambda: press52s(2),bg=color_suited)
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

buttonA4o = tk.Button(mywindow,text='A4',command = lambda: pressA4o(2),bg=color_offsuit)
buttonA4o.grid(row=11,column=0,sticky = "NSEW")
buttonK4o = tk.Button(mywindow,text='K4',command = lambda: pressK4o(2),bg=color_offsuit)
buttonK4o.grid(row=11,column=1,sticky = "NSEW")
buttonQ4o = tk.Button(mywindow,text='Q4',command = lambda: pressQ4o(2),bg=color_offsuit)
buttonQ4o.grid(row=11,column=2,sticky = "NSEW")
buttonJ4o = tk.Button(mywindow,text='J4',command = lambda: pressJ4o(2),bg=color_offsuit)
buttonJ4o.grid(row=11,column=3,sticky = "NSEW")
buttonT4o = tk.Button(mywindow,text='T4',command = lambda: pressT4o(2),bg=color_offsuit)
buttonT4o.grid(row=11,column=4,sticky = "NSEW")
button94o = tk.Button(mywindow,text='94',command = lambda: press94o(2),bg=color_offsuit)
button94o.grid(row=11,column=5,sticky = "NSEW")
button84o = tk.Button(mywindow,text='84',command = lambda: press84o(2),bg=color_offsuit)
button84o.grid(row=11,column=6,sticky = "NSEW")
button74o = tk.Button(mywindow,text='74',command = lambda: press74o(2),bg=color_offsuit)
button74o.grid(row=11,column=7,sticky = "NSEW")
button64o = tk.Button(mywindow,text='64',command = lambda: press64o(2),bg=color_offsuit)
button64o.grid(row=11,column=8,sticky = "NSEW")
button54o = tk.Button(mywindow,text='54',command = lambda: press54o(2),bg=color_offsuit)
button54o.grid(row=11,column=9,sticky = "NSEW")
button44 = tk.Button(mywindow,text='44',command = lambda: press44(2),bg=color_pp)
button44.grid(row=11,column=10,sticky = "NSEW")
button43s = tk.Button(mywindow,text='43',command = lambda: press43s(2),bg=color_suited)
button43s.grid(row=11,column=11,sticky = "NSEW")
button42s = tk.Button(mywindow,text='42',command = lambda: press42s(2),bg=color_suited)
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

buttonA3o = tk.Button(mywindow,text='A3',command = lambda: pressA3o(2),bg=color_offsuit)
buttonA3o.grid(row=12,column=0,sticky = "NSEW")
buttonK3o = tk.Button(mywindow,text='K3',command = lambda: pressK3o(2),bg=color_offsuit)
buttonK3o.grid(row=12,column=1,sticky = "NSEW")
buttonQ3o = tk.Button(mywindow,text='Q3',command = lambda: pressQ3o(2),bg=color_offsuit)
buttonQ3o.grid(row=12,column=2,sticky = "NSEW")
buttonJ3o = tk.Button(mywindow,text='J3',command = lambda: pressJ3o(2),bg=color_offsuit)
buttonJ3o.grid(row=12,column=3,sticky = "NSEW")
buttonT3o = tk.Button(mywindow,text='T3',command = lambda: pressT3o(2),bg=color_offsuit)
buttonT3o.grid(row=12,column=4,sticky = "NSEW")
button93o = tk.Button(mywindow,text='93',command = lambda: press93o(2),bg=color_offsuit)
button93o.grid(row=12,column=5,sticky = "NSEW")
button83o = tk.Button(mywindow,text='83',command = lambda: press83o(2),bg=color_offsuit)
button83o.grid(row=12,column=6,sticky = "NSEW")
button73o = tk.Button(mywindow,text='73',command = lambda: press73o(2),bg=color_offsuit)
button73o.grid(row=12,column=7,sticky = "NSEW")
button63o = tk.Button(mywindow,text='63',command = lambda: press63o(2),bg=color_offsuit)
button63o.grid(row=12,column=8,sticky = "NSEW")
button53o = tk.Button(mywindow,text='53',command = lambda: press53o(2),bg=color_offsuit)
button53o.grid(row=12,column=9,sticky = "NSEW")
button43o = tk.Button(mywindow,text='43',command = lambda: press43o(2),bg=color_offsuit)
button43o.grid(row=12,column=10,sticky = "NSEW")
button33 = tk.Button(mywindow,text='33',command = lambda: press33(2),bg=color_pp)
button33.grid(row=12,column=11,sticky = "NSEW")
button32s = tk.Button(mywindow,text='32',command = lambda: press32s(2),bg=color_suited)
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

buttonA2o = tk.Button(mywindow,text='A2',command = lambda: pressA2o(2),bg=color_offsuit)
buttonA2o.grid(row=13,column=0,sticky = "NSEW")
buttonK2o = tk.Button(mywindow,text='K2',command = lambda: pressK2o(2),bg=color_offsuit)
buttonK2o.grid(row=13,column=1,sticky = "NSEW")
buttonQ2o = tk.Button(mywindow,text='Q2',command = lambda: pressQ2o(2),bg=color_offsuit)
buttonQ2o.grid(row=13,column=2,sticky = "NSEW")
buttonJ2o = tk.Button(mywindow,text='J2',command = lambda: pressJ2o(2),bg=color_offsuit)
buttonJ2o.grid(row=13,column=3,sticky = "NSEW")
buttonT2o = tk.Button(mywindow,text='T2',command = lambda: pressT2o(2),bg=color_offsuit)
buttonT2o.grid(row=13,column=4,sticky = "NSEW")
button92o = tk.Button(mywindow,text='92',command = lambda: press92o(2),bg=color_offsuit)
button92o.grid(row=13,column=5,sticky = "NSEW")
button82o = tk.Button(mywindow,text='82',command = lambda: press82o(2),bg=color_offsuit)
button82o.grid(row=13,column=6,sticky = "NSEW")
button72o = tk.Button(mywindow,text='72',command = lambda: press72o(2),bg=color_offsuit)
button72o.grid(row=13,column=7,sticky = "NSEW")
button62o = tk.Button(mywindow,text='62',command = lambda: press62o(2),bg=color_offsuit)
button62o.grid(row=13,column=8,sticky = "NSEW")
button52o = tk.Button(mywindow,text='52',command = lambda: press52o(2),bg=color_offsuit)
button52o.grid(row=13,column=9,sticky = "NSEW")
button42o = tk.Button(mywindow,text='42',command = lambda: press42o(2),bg=color_offsuit)
button42o.grid(row=13,column=10,sticky = "NSEW")
button32o = tk.Button(mywindow,text='32',command = lambda: press32o(2),bg=color_offsuit)
button32o.grid(row=13,column=11,sticky = "NSEW")
button22 = tk.Button(mywindow,text='22',command = lambda: press22(2),bg=color_pp)
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
Slider = (tk.Scale(mywindow,variable=0,orient="horizontal", length=220))
SliderButton = (tk.Button(mywindow,text='Set',command=slideValueSet))
Slider.grid(row=15,column=0, columnspan=12)
SliderButton.grid(row=15,column=13)


mywindow.mainloop()