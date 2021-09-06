import csv
l=[]
with open("E:\csv file.txt", mode='r') as file:
    for i in csv.DictReader(file):
        l.append(i)
print(l)
