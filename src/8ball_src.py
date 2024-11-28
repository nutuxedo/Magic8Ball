# 8 ball GUI program for funsies heehee
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import sys
import time

# main 8 ball content here
class EightBall:
    def __init__(self):
        # Answers provided from https://en.wikipedia.org/wiki/Magic_8_Ball
        self.answers = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]
    def shake(self):
        print("Shaking the ball...")
        time.sleep(2)
        return self.get_answer()
    
    def get_answer(self):
        return random.choice(self.answers)
        
def about_win(root):
    #img = PhotoImage(file="imgs/Magic_eight_ball.png")
    about_window = tk.Toplevel(root)
    about_window.geometry("150x80")
    about_window.title("About")
    about_window.resizable(False, False)
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
    
def exit_con(root):
    con_window = tk.Toplevel(root)
    con_window.title("Exit")
    con_window.resizable(False,False)
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
        command = lambda: (print("Program exited"), root.destroy())
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
    
# main window code here
def mainwindow():
    root = tk.Tk()
    root.title("8 Ball funsies")
    root.geometry("250x160")
    root.resizable(False,False)
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
        command=lambda: print(EightBall().shake())
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
        command = lambda: about_win(root)
    )
    exit_btn = tk.Button(
        root,
        text = "Exit",
        bg = "sky blue",
        command = lambda: exit_con(root)
    )
# grid placement
    maincontent.grid(row = 0, column = 0, columnspan = 2, pady = 0)
    fortune_btn.grid(row =1, column=0, columnspan=2, pady=8)
    shaken_confirm.grid(row=2, columnspan=2)
    #shaken_confirm.grid_remove()
    about_btn.grid(row = 3, column = 0, ipadx = 10, pady = 5)
    exit_btn.grid(row = 3, column = 1, ipadx = 10, pady = 5)
    root.mainloop()

root = mainwindow()
