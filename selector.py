import tkinter as tk

mywindow = tk.Tk()
mywindow.geometry("469x339")

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
    print("Button Pressed!!")
    #Slider.set(0)
    open_secondary_window()
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
        open_secondary_window()

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

def pressJJ():
    print("JJ")

def pressTT():
    print("TT")

def press99():
    print("99")

def press88():
    print("88")

def press77():
    print("77")

def press66():
    print("66")

def press55():
    print("55")

def press44():
    print("44")

def press33():
    print("33")

def press22():
    print("22")

#pocket suited handlers
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

#offsuited handlers
def pressAKo():
    print("AKo")
    if 'AKo' in selected_range:
        buttonAKo.config(bg = color_offsuit)
        selected_range.remove('AKo')
    else:
        buttonAKo.config(bg = color_offsuit_selected)
        selected_range.append('AKo') 

'''
def textBox():
    print(textb.get())
    
def slideValue():
    print (Slider.get())
'''


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
buttonATs = tk.Button(mywindow,text='AT',command=buttonPress,bg=color_suited) #,bg='red
buttonATs.grid(row=1,column=4,sticky = "NSEW")
buttonA9s = tk.Button(mywindow,text='A9',command=buttonPress,bg=color_suited) #,bg='red
buttonA9s.grid(row=1,column=5,sticky = "NSEW")
buttonA8s = tk.Button(mywindow,text='A8',command=buttonPress,bg=color_suited) #,bg='red
buttonA8s.grid(row=1,column=6,sticky = "NSEW")
buttonA7s = tk.Button(mywindow,text='A7',command=buttonPress,bg=color_suited) #,bg='red
buttonA7s.grid(row=1,column=7,sticky = "NSEW")
buttonA6s = tk.Button(mywindow,text='A6',command=buttonPress,bg=color_suited) #,bg='red
buttonA6s.grid(row=1,column=8,sticky = "NSEW")
buttonA5s = tk.Button(mywindow,text='A5',command=buttonPress,bg=color_suited) #,bg='red
buttonA5s.grid(row=1,column=9,sticky = "NSEW")
buttonA4s = tk.Button(mywindow,text='A4',command=buttonPress,bg=color_suited) #,bg='red
buttonA4s.grid(row=1,column=10,sticky = "NSEW")
buttonA3s = tk.Button(mywindow,text='A3',command=buttonPress,bg=color_suited) #,bg='red
buttonA3s.grid(row=1,column=11,sticky = "NSEW")
buttonA2s = tk.Button(mywindow,text='A2',command=buttonPress,bg=color_suited) #,bg='red
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

buttonKQs = tk.Button(mywindow,text='KQ',command=buttonPress,bg=color_suited) #,bg='red
buttonKQs.grid(row=2,column=2,sticky = "NSEW")
buttonKJs = tk.Button(mywindow,text='KJ',command=buttonPress,bg=color_suited) #,bg='red
buttonKJs.grid(row=2,column=3,sticky = "NSEW")
buttonKTs = tk.Button(mywindow,text='KT',command=buttonPress,bg=color_suited) #,bg='red
buttonKTs.grid(row=2,column=4,sticky = "NSEW")
buttonK9s = tk.Button(mywindow,text='K9',command=buttonPress,bg=color_suited) #,bg='red
buttonK9s.grid(row=2,column=5,sticky = "NSEW")
buttonK8s = tk.Button(mywindow,text='K8',command=buttonPress,bg=color_suited) #,bg='red
buttonK8s.grid(row=2,column=6,sticky = "NSEW")
buttonK7s = tk.Button(mywindow,text='K7',command=buttonPress,bg=color_suited) #,bg='red
buttonK7s.grid(row=2,column=7,sticky = "NSEW")
buttonK6s = tk.Button(mywindow,text='K6',command=buttonPress,bg=color_suited) #,bg='red
buttonK6s.grid(row=2,column=8,sticky = "NSEW")
buttonK5s = tk.Button(mywindow,text='K5',command=buttonPress,bg=color_suited) #,bg='red
buttonK5s.grid(row=2,column=9,sticky = "NSEW")
buttonK4s = tk.Button(mywindow,text='K4',command=buttonPress,bg=color_suited) #,bg='red
buttonK4s.grid(row=2,column=10,sticky = "NSEW")
buttonK3s = tk.Button(mywindow,text='K3',command=buttonPress,bg=color_suited) #,bg='red
buttonK3s.grid(row=2,column=11,sticky = "NSEW")
buttonK2s = tk.Button(mywindow,text='K2',command=buttonPress,bg=color_suited) #,bg='red
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
buttonAQo = tk.Button(mywindow,text='AQ',command=buttonPress,bg=color_offsuit)
buttonAQo.grid(row=3,column=0,sticky = "NSEW")
buttonKQo = tk.Button(mywindow,text='KQ',command=buttonPress,bg=color_offsuit)
buttonKQo.grid(row=3,column=1,sticky = "NSEW")
buttonQQ = tk.Button(mywindow,text='QQ',command=pressQQ,bg=color_pp)
buttonQQ.grid(row=3,column=2,sticky = "NSEW")

