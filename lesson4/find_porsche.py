#!/usr/bin/env python
"""
Your task is to complete the 'porsche_query' function and in particular the query
to find all autos where the manufacturer field matches "Porsche".
Please modify only 'porsche_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB and download and insert the dataset.
"""

def porsche_query():
    # Please fill in the query to find all autos manuafactured by Porsche.
    query = {'manufacturer': 'Porsche'}
    return query


# Do not edit code below this line in the online code editor.
# Code here is for local use on your own computer.
def get_db(db_name):
    # For local use
    # =======================================
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def find_porsche(db, query):
    # For local use
    # =======================================
    return db.autos.find(query)


if __name__ == "__main__":
    # For local use
    # =======================================
    db = get_db('examples')
    query = porsche_query()
    results = find_porsche(db, query)

    print("Printing first 3 results\n")
    import pprint
    for car in results[:3]:
        pprint.pprint(car)


#OUTPUT
# Printing first 3 results

# {u'_id': ObjectId('52fe99575a98d659a6629101'),
#  u'assembly': [u'Germany', u'Stuttgart'],
#  u'bodyStyle': u'coup\xe9',
#  u'class': u'grand tourer',
#  u'dimensions': {u'height': 1.27508,
#                  u'length': 4.52,
#                  u'weight': 1450.0,
#                  u'wheelbase': 2.5,
#                  u'width': 1.89},
#  u'engine': [u'Porsche_928__1',
#              u'Porsche_928__2',
#              u'Porsche_928__3',
#              u'Porsche_928__4'],
#  u'layout': u'front-engine rear-wheel-drive layout',
#  u'manufacturer': u'Porsche',
#  u'modelYears': [],
#  u'name': u'Porsche 928',
#  u'productionYears': [1977,
#                       1978,
#                       1979,
#                       1980,
#                       1981,
#                       1982,
#                       1983,
#                       1984,
#                       1985,
#                       1986,
#                       1987,
#                       1988,
#                       1989,
#                       1990,
#                       1991,
#                       1992,
#                       1993,
#                       1994,
#                       1995],
#  u'transmission': [u'3-speed automatic',
#                    u'4-speed automatic',
#                    u'5-speed manual']}
# {u'_id': ObjectId('52fe99575a98d659a6629102'),
#  u'bodyStyle': u'2+2 (car body style)',
#  u'class': u'sports car',
#  u'designer': u'Harm Lagaay',
#  u'dimensions': {u'height': 1.27,
#                  u'length': 4.2,
#                  u'weight': 1080.0,
#                  u'width': 1.685},
#  u'engine': u'Porsche_924__1',
#  u'layout': u'front-engine rear-wheel-drive layout',
#  u'manufacturer': u'Porsche',
#  u'modelYears': [],
#  u'name': u'Porsche 924',
#  u'productionYears': [1976,
#                       1977,
#                       1978,
#                       1979,
#                       1980,
#                       1981,
#                       1982,
#                       1983,
#                       1984,
#                       1985,
#                       1986,
#                       1987,
#                       1988]}
# {u'_id': ObjectId('52fe99575a98d659a6629103'),
#  u'assembly': [u'Germany', u'Neckarsulm'],
#  u'bodyStyle': [u'convertible', u'coup\xe9'],
#  u'class': u'sports car',
#  u'designer': u'Harm Lagaay',
#  u'dimensions': {u'height': 1.27508,
#                  u'length': 4.318,
#                  u'wheelbase': 2.4003,
#                  u'width': 1.73482},
#  u'engine': [u'Porsche_944__1', u'Porsche_944__2', u'Porsche_944__3'],
#  u'layout': u'front-engine rear-wheel-drive layout',
#  u'manufacturer': u'Porsche',
#  u'modelYears': [],
#  u'name': u'Porsche 944',
#  u'productionYears': [1982,
#                       1983,
#                       1984,
#                       1985,
#                       1986,
#                       1987,
#                       1988,
#                       1989,
#                       1990,
#                       1991],
#  u'transmission': [u'3-speed automatic', u'5-speed manual']}