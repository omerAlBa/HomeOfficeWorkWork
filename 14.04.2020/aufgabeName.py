import os
from collections import defaultdict

name = defaultdict(lambda: 0)

# wie häufig ist der Name "Max" in allen Datein vorzufinden?

# current path
# was eine Datei und ob es Ordner ist

filenName = os.path.dirname(__file__)
joinedpath = filenName + "/names"

files = os.listdir(joinedpath)
for file in files:
    if os.path.isdir(file):
        print("es ist ein Ordner")
    else:
        print("{file} ist eine Datei".format(file = file))
        with open(joinedpath + "/" + file, "r", encoding='utf-8') as currentFile:
            for line in currentFile:
                isMax = line.split(" ")[0]
                if isMax == "Max":
                    name[isMax] += 1

print(name)