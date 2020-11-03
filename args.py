#!/usr/local/bin/python3
import argparse

# https://docs.python.org/2/library/argparse.html
# Define the parser for the command line options.
argumentParser = argparse.ArgumentParser(description='Issue Invoices for Angels Academy Online')
argumentParser.add_argument('--SheetName', help='Name of Google Sheet to Parse')
argumentParser.add_argument('--Mode', help='Live or Preview: Live sends the emails to customers, preview sends the email to us')

# Now parse the arguments passed in.
parsedArguments = argumentParser.parse_args()

# Debug
print('parsed Arguments:', parsedArguments)
print('Mode', parsedArguments.Mode)
print('SheetName', parsedArguments.SheetName)
