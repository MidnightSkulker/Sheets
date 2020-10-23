# Functions to manipulate Google Sheets

# Read specified 2 columns from a specified range of columns
def get2Columns(service, sheetId: str, rge: list) -> list:
    # Call the Sheets API
    sheet = service.spreadsheets()
    # Get the range of columns
    result = sheet.values().get(spreadsheetId=sheetId, range = rge).execute()
    values = result.get('values', [])
    return values
