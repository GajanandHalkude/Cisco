import json
fobj = open("jsonEmployeeData.txt",'r')
employees = json.load(fobj)
print(employees)