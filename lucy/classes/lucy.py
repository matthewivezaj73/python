class Lucy:
    def __init__(self,name,age):
        """Initializing the name and age attributes"""
        self.name = name
        self.age = age
    def strike(self,strike):
        """Created a method to indicate that Lucy performed a strike."""
        if strike.isalpha():
            return True
        else:
            return False