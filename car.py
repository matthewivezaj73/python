#car.py
class car:
    def __init__(self,color,name,make):
        """
        Initializing color, name, and make
        """
        self.color = color
        self.name = name
        self.make = make
    def get_make(self,make):
        """
        Created a method that gets the make of a car and stores it in a database.
        """
        #Asking the user for the make of the car
        print("What is the make of the car?")
        #Setting a flag.
        not_make = False