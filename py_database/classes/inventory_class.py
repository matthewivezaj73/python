#Matthew Ivezaj
#03/16/2021
#IT 412
#https://github.com/matthewivezaj/IT412/blob/main/weeks%208%20through%2010%20%20Final/classes/customer_class.py
class Inventory:
    def __init__(self,Iname="",Iprice="",Ilocation=""):
        """
        It takes name, age, and location as passed values.

        Setting the defaults of these as blanks so I do not have to 
        create an instance every time I want to work with an instance of a class.
        """
        #Initializing address, city_information, firstname, lastname, 
        #company_name, email, phone_number, state_information, and zipcode
        self.Iname = Iname
        self.Iprice = Iprice
        self.Ilocation = Ilocation
    def item_brand_check(self,item_brand):
        """
        Created a item_brand_check method to check a items 
        brand. This may be comprised of any type of character
        It accepts alphanumeric characters as passed arguments.
        """
        #Checking to see if the item brand is atleast 1 character in 
        # length or greater and is only comprised of alphanumeric characters.
        if item_brand.isalnum() and len(item_brand.strip()) >= 1:
            #Returning true if the condition is met.
            return True
        #The option to run if the condition is not met.
        else:
            #Telling the user why the entry is incorrect.
            print("\'"+item_brand+"\'"+" is incorrect, please try again!")
            #Returning false if the condition is not met.
            return False
    def item_name_check(self,item_name_value):
        """
        Created a customer_name_check method to check a customer's first
        name. It is testing the customer's name to be comprised of 
        uppercause and lowercase letters, single quotes,
        and hyphen characters. 
        It accepts a customer name as passed arguments.
        """
        #Creating a list of bad values to not include in the  name
        bad_values = ['!','@','#','$','%','^','&','*','(',')','{','}','[',']','\\','|','`','~','<','>','.','?','/','"',';',':','_','+','=',"0","1","2","3","4","5","6","7","8","9"]
        #Checking to see if the model has any bad chars in it.
        if len(item_name_value.strip()) >= 1:
            #Checks if bad chars were entered into model.
            for character in item_name_value: 
                #Checking to make sure that the characters. 
                # inside of the model are not in the list of bad characters.   
                if character in bad_values:
                    #Telling the user why the name they entered was bad.
                    print("\'"+item_name_value+"\'" + " is an invalid input, please try again!")
                    #Returning true.
                    return False
            #If bad chars are not entered, return true.
            return True
        #For all else.
        else:
            #Notifying the user why the input did not pass.
            print("\'"+item_name_value +"\'"+ " is an invalid input, please try again!")
            #Returning False
            return False
    def item_color_check(self,item_color):
        """
        Created an item_color_check method to ensure 
        that the item_color is comprised of
        primarily of alphanumeric characters.
        It accepts a email address as passed arguments.
        """
        #Creating a list of bad values to not include in the  name
        bad_values = ["!", "\"", "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}"]
        #Checking to see if the model has any bad chars in it.
        if len(item_color.strip()) >= 1 and item_color.isalnum():
            #Checks if bad chars were entered into model.
            return True
        #For all else.
        else:
            #Notifying the user why the input did not pass.
            print("\'"+item_color +"\'"+ " is an invalid input, please try again!")
            return False
            #Returning false
    def price_check(self,pricepaid):
        """
        Checks to make sure that the vehicle price paid is a float value.

        This method also checks to make sure that the values are only comprised
        of a decimal and numbers.
        """
        #Making sure that the pricepaid is a float.
        if ("." in pricepaid) and (pricepaid.replace('.','')).isdigit() or pricepaid.isdigit():
            #returning true if the price entered has digits and decimals in it.
            return True
        else:
            print("\'"+pricepaid +"\'"+ " is an invalid input, please try again!")
            #returning false if the price entered has digits and decimals in it.
            return False
    def quantity_check(self,item_quanitity):
        """
        Created a quantity_check method to ensure
        a quantity is accepted for the items on hand.

        It accepts a quantity amount as passed arguments.
        """
        if item_quanitity.isdigit() and len(item_quanitity) >= 1:
            #If the quantity value passed is digits,
            # and is atleast 1 digit long. If that is met, it returns true.
            return True
        #Else handling the case where the quantity is not passed a digit.
        else:
            #Notifying the user that the zip code entered is an incorrect value.
            print("\'"+item_quanitity+"\'"+" is an incorrect value, please try again!")
            #return false if test does not pass the three requirements.
            return False
    def shelf_life_check(self,shelf_life):
        """
        Created a shelf_life_check method to ensure that only
        digits or doubles may be accepted and the length is 
        at least 1 character long. 

        It accepts a number as passed arguments.

        """
        #Checking while not shelf_life_ok
        if shelf_life.isdigit() or ("." in shelf_life) and (shelf_life.replace('.','')).isalnum() and len(shelf_life) > 0:
            #If the shelf life value is a numeric value that is 4 or 5 digits long, return true.
            return True
        #Else telling the user why the zip code is incorrect.
        else:
            #Notifying the user that the zip code entered is an incorrect value.
            print("\'"+shelf_life+"\'"+" is an incorrect value, please try again!")
            #If the shelf life value entered does not satisfy requirements, return false.
            return False
    def item_location_check(self,location):
        """ 
        Created a item_location_check to ensure that only
        letters, numbers, and the . character are entered.
            
        Takes one argument that should be the location.
        """
        #Checking to see if the 
        if ("." in location) and (location.replace('.','')).isalnum() or len(location) > 0:
            #If the location value is a numeric value that is 4 or 5 digits long, return true.
            return True
        #Else telling the user why the location is incorrect.
        else:
            #Notifying the user that the zip code entered is an incorrect value.
            print("\'"+location+"\'"+" is an incorrect value, please try again!")
            #If the zipcode value entered does not satisfy requirements, return false.
            return False