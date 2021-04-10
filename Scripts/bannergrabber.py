#!/usr/bin/python
import urllib.request as urllib2, sys, time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", dest="iprange",help="target IP range, i.e. 192.168.1.1-25")
parser.add_option("-p", dest="port",default="80",help="port, default=80")
parser.add_option("-d", dest="delay", default=".5", help="delay (in seconds), default = .5 seconds")

(opts, args) = parser.parse_args()

if opts.iprange is None:
    parser.error("you must supply an IP range")

ips = []
headers = {}

octets = opts.iprange.split('.')

start = octets[3].split('-')[0]
stop = octets[3].split('-')[1]

for i in range(int(start), int(stop) +1):
    ips.append('%s.%s.%s.%d' % (octets[0],octets[1],octets[2],i))

print("\nScanning IPS: %s\n" % (ips))

for ip in ips:
    try:
        response = urllib2.urlopen('https://%s:%s' % (ip,opts.port))
        headers[ip] = dict(response.info())
    except Exception as e:
        headers[ip] = "Error: " + str(e)

    time.sleep(float(opts.delay))

for header in headers:
    try:
        print('%s : %s' % (header,headers[header].get('server')))
    except:
        print("%s : %s" % (header,headers[header]))