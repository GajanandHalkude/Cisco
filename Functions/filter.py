cities = ["Banglore", "Hyderabad","Chennai","Pune"]
filter = list(filter(lambda val: len(val)>=8,cities))
print(filter)

#List comprehension
#Ques
items = list(range(3,30))
lis = [item for item in items if item%3==0]
print(lis)

lis = [item+10 for item in items]
print(lis)

elenames = ["Ele2004.txt","sele2009.txt","sachin2014.txt"]
import re
pat = "[^0-9]"
res = [re.sub(pat,"",ele) for ele in elenames]
print(res)

cities = ["mumbai", "bhuvaneshwar","mysore","pandaji","mangalore"]
listRes = [city.capitalize() for city in cities if city.startswith('m')]
print(listRes)