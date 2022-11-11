import os
from inspect import stack
from pickletools import stackslice
from tkinter import *
from math import sqrt
import random
import subprocess

global cwd
cwd = os.getcwd()

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

win = Tk() # This is to create a basic window
win.geometry("312x425")  # this is for the size of the window 
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")

global pot
global stacks
global ggopbet

###################Starting with functions ####################
# 'btn_click' function : 
# This Function continuously updates the 
# input field whenever you enter a number

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""

def get_pot():
    global expression
    global pot
    pot = float(expression)
    print("pot is: " + str(expression))

def get_stacks():
    global expression
    global stacks
    stacks = float(expression)
    print("stacks are: " + str(expression))

def calculate_ggop_bet(street):
    global pot
    global stacks
    global ggopbet
    ggopbet_percent = 1
    if street == 3:
        #Flop:
        ggopbet_percent = 0.5*((((pot + 2*stacks)/pot)**(1.0/3)) - 1)
    elif street == 2:
        #Turn:
        ggopbet_percent = 0.5*((((pot + 2*stacks)/pot)**(1.0/2)) - 1)
    ggopbet = (ggopbet_percent * pot)
    input_text.set("bet: " + str(ggopbet)[0:5])
    print("ggop bbet is: " + str(ggopbet))

def randomizer():
    rnd = random.uniform(1.0,99.9)
    input_text.set(str(rnd)[0:5] + "%")
    print("randomizer: " + str(rnd))

 
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar()
 
# Let us creating a frame for the input field
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
 
btns_frame.pack()
 
# first row
 
clear = Button(btns_frame, text = "CLEAR", fg = "black", width = 32, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

# fifth row

pot_btn = Button(btns_frame, text = "POT", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: get_pot()).grid(row = 5, column = 0, padx = 1, pady = 1)
 
stack_btn = Button(btns_frame, text = "STACK", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: get_stacks()).grid(row = 5, column = 1, padx = 1, pady = 1)
 
#bet_btn = Button(btns_frame, text = "BET", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: calculate_ggop_bet()).grid(row = 5, column = 2, padx = 1, pady = 1)
 
#randomize = Button(btns_frame, text = "RAND", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: randomizer()).grid(row = 5, column = 2, columnspan = 4, padx = 1, pady = 1)
turn_ggop = Button(btns_frame, text = "RAND", fg = "black", width = 21, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: randomizer()).grid(row = 5, column = 2, columnspan = 2, padx = 1, pady = 1)
# sixt row
 
flop_ggop = Button(btns_frame, text = "FLOP BET", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: calculate_ggop_bet(3)).grid(row = 6, column = 0, columnspan = 2, padx = 1, pady = 1)
turn_ggop = Button(btns_frame, text = "TURN BET", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: calculate_ggop_bet(2)).grid(row = 6, column = 2, columnspan = 2, padx = 1, pady = 1)

win.mainloop()
