import subprocess
#Asking the user for the IP address that they want to scan.
print("What is the IP address that you want to scan?")
#Allowing for input and assigning the input to ip_address.
ip_address = input("")
#Writing the output to a new file.
with open('nmap_output', 'w+') as netoutput:
	netout = subprocess.run(['\"'+'nmap' + ip_address +'\"'])