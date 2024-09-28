filenames = ["Elections2004.txt","Elections2009.txt","Elections2014.txt"]
highMargins = {}
females = []
parties = []
import re
for filename in filenames:
    fobj = open(filename,'r')

    eledata = []
    margins = []
    countOfFemales = 0
    countOfFemalesWon = 0
    bjp =0
    inc =0
    jds = 0
    year = 2004

    pat = "[^0-9 ]"
    fname = re.sub(pat,"",filename)
    
    for line in fobj:
        columns = line.split()

        constutuncy = columns[1]

        wonPerson = columns[2]
        wonGender = columns[3]
        wonParty = columns[4]
        wonVotes = int(columns[5])

        lossPerson = columns[6]
        lossGender = columns[7]
        lossParty = columns[8]
        lossVotes = int(columns[9])

        row = {constutuncy: {"wonPerson":wonPerson,"wonGender":wonGender,"wonParty":wonParty,"wonVotes":wonVotes,"lossPerson":lossPerson,
                        "lossGender":lossGender,"lossParty":lossParty,"lossVotes":lossVotes }}
        eledata.append(row)

        if(wonParty=="BJP"):
            bjp = bjp + 1
        if(wonParty=="INC"):
            inc = inc + 1
        if(wonParty=="JD(S)"):
            jds = jds + 1
        party = {fname: {"BJP":bjp, "INC":inc,"JD(S)":jds}}

        
        if(wonGender == "F" or lossGender == 'F'):
            countOfFemales = countOfFemales + 1
        if(wonGender == 'F'):
            countOfFemalesWon = countOfFemalesWon + 1

        diff = wonVotes-lossVotes
        margins.append(diff)
        highMargins[fname] = max(margins)

        #females[filename]["TotalFe"] = countOfFemales
    female = {fname: {"TotalFemaleParticipated":countOfFemales, "TotalFemaleWon":countOfFemalesWon}}
    females.append(female)
    parties.append(party)
        #females[filename]["FeWon"] = countOfFemalesWon
        
print(parties)
print('\n')
print(females)
print('\n')
print(highMargins)
print("\n")



