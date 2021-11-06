class Account():
    """ 
        Creating a class to hold all of the methods that you can do to a persons account.
    """
    def __init__(self,account_name,creation_date,security_question,account_type):
        """
        Initializing the account_name, creation_date, security_question, account_type fields.
        """
        self.account_name = account_name
        self.creation_date = creation_date
        self.security_question = security_question
        self.account_type = account_type

    def CheckBirth(self,passed_date):
        """
        Created a method to validate the date of the account creation.

        This method checks to see if the passed_name variable 
        is comprised of only numeric values and the hyphen symbol. If it is, 
        the method returns true. If it is not, the method 
        returns false and that prompts the user to try again.
        """
        if ("-" in passed_date) and (passed_date.replace('-','')).isdigit():
            return True
        else:
            print(f"Sorry, but \'{passed_date}\', is incorrect! Please try again!")
            return False
    def checkID(self,ID_passed):
        """
        Creating a method to check the ID passed.

        This method checks to see if the ID passed is comprised of
        only numerical values. It returns false if anything else.
        """
        if ID_passed.isdigit():
            return True
        else:
            return False
    def CheckName(self,passed_name):
        """
        Created a method to check the name of the account.

        This method checks to see if the passed_name variable 
        is comprised of only alpha characters as well as - ' . . If it is, 
        the method returns true. If it is not, the method 
        returns false and that prompts the user to try again. 
        """
        if ("-" in passed_name) and (passed_name.replace('-','')).isalpha() or ("'" in passed_name) and (passed_name.replace('\'','')).isalpha() or ("." in passed_name) and (passed_name.replace('.','')).isalpha() or passed_name.isalpha():
            return True
        else:
            print(f"Sorry, but \'{passed_name}\', is incorrect! Please try again!")
            return False
    def CheckUserName(self,passed_name):
        """
        Created a method to check the name of the account.

        This method checks to see if the passed_name variable 
        is comprised of only alphanumeric characters. If it is, 
        the method returns true. If it is not, the method 
        returns false and that prompts the user to try again.
        """
        if passed_name.isalnum():
            return True
        else:
            print(f"Sorry, but \'{passed_name}\', is incorrect! Please try again!")
            return False
    def LengthCheck(self,passed_length):
        """
        Created a method to check the length of the name of the account.

        This method checks to see if the passed_length variable 
        meets a length requirement that the program depicts. If it is, 
        the method returns true. If it is not, the method 
        returns false and that prompts the user to try again.
        """
        if 3 <= len(passed_length) >= 15:
            return True
        else:
            print(f"Sorry, but \'{passed_length}\', is an incorrect number of characters! Please try again!")
            return False
    def validateCountry(self,country_name):
        """
        Created a method to validate a country name passed.

        This method checks to see if the country_name is comprised
        of only letters of the alphabet.
        """
        if country_name.isalpha():
            return True
        else:
            return False