buttonQJs = tk.Button(mywindow,text='QJ',command=buttonPress,bg=color_suited) #,bg='red
buttonQJs.grid(row=3,column=3,sticky = "NSEW")
buttonQTs = tk.Button(mywindow,text='QT',command=buttonPress,bg=color_suited) #,bg='red
buttonQTs.grid(row=3,column=4,sticky = "NSEW")
buttonQ9s = tk.Button(mywindow,text='Q9',command=buttonPress,bg=color_suited) #,bg='red
buttonQ9s.grid(row=3,column=5,sticky = "NSEW")
buttonQ8s = tk.Button(mywindow,text='Q8',command=buttonPress,bg=color_suited) #,bg='red
buttonQ8s.grid(row=3,column=6,sticky = "NSEW")
buttonQ7s = tk.Button(mywindow,text='Q7',command=buttonPress,bg=color_suited) #,bg='red
buttonQ7s.grid(row=3,column=7,sticky = "NSEW")
buttonQ6s = tk.Button(mywindow,text='Q6',command=buttonPress,bg=color_suited) #,bg='red
buttonQ6s.grid(row=3,column=8,sticky = "NSEW")
buttonQ5s = tk.Button(mywindow,text='Q5',command=buttonPress,bg=color_suited) #,bg='red
buttonQ5s.grid(row=3,column=9,sticky = "NSEW")
buttonQ4s = tk.Button(mywindow,text='Q4',command=buttonPress,bg=color_suited) #,bg='red
buttonQ4s.grid(row=3,column=10,sticky = "NSEW")
buttonQ3s = tk.Button(mywindow,text='Q3',command=buttonPress,bg=color_suited) #,bg='red
buttonQ3s.grid(row=3,column=11,sticky = "NSEW")
buttonQ2s = tk.Button(mywindow,text='Q2',command=buttonPress,bg=color_suited) #,bg='red
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
buttonAJo = tk.Button(mywindow,text='AJ',command=buttonPress,bg=color_offsuit)
buttonAJo.grid(row=4,column=0,sticky = "NSEW")
buttonKJo = tk.Button(mywindow,text='KJ',command=buttonPress,bg=color_offsuit)
buttonKJo.grid(row=4,column=1,sticky = "NSEW")
buttonQJo = tk.Button(mywindow,text='QJ',command=buttonPress,bg=color_offsuit)
buttonQJo.grid(row=4,column=2,sticky = "NSEW")

