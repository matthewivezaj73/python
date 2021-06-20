#!/usr/bin/python 
import smtplib, string
import os, time

os.system("/etc/init.d/sendmail start")
time.sleep(4)

HOST = "localhost"
SUBJECT = "Email from spoofed sender"
TO = "daveschippers@walshcollege.edu"
FROM = "mlevens@walshcollege.edu"
TEXT = "Staff, please click this link to view the upcoming changes to the buili."
BODY = string.join((
        "From: %s" % FROM, 
        "",
        TEXT
        ), "\r\n")
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()

time.sleep(4)
os.system("/etc/init.d/sendmail stop")
