import csv
nameOfChilder = set()
with open("baby.csv","r") as file:
   lines = csv.reader(file, delimiter=",")
   for line in lines:
        if line[2] == "name":
           continue
        nameOfChilder.add(line[2])

print(nameOfChilder.__len__())