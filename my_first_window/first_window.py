#Matthew Ivezaj
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
# Create instance
win = tk.Tk()   

def click_me():
    action.configure(text="** Button has been clicked!")
    a_label.configure(foreground='blue')
    a_label.configure(text="This is a blue label")

# Add a title       
win.title("Python GUI")

# Disable resizing the GUI by passing in False/False
#win.resizable(False, False)  
# 
# #Adding a label 
a_label = ttk.Label(win, text="This is my virtual box!")
a_label.grid(column=0, row=0)
# Enable resizing x-dimension, disable y-dimension 
win.resizable(True, True) 

#Adding a button
action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=1, row=0)
#======================
# Start GUI
#======================
win.mainloop()