buttonJJ = tk.Button(mywindow,text='JJ',command=pressJJ,bg=color_pp) #,bg='red
buttonJJ.grid(row=4,column=3,sticky = "NSEW")
buttonJTs = tk.Button(mywindow,text='JT',command=buttonPress,bg=color_suited) #,bg='red
buttonJTs.grid(row=4,column=4,sticky = "NSEW")
buttonJ9s = tk.Button(mywindow,text='J9',command=buttonPress,bg=color_suited) #,bg='red
buttonJ9s.grid(row=4,column=5,sticky = "NSEW")
buttonJ8s = tk.Button(mywindow,text='J8',command=buttonPress,bg=color_suited) #,bg='red
buttonJ8s.grid(row=4,column=6,sticky = "NSEW")
buttonJ7s = tk.Button(mywindow,text='J7',command=buttonPress,bg=color_suited) #,bg='red
buttonJ7s.grid(row=4,column=7,sticky = "NSEW")
buttonJ6s = tk.Button(mywindow,text='J6',command=buttonPress,bg=color_suited) #,bg='red
buttonJ6s.grid(row=4,column=8,sticky = "NSEW")
buttonJ5s = tk.Button(mywindow,text='J5',command=buttonPress,bg=color_suited) #,bg='red
buttonJ5s.grid(row=4,column=9,sticky = "NSEW")
buttonJ4s = tk.Button(mywindow,text='J4',command=buttonPress,bg=color_suited) #,bg='red
buttonJ4s.grid(row=4,column=10,sticky = "NSEW")
buttonJ3s = tk.Button(mywindow,text='J3',command=buttonPress,bg=color_suited) #,bg='red
buttonJ3s.grid(row=4,column=11,sticky = "NSEW")
buttonJ2s = tk.Button(mywindow,text='J2',command=buttonPress,bg=color_suited) #,bg='red
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

buttonATo = tk.Button(mywindow,text='AT',command=buttonPress,bg=color_offsuit)
buttonATo.grid(row=5,column=0,sticky = "NSEW")
buttonKTo = tk.Button(mywindow,text='KT',command=buttonPress,bg=color_offsuit)
buttonKTo.grid(row=5,column=1,sticky = "NSEW")
buttonQTo = tk.Button(mywindow,text='QT',command=buttonPress,bg=color_offsuit)
buttonQTo.grid(row=5,column=2,sticky = "NSEW")
buttonJTo = tk.Button(mywindow,text='JT',command=buttonPress,bg=color_offsuit) #,bg='red
buttonJTo.grid(row=5,column=3,sticky = "NSEW")
buttonTT = tk.Button(mywindow,text='TT',command=pressTT,bg=color_pp) #,bg='red
buttonTT.grid(row=5,column=4,sticky = "NSEW")
buttonT9s = tk.Button(mywindow,text='T9',command=buttonPress,bg=color_suited) #,bg='red
buttonT9s.grid(row=5,column=5,sticky = "NSEW")
buttonT8s = tk.Button(mywindow,text='T8',command=buttonPress,bg=color_suited) #,bg='red
buttonT8s.grid(row=5,column=6,sticky = "NSEW")
buttonT7s = tk.Button(mywindow,text='T7',command=buttonPress,bg=color_suited) #,bg='red
buttonT7s.grid(row=5,column=7,sticky = "NSEW")
buttonT6s = tk.Button(mywindow,text='T6',command=buttonPress,bg=color_suited) #,bg='red
buttonT6s.grid(row=5,column=8,sticky = "NSEW")
buttonT5s = tk.Button(mywindow,text='T5',command=buttonPress,bg=color_suited) #,bg='red
buttonT5s.grid(row=5,column=9,sticky = "NSEW")
buttonT4s = tk.Button(mywindow,text='T4',command=buttonPress,bg=color_suited) #,bg='red
buttonT4s.grid(row=5,column=10,sticky = "NSEW")
buttonT3s = tk.Button(mywindow,text='T3',command=buttonPress,bg=color_suited) #,bg='red
buttonT3s.grid(row=5,column=11,sticky = "NSEW")
buttonT2s = tk.Button(mywindow,text='T2',command=buttonPress,bg=color_suited) #,bg='red
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

