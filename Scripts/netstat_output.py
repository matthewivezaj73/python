import subprocess
with open('netstat_output.txt','w+') as netstat_output:
    net_output = subprocess.run('netstat', stdout=netstat_output, text=True)