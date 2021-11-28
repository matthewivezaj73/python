class Customer:
    """
    Creating a representation of a customer.
    """
    def __init__(self, Customer_name, customer_age, customer_phone_number, customer_email):
        """
        Initializing the customers name, customer age, phone number, and customer_email.
        """
        self.Customer_name = Customer_name 
        self.customer_age = customer_age
        self.customer_phone_number = customer_phone_number
        self.customer_email = customer_email 
    def checkOut_Book(self,book_name,book_list):
        """
        A method that will remove books from the list of available books.
        """
        try:
            if book_name in book_list:
                #Removing the book from the libraries available list.
                book_list.remove(book_name)
            else:
                print("Sorry, the book is not available.")
        except:
            print("Sorry, I did not understand what you entered.")
    def validate_customer_address(self, customer_address):
        """
        Creating a method to validate a customer's address.
        """
        bad_chars = ['!',"@","#","$","%","^","&","*","(",")","~","`","[","]","{","}","|","\\","/","?",">","<",",","=","+"]
        if len(customer_address) > 0:
            for char in bad_chars:
                if char in customer_address:
                    return False
                else:
                    return True
        else:
            return False
    def validate_customer_age(self,customer_age):
        """
        Creating a method to validate a customer's age.
        """
        if customer_age.isdigit():
            return True
        else:
            return False
    def validate_customer_email(self, customer_email):
        """
        Creating a method to validate a customer's email address.
        """
        if ('.' and '@' in customer_email):
            return True
        else:
            print("That is not a proper email!")
            return False
    def validate_customer_name(self,customer_name):
        """
        Creating a method to validate a customer's name.

        This method returns true if the first name is comprised of only 
        """
        if customer_name.isalpha(): 
            return True
        else:
            return False
    def validate_customer_phone(self, customer_phone):
        """
        Creating a method to validate a customer's phone number.
        """
        if customer_phone.isdigit() and len(customer_phone) == 10 or ("-" in customer_phone) and customer_phone.isdigit() and len(customer_phone) == 12:
            return True
        else:
            return False