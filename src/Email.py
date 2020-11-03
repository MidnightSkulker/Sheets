import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.Email import *

# We get a list of student records that look like this:
# {'name': 'Tejas', 'charge': '', 'color': 'black', 'status': 'No Charge', 'email': 's.roopaa@gmail.com'}
#
# We send a message to each student with a statue of 'Due', and a non-zero charge.

port = 465  # For SSL

# Create a secure SSL context
def getSMTP_SSL(password: str) -> object:
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL('smtp.gmail.com', port, context=context)
    server.login('AngelsAcademyOnline@gmail.com', password)
    print('Logged in!')
    return server

def getEmailPassword() -> str:
    with open ("pw", "r") as pwfile:
        data = pwfile.readline().strip()
    return data

def mkEmail(fromEmail: str, toEmail: str, month: str, student: dict) -> object:
    message = MIMEMultipart("alternative")
    message['Subject'] = month + ' tuition statement for ' + student['name']
    message['From'] = 'AngelsAcademyOnline@gmail.com'
    message['To'] = student['email'] + ', ' + 'gracetwhite@gmail.com'
    text = 'The tuition for ' + student['name'] + ' for the month of ' + month + ' is $' + str(student['charge']) + '\n' + 'You can pay using zelle pay with email id gracetwhite@gmail.com'
    part1 = MIMEText(text, 'plain')
    message.attach(part1)
    return message

# Send a single Email with invoice.
def sendEmailToStudent(server: object, fromEmail: str, toEmail: str, student: dict, month: str):
    message = mkEmail(fromEmail, toEmail, month, student)
    server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', message.as_string())

# Send invoices to all the students.
def sendEmailsToStudents(fromEmail: str, toEmail: str, students: list, month: str):
    port = 465  # For SSL
    pw = getEmailPassword()
    print('pw:', pw)
    server = getSMTP_SSL(pw)
    for student in students:
        if student['status'] == 'Due':
            message = mkEmail(fromEmail, toEmail, month, student)
            print(student['email'])
            server.sendmail('AngelsdAcademyOnline@gmail.com', student['email'], message.as_string())
        else:
            continue
    server.close()
    
def sendOneEmail(server: object, record:dict):
    server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', str(record))
