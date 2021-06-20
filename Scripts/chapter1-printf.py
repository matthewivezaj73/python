#Matthew Ivezaj
#Imported libraries
from ctypes import *
#Asking the user for input
which_print = input("Would you like to print your message to the user using standard print"+
" or printf? Enter 'standard' for standard print or 'f' for printf")
#If the user selects option f.
if which_print.lower() == 'f':
    msvcrt = cdll.msvcrt
    message_string = "Here, I am printing to you utilizing the printf operator!\n"
    msvcrt.printf("Testing: %s", message_string)
#If the user selects option standard.
elif which_print.lower() == "standard":
    print("Here I am printing to you from a standard print operator!")
#if the user does anything else.
else:
    print("Sorry, didn't get that, we are now exiting the program!")