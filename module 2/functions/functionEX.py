#Importing the functions
from classes.classesLib import *
#Creating an instance of the class.
my_person = Person("12","Tommy","1-12-2022")
#Setting a flag
not_date = False
#Testing for the name.
while not not_date:
    #Printing a message Asking the user for the date.
    print("Please enter the date: ")
    #Allowing the user to input a date.
    date_passed = input("")
    if date_passed:
        not_date = my_person.getDate(date_passed)
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
        not_name = my_person.getName(name_passed)
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
        not_age = my_person.getAge(age_passed)
    else:
        print("Try again!")
#Calling the printOutput method.
my_person.printOutput(age_passed,name_passed,date_passed)
