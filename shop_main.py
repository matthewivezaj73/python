#Importing the validator class.
from classes.validator import *
from classes.database_access import DB_Connect
#Creating an instance of DB_Connect
my_db = DB_Connect('root', '', 'python_projects')
#Creating an instance of the Validator class.
my_validator = Validator("L Wrench", "American Express", "12")
#Creating a variable to represent the data in the database table.
my_result = my_db.executeSelectQuery("SELECT * FROM online_inventory")
#setting a flag.
not_shop = False
#Testing for what the user would like to do at the shop.
while not not_shop:
    #Asking for input from the user.
    my_action = input("Enter s to show inventory.\nEnter f to finish order.\nEnter a to "+
    "add to cart.\nEnter r to remove from cart\nEnter e to exit.\nPlease enter your choice: ")
    if my_action.lower() == "a":
        #Setting a flag.
        not_name = False
        #Testing for adding items to the cart.
        while not not_name:
            #Asking for user input on items that they would like to purchase.
            item_name = input("Please enter an item that you would like to add: ")
            #Validating the item_price.
            not_name = my_validator.check_item(item_name)
        #Setting a flag.
        not_price = False
        #Testing for adding items price.
        while not not_price:
            #Asking for user input on item price.
            item_price = input("Please enter enter the total of the price (be sure to include a decimal in your response): ")
            not_price = my_validator.check_price(item_price)
        #Setting a flag.
        not_quantity = False
        #Testing for adding items quantity.
        while not not_quantity:
            #Asking for user input on item quantity.
            item_quantity = input("Please enter enter the quantity you have on hand (be sure to include a decimal in your response): ")
            not_quantity = my_validator.check_price(item_quantity)
        #Setting a flag.
        not_description = False
        #Testing for adding items description.
        while not not_description:
            #Asking for user input on item quantity.
            item_description = input("Please enter enter the description of the item: ")
            not_description = my_validator.check_description(item_description)
        #SQL statement to insert data into the database.
        my_db.executeQuery("INSERT INTO online_inventory (item_name, item_price, item_quantity, item_description) VALUES (\'"+
        item_name +"\',\'"+ item_price+"\',\'"+item_quantity +"\',\'"+ item_description +"\')")

        #Setting a flag.
        add_another = False
        while not add_another:
            add_more = input("Would you like to enter in another item? Please respond with \'y\' for Yes/ and \'n\' for No: ")
            if add_more.lower() == 'y':
                add_another = True
            elif add_more.lower() == 'n':
                not_shop = True
                add_another = True
            else:
                print(f"{add_more} is not a valid choice, please try again!")
    elif my_action.lower() == "s":
        for item in my_result:
            print("Item name: " + str(item['item_id']) + str(item['item_name'])+ str(item['item_price'])+ str(item['item_quantity'])+ str(item['item_description']))