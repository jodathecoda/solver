import tkinter as tk
from tkinter import Tk, BOTH, Menu


def pop(evt):
    but = evt.widget
    if str(evt.type) == "Enter":
        # Map the menu in the center of the width.
        x = but.winfo_rootx() + int(but.winfo_width()/2)
        y = but.winfo_rooty() + int(but.winfo_height()/2)
        popup.tk_popup(x, y)

    elif str(evt.type) == "Leave":
        popup.unpost()


root = tk.Tk()
root.geometry("300x300")

popup = Menu(root, tearoff=0, relief='raised')
popup.add_command(label="About")
popup.add_command(label="User manual")
popup.add_command(label="Contact us")

button1 = tk.Button(root, text="HELP", height=3, width=26)
button1.bind('<Enter>', pop)
button1.bind('<Leave>', pop)
button1.pack(pady=100)

root.mainloop()