# Test code for the SMTP server
import smtplib, ssl
from src.Email import *
from src.Students import *

port = 465  # For SSL
# password = input('Type your password and press enter: ')
# print('password: ', password)

# Create a secure SSL context
context = ssl.create_default_context()

pw = getEmailPassword()
print('pw:', pw)

student = {'name': 'Tejas', 'charge': '90', 'color': 'black', 'status': 'Due', 'email': 's.roopaa@gmail.com'}
message = mkEmail(pw, 'October', student)
studentstr = str(student)
studentstr2 = student['name'] + ' - ' + student['email'] + ' - ' + student['status']  + ' - $' + student['charge']
print('studentstr', studentstr)

server = getSMTP_SSL(pw)

server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', outStudent(student))
server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', message.as_string())
server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', 'High Their!')

server.close()



