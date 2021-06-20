#Creating a blank list to hold users
user_list = []
#Setting a flag
not_user = False
#Testing to create a username
while not not_user:
    new_user = input("Please enter your preferred username (please only include letters and numbers): ")
    #Performing a check on the characters entered
    if not new_user.isalnum():
        print("Sorry, but, "+"'"+new_user+"'"+ " does not work.")
    else:
        pass_list.append(select_pass)
#NOT SURE WHY, BUT THIS IS NOT WORKING OUT, WILL NEED TO INVESTIGATE MORE.
        #not_user = True
#Creating a blank list
pass_list = []
#Setting a flag
not_select = False
#Testing to create a password
while not not_select:
    #Asking the user to create a password
    select_pass = input("Please create a password (Only letters and numbers): ")
    #Checking to see if the password has characters that are not alphanumeric.
    if not select_pass.isalnum():
        print("Sorry, but, "+"'"+select_pass+"'"+"  does not work.")
    else:
        #If the characters are alphanumeric, we will append the password to a list.
        pass_list.append(select_pass)
        not_select = True
not_user = False
while not not_user:
    user_passed = input("Please enter your user name: ")
    if user_passed in user_list:
        not_user = True
    else:
        print("That is not a registered user!")
#Creating a flag
not_pass = False
#Testing for the password
while not not_pass:
    #Creating a loop to keep executing until the required data is entered.
    password_phrase = input("Please enter the password password: ")
    if password_phrase in pass_list:
        not_pass = True
    else:
        print("Sorry, that is not a password!")
