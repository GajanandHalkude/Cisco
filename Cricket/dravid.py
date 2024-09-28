myFile = open("dravid.txt","r")
st_rates = []
for item in myFile:
    columns = item.split()

    runs = int(columns[2])
    balls = int(columns[3])

    st_rate = runs/balls*100
    st_rates.append(st_rate)
import statistics
stdiv = statistics.stdev(st_rates)
print(stdiv)

    
