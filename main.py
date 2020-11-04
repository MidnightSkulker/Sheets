#!/usr/bin//python3
import sys
import argparse
from sheetfu import SpreadsheetApp
from src.Sheets import *
from src.Students import *
from src.Email import *

# https://docs.python.org/2/library/argparse.html
# ---- Parse the command line arguments
# Define the parser for the command line options.
argumentParser = argparse.ArgumentParser(description='Issue Invoices for Angels Academy Online')
argumentParser.add_argument('--SheetID', help='Id of Spreadsheet (part of the URL)')
argumentParser.add_argument('--SheetName', help='Name of Google Sheet to Parse')
argumentParser.add_argument('--Mode', help='Live or Preview: Live sends the emails to customers, preview sends the email to us')

# Now parse the arguments passed in.
parsedArguments = argumentParser.parse_args()

# Debug
print('---> parsed Arguments:', parsedArguments)
print('---> Mode', parsedArguments.Mode)
print('---> SheetId', parsedArguments.SheetID)
print('---> SheetName', parsedArguments.SheetName)
if not parsedArguments.Mode in ['Live', 'Preview']:
    print('Invalid Mode:', parsedArguments.Mode)
    sys.exit(2)

# ---- Google Sheets
# Load the sheet for Grace's class from Google Sheets.
data_range = loadSheet(parsedArguments.SheetID, parsedArguments.SheetName)
if data_range:
    # Print out the students from the sheet.
    studentRecords = getStudentSheetInfo(data_range, 'Oct')
    # ---- Student Information from Address Book
    # Read in the .json file with the student information, and convert it to a dictionary.
    studentData = getStudents('outputs/students.json')
    # Now get the email addresses
    students = getStudentsAndEmails(studentRecords, studentData)
    printStudentRecords(students)
else:
    print('Could not open', parsedArguments,sheetID, parsedArguments.sheetName)
    sys.exit(1)

student = students[0]
print('---> student', student)
target = mkTargetEmail(parsedArguments.Mode, 'gracetwhite@gmail.com', student['email'], student['name'])
print('---> target', target)
email = mkEmail('AngelsdAcademyOnline@gmail.com', target, 'October', student)
print('---> email', email)
print('\n----------> Almost Emails\n')
sendEmailsToStudents(parsedArguments.Mode, 'AngelsdAcademyOnline@gmail.com', 'gracetwhite@gmail.com', students, 'October')
# desourdesourde@gmail.com,gracetwhite+Student_AadhyaChiranji@gmail.com
