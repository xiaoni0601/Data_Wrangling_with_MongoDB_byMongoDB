# Parsing CSV Files
# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "/Users/xiaonili/lesson1/beatles-discography.csv"


def parse_file(datafile):
    data = []
    # 1. open datafile
    with open(datafile, "r") as f:
        # 2. split the first line by comma
        header = f.readline().split(',')
        counter = 0
        for line in f:
            if counter == 10:
                break

            fields = line.split(',')
            entry = {}
            for i, value in enumerate(fields):
                # Python string method strip() will come in handy to get rid of the extra whitespace 
                # (that includes newline character at the end of line)
                entry[header[i].strip()] = value.strip() 
            
            data.append(entry)
            counter += 1
    return data

def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()