buttonA9o = tk.Button(mywindow,text='A9',command=buttonPress,bg=color_offsuit)
buttonA9o.grid(row=6,column=0,sticky = "NSEW")
buttonK9o = tk.Button(mywindow,text='K9',command=buttonPress,bg=color_offsuit)
buttonK9o.grid(row=6,column=1,sticky = "NSEW")
buttonQ9o = tk.Button(mywindow,text='Q9',command=buttonPress,bg=color_offsuit)
buttonQ9o.grid(row=6,column=2,sticky = "NSEW")
buttonJ9o = tk.Button(mywindow,text='J9',command=buttonPress,bg=color_offsuit) #,bg='red
buttonJ9o.grid(row=6,column=3,sticky = "NSEW")
buttonT9o = tk.Button(mywindow,text='T9',command=buttonPress,bg=color_offsuit) #,bg='red
buttonT9o.grid(row=6,column=4,sticky = "NSEW")
button99 = tk.Button(mywindow,text='99',command=press99,bg=color_pp) #,bg='red
button99.grid(row=6,column=5,sticky = "NSEW")
button98s = tk.Button(mywindow,text='98',command=buttonPress,bg=color_suited) #,bg='red
button98s.grid(row=6,column=6,sticky = "NSEW")
button97s = tk.Button(mywindow,text='97',command=buttonPress,bg=color_suited) #,bg='red
button97s.grid(row=6,column=7,sticky = "NSEW")
button96s = tk.Button(mywindow,text='96',command=buttonPress,bg=color_suited) #,bg='red
button96s.grid(row=6,column=8,sticky = "NSEW")
button95s = tk.Button(mywindow,text='95',command=buttonPress,bg=color_suited) #,bg='red
button95s.grid(row=6,column=9,sticky = "NSEW")
button94s = tk.Button(mywindow,text='94',command=buttonPress,bg=color_suited) #,bg='red
button94s.grid(row=6,column=10,sticky = "NSEW")
button93s = tk.Button(mywindow,text='93',command=buttonPress,bg=color_suited) #,bg='red
button93s.grid(row=6,column=11,sticky = "NSEW")
button92s = tk.Button(mywindow,text='92',command=buttonPress,bg=color_suited) #,bg='red
button92s.grid(row=6,column=12,padx=(0,15))

#row=7

buttonA8o = tk.Button(mywindow,text='A8',command=buttonPress,bg=color_offsuit)
buttonA8o.grid(row=7,column=0,sticky = "NSEW")
buttonK8o = tk.Button(mywindow,text='K8',command=buttonPress,bg=color_offsuit)
buttonK8o.grid(row=7,column=1,sticky = "NSEW")
buttonQ8o = tk.Button(mywindow,text='Q8',command=buttonPress,bg=color_offsuit)
buttonQ8o.grid(row=7,column=2,sticky = "NSEW")
buttonJ8o = tk.Button(mywindow,text='J8',command=buttonPress,bg=color_offsuit) #,bg='red
buttonJ8o.grid(row=7,column=3,sticky = "NSEW")
buttonT8o = tk.Button(mywindow,text='T8',command=buttonPress,bg=color_offsuit) #,bg='red
buttonT8o.grid(row=7,column=4,sticky = "NSEW")
button98o = tk.Button(mywindow,text='98',command=buttonPress,bg=color_offsuit) #,bg='red
button98o.grid(row=7,column=5,sticky = "NSEW")
button88 = tk.Button(mywindow,text='88',command=press88,bg=color_pp) #,bg='red
button88.grid(row=7,column=6,sticky = "NSEW")
button87s = tk.Button(mywindow,text='87',command=buttonPress,bg=color_suited) #,bg='red
button87s.grid(row=7,column=7,sticky = "NSEW")
button86s = tk.Button(mywindow,text='86',command=buttonPress,bg=color_suited) #,bg='red
button86s.grid(row=7,column=8,sticky = "NSEW")
button85s = tk.Button(mywindow,text='85',command=buttonPress,bg=color_suited) #,bg='red
button85s.grid(row=7,column=9,sticky = "NSEW")
button84s = tk.Button(mywindow,text='84',command=buttonPress,bg=color_suited) #,bg='red
button84s.grid(row=7,column=10,sticky = "NSEW")
button83s = tk.Button(mywindow,text='83',command=buttonPress,bg=color_suited) #,bg='red
button83s.grid(row=7,column=11,sticky = "NSEW")
button82s = tk.Button(mywindow,text='82',command=buttonPress,bg=color_suited) #,bg='red
button82s.grid(row=7,column=12,padx=(0,15))

