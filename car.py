#car.py
class Car:
    def __init__(self,color,name,make):
        """
        Initializing color, name, and make
        """
        self.color = color
        self.name = name
        self.make = make
    def get_color(self,color):
        """
        Created a method that gets the color of a car and stores it in a database.
        """
        #Asking the user for the make of the car
        print("What is the make of the car?")
        #Setting a flag.
        not_color = False
        #Testing for the make.
        while not not_color:
            #Asking for the user's input.
            color = input("")
            if ("-" in color) and (color.replace('-','')).isalnum():
                print("color has been recorded!")
            else:
                print("Sorry, but: \'"+color+"\'"+" is not a color of the proper format. Please try again")
    def get_make(self,make):
        """
        Created a method that gets the make of a car and stores it in a database.
        """
        #Asking the user for the make of the car
        print("What is the make of the car?")
        #Setting a flag.
        not_make = False
        #Testing for the make.
        while not not_make:
            #Asking for the user's input.
            make = input("")
            if ("-" in make) and (make.replace('-','')).isalnum():
                print("Make has been recorded!")
            else:
                print("Sorry, but: \'"+make+"\'"+" is not a make of the proper format. Please try again")
    def get_name(self,name):
        """
        Created a method that gets the name of a car and stores it in a database.
        """
        #Asking the user for the make of the car
        print("What is the make of the car?")
        #Setting a flag.
        not_name = False
        #Testing for the make.
        while not not_name:
            #Asking for the user's input.
            name = input("")
            if ("-" in name) and (name.replace('-','')).isalnum():
                print("Name has been recorded!")
            else:
                print("Sorry, but: \'"+name+"\'"+" is not a name of the proper format. Please try again")

#Creating an instance of a car
my_newCar = Car("Red","Honda","F-150")
#Setting a flag.
not_done = False
while not not_done:
    #Calling the get_color() method.
    my_newCar.get_color()
    #Calling the get_make() method
    my_newCar.get_make()
    #Calling the get_name() method
    my_newCar.get_name()
    #Asking the user if they would like to continue or not.
    print("Would you like to enter a new vehicle? Please respond with y for yes or n for no:")
    #Getting the users input.
    response = input("")
    if response.lower() == "y":
        print("Great, moving on!")
    else:
        print("See you later!")
        not_done = True