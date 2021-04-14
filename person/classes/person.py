class Person:
    def __init__(self,name=""):
        """Initializing the person's name"""
        self.name = name
    def persons_age_check(self):
        """ Created a method to check the input of the users age""" 
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
    