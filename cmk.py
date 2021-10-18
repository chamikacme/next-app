import csv
from operator import itemgetter

def converter(row):
    dataList = []
    dataList.append(int(row[0]))
    dataList.append(row[1])
    dataList.append(row[2])
    dataList.append(float(row[3]))
    dataList.append(float(row[4]))
    dataList.append(float(row[5]))
    dataList.append(float(row[6]))
    return dataList

players = []
header=[]

print("Data should be in this order.")
print("Index No., Starting Rank, Name, School, Pts, Buch, Prog, Sonn")
inputFileName = str(input("Name of csv file : ")) +".csv"
outputFileName = "Ranked_" + inputFileName

with open(inputFileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            header = row
            line_count += 1
        else:
            line_count += 1
            players.append(converter(row[1:]))

sortedList = sorted(sorted(sorted(sorted(players, key=itemgetter(6), reverse=True), key=itemgetter(5), reverse=True), key=itemgetter(4), reverse=True), key=itemgetter(3), reverse=True)

for a in range(0,len(sortedList)):
    sortedList[a].insert(0,a+1) 

for b in range(0,len(sortedList)):
    if b>0:
        term1 = sortedList[b-1][4:]
        term2 = sortedList[b][4:]
        if term1==term2:
            sortedList[b].pop(0)
            sortedList[b].insert(0,sortedList[b-1][0])

with open(outputFileName, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in sortedList:
        writer.writerow(row)

print("Completed " + str(line_count) + " lines!")
input("Press any key to exit!!")








