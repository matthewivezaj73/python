# Python Script written by Matthew Ivezaj
import os
import csv
import subprocess
import datetime
import optparse

now=datetime.datetime.now()
filename = now.strftime("%Y%m%d%H%M") + 'export.txt'
def netstat():
    try:
        logfile=open(filename,'a')
    except IOError:
        logfile=open(filename,'w')
    logfile.close()

    output = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
    newlines = output[0].split('\r\n') #Identify the string that marks the end of a line
    
    for line in newlines:
        if line.find("Foreign") != -1:
            print(line)
            logfile.write(line + '\n')
        if line.find("ESTABLISHED") != -1:
            print(line)
            logfile.write(line + '\n')


    logfile.close()

def main():
    #This function to kick off the process
    parser = optparse.OptionParser('This script runs common Windows commands')
    parser.add_option('-n', action='store_true', dest='net', default=False, help='calls netstat output')
    parser.add_option('-a', action='store_true', dest='arp', default=False, help='calls arp output')
    parser.add_option('-u', action='store_true', dest='netuser', default=False, help='calls netuser output')
    parser.add_option('-A', action='store_true', dest='allcommands', default=False, help='calls all available comand outputs')
    (options,args) = parser.parse_args()
    net = options.net
    arp = options.arp
    netuser = options.netuser
    allcommands = options.allcommands
    
    if net == True:
        netstat()
    if arp == True:
        arp()
    if netuser == True:
        netuser()
    if allcommands == True:
        allcommands()
    if __name__ == '__main__':
        main()

print('Script complete')
