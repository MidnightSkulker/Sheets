#!/usr/bin//python3
from sheetfu import SpreadsheetApp
from src.Sheets import *
from src.Students import *

# ---- Google Sheets
# Load the sheet for Grace's class from Google Sheets.
data_range = loadGrace()
# Print out the students from the sheet.
studentRecords = getStudentSheetInfo(data_range, 'Oct')

# ---- Student Information from Address Book
# Read in the .json file with the student information, and convert it to a dictionary.
studentData = getStudents('outputs/students.json')
# Now get the email addresses
namesAndEmails = getStudentsAndEmails(studentRecords, studentData)



