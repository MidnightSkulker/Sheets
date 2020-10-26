from sheetfu import SpreadsheetApp

def loadGrace ():
    sa = SpreadsheetApp('service_account.json')
    spreadsheet = sa.open_by_id('1fLDy8hmgYdxYvQPhbi6DFL0BqR8hvlvK2YaA7vgoEzc')
    sheet = spreadsheet.get_sheet_by_name('GracesClass')

    return sheet

sheet = loadGrace()

data_range = sheet.get_data_range()           # returns the sheet range that contains data values.
# this is how you get things
values = data_range.get_values()              # returns a 2D matrix of values.
backgrounds = data_range.get_backgrounds()    # returns a 2D matrix of background colors in hex for
colors = data_range.get_font_colors()



# this is how you set things
# data_range.set_background('#000000')          # set every cell backgrounds to black
# data_range.set_font_color('#ffffff')          # set every cell font colors to white


