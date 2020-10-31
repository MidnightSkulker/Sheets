import smtplib, ssl

# We get a list of student records that look like this:
# {'name': 'Tejas', 'charge': '', 'color': 'black', 'status': 'No Charge', 'email': 's.roopaa@gmail.com'}
#
# We send a message to each student with a statue of 'Due', and a non-zero charge.

port = 465  # For SSL

# Create a secure SSL context
def getSMTP_SSL(password: str) -> object:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login('AngelsAcademyOnline@gmail.com', password)
        print('Logged in!')
        return server

def getEmailPassword() -> str:
    with open ("pw", "r") as pwfile:
        data = pwfile.readline().strip()
    return data

# Send emails to students parents with status 'Due' and non zero charges.
def sendEmails(studentRecords:list):
    server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', 'High Their!')
