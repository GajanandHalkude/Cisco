class SchoolMenmber:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def tell(self):
        '''My Details'''
        print(f"Name:{self.name} , Age: {self.age}")

class Teacher(SchoolMenmber):           #Teacher is Inheriting the properties from SchoolMember
    def __init__(self,name,age,salary):
        SchoolMenmber.__init__(self,name,age)
        self.salary = salary
    def tell(self):
        '''Teacher Details'''
        SchoolMenmber.tell(self)
        print(f"Salary: {self.salary}")
t = Teacher("Saumya",24,38000)
s = SchoolMenmber("Soumy",24)
# t.tell()
# s.tell()
res = [t,s]
for i in res:
    i.tell()