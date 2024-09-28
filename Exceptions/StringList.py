class NotAStringError(Exception):
    def __init__(self,element):
        self.element = element

    def __str__(self):
        return f"What was added by you was not a String, You added {self.element}"
    
class StringList(list):
    def append(self,element):
        if(type(element) == str):
            list.append(self,element)
        else:
            raise NotAStringError(element)
s1 = StringList()
s1.append("Janen")
s1.append("Gaja")
try:
    s1.append("100")
except:
    print("There is an exception")
else:
    print("There is no exception")
finally:
    print("I always get printed")
print(s1)