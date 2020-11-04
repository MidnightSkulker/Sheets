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

# Print out the list of student records.
def printStudentRecords(students: list):
    for s in students:
        print(str(s))

# Print out the list of students and their E-mail addresses.
def getStudentsAndEmails(studentNames: list, studentData: list) -> list:
    ret = []
    for child in studentNames:
        name = child['name']
        student = findStudent(studentData, name)
        if student:
            fullName = student['FN']
            if 'EMAIL1' in student:
                email = student['EMAIL1']
                child['email'] = email
                ret.append(child)
            else:
                child['email'] = 'NO EMAIL'
                ret.append(child)
        else:
            print('student not found, try processing Address Book (rall)', name)
            continue
    return ret
