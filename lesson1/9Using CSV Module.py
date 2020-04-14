import os
import pprint
import csv

DARADIR = ""
DATAFILE = "/Users/xiaonili/lesson1/beatles-discography.csv"

def parse_csv(datafile):
    data = []
    
    with open(datafile, 'rb') as sd:
        r = csv.DictReader(sd)
    
        for line in r:
            data.append(line)
    return data

if __name__ == '__main__':
    datafile = os.path.join(DARADIR, DATAFILE)
    parse_csv(datafile)
    d = parse_csv(datafile)
    pprint.pprint(d)
