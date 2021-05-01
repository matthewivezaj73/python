#Matthew Ivezaj
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")

# Disable resizing the GUI by passing in False/False
#win.resizable(False, False)   
ttk.Label(win, text="This is my virtual box!").grid(column=0, row=0)
# Enable resizing x-dimension, disable y-dimension 
win.resizable(True, True) 

#======================
# Start GUI
#======================
win.mainloop()
