def add(x,y,z):
    return x+y+z
a = add(10,20,30)
print(a)

#Que
fun = lambda x,y : x+y
ans = fun(100,200)
print(ans)

#Que
cities = [(12,"Bhopal"), (24,"Telangana"),(30,"Andra"),(120,"Kerala")]
cities.sort()
print(cities)
cities.sort(key = lambda item : item[1])
print(cities)

#Que
salaries = [20,10,30,5,100]
updated = list(map(lambda salary:salary+100, salaries))
print(updated)

#Que
filenames = ["dravid.txt","virat.txt","sachin.txt"]
result = list(map(lambda itm : itm.replace(".txt",""),filenames))
print(result)

#Que
elenames = ["Ele2004.txt","sele2009.txt","sachin2014.txt"]
result = list(map(lambda itm : itm.replace(".txt",""),elenames))
import re
pattern = "[^0-9]"
ans = list(map(lambda itm : re.sub(pattern,"",itm),result))
print(ans)

#Que
lines = ["lion is old, strong!!!", "paris is burning?/","o jerusalem!!#"]
pat = "[^A-Za-z0-9 ]"
answer = list(map(lambda it : re.sub(pat,"",it),lines))
print(answer)

#Que
filtered = list(filter(lambda itm : itm < 130,salaries))
print(filtered)