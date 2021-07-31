from classes.database_access import DB_Connect
from classes.buy_items import Items
#Creating a connection to the database
my_db = DB_Connect('root','','python_projects')
#Creating an instance of the class.
my_items = Items("Mike","322.32","32")
#Creating a list of food to choose from.
food_available = ["Hot dog buns","Celery","Lettuce","Milk","Eggs","Bread","Ramen Noodles","Ketchup","Muffins","Ground Beef"]
#Creating a blank list that will hold food the user selects.
stored_food = []
#Setting a flag
not_food = False
#Truncating the database table.
my_db.executeQuery("TRUNCATE item_data")
#Testing for the food.
while not not_food:
    #Asking the user what kind of food they would like to buy.
    my_food = input("What food would you like to buy today: ")
    #Checking if the food that the user entered is in the list.
    for food in food_available:
        if food in food_available:
            print("That food is available!")
            stored_food.append(my_food)
            break
        else:
            print("That food is not available, please choose again!")
    #Adding the food that you are buying to the database.
    for food in stored_food:
        #Inserting into the crm_data table.
        my_db.executeQuery("INSERT INTO crm_data(f_name, l_name, address, city, state, zip, company, primary_phone, secondary_phone, email_address) VALUES (\'"+
        str(f_name) +"\',\'"+ str(l_name) +"\',\'"+str(street_address) +"\',\'"+ str(city)  +"\',\'"+str(state) +"\',\'"+str(zip_code) +"\',\'"+ str(company_name) +
        "\',\'"+ phone1 +"\',\'"+ phone2 +"\',\'"+ str(email) +"\')")

    #Setting a flag
    not_more = False
    #Testing for the user's input.
    while not not_more:
        #Asking the user if they would like to buy more food.
        more_food = input("Would you like to buy some more food? Y/N: ")