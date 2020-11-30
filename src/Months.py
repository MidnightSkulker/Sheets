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

