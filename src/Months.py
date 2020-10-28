import re

months3Letters = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Determine if a string matches a month
def isMonth(s:str):
    for m in months3Letters:
        if re.match(m, s): return m
    return None
