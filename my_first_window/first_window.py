#Matthew Ivezaj
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
# Create instance
win = tk.Tk()   

def click_me():
    """Creating a function that inserts a text 
    box once the button is clicked in the GUI"""
    action.configure(text="Hello " + name.get())

# Add a title       
win.title("Python GUI")

# Disable resizing the GUI by passing in False/False
#win.resizable(False, False)  
# 
# #Adding a label 
ttk.Label(win, text="Please enter your first name: ").grid(column=0, row=0)
# ttk.Label(win, text="Please enter your last name: ").grid(column=0, row=0)
# ttk.Label(win, text="Please enter your phone number: ").grid(column=0, row=0)
# ttk.Label(win, text="Please enter your street address: ").grid(column=0, row=0)
# Enable resizing x-dimension, disable y-dimension 
win.resizable(True, True) 

#Adding a text box entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, rows=1)
#Adding a button
action = ttk.Button(win, text="Click me!", command=click_me)
action.grid(column=1, row=0)
#======================
# Start GUI
#======================
win.mainloop()
