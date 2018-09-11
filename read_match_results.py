import csv

def readMatchResults():
    matchResults = []
    with open('./matchResults_2016-2018_GB.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # skipping the header
        for row in csv_reader:
            matchResults.append([row[0], {row[1]:"WINNER"}, {row[2]:"LOSER"}, {row[3]:"LOSER"}])
    return matchResults