from classes.database_access import DB_Connect
from classes.buy_items import Items
#Creating a connection to the database
my_db = DB_Connect('root','','python_projects')
#Creating an instance of the class.
my_items = Items("Mike","322.32","32")
#Creating a list of food to choose from.
food_available = ["Hot Dog Buns","Celery","Lettuce","Milk","Eggs","Bread","Ramen Noodles","Ketchup","Muffins","Ground Beef"]
#Creating a list of drinks to choose from.
drink_available = ['Lemonade', 'water', 'pepsi', 'root beer']
#Creating a list of utilities available to buy.
utilities_avialable  = ["Hammer","Saw","Ethernet cable","Mouse"]
#Creating a list of items available to buy.
items_available  = ["Gold Coin","Cusion","Flag","Hose"]
#Creating a blank list that will hold food the user selects.
stored_food = []
stored_drink = []
stored_utility = []
stored_item = []
#Setting a flag
not_items_to_buy = False
#Truncating the database table.
my_db.executeQuery("TRUNCATE item_data")
#Testing for the food.
while not not_items_to_buy:
    #Asking the user what kind of food they would like to buy.
    my_food = input("What food would you like to buy today: ")
    #Checking if the food that the user entered is in the list.
    for food in food_available:
        if food.title() in food_available:
            print(f"{my_food} is not available!")
            break
        else:
            print(f"{my_food} is  available!")
            stored_food.append(my_food)
            break
#Setting a flag
not_drink = False
#Testing for the beverage.
while not not_drink:
    #Asking the user what kind of food they would like to buy.
    my_beverage = input("What drink would you like to buy today: ")
    #Checking if the food that the user entered is in the list.
    for drink in drink_available:
        if drink not in drink_available:
            print(f"{my_beverage} is not available!")
            break
        else:
            print(f"{my_beverage} is available!")
            stored_drink.append(my_beverage)
            break
#Setting a flag
not_utility = False
#Testing for the beverage.
while not not_utility:
    #Asking the user what kind of food they would like to buy.
    my_utility = input("What utility would you like to buy today: ")
    #Checking if the food that the user entered is in the list.
    for utility in utilities_avialable:
        if utility not in utilities_avialable:
            print(f"{my_utility} is not available!")
            break
        else:
            print(f"{my_utility} is available!")
            stored_utility.append(my_utility)
            break
#Setting a flag
not_item = False
#Testing for the item.
while not not_item:
    #Asking the user what kind of food they would like to buy.
    my_item = input("What item would you like to buy today: ")
    #Checking if the food that the user entered is in the list.
    for item in stored_item:
        if item not in items_available:
            print(f"{my_item} is not available!")
            break
        else:
            print(f"{my_item} is available!")
            stored_item.append(my_item)
            break
    #Inserting into the item_data table.
    my_db.executeQuery("INSERT INTO item_data(food, beverage, utility, item_quantity) VALUES (\'"+
    str(my_food) +"\',\'"+ str(my_beverage) +"\',\'"+str(my_utility) +"\',\'"+ str(my_item)  +"\')")
    #Setting a flag
    not_more = False
    #Testing for the user's input.
    while not not_more:
        #Asking the user if they would like to buy more food.
        more_food = input("Would you like to buy some more food? Y/N: ")
        if more_food.lower == "y":
            not_more = True
        elif more_food.lower() == "n":
            not_items_to_buy = True
            not_more = True
