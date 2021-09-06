class CyberValidation():
    """ 
    Creating a class to hold a host of methods for the users desire.
    """
    def __init__(self,CY_term="", CY_def="", hours=""):
        """
        Creating an init method and initializing CY_term, CY_def, and hours.
        """
        self.CY_term = CY_term
        self.CY_def = CY_def
        self.hours = hours
    def add_Definition(self, definition):
        """
        Created a method to validate the definition 
        before it needs to be added to the database.
        """
        #Creating a list of bad values to not include in the  name
        bad_values = ['!','@','#','$','%','^','&','*','(',')','{','}','[',']','\\','|','`','~','<','>','.','?','/','"',';',':','_','+','=','1','2','3','4','5','6','7','8','9','0']
        #Checking to see if the model has any bad chars in it.
        if len(definition.strip()) >= 1:
            #Checks if bad chars were entered into model.
            for character in definition: 
                #Checking to make sure that the characters. 
                # inside of the model are not in the list of bad characters.   
                if character in bad_values:
                    #Telling the user why the city name is bad.
                    print("\'"+definition+"\'" + " is an invalid input, please try again!")
                    #Returning false
                    return False
            #If bad chars are not entered, return true.
            return True
        #For all else.
        else:
            #Notifying the user why the input did not pass.
            print("\'"+definition +"\'"+ " is an invalid input, please try again!")
            #Returning flase
            return False
    def add_term(self, term):
        """
        Created a method to validate the term 
        before it needs to be added to the database.
        """
        #Creating a list of bad values to not include in the  name
        bad_values = ['!','@','#','$','%','^','&','*','(',')','{','}','[',']','\\','|','`','~','<','>','.','?','/','"',';',':','_','+','=','1','2','3','4','5','6','7','8','9','0']
        #Checking to see if the model has any bad chars in it.
        if len(term.strip()) >= 1:
            #Checks if bad chars were entered into model.
            for character in term: 
                #Checking to make sure that the characters. 
                # inside of the model are not in the list of bad characters.   
                if character in bad_values:
                    #Telling the user why the city name is bad.
                    print("\'"+term+"\'" + " is an invalid input, please try again!")
                    #Returning false
                    return False
            #If bad chars are not entered, return true.
            return True
        #For all else.
        else:
            #Notifying the user why the input did not pass.
            print("\'"+term +"\'"+ " is an invalid input, please try again!")
            #Returning flase
            return False