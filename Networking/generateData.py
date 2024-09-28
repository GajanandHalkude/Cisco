from random import randint
fobj = open("salaries.txt",'w')
for item in range(10000):
    salary = randint(10000,99999)
    salary = str(salary)

    salary = salary[:2] + ',' + salary[2:]
    fobj.write(salary)
    fobj.write('\n')
fobj.close()