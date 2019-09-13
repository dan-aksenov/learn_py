#!/bin/python
import smtplib
from getopt import getopt
import sys

frm = ''
gmail_user = ''
gmail_pwd = ''

smtpserver = smtplib.SMTP( "smtp.gmail.com", 587 )
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_pwd)

header = 'To: A \n' + 'From: B \n' + 'Subject:stuff \n'
msg = header
smtpserver.sendmail(frm, '', msg)
smtpserver.close()