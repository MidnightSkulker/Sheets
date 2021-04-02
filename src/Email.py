import sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.Email import *

# We get a list of student records that look like this:
# {'name': 'Tejas', 'charge': '', 'color': 'black', 'status': 'No Charge', 'email': 's.roopaa@gmail.com'}
#
# We send a message to each student with a statue of 'Due', and a non-zero charge.

# Create a secure SSL context for sending Email.
def getSMTP_SSL(password: str) -> object:
    port = 465  # For SSL
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL('smtp.gmail.com', port, context=context)
    server.login('AngelsAcademyOnline@gmail.com', password)
    print('Logged in!')
    return server

# Fetch the Email password from a file (which is not part of the repository).
def getEmailPassword() -> str:
    with open ("pw", "r") as pwfile:
        data = pwfile.readline().strip()
    return data

# Make a subject string based on the mode
def mkSubject(reminder: bool, month: str, student: dict) -> str:
    common = month + ' tuition statement for ' + student['name']
    if reminder:
        return 'Reminder: ' + common
    else:
        return common

# Construct the email with the amount due.
# ToDo: Change this the HTML format.
def mkEmail(fromEmail: str, targetEmail: str, month: str, student: dict, reminder: bool) -> object:
    message = MIMEMultipart("alternative")
    message['Subject'] = mkSubject(reminder, month, student)
    message['From'] = 'AngelsAcademyOnline@gmail.com'
    message['To'] = targetEmail
    remind = 'Reminder, ' if reminder else ''
    thisMonthTuitionStatement = 'The tuition for ' + student['name'] + ' for the month of ' + month + ' is $' + str(student['charge']) +'.\n'
    if student['previousChargeOwed']:
        print('mkEmail student ', student['name'])
        previousMonth = 'Reminder, payment is still due for the previous month\'s charges of $' + str(student['previousCharge']) + '.\n'
        totalCharge = int(student['charge']) + int(student['previousCharge'])
        totalChargeStatement = 'The total charges are $' + str(totalCharge) + '.\n'
        tuitionStatement = thisMonthTuitionStatement + previousMonth + totalChargeStatement
    else:
        previousMonth = ''
        totalCharge = str(student['charge'])
        tuitionStatement = thisMonthTuitionStatement
    zellePay = 'You can pay using zelle pay with email id ' + 'gracetwhite@gmail.com.\n' + 'Please include your child\'s name in the description part of the payment.\n'
    angelsEIN = 'Angels Academy EIN is 54-2192560.\n'
    text = remind + tuitionStatement + zellePay + angelsEIN
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
# The toEmail will the augmented with the student name, so when we receive
# our copy of the email, we can tell that it was sent to the right place.
def mkTargetEmail(mode: str, toEmail: str, studentEmail: str, name: str) -> str:
    augmentedToEmail = addStudentNameToEmail(toEmail, name)
    if mode == 'Preview':
        return augmentedToEmail
    elif mode == 'Live':
        return studentEmail + ',' + augmentedToEmail
    else:
        print('Invalid mode:', mode)
        sys.exit(2)

# Send invoices to all the students.
def sendEmailsToStudents(mode: str,
    reminder: bool,
    fromEmail: str,
    toEmail: str,
    students: list,
    month: str):
    pw = getEmailPassword()
    server = getSMTP_SSL(pw)
    for student in students:
        if student['status'] == 'Due':
            if student['email'] == 'NO EMAIL':
                print('----->>', student['name'], 'has no email ***')
                continue
            targetEmail = mkTargetEmail(mode, 'gracetwhite@gmail.com', student['email'], student['name'])
            print('targetEmail = ', targetEmail)
            message = mkEmail(fromEmail, targetEmail, month, student, reminder)
            print('message = ', message)
            server.sendmail('AngelsdAcademyOnline@gmail.com', targetEmail, message.as_string())
        else:
            continue
    server.close()
