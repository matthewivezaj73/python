#Making a list
list_of_names = ["Suzie","Will","Rukia","Chad","Ichigo","Asuna","Fred","Teddy","Gilbert","Elizabeth","Honey"]
#Printing each name in the list
for name in list_of_names:
    #Creating a flag
    not_done = False
    #Testing for the drink
    while not not_done:
        #Sending out a customized message to each guest.
        print("Hello "+name+", welcome to the party!")
        #Asking the user if they would like a drank.
        get_drink = input("Would you like a drink? Please respond with y for yes and n for no")
        #If the user selects y for yes.
        if get_drink.lower() == "y":
            print("Ok, "+name+"! Here is your drink!")
            break
        #If the user selects n for no.
        elif get_drink.lower() == "n":
            print("Ok, so no drink for you!")
            break
        #If the user does not enter y or n.
        else:
            print("Sorry, I didn't get that")

        