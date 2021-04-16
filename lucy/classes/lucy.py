class Lucy:
    def __init__(self,name,age):
        """Initializing the name and age attributes"""
        self.name = name
        self.age = age
    def strike(self):
        """Created a method to indicate that Lucy performed a strike."""
        which_strike = input("Which blade will you be using to perform this strike?")