import sys
import argparse
from sheetfu import SpreadsheetApp
from src.Sheets import *
from src.Students import *
from src.Email import *
from src.Months import *

# https://docs.python.org/2/library/argparse.html
# ---- Parse the command line arguments
# Define the parser for the command line options.
argumentParser = argparse.ArgumentParser(description='Issue Invoices for Angels Academy Online')
argumentParser.add_argument('--SheetID', help='Id of Spreadsheet (part of the URL)')
argumentParser.add_argument('--SheetName', help='Name of Google Sheet to Parse')
argumentParser.add_argument('--Month', help='Month for invoices to process')
argumentParser.add_argument('--Mode', help='Live or Preview: Live sends the emails to customers, preview sends the email to us')
argumentParser.add_argument("-v", "--Reminder", help="Make it a reminder email", action="store_true")

# Now parse the arguments passed in.
parsedArguments = argumentParser.parse_args()

# Debug
print('---> parsed Arguments:', parsedArguments)
print('---> Mode =', parsedArguments.Mode)
print('---> Month =', parsedArguments.Month)
print('---> SheetId =', parsedArguments.SheetID)
print('---> SheetName =', parsedArguments.SheetName)
print('---> Reminder =', parsedArguments.Reminder)

if not parsedArguments.Mode in ['Live', 'Preview']:
    print('Invalid Mode:', parsedArguments.Mode)
    sys.exit(2)
if not parsedArguments.Month in months.keys():
    print('Invalid Month:', parsedArguments.Month)
    sys.exit(3)

# ---- Google Sheets
# Load the sheet for Grace's class from Google Sheets.
data_range = loadSheet(parsedArguments.SheetID, parsedArguments.SheetName)
if data_range:
    # Print out the students from the sheet.
    studentRecords = getStudentSheetInfo(data_range, parsedArguments.Month)
    # ---- Student Information from Address Book
    # Read in the .json file with the student information, and convert it to a dictionary.
    studentData = getStudents('outputs/students.json')
    # Now get the email addresses
    students = getStudentsAndEmails(studentRecords, studentData)
    printStudentRecords(students)
else:
    print('Could not open', parsedArguments.SheetID, parsedArguments.SheetName)
    sys.exit(1)

# student = students[0]
# print('---> student', student)
# target = mkTargetEmail(parsedArguments.Mode, 'gracetwhite@gmail.com', student['email'], student['name'])
# print('---> target', target)
# email = mkEmail('AngelsdAcademyOnline@gmail.com', target, 'October', student)
# print('---> email', email)
# print('\n----------> Almost Emails\n')
numberSent = sendEmailsToStudents(parsedArguments.Mode,
    parsedArguments.Reminder,
    'AngelsdAcademyOnline@gmail.com',
    'gracetwhite@gmail.com',
    students,
    months[parsedArguments.Month])
print('---> Number of emails sent: ', numberSent, '\n')
# desourdesourde@gmail.com,gracetwhite+Student_AadhyaChiranji@gmail.com
