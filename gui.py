from tkinter import *
import tkinter as tk

window = tk.Tk()

# To rename the title of the window
window.title("GUI")

#pack is used to show the object in the window
label = tk.Label(window, text = "Hello world!").pack()

window.mainloop()
