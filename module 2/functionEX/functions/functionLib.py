def getAge(age):
    """
    Creating a function that gets a users name and validates it.


    Arguments passed are: none.
    """
    #Ensuring that the name may only contain ' and letters of the alphabet.
    if ("." in age) and (age.replace(".",'')).isdigit() or age.isdigit():
        return True
    else:
        print("\'"+age+"\' Is not a proper age, please try again!")
        return False
def getDate(date):
    """
    Creating a function that gets the date a user enters and validates it.


    Arguments passed are: none.
    """
    #Ensuring that the name may only contain ' and letters of the alphabet.
    if ("-" in date) and (date.replace("-",'')).isdigit() or ("/" in date) and (date.replace("/",'')).isdigit() or ("." in date) and (date.replace(".",'')).isdigit():
        return True
    else:
        print("\'"+date+"\' Is not a proper date, please try again!")
        return False
def getName(name):
    """
    Creating a function that gets a users name and validates it.


    Arguments passed are: none.
    """
    #Ensuring that the name may only contain ' and letters of the alphabet.
    if ("'" in name) and (name.replace("'",'')).isalpha() or name.isalpha() or ("." in name) and (name.replace(".",'')).isalpha():
        return True
    else:
        print("\'"+name+"\' Is not a proper name, please try again!")
        return False

def printOutput(age_passed,name_passed,date_passed):
    """
    Creating a function to print the output of data collected.

    Arguments passed are: name, date, age
    """
    print("Here is the data that was entered. \nYour age: " +age_passed+"\nYour name: "+name_passed+"\nThe date: "+date_passed)