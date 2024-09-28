fobj = open("employeeData.txt",'r')
employeeData = []
for line in fobj:
   columns = line.split()

   code = columns[0]
   gender = columns[1]
   age = int(columns[2])
   salary = int(columns[3])
   technologies = columns[4:]
   employee = {code: {"gender":gender, "age":age, "salary":salary,"technologies":technologies}}
   employeeData.append(employee)

print(employeeData)