# Test code for the SMTP server
import smtplib, ssl

port = 465  # For SSL
password = input('Type your password and press enter: ')
print('password: ', password)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login('AngelsAcademyOnline@gmail.com', password)
    print('Logged in!')
    # TODO: Send email here
    server.sendmail('AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', 'High Their!')

