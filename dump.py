import tkinter.ttk as ttk
import tkinter as tk

window = tk.Tk()
window.title("what")
#window.geometry("150x50")
lbl_greeting = tk.Label(
    text="Hello, world",
    fg="cadet blue",
    bg="azure",
    width=15,
    height=1,
)
lbl_greeting.pack()
button = tk.Button(
    text = "yes",
    bg = "black",
    fg = "red",
)
button.pack()
window.mainloop()