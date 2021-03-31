import re

months3Letters = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Determine if a string matches a month
def isMonth(s: str):
    for m in months3Letters:
        if re.match(m, s): return m
    return None

months = { 'Jan': 'January',
           'Feb': 'February',
           'Mar': 'March',
           'Apr': 'April',
           'May': 'May',
           'Jun': 'June',
           'Jul': 'July',
           'Aug': 'August',
           'Sep': 'September',
           'Oct': 'October',
           'Nov': 'November',
           'Dec': 'December'
           }

# Find the index of the previous month, return -1 if a
# bad month name is passed in.
def previousMonthIdx(month: str) -> int:
    if month in months3Letters:
        idx = months3Letters.index(month)
        if idx == 0:
            return len(months3Letters) - 1
        else:
            return idx - 1
    else:
        return (-1)

# Find the name of the previous months
def previousMonth(month: str) -> str:
    idx = previousMonthIdx(month)
    if idx == -1:
        # Garbage in, garbage out
        return month
    else:
        return months3Letters[previousMonthIdx(month)]
