#Setting a flag.
not_profile = False
#Testing for the customer profile.
while not not_profile:
    #Opening the text file for reading.
    customername = open('listofnames.txt')
    #Reading each line in the text file.
    customer_name = customername.read()
    #Setting a flag.
    not_name = False
    #Testing for the account number.
    while not not_name:
        #Asking the user for the account number.
        name = input("Please enter your name: ")
        #If the account number that the user enters is truly the account number read from the file.
        if name == customer_name:
            print("That is the correct name!")
            #If the user enters 123
            if name == "Matt":
                print("That is a nice name!")
            #Setting the flag to true to break out of the loop
            not_name = True
        else:
            print("That is not a proper account number, please try again!")
    #Opening the text file for reading.
    customerdob = open('listofdob.txt')
    #Reading each line in the text file.
    customer_dob = customerdob.read()
    #Setting a flag.
    not_dob = False
    #Testing for the account number.
    while not not_dob:
        #Asking the user for the account number.
        dob = input("Please enter your date of birth: ")
        #If the account number that the user enters is truly the account number read from the file.
        if dob == customer_dob:
            print("That is the correct date of birth!")
            #If the user enters 123
            if dob == "01-31-2000":
                print("I have your date of birth down as: "+dob)
            #Setting the flag to true to break out of the loop
            not_dob = True
        else:
            print("That is not a date of birth, please try again!")
    #Opening the text file for reading.
    accountNumber = open('myAccountNumber.txt')
    #Reading each line in the text file.
    account_number = accountNumber.read()
    #Setting a flag.
    not_account = False
    #Testing for the account number.
    while not not_account:
        #Asking the user for the account number.
        my_account_number = input("Please type in your account number: ")
        #If the account number that the user enters is truly the account number read from the file.
        if my_account_number == account_number:
            print("That is the correct account number!")
            #If the user enters 123
            if my_account_number == "123":
                print("That is an account number that idiots use!")
            #Setting the flag to true to break out of the loop
            not_account = True
        else:
            print("That is not a proper account number, please try again!")
