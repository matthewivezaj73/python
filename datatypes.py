#Setting a flag
not_decimal = False
#Testing for whether the user enters a decimal or not.
while not not_decimal:
    #Asking the user to insert a float value.
    costofitem = input("Please input the cost of the item as a float value (i.e 37.21, 4.32, 5.00, 7.04): ")
    #Testing to see if a decimal is inside of the value entered.
    if ("." in costofitem) and (costofitem.replace('.','')).isdigit():
        print("You have entered a correct value!")
    else:
        print("That is not the proper format!")
    #Setting a flag to ask the user if they would like to keep adding prices.
    my_continue = False
    #Testing for whether the user would like to continue or not
    while not my_continue:
        #Asking the user if they would like to continue entering prices
        icontinue = input("Would you like to continue entering prices, please respond with y for yes or n for no: ")
        if icontinue.lower() == "y":
            print("Moving on!")
            my_continue = True
        elif icontinue.lower() == "n":
            #Setting flags to true to break out of the loop.
            not_decimal = True
            my_continue = True
        #Notifying the user that the value that they had entered is not valid.
        else:
            print("That is not a valid option, please try again!")