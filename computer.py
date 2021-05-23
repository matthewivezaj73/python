computer_one = {'computer_name': 'Dell Precision 7750', 'Rating': '7.5/10',
                  'Manufacturer': 'Dell', 'Release_Year': '2019',
                   'color': 'gray', 'core': 'i9'}
#Printing out the components of the first computer.
for key, value in computer_one.items():
    print(key, value)

#Creating a second computer
computer_two = {
    'computer_name': 'Dell Precision 7740', 'Rating': '8.5/10',
    'Manufacturer': 'Dell', 'Release_Year': '2019',
    'core': 'i9' 
}
#Printing out the components of the second computer.
for word, definition in computer_two.items():
    print("\n" + word + ": " + definition)

#Changing the value o the core on the irst computer.
computer_one['core'] = "i7"
#Printing a message telling tfhe user what the value of the core on the computer is.
print("The core on"+computer_one["computer_name"]+": " + computer_one['core'])