#row=8

buttonA7o = tk.Button(mywindow,text='A7',command=buttonPress,bg=color_offsuit)
buttonA7o.grid(row=8,column=0,sticky = "NSEW")
buttonK7o = tk.Button(mywindow,text='K7',command=buttonPress,bg=color_offsuit)
buttonK7o.grid(row=8,column=1,sticky = "NSEW")
buttonQ7o = tk.Button(mywindow,text='Q7',command=buttonPress,bg=color_offsuit)
buttonQ7o.grid(row=8,column=2,sticky = "NSEW")
buttonJ7o = tk.Button(mywindow,text='J7',command=buttonPress,bg=color_offsuit) #,bg='red
buttonJ7o.grid(row=8,column=3,sticky = "NSEW")
buttonT7o = tk.Button(mywindow,text='T7',command=buttonPress,bg=color_offsuit) #,bg='red
buttonT7o.grid(row=8,column=4,sticky = "NSEW")
button97o = tk.Button(mywindow,text='97',command=buttonPress,bg=color_offsuit) #,bg='red
button97o.grid(row=8,column=5,sticky = "NSEW")
button87o = tk.Button(mywindow,text='87',command=buttonPress,bg=color_offsuit) #,bg='red
button87o.grid(row=8,column=6,sticky = "NSEW")
button77 = tk.Button(mywindow,text='77',command=press77,bg=color_pp) #,bg='red
button77.grid(row=8,column=7,sticky = "NSEW")
button76s = tk.Button(mywindow,text='76',command=buttonPress,bg=color_suited) #,bg='red
button76s.grid(row=8,column=8,sticky = "NSEW")
button75s = tk.Button(mywindow,text='75',command=buttonPress,bg=color_suited) #,bg='red
button75s.grid(row=8,column=9,sticky = "NSEW")
button74s = tk.Button(mywindow,text='74',command=buttonPress,bg=color_suited) #,bg='red
button74s.grid(row=8,column=10,sticky = "NSEW")
button73s = tk.Button(mywindow,text='73',command=buttonPress,bg=color_suited) #,bg='red
button73s.grid(row=8,column=11,sticky = "NSEW")
button72s = tk.Button(mywindow,text='72',command=buttonPress,bg=color_suited) #,bg='red
button72s.grid(row=8,column=12,padx=(0,15))

#row=9

