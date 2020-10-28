# Functions to manipulate Google Sheets
from sheetfu import *

red = '#ff0000'
blue = '#0000ff'
green = '#37761c'
purple = '#9900ff'
colorsToIgnore = [red, blue, green, purple]
namesToIgnore = ['Totals', 'Remaining', 'Check Sum', 'Paid', 'Debt']
monthRow = 2

# Load the spreadsheet for Grace's classes from Google Sheets
def loadGrace ():
    sa = SpreadsheetApp('service_account.json')
    spreadsheet = sa.open_by_id('1fLDy8hmgYdxYvQPhbi6DFL0BqR8hvlvK2YaA7vgoEzc')
    sheet = spreadsheet.get_sheet_by_name('GracesClass')
    return sheet

def getStudentNames(sheet: object) -> list:
    data_range = sheet.get_data_range()
    values = data_range.get_values()
    colors = data_range.get_font_colors()
    maxRow = data_range.get_max_row()
    names = []
    for j in range(0,maxRow):
        potentialStudent = values[j][0]
        if str(potentialStudent).isnumeric(): continue
        if potentialStudent is None or potentialStudent == '': continue
        if potentialStudent in namesToIgnore: continue
        color = colors[j][0]
        if color in colorsToIgnore: continue
        names.append((j, potentialStudent))
    return names
        
# Read the first column, and get all the student names and their row numbers.
def printStudents(sheet: object):
    data_range = sheet.get_data_range()
    values = data_range.get_values()
    colors = data_range.get_font_colors()
    maxRow = data_range.get_max_row()
    for j in range(0,maxRow):
        potentialStudent = values[j][0]
        if str(potentialStudent).isnumeric(): continue
        if potentialStudent is None or potentialStudent == '': continue
        if potentialStudent in namesToIgnore: continue
        color = colors[j][0]
        if color in colorsToIgnore: continue
        print((j, potentialStudent))
    

# Read specified 2 columns from a specified range of columns.
def get2Columns(sheet: object, rge: list) -> list:
    # Call the Sheets API
    sheet = service.spreadsheets()
    # Get the range of columns
    result = sheet.values().get(spreadsheetId=sheetId, range = rge).execute()
    values = result.get('values', [])
    return values

# Print the month row
def printMonthRow(service, sheetId: str, mr:int):
    data_range = sheet.get_data_range()
    values = data_range.get_values()
    maxCol = data_range.get_max_col()
    for j in range(0, maxCol):
        print(j, data_range.get_values()[mr][j])

# Find a column for the specified month
