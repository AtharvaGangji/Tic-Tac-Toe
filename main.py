# imports
import tkinter as tk
from tkinter import *
from tkinter import messagebox

xpo = tk.Tk()
xpo.title("Tic Tac Toe")
xpo.resizable(0,0)

# Winner
winner = None


def t_ie():
    messagebox.showinfo("Tic Tac Toe", "Oh \nIts a Tie.")


def disable():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)

def w_inner():
    if winner == 1:
      messagebox.showinfo("Tic Tac Toe", "Congratulations X \nYou Win")
    elif winner == 2:
      messagebox.showinfo("Tic Tac Toe", "Congratulations O \nYou Win")

# Variables
WIDTH = 10
HEIGHT = 5
BG = "White"
WIN_BG = "Lime"
TIE = "Red"
FONT = ("Helvetica", 10)
xpo2 = 1

def check_win():
    global winner

    # check row (X)
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg = WIN_BG)
        b2.config(bg=WIN_BG)
        b3.config(bg=WIN_BG)
        winner = 1
        disable()
        w_inner()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg = WIN_BG)
        b5.config(bg=WIN_BG)
        b6.config(bg=WIN_BG)
        winner = 1
        disable()
        w_inner()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg = WIN_BG)
        b8.config(bg=WIN_BG)
        b9.config(bg=WIN_BG)
        winner = 1
        disable()
        w_inner()


    # check row (O)
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg = WIN_BG)
        b2.config(bg=WIN_BG)
        b3.config(bg=WIN_BG)
        winner = 2
        disable()
        w_inner()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg = WIN_BG)
        b5.config(bg=WIN_BG)
        b6.config(bg=WIN_BG)
        winner = 2
        disable()
        w_inner()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg = WIN_BG)
        b8.config(bg=WIN_BG)
        b9.config(bg=WIN_BG)
        winner = 2
        disable()
        w_inner()


    # check coloum (X)
    if b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg = WIN_BG)
        b4.config(bg=WIN_BG)
        b7.config(bg=WIN_BG)
        winner = 1
        disable()
        w_inner()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg = WIN_BG)
        b5.config(bg=WIN_BG)
        b8.config(bg=WIN_BG)
        winner = 1
        disable()
        w_inner()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg = WIN_BG)
        b6.config(bg=WIN_BG)
        b9.config(bg=WIN_BG)
        winner = 1
        disable()
        w_inner()


    # check coloum (O)
    if b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg = WIN_BG)
        b4.config(bg=WIN_BG)
        b7.config(bg=WIN_BG)
        winner = 2
        disable()
        w_inner()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg = WIN_BG)
        b5.config(bg=WIN_BG)
        b8.config(bg=WIN_BG)
        winner = 2
        disable()
        w_inner()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg = WIN_BG)
        b6.config(bg=WIN_BG)
        b9.config(bg=WIN_BG)
        winner = 2
        disable()
        w_inner()


    # check diagonals (O)
    if b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg = WIN_BG)
        b5.config(bg=WIN_BG)
        b9.config(bg=WIN_BG)
        winner = 2
        disable()
        w_inner()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg = WIN_BG)
        b5.config(bg=WIN_BG)
        b7.config(bg=WIN_BG)
        winner = 2
        disable()
        w_inner()


    # check diagonals (O)
    if b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg = WIN_BG)
        b5.config(bg=WIN_BG)
        b9.config(bg=WIN_BG)
        winner = 1
        disable()
        w_inner()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg = WIN_BG)
        b5.config(bg=WIN_BG)
        b7.config(bg=WIN_BG)
        winner = 1
        disable()
        w_inner()


    # check Tie
    if b1["text"] != " " and b2["text"]  != " " and b3["text"] != " " and b4["text"] != " " and b5["text"] != " " and b6["text"] != " " and b7["text"] != " " and b8["text"] != " " and b9["text"] != " " and winner == None:
        b1.config(bg=TIE)
        b2.config(bg=TIE)
        b3.config(bg=TIE)
        b4.config(bg=TIE)
        b5.config(bg=TIE)
        b6.config(bg=TIE)
        b7.config(bg=TIE)
        b8.config(bg=TIE)
        b9.config(bg=TIE)
        disable()
        t_ie()


