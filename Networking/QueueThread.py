from queue import Queue
q1= Queue()
q2= Queue()
q3= Queue()
def extract():
    fobj = open("salaries.txt",'r')
    for salary in fobj:
        q1.put(salary)
    q1.put(None)

def clean():
    while True:
        salary = q1.get()
        if(salary == None):
            q2.put(None)
            break
        salary = salary.replace(",","")
        salary = int(salary)
        q2.put(salary)
def hike():
    while True:
        salary = q2.get()
        if(salary == None):
            q3.put(None)
            break
        salary = salary + salary * 0.05
        q3.put(salary)

from time import time
from threading import Thread

t1 = Thread(target = extract)
t2 = Thread(target= clean)
t3 = Thread(target = hike)

now = time()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

stop = time()
while True:
    salary = q3.get()
    if(salary == None):
        break
    print(salary)
    print("")
print(stop - now)