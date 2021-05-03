class Login:
    """
    Created a class to handle when a user is logging into a system.
    """
    def __init__(self,name,date,time):
        """
        Initializing the following attributes in the class.
        """
        self.name = name
        self.date = date
        self.time = time
    def check_name(self,username):
        """
        Created a method to verify the user name.
        """
        #Validating the username.
        if (("." in username) and (username.replace('.','')).isalnum()) or (("." in username) and (username.replace('.','')).isalnum()) or username.isalnum():
            return True
        else:
            #Notifying the user that the username entered is not a valid option to choose.
            print("Sorry, but, "+username+" is not a valid choice, please try again!")
            return False
    def check_password(self,password):
        """
        Creating a method to verify a password.
        """
        #Validating the password
        if len(password) >= 8:
            print("Your account has been created!")
            return True
        else:
            #Notifying the user that the password entered is not a valid option to choose.
            print("Sorry, but, "+password+" is not a valid choice, please try again!")
            return False