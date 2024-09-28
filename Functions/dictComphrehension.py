items = [10,9,13,10,30,55,9,7,10]
freq = {}
for item in items:
    if item in freq:
        freq[item] = freq[item] + 1
    else:
        freq[item] = 1
# print(freq)

#Dictionary comphrehension
frequ = {item:items.count(item) for item in items}
# print(frequ)

#
cities = [(4,"mysore"),(12,"pune"),(3,"panaji")]
{city:rank for rank,city in cities}