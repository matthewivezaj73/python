#Matthew Ivezaj
#03/16/2021
#IT 412
#https://github.com/matthewivezaj/IT412/blob/main/weeks%208%20through%2010%20%20Final/classes/customer_class.py
class Player:
    def __init__(self, pid="", pname="", ptype=""):
        """
        It takes pid, pname, and ptype as passed values.

        Setting the defaults of these as blanks so I do not have to 
        create an instance every time I want to work with an instance of a class.
        """
        #Initializing pid, pname, and ptype. 
        self.pid = pid
        self.pname = pname
        self.ptype = ptype
