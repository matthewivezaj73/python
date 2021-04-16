class Lucy:
    def __init__(self,name,age):
        """Initializing the name and age attributes"""
        self.name = name
        self.age = age
    def strike(self,strike):
        """Created a method to indicate that Lucy performed a strike."""
        #Checking to see if the strike is comprised of only alphabetical characters.
        if strike.isalpha():
            return True
        else:
            print("Shoot, that didn't work!")