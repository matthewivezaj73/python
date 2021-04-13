#car.py
class car:
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
