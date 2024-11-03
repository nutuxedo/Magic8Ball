# 8 ball GUI program for funsies heehee
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pygame

def exit_confirmation():
    con_window = tk.Tk()
    con_window.title("Exit")
    ex_com = tk.Label(
        con_window,
        text = "Are you sure you want to exit?"
    )
    ex_yes = tk.Button(
        con_window,
        text = "Yes",
        command = con_window.destroy
    )

    ex_no = tk.Button(
        con_window,
        text = "No",
        command = con_window.destroy
    )
    ex_com.pack()
    ex_yes.pack()
    ex_no.pack()


def about_btn():
    #img = PhotoImage(file="imgs/Magic_eight_ball.png")
    about_window = tk.Tk()
    about_window.geometry("150x150")
    about_window.title("About")
    #about_img = tk.Label(
        #about_window,
        #image = img
    #)
    about_msg = tk.Label(
        about_window,
        text="About lorem ipsum\n v0"
    )
    new_button = tk.Button(
        about_window,
        text = "Exit",
        command = about_window.destroy
    )
    #about_img.pack()
    about_msg.pack()
    new_button.pack()



# main window code here
def mainwindow():
    eightball_window = tk.Tk()
    eightball_window.title("8 Ball funsies")
    eightball_window.geometry("180x90")
    greeting = tk.Label(
        text="Hello, world",
        fg="cadet blue",
        bg="azure",
        width=25,
        height=1,
    )
    greeting.pack()
    about_button = tk.Button(
        text = "About",
        #bg = "black",
        #fg = "red",
        command = about_btn
    )
    exit_button = tk.Button(
        text = "Exit",
        command = exit_confirmation
    )

    about_button.pack()
    exit_button.pack()
    eightball_window.mainloop()

if __name__ == "__main__":
    mainwindow()