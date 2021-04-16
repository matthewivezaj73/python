#Importing the Lucy class


#Setting a flag
not_done = False
#Testing for the dialogue
while not not_done:
    #Asking the user which blade they will be using
    which_strike = input("Which blade will you be using to perform this strike?")
    if which_strike.isalpha():
        print("Arrrgghhhhh!!!!!")
    else:
        print("Shoot, it missed...")