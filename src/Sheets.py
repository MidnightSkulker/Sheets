# Functions to manipulate Google Sheets
from sheetfu import *

red = '#ff0000'
blue = '#0000ff'
green = '#37761c'
purple = '#9900ff'
colorsToIgnore = [red, blue, green, purple]
namesToIgnore = ['Totals', 'Remaining', 'Check Sum', 'Paid', 'Debt']

# Read the first column, and get all the student names and their row numbers.
def getStudents(sheet: object):
    data_range = sheet.get_data_range()
    values = data_range.get_values()
    maxRow = data_range.get_max_row()
    for j in range(0,maxRow):
        potentialStudent = data_range.get_values()[j][0]
        if str(potentialStudent).isnumeric(): continue
        if potentialStudent is None or potentialStudent == '': continue
        if potentialStudent in namesToIgnore: continue
        color = data_range.get_font_colors()[j][0]
        if color in colorsToIgnore: continue
        print((j, potentialStudent))
    

# Read specified 2 columns from a specified range of columns.
def get2Columns(service, sheetId: str, rge: list) -> list:
    # Call the Sheets API
    sheet = service.spreadsheets()
    # Get the range of columns
    result = sheet.values().get(spreadsheetId=sheetId, range = rge).execute()
    values = result.get('values', [])
    return values
