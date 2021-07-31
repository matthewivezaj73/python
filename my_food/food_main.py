#Creating a list of food to choose from.
food_available = ["Hot dog buns","Celery","Lettuce","Milk","Eggs","Bread","Ramen Noodles","Ketchup","Muffins","Ground Beef"]
#Creating a blank list that will hold food the user selects.
stored_food = []
#Setting a flag
not_food = False
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
    #Setting a flag
    not_more = False
    #Testing for the user's input.
    while not not_more:
        #Asking the user if they would like to buy more food.
        more_food = input("Would you like to buy some more food? Y/N: ")