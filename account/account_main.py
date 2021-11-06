#Importing modules.
from classes.account import Account
from classes.database_access import DB_Connect


#Creating login connection
my_db = DB_Connect('root', '', 'python_projects')
#Making an instance of the database
my_account_list = my_db.executeSelectQuery("SELECT * FROM account_list")
#Creating an instance of the class.
my_account = Account("Alfi323","11-01-2000","What is the name of your pet?","Client")
#Setting a flag.
not_done = False
#Testing for input.
while not not_done: 
    #Asking the user what they would like to do.
    what_do = input("Would you like to create a new account.\nShow all existing accounts.\nUpdate an existing account.\nDelete an existing account.\nPlease respond with create, update, show, or delete: ")
    #Handling the case where the user wants to create an account.
    if what_do.lower() == "show":
        for result in my_account_list:
            #Printing each key value in every dictionary inside of the list.
            print("user_id: " +str(result['user_id'])+", user name: "+str(result['user_name'])+", Date Of Birth: "+
            str(result['DateOfBirth'])+", country name: "+str(result['country_name'])+", User First Name: "+
            str(result['f_name'])+", User Last Name: "+str(result['l_name']))

    elif what_do.lower() == "create":
        #Setting a flag.
        not_profile = False
        #Testing for input.
        while not not_profile:
            #Asking the user for the name of their account.
            userName = input("Enter your account name: ")
            #Evaluating the account_name.
            not_profile = my_account.CheckUserName(userName)
        #Setting a flag.
        not_DOB = False
        #Testing for the input of DOB.
        while not not_DOB:
            #Asking the user to enter the dob.
            creationDate = input("Enter your accounts creation date, please seperate mmddyyyy by a hyphen (-): ")
            #Evaluating the account creation date.
            not_DOB = my_account.CheckCreation(creationDate)
        #Setting a flag.
        not_Country = False
        #Testing for the input of DOB.
        while not not_Country:
            #Asking the user to enter the dob.
            countryName = input("Enter your country name: ")
            #Evaluating the account creation date.
            not_Country = my_account.validateCountry(countryName)
        #Setting a flag.
        not_f_name = False
        #Testing for input.
        while not not_f_name:
            #Asking the user for the name of their account.
            f_name = input("Enter your first name: ")
            #Evaluating the account_name.
            not_f_name = my_account.CheckName(f_name)
        #Setting a flag.
        not_l_name = False
        #Testing for input.
        while not not_l_name:
            #Asking the user for the name of their account.
            l_name = input("Enter your last name: ")
            #Evaluating the account_name.
            not_l_name = my_account.CheckName(l_name)
        if not_l_name and not_DOB and not_Country:
            #INSERTING DATA INTO THE DATABASE TABLE.
            my_db.executeQuery("INSERT INTO account_list (user_name, DateOfBirth, country_name, f_name, l_name) VALUES (\'" + userName+"\',\'"+creationDate +"\',\'"+ countryName +"\',\'"+f_name+"\',\'"+ l_name+"\')")
            #Saving to the database.
            my_db.conn.commit()
        else:
            #Saving to the database.
            my_db.conn.commit()
        #Setting a flag.
        continue_creating = False
        #Testing for input.
        while not continue_creating:
            #Asking the user if they would like to continue creating accounts.
            continue_creation = input("Would you like to continue? Please respond with Y/N: ")
            #If the user input y.
            if continue_creation.lower() == "y":
                #Setting flags to preference.
                not_done = False
                continue_creating = True
            elif continue_creation.lower() == "n":
                #Setting flags to preference.
                not_done = True
                continue_creating = True
            else:
                print(f"Sorry, I did not understand, \'{continue_creation}\', please try again!")
    elif what_do.lower() == "update":
        #Setting a flag to false to test for the id.
        car_id_ok = False
        #Testing for the ID.
        while not car_id_ok:  
            #Selecting all rows from the car_data table.
            my_result = my_db.executeSelectQuery("SELECT * FROM account_list") 
            #Asking the user for the vehicle_id
            user_id = input("Please enter the user_id for whose field you would like to edit "+
            "(please only include a valid user_id or you will be asked to enter a new ID after you "+
            "are finished going through the edit process) or enter q to quit: ") 
            #Checking if the id enetered is a digit, else returns false.             
            if user_id.isdigit():
                #selecting user_id from the account_list where user_id = the value inputted for user_id.
                my_db.executeSelectQuery("SELECT user_id FROM account_list WHERE user_id ="+"\'"+user_id +"\'") 
                #Setting car_id to true to escape the loop.
                column_ok = False
                car_data_ok = False 
                car_id_ok = True
            elif user_id.lower() == "q":
                #Setting flags to true to break out of the loop.
                car_data_ok = True
                column_ok = True
                car_id_ok = True
            else:
                #Notifying the user that they have entered something invalid.
                print("\'"+user_id +"\'"+ " is entered an invalid id")
                #Returning false to stay in the loop.
                car_data_ok = True
                column_ok = True
                car_id_ok = False
            #Testing for the column.
            while not column_ok:
                #Asking the user to input which column they would like to edit.
                user_column = input("Which column of the account_list table would you like to edit?\n- Date of Birth\n- country name\n- first name\n- last name\n- Or Q to quit (takes you back to the edit menu): ")
                #If the user selects vehicle_make.
                if user_column.lower() == 'user_name':
                    #Setting flags to true.
                    column_ok = True
                #If the user selects vehicle_model.
                elif user_column.lower() == 'DateOfBirth':
                    #Setting flags to true.
                    column_ok = True
                #If the user selects vehicle_identification_number.
                elif user_column.lower() == 'country_name':
                    #Setting flags to true.
                    column_ok = True
                #If the user selects seller_name.
                elif user_column.lower() == 'f_name':
                    #Setting flags to true.
                    column_ok = True
                #If the user selects price_paid.
                elif user_column.lower() == 'l_name':
                    #Setting flags to true.
                    column_ok = True
                #Handling the case where the user enters q to quit.
                elif user_column.lower() == 'q':
                    #Setting flags to go back to the original loop.
                    car_id_ok = False
                    user_ok = True
                    column_ok = True
                else:
                    #Setting column_ok flag to false.
                    column_ok = False
            # While loop to keep asking the user which column they would like to edit.
            while not user_ok:
                #If the user selects vehicle_make.
                if user_column.lower() == "user_name":
                    #Setting vehicle_make_ok to false.
                    user_name_ok = False
                    #Testing for the car_make.
                    while not user_name_ok:
                        #Asking the user to enter a value for the car make.
                        userName = input("Please enter only letters of the alphabet for values "+
                        "you would like to input for your username so that it can be updated: ")
                        #Setting flag to true to break out of the loop.
                        user_name_ok = my_account.CheckName(userName)
                    #Updating the database with the new value. 
                    my_db.executeQuery("UPDATE account_list SET "+"user_name="+"\'"+userName+"\'"+
                    " WHERE user_id ="+"\'"+user_id+"\'")
                #Handling the case where the user selects DateOfBirth.
                elif user_column.lower() == "DateOfBirth":
                    #Setting DOB_ok to false.
                    DOB_ok = False
                    #Testing for the car_make.
                    while not DOB_ok:
                        #Asking the user to enter a value for the date of birth.
                        DOB = input("Please enter only numerical values "+
                        "you would like to input for your DOB so that it can be updated: ")
                        #Setting flag to true to break out of the loop.
                        DOB_ok = my_account.CheckBirth(DOB)
                    #Updating the database with the new value. 
                    my_db.executeQuery("UPDATE account_list SET "+"DateOfBirth="+"\'"+DOB+"\'"+
                    " WHERE user_id ="+"\'"+user_id+"\'")
                #Handling the case where the user selects country_name.
                elif user_column.lower() == "country_name":
                    #Setting country_ok to false.
                    country_ok = False
                    #Testing for the country.
                    while not country_ok:
                        #Asking the user to enter a value for the country name.
                        country = input("Please enter only alphabetical values "+
                        "you would like to input for your country so that it can be updated: ")
                        #Setting flag to true to break out of the loop.
                        country_ok = my_account.validateCountry(country)
                    #Updating the database with the new value. 
                    my_db.executeQuery("UPDATE account_list SET "+"country_name="+"\'"+country+"\'"+
                    " WHERE user_id ="+"\'"+user_id+"\'")
                #Handling the case where the user selects f_name.
                elif user_column.lower() == "f_name":
                    #Setting f_name_ok to false.
                    f_name_ok = False
                    #Testing for the first name.
                    while not f_name_ok:
                        #Asking the user to enter a value for the country name.
                        f_name = input("Please enter only alphabetical values "+
                        "you would like to input for your first name so that it can be updated: ")
                        #Setting flag to true to break out of the loop.
                        f_name_ok = my_account.validateCountry(f_name)
                    #Updating the database with the new value. 
                    my_db.executeQuery("UPDATE account_list SET "+"f_name="+"\'"+f_name+"\'"+
                    " WHERE user_id ="+"\'"+user_id+"\'")
                #Handling the case where the user selects l_name.
                elif user_column.lower() == "l_name":
                    #Setting l_name_ok to false.
                    l_name_ok = False
                    #Testing for the last name.
                    while not l_name_ok:
                        #Asking the user to enter a value for the country name.
                        l_name = input("Please enter only alphabetical values "+
                        "you would like to input for your last name so that it can be updated: ")
                        #Setting flag to true to break out of the loop.
                        l_name_ok = my_account.validateCountry(l_name)
                    #Updating the database with the new value. 
                    my_db.executeQuery("UPDATE account_list SET "+"l_name="+"\'"+l_name+"\'"+
                    " WHERE user_id ="+"\'"+user_id+"\'")
                else:
                    print("Sorry, didn't get that, please try again!")
