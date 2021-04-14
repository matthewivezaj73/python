#mporting a class
from classes.person import Person
#Creating an instance of a person
new_person = Person("Phil")
#Adding a flag
not_age_done = False
# Asking for the persons age.
while not not_age_done:
    print("What is your age?")
    #Allowing the user to input an age.
    persons_age = input()
not_name_done = False
# Asking for the not_name_done.
while not not_name_done:
    print("What is your name?")
    #Allowing the user to input an name.
    user_name = input()
#Setting a flag
not_color_done = False
#Testing for the favorite color
while not not_color_done:
    #Asking the user for their favorite color.
    print("What is your favorite color?")
    #Asking the user for input.
    favorite_color = input()
    not_color_done = new_person.persons_color_check