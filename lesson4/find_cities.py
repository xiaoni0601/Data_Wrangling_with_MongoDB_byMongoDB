#!/usr/bin/env python
"""
Your task is to write a query that will return all cities
that are founded in 21st century.
Please modify only 'range_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.
"""

from datetime import datetime
    
def range_query():
    # Modify the below line with your query.
    # You can use datetime(year, month, day) to specify date in the query
    query = {'foundingDate': {'$gte': datetime(2001, 1, 1)}}
    return query

# Do not edit code below this line in the online code editor.
# Code here is for local use on your own computer.
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db

if __name__ == "__main__":
    # For local use
    db = get_db()
    query = range_query()
    cities = db.cities.find(query)

    print("Found cities:", cities.count())
    import pprint
    pprint.pprint(cities[0])


#OUTPUT
# Found cities: 129
# Printing first 3 results

# {u'_id': ObjectId('52fe79405a98d658e80ad93a'),
#  u'areaCode': [u'210'],
#  u'country': u'Bexar County Texas',
#  u'elevation': 185.318,
#  u'foundingDate': datetime.datetime(2008, 5, 30, 0, 0),
#  u'homepage': [u'http://www.vonormytexas.com'],
#  u'isPartOf': [u'Texas'],
#  u'lat': 29.2857,
#  u'leaderName': u'Art Martinez de Vara',
#  u'leaderTitle': u'Alderman',
#  u'lon': -98.6473,
#  u'motto': u'(Spanish for God and Texas)',
#  u'name': u'City of Von Ormy',
#  u'population': 1300,
#  u'populationDensity': 228.1,
#  u'postalCode': u'78073',
#  u'timeZone': [u'Central Time Zone (North America)'],
#  u'utcOffset': [u'-5', u'-6']}
# {u'_id': ObjectId('52fe79415a98d658e80adacc'),
#  u'areaCode': [u'819 873'],
#  u'areaLand': 342980000.0,
#  u'areaMetro': 2999900000.0,
#  u'country': u'Canada',
#  u'foundingDate': datetime.datetime(2002, 1, 1, 0, 0),
#  u'governmentType': [u'Gatineau City Council'],
#  u'isPartOf': [u'Outaouais'],
#  u'lat': 45.4278,
#  u'leaderName': u'Chapleau (provincial electoral district)',
#  u'leaderTitle': u'Federal riding',
#  u'lon': -75.7106,
#  u'motto': u"Fortunae meae multorum faber''",
#  u'name': u'Gatineau',
#  u'population': 265349,
#  u'populationDensity': 773.7,
#  u'postalCode': u'J8L to J8Z J9A',
#  u'timeZone': [u'Eastern Time Zone']}
# {u'_id': ObjectId('52fe79415a98d658e80adb0c'),
#  u'areaCode': [u'479'],
#  u'areaLand': 169900000.0,
#  u'country': u'United States',
#  u'elevation': 314.858,
#  u'foundingDate': datetime.datetime(2006, 12, 7, 0, 0),
#  u'isPartOf': [u'Arkansas', u'Benton County Arkansas'],
#  u'lat': 36.4639,
#  u'leaderTitle': u'Mayor',
#  u'lon': -94.2711,
#  u'name': u'Bella Vista Arkansas',
#  u'population': 25250,
#  u'populationDensity': 96.4,
#  u'postalCode': u'72714-72715',
#  u'timeZone': [u'Central Time Zone (North America)'],
#  u'utcOffset': [u'-5', u'-6']}