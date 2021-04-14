#Setting a flag.
not_finished_yet = False
#Testing until the user if finished.
while not not_finished_yet:
    #Creating a blank list.
    list_of_people = []
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
        #Testing for the person's age.
        not_age_done = new_person.persons_age_check(persons_age)
    #Setting a flag
    not_name_done = False
    # Asking for the not_name_done.
    while not not_name_done:
        print("What is your name?")
        #Allowing the user to input an name.
        user_name = input()
        #Testing for the person's name.
        not_name_done = new_person.persons_name_check(user_name)
    #Setting a flag
    not_color_done = False
    #Testing for the favorite color
    while not not_color_done:
        #Asking the user for their favorite color.
        print("What is your favorite color?")
        #Asking the user for input.
        favorite_color = input()
        #Testing for the person's favorite color.
        not_color_done = new_person.persons_color_check(favorite_color)
    #Creating the dictionary
    person_profile = {"The persons name:":user_name,"The persons age:":persons_age, "The persons favorite color:":favorite_color}
    #Appending each profile to the list of people.
    list_of_people.append(person_profile)
    #Asking the user if they would like ot add another user.
    print("Would you like to add another user")
    #Asking for the users input.
    add_another = input("Please enter y for yes or n for no: ")
    if add_another.lower() == "y":
        #Notifying the user that they are moving on.
        print("Moving on!")
    elif add_another.lower() == "n":
        #Notifying the user that the process is complete
        print("Ok, all done!")
        #Setting flag to true to break out of the loop
        not_finished_yet = True