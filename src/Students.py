import json
import re

# Get the student data from a file that is in JSON format
def getStudents(jsonFileName:str) -> dict:
    jsonFile = open(jsonFileName)
    jsonData = json.load(jsonFile)
    return jsonData

# Find a student in the student data.
def findStudent(studentData:list, studentName:str) -> dict:
    for student in studentData:
        fields = student['fields']
        fullName = fields['FN']
        if re.match(studentName + '.*', fullName): return fields
    return None

# Print out the list of students and their E-mail addresses.
def printStudentsAndEmails(studentData: list):
    for student in studentData:
        fields = student['fields']
        fullName = fields['FN']
        if 'EMAIL1' in fields:
            print(fullName + ': ' + fields['EMAIL1'])
        else:
            print(fullName + ': has no EMAIL')

# Print out the list of students and their E-mail addresses.
def getStudentsAndEmails(studentNames: list, studentData: list) -> list:
    ret = []
    for child in studentNames:
        name = child[1]
        print('name', name)
        student = findStudent(studentData, name)
        if student:
            print('student', name, student['FN'])
            fullName = student['FN']
            if 'EMAIL1' in student:
                email = student['EMAIL1']
                ret.append((child[1], child[0], email))
            else:
                ret.append((child[1], child[0], 'NO EMAIL'))
        else:
            print('student', None)
            continue
    return ret
