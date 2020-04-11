import csv
import queue

häufigekeitName = {}

with open("baby.csv","r") as file:
    lines = csv.reader(file,delimiter=",")
    for line in lines:
        if line[2]=="name":
            continue
        if line[2] in häufigekeitName:
            häufigekeitName[line[2]] += 1
        else:
            häufigekeitName[line[2]] = 1

highScoreName = queue.PriorityQueue()

for key,value in häufigekeitName.items():
    highScoreName.put(
        (int(-value),key)
        )


for i in range(0,10):
    print(highScoreName.get())
