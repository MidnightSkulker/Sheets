#!/usr/bin//python3
from sheetfu import SpreadsheetApp
from src.Sheets import *
from src.Students import *

# ---- Google Sheets
# Load the sheet for Grace's class from Google Sheets.
sheet = loadGrace()
# Print out the students from the sheet.
studentNames = getStudentNames(sheet)
print(studentNames)
print('\n')

# ---- Student Information from Address Book
# Read in the .json file with the student information, and convert it to a dictionary.
studentData = getStudents('outputs/students.json')
# Do a test lookup for Aadhya Chiranji
aadhya = findStudent(studentData, 'Aadhya C')
print('Aadhya: ', aadhya)
print('\n')
# Now get the email addresses
namesAndEmails = getStudentsAndEmails(studentNames, studentData)
print(namesAndEmails)

# data_range = sheet.get_data_range()           # returns the sheet range that contains data values.
# this is how you get things
# values = data_range.get_values()              # returns a 2D matrix of values.
# backgrounds = data_range.get_backgrounds()    # returns a 2D matrix of background colors in hex for
# colors = data_range.get_font_colors()



# this is how you set things
# data_range.set_background('#000000')          # set every cell backgrounds to black
# data_range.set_font_color('#ffffff')          # set every cell font colors to white


