class Person:
    def __init__(self,name=""):
        """Initializing the person's name"""
        self.name = name
    def persons_age_check(self,age):
        """Created a method to check the input of the users age""" 
        if age.isdigit():
            print("Great, we have your age down!")
        else:
            print("Sorry, please try again!")
    def persons_name_check(self,name):
        """Created a method to check the input of the users name""" 
        if ("." in name) and (name.replace('.','')).isalnum() or ("-" in name) and (name.replace('-','')).isalnum():
            print("Great, we have your name down!")
        else:
            print("Sorry, please try again!")
    def persons_color_check(self,color):
        """Created a method to check the input of the users favorite color""" 
        if (" " in color) and (color.replace(' ','')).isalnum() and len(color.strip()) > 0: 
            print("Great, we have your favorite color down!")
        else:
            print("Sorry, please try again!")
