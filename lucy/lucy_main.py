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
    #Prompting the user to see if they would like to leave the dialogue.
    print("Would you like to leave the dialogue?")
    #Setting a flag
    not_question = False
    while not not_question:
        #Asking for the users input.
        areyoudone = input("Please respond with y for yes or n for no: ")
        #If the user selects y for yes
        if areyoudone.lower() == "y":
            #Setting flags to true to break out of both of the loops.
            not_done = True
            not_question = True
        elif areyoudone.lower() == "n":
            print("Moving on!")
            not_question = True