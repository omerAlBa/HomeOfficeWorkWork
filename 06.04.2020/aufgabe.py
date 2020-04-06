with open('baby.csv','r') as file:
    names = {}
    for line in file:
        parsedLine = line.strip().replace('"','').split(',')
        if parsedLine[2] == 'name':
            continue

        if not parsedLine[2] in names:
            names[parsedLine[2]] = 1
        else:
            names[parsedLine[2]] += 1
print(names)

def getLagestName(dict, prevent):
    thisName = ""
    for name, number in dict.items():
        if number > prevent:
            prevent = number
            thisName = name
    print("Hier der häufigste Name:")
    print(prevent,thisName)

getLagestName(names,0)