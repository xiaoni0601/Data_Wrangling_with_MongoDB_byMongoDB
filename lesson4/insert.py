#!/usr/bin/env python
""" 
Add a single line of code to the insert_autos function that will insert the
automobile data into the 'autos' collection. The data variable that is
returned from the process_file function is a list of dictionaries, as in the
example in the previous video.
"""

from autos import process_file


def insert_autos(infile, db):
    data = process_file(infile)
    # Add your code here. Insert the data in one command.
    for i in data:
        db.autos.insert(i)
    
  
if __name__ == "__main__":
    # Code here is for local use on your own computer.
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('autos-small.csv', db)
    print(db.autos.find_one())


#OUTPUT: 
# {u'assembly': [u'Hiroshima', u'Japan'], 
# u'name': [u'Eunos Roadster', u'Mazda MX-5', 
# u'Mazda MX-5 Miata', u'Mazda Miata', u'Mazda Roadster'], 
# u'modelYears': [], u'productionYears': [], 
# u'layout': u'front-engine rear-wheel-drive layout', 
# u'_id': ObjectId('5e9feb6c9475fb51943c3775'), u'class': u'roadster', u'manufacturer': u'Mazda'}