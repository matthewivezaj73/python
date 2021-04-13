#Creating a blank list to hold the names.
my_names = []
#Setting a flag.
not_name = False
#Testing for a list of names
while not not_name:    
    #Asking the user for their name
    name = input("Please enter the names of people that you would like to invite to the party: ")
    #Checking to see if the name entered is only comprised of characters of the alphabet.
    if name.isalpha():
        #Telling the user the length of their name
        print("The name you have entered is: " + name) 
        #Appending the name to a list
        my_names.append(name)
    else:
        print("That is not a proper name")
    not_done = False
    while not not_done:
        #Asking the user if they would like to continue
        enter_another = input("Would you like to enter another name?\n Please respond with Y/N: ")
        #If the user does want to enter another name.
        if enter_another == "y":
            print("Moving on!")
            #Setting flag to true to break out of this loop
            not_done = True
        #If the user does not want to enter another name.
        elif enter_another == "n":
            #Showing the user the names that they have entered so far.
            print("Here is the list of names that you have entered so far: ")
            for name in my_names:
                print(name)
            print("Here are the number of tickets you need to buy: ")
            #Printing the length of the list so that the user can see how many tickets that they need to buy.
            print(len(my_names))
            #Breaking out of the loop
            not_name = True
            not_done = True
        #If the user enters a value in other than y or n.
        else:
            print("Sorry, I didn't get that!")
