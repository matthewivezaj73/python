#Importing the subprocess library.
import subprocess

#Asking the user to enter a command to run.
print("Please enter a windows command to run it: ")
#Asking for input from the user.
command = input("")
#If the user selects the dir command.
if command.lower() == "dir":
    #running the dir command
    subprocess.run('dir', shell=True)
#If the user selects systeminfo.
elif command.lower() == "systeminfo":
    #Asking the user if they would like to save the output to a file.
    print("Would you like to save this process output to a file: (y/n)?")
    #asking for the users input.
    save_to_file = input("")
    #If the user selects y for yes.
    if save_to_file.lower() == "y":
        #Creating a file for the output to go to.
        with open('sysinfo_output.txt','w+') as sysinfo_output:
            #Assinging the variable sys_info to the subprocess
            sys_info = subprocess.run('systeminfo', stdout=sysinfo_output, text=True)
    #If the user selects n for no.
    elif save_to_file.lower() == "n":
        #running the command
        subprocess.run('systeminfo')
    else:
        #N0tifying the user that something went wrong.
        print("Something went wrong here...")
#If the user enters nslookup
elif command.lower() == "nslookup":
    #Running the nslookup command
    subprocess.run('nslookup', text=True)
#If the user enters getmac.
elif command.lower() == "getmac":
    #Running the subprocess command.
    subprocess.run('getmac', text=True)
    #Assigning the output to a variable.
    mac_data = subprocess.run('getmac', text=True)





####Part to add next####
    #Asking the user a question.
    #print("Would you like to save to a file?")
    #Asking for the user to enter input.

    # open_file = input("")
    # if open_file.lower() == "y":
    #     with open("mac_data.txt", "w+") as file_object:
    #         for line in mac_data:
    #             file_object.write(line)
