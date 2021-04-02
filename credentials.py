#This program will ask a user for their user name and password
#Send the user a message that will ask for their username
print("Please enter your user name: ")
#Accepting the user input for their username.
username = input()
#Send the user a message that will ask for their password
print("Please enter your password: ")
#Accepting the user input for their password.
password = input()
#If the username and password match
if password == "0179932" and username == "Matt":
    print("Welcome, " + username+"!")
else:
    print("Sorry, we could not find that profile in our database!")