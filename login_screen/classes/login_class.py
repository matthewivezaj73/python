class Login:
    """
    Created a class to handle when a user is logging into a system
    """
    def __init__(self,name,date,time):
        """
        Initializing the following attributes in the class
        """
        self.name = name
        self.date = date
        self.time = time
    def check_name(self):
        """Created a method to verify the user name"""
        
