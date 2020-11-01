import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

def mkEmail(password:list, month: str, student: dict) -> object:
    message = MIMEMultipart("alternative")
    message['Subject'] = month + ' tuition statement for ' + student['name']
    message['From'] = 'AngelsAcademyOnline@gmail.com'
    message['To'] = 'gracetwhite' + '+' + student['name'] + '@gmail.com'
    text = 'The tuition for ' + student['name'] + ' for the month of ' + month + ' is $' + student['charge'] + '\n' + str(student)
    part1 = MIMEText(text, 'plain')
    message.attach(part1)
    return message

# Send emails to students parents with status 'Due' and non zero charges.
def sendEmails(studentRecords:list):
    server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', 'High Their90!')

def sendOneEmail(server: object, record:dict):
    server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', str(record))
