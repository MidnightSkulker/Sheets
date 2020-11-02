# Functions to manipulate Google Sheets
from sheetfu import *
import re
from webcolors import *

red = '#ff0000'
blue = '#0000ff'
green = '#37761c'
purple = '#9900ff'
black = '#000000'
colorsToIgnore = [red, blue, green, purple]
namesToIgnore = ['Totals', 'Remaining', 'Check Sum', 'Paid', 'Debt']
monthRow = 2

# Determine the payment status
def paymentStatus(amount: str, color: str) -> str:
    status = 'Unknown'
    if amount == None or amount == '':
        status = 'No Charge'
    elif color == black: # Black
        status = 'Due'
    elif color == blue:
        status = 'Paid'
    elif color == purple:
        status = 'Debt Payback'
    elif color == green:
        status = 'Cash'
    return status

# Find a column for the specified month
def getMonthCol(data_range: object, month: str) -> int:
    values = data_range.get_values()
    maxCol = data_range.get_max_column()
    for j in range(0, maxCol):
        cellValue = values[monthRow][j]
        if re.match(month, cellValue): return j
    return None

# Load the spreadsheet for Grace's classes from Google Sheets
def loadGrace ():
    sa = SpreadsheetApp('service_account.json')
    spreadsheet = sa.open_by_id('1fLDy8hmgYdxYvQPhbi6DFL0BqR8hvlvK2YaA7vgoEzc')
    sheet = spreadsheet.get_sheet_by_name('GracesClass')
    data_range = sheet.get_data_range()
    return data_range

def getStudentSheetInfo(data_range: object, month: int) -> list:
    values = data_range.get_values()
    colors = data_range.get_font_colors()
    maxRow = data_range.get_max_row()
    # Determine which column is for the month requested.
    monthCol = getMonthCol(data_range, month)
    if monthCol == None: return None
    names = []
    for j in range(0,maxRow):
        potentialStudent = values[j][0] # Student Name
        attendanceStatus = values[j][1] # Gone or Break
        charge = values[j][monthCol]
        chargeColor = colors[j][monthCol]
        if str(potentialStudent).isnumeric(): continue
        if potentialStudent is None or potentialStudent == '': continue
        if potentialStudent in namesToIgnore: continue
        color = colors[j][0]
        if color in colorsToIgnore: continue
        if (attendanceStatus == 'Break') or (attendanceStatus == 'Gone'): continue
        if not chargeColor: chargeColor = '#000000' # black
        chargeStatus = paymentStatus(charge, chargeColor)
        try:
            chargeColor = hex_to_name(chargeColor)
        except:
            if chargeColor == '#9900ff': chargeColor = 'purple'
            else:
                print('ERROR: Charge Color ', chargeColor)
                chargeColor = 'purple'

        studentInfo = { 'name': potentialStudent
                      , 'charge': charge
                      , 'color': chargeColor
                      , 'status': chargeStatus }
        names.append(studentInfo)
    return names
        
# Read the first column, and get all the student names and their row numbers.
def printStudents(data_range: object):
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
        print({'row': j, 'name': potentialStudent})
    
# Read specified 2 columns from a specified range of columns.
def get2Columns(sheet: object, rge: list) -> list:
    # Call the Sheets API
    sheet = service.spreadsheets()
    # Get the range of columns
    result = sheet.values().get(spreadsheetId=sheetId, range = rge).execute()
    values = result.get('values', [])
    return values

# Find a column for the specified month
def getMonthCol(data_range: object, month: str) -> int:
    values = data_range.get_values()
    maxCol = data_range.get_max_column()
    for j in range(0, maxCol):
        cellValue = values[monthRow][j]
        if re.match(month, cellValue): return j
    return None

    