# Buttons
b1 = tk.Button(xpo, width = WIDTH, height = HEIGHT, text = " ", bg = BG, font = FONT, command = lambda: mad(1))
b1.grid(row = 0, column = 0)
b2 = tk.Button(xpo, width = WIDTH, height = HEIGHT, text = " ", bg = BG, font = FONT, command = lambda: mad(2))
b2.grid(row = 0, column = 1)
b3 = tk.Button(xpo, width = WIDTH, height = HEIGHT, text = " ", bg = BG, font = FONT, command = lambda: mad(3))
b3.grid(row = 0, column = 2)

b4 = tk.Button(xpo, width = WIDTH, height = HEIGHT, text = " ", bg = BG, font = FONT, command = lambda: mad(4))
b4.grid(row = 1, column = 0)
b5 = tk.Button(xpo, width = WIDTH, height = HEIGHT, text = " ", bg = BG, font = FONT, command = lambda: mad(5))
b5.grid(row = 1, column = 1)
b6 = tk.Button(xpo, width = WIDTH, height = HEIGHT, text = " ", bg = BG, font = FONT, command = lambda: mad(6))
b6.grid(row = 1, column = 2)

b7 = tk.Button(xpo, width = WIDTH, height = HEIGHT, text = " ", bg = BG, font = FONT, command = lambda: mad(7))
b7.grid(row = 2, column = 0)
b8 = tk.Button(xpo, width = WIDTH, height = HEIGHT, text = " ", bg = BG, font = FONT, command = lambda: mad(8))
b8.grid(row = 2, column = 1)
b9 = tk.Button(xpo, width = WIDTH, height = HEIGHT, text = " ", bg = BG, font = FONT, command = lambda: mad(9))
b9.grid(row = 2, column = 2)


def mad(x):
    global xpo2
    if x == 1 and b1["text"] == " ":
        if xpo2 == 1:
            b1["text"] = "X"
            xpo2 = 2
            check_win()
        elif xpo2 == 2:
            b1["text"] = "O"
            xpo2 = 1
            check_win()
    elif x == 2 and b2["text"] == " ":
        if xpo2 == 1:
            b2["text"] = "X"
            xpo2 = 2
            check_win()
        elif xpo2 == 2:
            b2["text"] = "O"
            xpo2 = 1
            check_win()
    elif x == 3 and b3["text"] == " ":
        if xpo2 == 1:
            b3["text"] = "X"
            xpo2 = 2
            check_win()
        elif xpo2 == 2:
            b3["text"] = "O"
            xpo2 = 1
            check_win()

    elif x == 4 and b4["text"] == " ":
        if xpo2 == 1:
            b4["text"] = "X"
            xpo2 = 2
            check_win()
        elif xpo2== 2:
            b4["text"] = "O"
            xpo2 = 1
            check_win()
    elif x == 5 and b5["text"] == " ":
        if xpo2 == 1:
            b5["text"] = "X"
            xpo2 = 2
            check_win()
        elif xpo2 == 2:
            b5["text"] = "O"
            xpo2 = 1
            check_win()
    elif x == 6 and b6["text"] == " ":
        if xpo2 == 1:
            b6["text"] = "X"
            xpo2 = 2
            check_win()
        elif xpo2 == 2:
            b6["text"] = "O"
            xpo2 = 1
            check_win()

    elif x == 7 and b7["text"] == " ":
        if xpo2 == 1:
            b7["text"] = "X"
            xpo2 = 2
            check_win()
        elif xpo2 == 2:
            b7["text"] = "O"
            xpo2 = 1
            check_win()
    elif x == 8 and b8["text"] == " ":
        if xpo2 == 1:
            b8["text"] = "X"
            xpo2 = 2
            check_win()
        elif xpo2 == 2:
            b8["text"] = "O"
            xpo2 = 1
            check_win()
    elif x == 9 and b9["text"] == " ":
        if xpo2 == 1:
            b9["text"] = "X"
            xpo2 = 2
            check_win()
        elif xpo2 == 2:
            b9["text"] = "O"
            xpo2 = 1
            check_win()

# mainloop
xpo.mainloop()
