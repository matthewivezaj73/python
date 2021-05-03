from classes.login_class import *

#Creating an instance of the login class
new_login = Login("Tom","1-21-2021","01:12:21")

#Setting a flag
not_done = False
#Starting the while loop
while not not_done:
    #Creating a flag for getting the name.
    get_name_not = False
    #Creating a while loop.
    while not get_name_not:
        #Notifying the user what the requirements are.
        print("Please enter the username that you would like to go by."+
        "\nPlease note that this can only contain alphanumeric characters, a period, and a hyphen: ")
        #Asking the user for the username that they would like to enter.
        username = input("")
        #Validating the username and setting it equal to the flag so that we break out of the loop.
        get_name_not = new_login.check_name(username)
    #Creating a flag for getting the password.
    get_pass_not = False
    #Creating a while loop.
    while not get_pass_not:
        #Notifying the user what the requirements are.
        print("Please enter a password with a minimum of 8 characters."+"\nA strong password should make use of letters, numbers, and special characters.")
        #Asking the user for the password.
        password = input("")
        #Validating the password.
        get_pass_not = new_login.check_password(password)