buttonA6o = tk.Button(mywindow,text='A6',command=buttonPress,bg=color_offsuit)
buttonA6o.grid(row=9,column=0,sticky = "NSEW")
buttonK6o = tk.Button(mywindow,text='K6',command=buttonPress,bg=color_offsuit)
buttonK6o.grid(row=9,column=1,sticky = "NSEW")
buttonQ6o = tk.Button(mywindow,text='Q6',command=buttonPress,bg=color_offsuit)
buttonQ6o.grid(row=9,column=2,sticky = "NSEW")
buttonJ6o = tk.Button(mywindow,text='J6',command=buttonPress,bg=color_offsuit) #,bg='red
buttonJ6o.grid(row=9,column=3,sticky = "NSEW")
buttonT6o = tk.Button(mywindow,text='T6',command=buttonPress,bg=color_offsuit) #,bg='red
buttonT6o.grid(row=9,column=4,sticky = "NSEW")
button96o = tk.Button(mywindow,text='96',command=buttonPress,bg=color_offsuit) #,bg='red
button96o.grid(row=9,column=5,sticky = "NSEW")
button86o = tk.Button(mywindow,text='86',command=buttonPress,bg=color_offsuit) #,bg='red
button86o.grid(row=9,column=6,sticky = "NSEW")
button76o = tk.Button(mywindow,text='76',command=buttonPress,bg=color_offsuit) #,bg='red
button76o.grid(row=9,column=7,sticky = "NSEW")
button66 = tk.Button(mywindow,text='66',command=press66,bg=color_pp) #,bg='red
button66.grid(row=9,column=8,sticky = "NSEW")
button65s = tk.Button(mywindow,text='65',command=buttonPress,bg=color_suited) #,bg='red
button65s.grid(row=9,column=9,sticky = "NSEW")
button64s = tk.Button(mywindow,text='64',command=buttonPress,bg=color_suited) #,bg='red
button64s.grid(row=9,column=10,sticky = "NSEW")
button63s = tk.Button(mywindow,text='63',command=buttonPress,bg=color_suited) #,bg='red
button63s.grid(row=9,column=11,sticky = "NSEW")
button62s = tk.Button(mywindow,text='62',command=buttonPress,bg=color_suited) #,bg='red
button62s.grid(row=9,column=12,padx=(0,15))

#row=10

buttonA5o = tk.Button(mywindow,text='A5',command=buttonPress,bg=color_offsuit)
buttonA5o.grid(row=10,column=0,sticky = "NSEW")
buttonK5o = tk.Button(mywindow,text='K5',command=buttonPress,bg=color_offsuit)
buttonK5o.grid(row=10,column=1,sticky = "NSEW")
buttonQ5o = tk.Button(mywindow,text='Q5',command=buttonPress,bg=color_offsuit)
buttonQ5o.grid(row=10,column=2,sticky = "NSEW")
buttonJ5o = tk.Button(mywindow,text='J5',command=buttonPress,bg=color_offsuit) #,bg='red
buttonJ5o.grid(row=10,column=3,sticky = "NSEW")
buttonT5o = tk.Button(mywindow,text='T5',command=buttonPress,bg=color_offsuit) #,bg='red
buttonT5o.grid(row=10,column=4,sticky = "NSEW")
button95o = tk.Button(mywindow,text='95',command=buttonPress,bg=color_offsuit) #,bg='red
button95o.grid(row=10,column=5,sticky = "NSEW")
button85o = tk.Button(mywindow,text='85',command=buttonPress,bg=color_offsuit) #,bg='red
button85o.grid(row=10,column=6,sticky = "NSEW")
button75o = tk.Button(mywindow,text='75',command=buttonPress,bg=color_offsuit) #,bg='red
button75o.grid(row=10,column=7,sticky = "NSEW")
button65o = tk.Button(mywindow,text='65',command=buttonPress,bg=color_offsuit) #,bg='red
button65o.grid(row=10,column=8,sticky = "NSEW")
button55 = tk.Button(mywindow,text='55',command=press55,bg=color_pp) #,bg='red
button55.grid(row=10,column=9,sticky = "NSEW")
button54s = tk.Button(mywindow,text='54',command=buttonPress,bg=color_suited) #,bg='red
button54s.grid(row=10,column=10,sticky = "NSEW")
button53s = tk.Button(mywindow,text='53',command=buttonPress,bg=color_suited) #,bg='red
button53s.grid(row=10,column=11,sticky = "NSEW")
button52s = tk.Button(mywindow,text='52',command=buttonPress,bg=color_suited) #,bg='red
button52s.grid(row=10,column=12,padx=(0,15))

