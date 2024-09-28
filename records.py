fobj = open("records.txt",'r')

salaries = []

for itm in fobj:
    columns = itm.split()
    salary = int(columns[3])
    salaries.append(salary)

avg_salary = sum(salaries)/len(salaries)
print(avg_salary)
    
