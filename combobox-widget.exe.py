


#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")  

# Modify adding a Label
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

# Modified Button Click Function
def click_me(): 
    action.configure(text='Submit ' + name.get())
#     print(number)
#     print(number.get())

# Changing our Label
ttk.Label(win, text="Item Name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
# column 0
name_entered.grid(column=0, row=1)                          

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
# <= change column to 2   
action.grid(column=2, row=1)                                

ttk.Label(win, text="Select Quantity:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number )
number_chosen['values'] = (1, 2, 4, 42, 100)
# <= Combobox in column 1
number_chosen.grid(column=1, row=1)                        
number_chosen.current(0)
# Place cursor into name Entry
name_entered.focus()      
#======================
# Start GUI
#======================
win.mainloop()