#row=11

buttonA4o = tk.Button(mywindow,text='A4',command=buttonPress,bg=color_offsuit)
buttonA4o.grid(row=11,column=0,sticky = "NSEW")
buttonK4o = tk.Button(mywindow,text='K4',command=buttonPress,bg=color_offsuit)
buttonK4o.grid(row=11,column=1,sticky = "NSEW")
buttonQ4o = tk.Button(mywindow,text='Q4',command=buttonPress,bg=color_offsuit)
buttonQ4o.grid(row=11,column=2,sticky = "NSEW")
buttonJ4o = tk.Button(mywindow,text='J4',command=buttonPress,bg=color_offsuit) #,bg='red
buttonJ4o.grid(row=11,column=3,sticky = "NSEW")
buttonT4o = tk.Button(mywindow,text='T4',command=buttonPress,bg=color_offsuit) #,bg='red
buttonT4o.grid(row=11,column=4,sticky = "NSEW")
button94o = tk.Button(mywindow,text='94',command=buttonPress,bg=color_offsuit) #,bg='red
button94o.grid(row=11,column=5,sticky = "NSEW")
button84o = tk.Button(mywindow,text='84',command=buttonPress,bg=color_offsuit) #,bg='red
button84o.grid(row=11,column=6,sticky = "NSEW")
button74o = tk.Button(mywindow,text='74',command=buttonPress,bg=color_offsuit) #,bg='red
button74o.grid(row=11,column=7,sticky = "NSEW")
button64o = tk.Button(mywindow,text='64',command=buttonPress,bg=color_offsuit) #,bg='red
button64o.grid(row=11,column=8,sticky = "NSEW")
button54o = tk.Button(mywindow,text='54',command=buttonPress,bg=color_offsuit) #,bg='red
button54o.grid(row=11,column=9,sticky = "NSEW")
button44 = tk.Button(mywindow,text='44',command=press44,bg=color_pp) #,bg='red
button44.grid(row=11,column=10,sticky = "NSEW")
button43s = tk.Button(mywindow,text='43',command=buttonPress,bg=color_suited) #,bg='red
button43s.grid(row=11,column=11,sticky = "NSEW")
button42s = tk.Button(mywindow,text='42',command=buttonPress,bg=color_suited) #,bg='red
button42s.grid(row=11,column=12,padx=(0,15))

#row=12

buttonA3o = tk.Button(mywindow,text='A3',command=buttonPress,bg=color_offsuit)
buttonA3o.grid(row=12,column=0,sticky = "NSEW")
buttonK3o = tk.Button(mywindow,text='K3',command=buttonPress,bg=color_offsuit)
buttonK3o.grid(row=12,column=1,sticky = "NSEW")
buttonQ3o = tk.Button(mywindow,text='Q3',command=buttonPress,bg=color_offsuit)
buttonQ3o.grid(row=12,column=2,sticky = "NSEW")
buttonJ3o = tk.Button(mywindow,text='J3',command=buttonPress,bg=color_offsuit) #,bg='red
buttonJ3o.grid(row=12,column=3,sticky = "NSEW")
buttonT3o = tk.Button(mywindow,text='T3',command=buttonPress,bg=color_offsuit) #,bg='red
buttonT3o.grid(row=12,column=4,sticky = "NSEW")
button93o = tk.Button(mywindow,text='93',command=buttonPress,bg=color_offsuit) #,bg='red
button93o.grid(row=12,column=5,sticky = "NSEW")
button83o = tk.Button(mywindow,text='83',command=buttonPress,bg=color_offsuit) #,bg='red
button83o.grid(row=12,column=6,sticky = "NSEW")
button73o = tk.Button(mywindow,text='73',command=buttonPress,bg=color_offsuit) #,bg='red
button73o.grid(row=12,column=7,sticky = "NSEW")
button63o = tk.Button(mywindow,text='63',command=buttonPress,bg=color_offsuit) #,bg='red
button63o.grid(row=12,column=8,sticky = "NSEW")
button53o = tk.Button(mywindow,text='53',command=buttonPress,bg=color_offsuit) #,bg='red
button53o.grid(row=12,column=9,sticky = "NSEW")
button43o = tk.Button(mywindow,text='43',command=buttonPress,bg=color_offsuit) #,bg='red
button43o.grid(row=12,column=10,sticky = "NSEW")
button33 = tk.Button(mywindow,text='33',command=press33,bg=color_pp) #,bg='red
button33.grid(row=12,column=11,sticky = "NSEW")
button32s = tk.Button(mywindow,text='32',command=buttonPress,bg=color_suited) #,bg='red
button32s.grid(row=12,column=12,padx=(0,15))

