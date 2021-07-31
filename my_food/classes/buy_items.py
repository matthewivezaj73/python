class Items():
    """
    Creating a class that will hold 
    methods for making purchases at a mall.
    """
    def __init__(self,customerName,moneySpent,itemPurchased):
        """
        Initializing the following attributes:
            -    Customer Name
            -    Money Spent
            -    Item's purchased
        """
        self.customerName = customerName
        self.moneySpent = moneySpent
        self.itemPurchased = itemPurchased
    def checkOut(self,totalPaid):
        """
        Creating a method to handle the task 
        of buying the items that are in the cart.

        Accepts the following passed values:
            - totalPaid
        """
    def moreFood(self,more_food):
        """
        Creating a method that asks the 
        user if they would like to buy more food.
        """

        #If the user select y for yes.
        if more_food.lower() == 'y':
            print("Moving on!")
            return True
        #If the user select y for yes.
        elif more_food.lower() == 'n':
            print("Here is what you bought:")
            for my_food in stored_food:
                print(f"You bought some: {my_food}")
            print("Good bye!")
            not_food = True
            not_more = True
        #Handling the alternative case.
        else:
            print("Try again!")
    def placeCart(self,itemname):
        """
        Creating a method to handle the task 
        of buying an item that is in the cart.

        Accepts the following passed values:
            - item_name
        """