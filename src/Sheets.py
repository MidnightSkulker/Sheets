# Functions to manipulate Google Sheets
from sheetfu import *
import re
from webcolors import *

red = '#ff0000'    # Ignore this cell
blue = '#0000ff'   # Paid
green = '#37761c'  # Paid Cash
purple = '#9900ff' # Paid off with debt from March
black = '#000000'  # Due
colorsToIgnore = [red, blue, green, purple] # Colors ignore in the student names column.
namesToIgnore = ['Totals', 'Remaining', 'Check Sum', 'Paid', 'Debt'] # Names to ignore in the student names Column.
# Row containing the months (Sep, Oct, ...)
# This needs to be followed in each spreadSheet
monthRow = 0 # I.e. the first row of the sheet

# Determine the payment status, based on the color of the entry.
def paymentStatus(amount: str, color: str) -> str:
    status = 'Unknown'
    if amount == None or amount == '':
        status = 'No Charge'
    elif color == black:
        status = 'Due'
    elif color == blue:
        status = 'Paid'
    elif color == purple:
        status = 'Debt Payback'
    elif color == green:
        status = 'Cash'
    return status

# Find a column for the specified month in the row that has month headings.
def getMonthCol(data_range: object, month: str) -> int:
    values = data_range.get_values()
    maxCol = data_range.get_max_column()
    for j in range(0, maxCol):
        cellValue = values[monthRow][j]
        if re.match(month, cellValue): return j
    return None

# Load the spreadsheet for Grace's classes from Google Sheets
def loadSheet (sheetId: str, sheetName: str) -> object:
    sa = SpreadsheetApp('service_account.json')
    try:
        spreadsheet = sa.open_by_id(sheetId)
        try:
            sheets = spreadsheet.get_sheets()
            sheet = spreadsheet.get_sheet_by_name(sheetName)
            data_range = sheet.get_data_range()
            return data_range
        except:
            print('Could not find sheet:', sheetName)
            return None
    except:
        print('Could not open sheet with Id:', sheetId)
        return None

def getStudentSheetInfo(data_range: object, month: int) -> list:
    values = data_range.get_values()        # Cell values.
    colors = data_range.get_font_colors()   # Cell font colors.
    maxRow = data_range.get_max_row()       # Number of rows used in the sheet.
    # Determine which column is for the month requested.
    monthCol = getMonthCol(data_range, month)
    if monthCol == None:
        print('-*-*-*-*-> No column found for month:', month)
        return None
    names = []
    for j in range(0,maxRow):
        potentialStudent = values[j][0]   # Student Name.
        attendanceStatus = values[j][1]   # Gone or Break.
        charge = values[j][monthCol]      # Charge for the student for the month.
        chargeColor = colors[j][monthCol] # Font color of the charge.
        # Ignore student names that are numeric.
        if str(potentialStudent).isnumeric(): continue
        # Ignore students names that are an empty cell.
        if potentialStudent is None or potentialStudent == '': continue
        # Ignore specified names.
        if potentialStudent in namesToIgnore: continue
        # Get the color of the student name.
        color = colors[j][0]
        # Ignore the specified colors.
        if color in colorsToIgnore: continue
        # Ignore students on break or gone or 'X'
        if (attendanceStatus == 'Break') or (attendanceStatus == 'Gone') or (attendanceStatus == 'X'): continue
        # Compute the charge color from the rgb hex value for the cell with the charge.
        if not chargeColor: chargeColor = '#000000' # black
        chargeStatus = paymentStatus(charge, chargeColor)
        try:
            chargeColor = hex_to_name(chargeColor)
        except:
            if chargeColor == '#9900ff': chargeColor = 'purple'
            elif chargeColor == '#37761c': chargeColor = 'green'
            else:
                print('ERROR: Charge Color ', chargeColor)
                chargeColor = 'purple'
        # Smash the relevant information together into a dict.
        studentInfo = { 'name': potentialStudent
                      , 'charge': charge
                      , 'color': chargeColor
                      , 'status': chargeStatus }
        names.append(studentInfo) # Add to the list of students.
    return names
