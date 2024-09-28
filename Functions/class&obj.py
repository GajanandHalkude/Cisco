class Person:
    def __init__(self,ename,egender,eage): #Special function, self is an object which stores all attributes passed as arguments to intit function.
        self.name = ename
        self.gender = egender
        self.age = eage
    def __str__(self):
        return f"{self.name} {self.gender} {self.age}" #format string
    def show(self): #Ordinary/Normal function
        print(self.name)
        print(self.gender)
        print(self.age)
p1 = Person("Gajanand","Male",23)
# p1.show()
# print(p1)
# p1 ----------> (name:"jane",gender:"male",age:23),type:Person,RC:2

class Employee(Person): #inheriting class Person
    def __init__(self,name,gender,age,salary):
        Person.__init__(self,name,gender,age) #taking help from Person
        self.salary = salary

    def __str__(self):
        return f"{Person.__str__(self)} {self.salary}"
    
    def __lt__(self,obj):
        return self.salary < obj.salary
    
# e1 = Employee("Baswaraj", "Male",24,35000)
# print(e1)

employees = []
fobj = open("records.txt",'r')
for line in fobj:
    columns = line.split()

    name = columns[0]
    age = int(columns[2])
    gender = columns[1]
    salary = int(columns[3])

    employee = Employee(name,gender,age,salary)
    employees.append(employee)
for emp in employees:
    print(emp)
print()
# employees.sort()
employees.sort(key = lambda employee : employee.age)
for emp in employees:
    print(emp)