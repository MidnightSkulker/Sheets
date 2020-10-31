# Test code for the SMTP server
import smtplib, ssl
from src.Email import *

port = 465  # For SSL
# password = input('Type your password and press enter: ')
# print('password: ', password)

# Create a secure SSL context
context = ssl.create_default_context()

pw = getEmailPassword()
print('pw:', pw)

server = getSMTP_SSL(pw)

