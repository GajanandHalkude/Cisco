def fun(fname,lname):
    for i in range(10):
        print(fname+ " " + lname)
        
from threading import Thread
t1 = Thread(target= fun, args = ("Gajanand", "Halkude",))
t1.start()