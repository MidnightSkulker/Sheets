from __future__ import print_function
from google.auth.transport.requests import Request
from src.Credentials import *
from src.SheetIds import *
from src.Scopes import *
from src.Sheets import *

# The ID and range of a sample spreadsheet.
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # Open the spread sheets using the OAuth protocol
    service = openSheet(SAMPLE_SPREADSHEET_ID, [readOnly])
    
    # Get the 2 columns from the spread sheet, using the sheets API
    values = get2Columns(service, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME)
    
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))

if __name__ == '__main__':
    main()
