#!/usr/bin//python3
from sheetfu import SpreadsheetApp
from src.Sheets import *
from src.Students import *

# ---- Google Sheets
# Load the sheet for Grace's class from Google Sheets.
sheet = loadGrace()
# Print out the students from the sheet.
studentNames = getStudentNames(sheet)

# ---- Student Information from Address Book
# Read in the .json file with the student information, and convert it to a dictionary.
studentData = getStudents('outputs/students.json')
# Now get the email addresses
namesAndEmails = getStudentsAndEmails(studentNames, studentData)
# print(namesAndEmails)

# this is how you set things
# data_range.set_background('#000000')          # set every cell backgrounds to black
# data_range.set_font_color('#ffffff')          # set every cell font colors to white


