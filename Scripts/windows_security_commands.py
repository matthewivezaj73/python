import subprocess
#Ask the user to enter a task number.
print("Please enter the PID.")
#Asking the user for input.
task_number = input("")
#Running the dir command
subprocess.run('taskkill /F /PID '+task_number, text=True)
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