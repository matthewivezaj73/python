#Importing the functions
from functions.functionLib import *
#Setting a flag
not_date = False
#Testing for the name.
while not not_date:
    #Printing a message Asking the user for the date.
    print("Please enter the date: ")
    #Allowing the user to input a date.
    date_passed = input("")
    if date_passed:
        not_date = getDate(date_passed)
    else:
        print("Try again!")
#Setting a flag
not_name = False
#Testing for the name.
while not not_name:
    #Printing a message Asking the user for their name.
    print("Please enter your name: ")
    #Allowing the user to input their name.
    name_passed = input("")
    if date_passed:
        not_name = getName(name_passed)
    else:
        print("Try again!")
#Setting a flag
not_age = False
#Testing for the age
while not not_age:
    #Printing a message asking for the users age.
    print("Please enter your age: ")
    #Asllowing the user to input their age.
    age_passed = input("")
    if age_passed:
        not_age = getAge(age_passed)
    else:
        print("Try again!")
#Calling the printOutput method.
printOutput(age_passed,name_passed,date_passed)
