employees = [
    {"E001":{"Sex":"m","Age":22,"Techologies":["JS","HTML"],"Salary":36000}},
    {"E002":{"Sex":"m","Age":23,"Techologies":["JS","HTML","CSS"],"Salary":26000}},
    {"E003":{"Sex":"f","Age":32,"Techologies":["SQL"],"Salary":30000}},
    {"E004":{"Sex":"m","Age":33,"Techologies":["SQL","Python"],"Salary":45000}},
    {"E005":{"Sex":"f","Age":29,"Techologies":["Python"],"Salary":30000}},
    {"E007":{"Sex":"f","Age":40,"Techologies":["JS"],"Salary":18000}},
    {"E008":{"Sex":"m","Age":25,"Techologies":["JS","HTML"],"Salary":22000}},
    {"E009":{"Sex":"m","Age":27,"Techologies":["JS","React"],"Salary":23000}},
    {"E010":{"Sex":"m","Age":30,"Techologies":["JS","React","Python"],"Salary":49500}},
    {"E011":{"Sex":"m","Age":33,"Techologies":["SQL"],"Salary":56000}},
    {"E012":{"Sex":"m","Age":35,"Techologies":["Python","SQL"],"Salary":75000}},
    {"E013":{"Sex":"f","Age":28,"Techologies":["Java","SQL"],"Salary":25000}},
    {"E014":{"Sex":"m","Age":40,"Techologies":["Rust"],"Salary":50000}},
    {"E015":{"Sex":"f","Age":34,"Techologies":["C++","Rust"],"Salary":55000}},
    {"E016":{"Sex":"m","Age":38,"Techologies":["Excel","Power BI"],"Salary":30000}},
    {"E017":{"Sex":"m","Age":42,"Techologies":["Python","Flask"],"Salary":27500}},
    {"E018":{"Sex":"m","Age":27,"Techologies":["SQL"],"Salary":29000}},
    {"E019":{"Sex":"f","Age":22,"Techologies":["Python"],"Salary":19000}},
    {"E020":{"Sex":"m","Age":21,"Techologies":["Java"],"Salary":22000}}
]
#
fobj = open("jsonEmployeeData.txt",'w')
import json
json.dump(employees, fobj,indent=4)
fobj.close()

#Question -01
salaries = []
for employee in employees:
    for code in employee:
        salary = employee[code]["Salary"]
        salaries.append(salary)
print(sum(salaries)/len(salaries))

#Question -02
MaleSalaries = []
for employee in employees:
    for code in employee:
        gender = employee[code]["Sex"]
        if(gender == "m"):
            MaleSalaries.append(employee[code]["Salary"])
print(sum(MaleSalaries)/len(MaleSalaries))

#Question-03

count = 0
for employee in employees:
    for code in employee:
        technology = employee[code]["Techologies"]
        for tech in technology:
            if(tech == "Python"):
                count = count + 1
print(count)

#Question-04

count2 = 0
for employee in employees:
    for code in employee:
        technology = employee[code]["Techologies"]
        if(len(technology)==1 and technology[0] == "Python"):
                count2 = count2 + 1
print(count2)

#Question -05

for employee in employees:
    for code in employee:
        technology = employee[code]["Techologies"]
        for tech in technology:
            if(tech == "Python"):
                salary = employee[code]["Salary"]
                hicked_salary = salary + salary * 5/100
                print(hicked_salary)

#Question - 06
for employee in employees:
    for code in employee:
        technology = employee[code]["Techologies"]
        if "Exel" not in tech:
            technology.append("Exel")
        print(technology)
#Question - 07 
fobj = open("employeeData.txt",'w')
for employee in employees:
    for code in employee:
        gender = employee[code]["Sex"]
        age = str(employee[code]["Age"])
        technologies = employee[code]["Techologies"]
        technologies = " ".join(technologies)
        salary = str(employee[code]["Salary"])
        fobj.write(code + " ")
        fobj.write(gender + " ")
        fobj.write(age + " ")
        fobj.write(technologies + " ")
        fobj.write(salary + " ")
        fobj.write("\n")
fobj.close()