#!/usr/bin/python3

import json
from src.Students import *

studentData = getStudents('outputs/students.json')
printStudentsAndEmails(studentData)
aadhya = findStudent(studentData, 'Aadhya C')
print('Aadhya: ', aadhya)
