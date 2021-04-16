#Importing the Lucy class
from lucy.classes.lucy_class import Lucy

#Setting a flag
not_done = False
#Testing for the dialogue
while not not_done:
    #Asking the user which blade they will be using
    which_strike = input("Which blade will you be using to perform this strike?")
    if which_strike:
        print("Arrrgghhhhh!!!!!")
    else:
        print("Shoot, it missed...")