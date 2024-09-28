import statistics
players = {}
filenames = ["dravid.txt","sachin.txt", "virat.txt","yuvraj.txt"]
for file in filenames:
    player = file.replace(".txt", "")
    strike_rates = []
    fobj = open(file,"r")
    for itm in fobj:
        columns = itm.split()

        runs = int(columns[2])
        balls = int(columns[3])
        strike_rate = runs/balls*100
        strike_rates.append(strike_rate)
        
    deviation = statistics.stdev(strike_rates)
        
    players[player] = deviation
print(players)
