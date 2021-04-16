#Importing the Lucy class
from classes.lucy_class import Lucy
new_lucy = Lucy("Lucy",23)
#Setting a flag
not_done = False
#Testing for the dialogue
while not not_done:
    #Setting a flag
    strike_done = False
    while not strike_done:
        #Asking the user which blade they will be using
        which_strike = input("Which blade will you be using to perform this strike?")
        #Testing the strike value passed.
        strike_done = new_lucy.strike(which_strike)
    print("Would you like to leave the dialogue?")
    areyoudone = input("Please respond with y for yes or n for no: ")