
import matplotlib.pyplot as plt
'matplotlib inline'

with open("baby.csv","r") as file:
    conunter = 0
    ax = []
    ay = []
    print("die Daten:")
    for line in file:
        parsedLine = line.strip().replace('"','').split(",")
        if parsedLine[0] == 'AK' and parsedLine[2] == 'David':
            print(parsedLine)
            ax.append(parsedLine[3])
            ay.append(parsedLine[1])

plt.plot(ay,ax)
plt.show()