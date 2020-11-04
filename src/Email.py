import sys
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

# Construct the email with the amount due.
def mkEmail(fromEmail: str, targetEmail: str, month: str, student: dict) -> object:
    message = MIMEMultipart("alternative")
    message['Subject'] = month + ' tuition statement for ' + student['name']
    message['From'] = 'AngelsAcademyOnline@gmail.com'
    message['To'] = targetEmail
    text = 'The tuition for ' + student['name'] + ' for the month of ' + month + ' is $' + str(student['charge']) + '\n' + 'You can pay using zelle pay with email id gracetwhite@gmail.com'
    part1 = MIMEText(text, 'plain')
    message.attach(part1)
    return message

# Add the student name after a '+' to the username portion of the email address.
# For example: gracetwhite@gmail.com ---> gracetwhite+arnav@gmail.com
def addStudentNameToEmail(toEmail: str, name: str) -> str:
    emailParts = toEmail.split('@')
    if len(emailParts) == 2:
        return emailParts[0] + '+Student_' + name.replace(' ','') + '@' + emailParts[1]
    else:
        return toEmail
    
# Based on the mode, create the target Email address.
def mkTargetEmail(mode: str, toEmail: str, studentEmail: str, name: str) -> str:
    augmentedToEmail = addStudentNameToEmail(toEmail, name)
    if mode == 'Preview':
        return augmentedToEmail
    elif mode == 'Live':
        return studentEmail + ',' + augmentedToEmail
    else:
        print('Invalid mode:', mode)
        sys.exit(2)

# Send a single Email with invoice.
def sendEmailToStudent(mode: str, fromEmail: str, toEmail: str, student: dict, month: str):
    port = 465  # For SSL
    pw = getEmailPassword()
    targetEmail = mkTargetEmail(mode, toEmail, student['email'], student['name'].strip())
    print('targetEmail = ', targetEmail, toEmail, student['email'])
    message = mkEmail(fromEmail, targetEmail, month, student)
    server = getSMTP_SSL(pw)
    server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', message.as_string())
    server.close

# Send invoices to all the students.
def sendEmailsToStudents(mode: str, fromEmail: str, toEmail: str, students: list, month: str):
    port = 465  # For SSL
    pw = getEmailPassword()
    server = getSMTP_SSL(pw)
    for student in students:
        if student['status'] == 'Due':
            targetEmail = mkTargetEmail(mode, 'gracetwhite@gmail.com', student['email'], student['name'])
            print('targetEmail = ', targetEmail)
            message = mkEmail(fromEmail, targetEmail, month, student)
            print('message = ', message)
            # server.sendmail('AngelsdAcademyOnline@gmail.com', targetEmail, message.as_string())
        else:
            continue
    server.close()
    
def sendOneEmail(server: object, record:dict):
    server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', str(record))