#row=13

buttonA2o = tk.Button(mywindow,text='A2',command=buttonPress,bg=color_offsuit)
buttonA2o.grid(row=13,column=0,sticky = "NSEW")
buttonK2o = tk.Button(mywindow,text='K2',command=buttonPress,bg=color_offsuit)
buttonK2o.grid(row=13,column=1,sticky = "NSEW")
buttonQ2o = tk.Button(mywindow,text='Q2',command=buttonPress,bg=color_offsuit)
buttonQ2o.grid(row=13,column=2,sticky = "NSEW")
buttonJ2o = tk.Button(mywindow,text='J2',command=buttonPress,bg=color_offsuit) #,bg='red
buttonJ2o.grid(row=13,column=3,sticky = "NSEW")
buttonT2o = tk.Button(mywindow,text='T2',command=buttonPress,bg=color_offsuit) #,bg='red
buttonT2o.grid(row=13,column=4,sticky = "NSEW")
button92o = tk.Button(mywindow,text='92',command=buttonPress,bg=color_offsuit) #,bg='red
button92o.grid(row=13,column=5,sticky = "NSEW")
button82o = tk.Button(mywindow,text='82',command=buttonPress,bg=color_offsuit) #,bg='red
button82o.grid(row=13,column=6,sticky = "NSEW")
button72o = tk.Button(mywindow,text='72',command=buttonPress,bg=color_offsuit) #,bg='red
button72o.grid(row=13,column=7,sticky = "NSEW")
button62o = tk.Button(mywindow,text='62',command=buttonPress,bg=color_offsuit) #,bg='red
button62o.grid(row=13,column=8,sticky = "NSEW")
button52o = tk.Button(mywindow,text='52',command=buttonPress,bg=color_offsuit) #,bg='red
button52o.grid(row=13,column=9,sticky = "NSEW")
button42o = tk.Button(mywindow,text='42',command=buttonPress,bg=color_offsuit) #,bg='red
button42o.grid(row=13,column=10,sticky = "NSEW")
button32o = tk.Button(mywindow,text='32',command=buttonPress,bg=color_offsuit) #,bg='red
button32o.grid(row=13,column=11,sticky = "NSEW")
button22 = tk.Button(mywindow,text='22',command=press22,bg=color_pp) #,bg='red
button22.grid(row=13,column=12,padx=(0,15))

'''
#Button
button = tk.Button(mywindow,text='Press',command=buttonPress)
button.grid(row=2,column=1)

#Textbox
textb = tk.Entry(mywindow,text="Entry")
textbutton = tk.Button(mywindow,text="Text Box",command=textBox)
textb.grid(row=3,column=0, sticky = tk.W+tk.E, columnspan=4)
textbutton.grid(row=3,column=2)

#Slider
Slider = (tk.Scale(mywindow,label=('Slider'),variable=0,orient="horizontal"))
SliderButton = (tk.Button(mywindow,text='Slider',command=slideValue))
Slider.grid(row=4,column=1)
SliderButton.grid(row=5,column=2)
'''

mywindow.mainloop()