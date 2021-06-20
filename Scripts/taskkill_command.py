#importing the subprocess library to run windows commands.
import subprocess
#Setting a flag
not_done = False
#Testing for the command.
while not not_done:
    #Asking the user a question.
    # print("Would you like to show a current list of tasks or kill one?")
    # #Giving the user choices and allowing them to enter input.
    # selection = input("Please enter L to list tasks or K to kill tasks: ")
    # if selection.lower == "k":
    #Ask the user to enter a task number.
    print("Please enter the PID.")
    #Asking the user for input.
    task_number = input("")
    #Running the taskkill /F command
    subprocess.run('taskkill /F /PID '+task_number, text=True)
    #Asking the user if they would like to kill another task.
    print("Would you like to kill another task?")
    #Gathering user response.
    my_answer = input("Please enter Y for yes or N for no: ")
    #If the user selects y for yes.
    if my_answer.lower() == "y":
        #Notifying the user that a new list of current tasks will appear.
        print("Here is a list of the current tasks: ")


    #     #If the user selects n for no.
    #     elif my_answer.lower() == "n":
    #         #Notifying the user that the program is ending.
    #         print("Ending the program...")
    #         #Setting the flag to true to break out of the loop and end the program.
    #         not_done = True
    # elif selection.lower == "l":
    #     #Calling the tasklist command
    #     listtasks = subprocess.check_output(['tasklist']).split("\r\n")
    #     p = []
    #     for task in listtasks:
    #         my_var = 1
    #         print(my_var+". "+task + "\n")
    #         my_var = my_var + 1










    #Telling the user to enter the path of their directory in.
    # print("Enter the path that you would like to change your directory to.")
    # #####################Starting the Try/except block##################### 
    # try:
    #     #Asking the user for input.
    #     current_directory = input("")
    #     #Using the cd command to the users desired directory
    #     subprocess.run('cd'+current_directory)
    # #Handling the exception where the directory does not exist.
    # except:
    #     print("Sorry, but that directory does not exist!")
    # #calling the hostname command
    # subprocess.run('cd'+current_directory)