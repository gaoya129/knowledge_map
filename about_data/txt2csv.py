import csv
csvFile = open("./data3.csv",'a',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("./data/高中地理必修一二三.txt",'r',encoding='utf-8')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()