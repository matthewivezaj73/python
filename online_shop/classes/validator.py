class Validator:
    """
    Created a class that will perform the act of validating data entered.
    """

    def __init__(self, item_name, payment_method, ItemsPurchased):
        """
        Initializing item_name, payment_method, and ItemsPurchased.
        """
        self.item_name = item_name 
        self.payment_method = payment_method
        self.ItemsPurchased = ItemsPurchased
    def check_description(self,item_description):
        """
        A method that will check whether an item exists in the list.
        """
        if (item_description.replace(' ','')).isalpha():
            return True
        else:
            return False
    def check_item(self,item_name):
        """
        A method that will check whether an item exists in the list.
        """
        my_list = ["Hammer","Nails","Paper","Mechanical Pencil","Tape", "12 lb ham", "Ribs", "12 oz. steak"]
        if item_name in my_list:
            print("Added!")
            return True
        else:
            print(f"Sorry, but, \'{item_name}\' that item does not exist in our inventory!")
    def check_price(self,price_entered):
        """
        A method that will check whether an iten exists.
        """
        if ("." in price_entered) and (price_entered.replace('.','')).isdigit():
            return True
        else:
            return False
    def check_quantity(self,item_quantity):
        """
        A method that will check whether the quantity entered for an item.
        """
        if ("." in item_quantity) and (item_quantity.replace('.','')).isdigit():
            return True
        else:
            return False