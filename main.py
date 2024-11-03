# 8 ball GUI program for funsies heehee
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pygame

def exit_con():
    con_window = tk.Tk()
    con_window.title("Exit")
    #con_window.geometry("150x150")
    ex_com = tk.Label(
        con_window,
        text = "Are you sure you want to exit?",
        font=("Cantarell", 12, "bold"),
        bg="white",
        height="2",
        width="30"
    )
    ex_yes = tk.Button(
        con_window,
        text = "Yes",
        bg="sky blue",
        command = con_window.destroy
    )

    ex_no = tk.Button(
        con_window,
        text = "No",
        bg="sky blue",
        command = con_window.destroy
    )
    ex_com.grid(row =0, column= 0, columnspan= 2)
    ex_yes.grid(row=1, column= 0, pady =10)
    ex_no.grid(row=1, column=1, pady=10)

def about_win():
    #img = PhotoImage(file="imgs/Magic_eight_ball.png")
    about_window = tk.Tk()
    about_window.geometry("150x80")
    about_window.title("About")
    #about_img = tk.Label(
        #about_window,
        #image = img
    #)
    about_msg = tk.Label(
        about_window,
        text="8 ball funsies",
        font=("Cantarell", 12, "bold"),
        bg="white",
        width="15"
    )
    version_num = tk.Label(
        about_window,
        text="by nutuxedo - version 0",
        font=("Cantarell", 8),
        bg="white",
        width="25"
    )
    new_button = tk.Button(
        about_window,
        text = "Exit",
        bg="sky blue",
        command = about_window.destroy
    )
    #about_img.pack()
    about_msg.pack()
    version_num.pack()
    new_button.pack()

# main window code here
def mainwindow():
    root = tk.Tk()
    root.title("8 Ball funsies")
    root.geometry("250x160")
    maincontent = tk.Label(
        root,
        text="8 ball content here",
        fg="black",
        bg="white",
        width=25,
        height=2,
        font=("Cantarell", 12, "bold")
    )

    fortune_btn = tk.Button(
        root,
        text ="Shake the ball!",
        bg="sky blue",
        font=("Cantarell", 12, "bold"),
        command= EightBall
    )

    shaken_confirm = tk.Label(
        root,
        text="You have shaken the ball!",
        font=("Cantarell", 8, "italic")
    )

    about_btn = tk.Button(
        root,
        text = "About",
        bg = "sky blue",
        #fg = "red",
        command = about_win
    )
    exit_btn = tk.Button(
        root,
        text = "Exit",
        bg="sky blue",
        command = exit_con
    )
# grid placement
    maincontent.grid(row = 0, column = 0, columnspan = 2, pady = 0)
    fortune_btn.grid(row =1, column=0, columnspan=2, pady=8)
    shaken_confirm.grid(row=2, columnspan=2)
    #shaken_confirm.grid_remove()
    about_btn.grid(row = 3, column = 0, ipadx = 10, pady = 5)
    exit_btn.grid(row = 3, column = 1, ipadx = 10, pady = 5)
    root.mainloop()

# main 8 ball content here
class EightBall:
    def __init__(self):
        print("You have shaken the ball!")

if __name__ == "__main__":
    mainwindow()