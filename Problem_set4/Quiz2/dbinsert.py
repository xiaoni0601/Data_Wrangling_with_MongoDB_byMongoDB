
## Python 3.7.4 64-bit('base':conda)
"""
Complete the insert_data function to insert the data into MongoDB.
"""
import pymongo
import json

def insert_data(data, db):

    # Your code here. Insert the data into a collection 'arachnid'

    db.arachnid.insert(data)


if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open('arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print(db.arachnid.find_one())


#OUTPUT
# {u'synonym': None, u'description': u'The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced.', u'classification': {u'kingdom': u'Animal', u'family': u'Orb-weaver spider', u'order': u'Spider', u'phylum': u'Arthropod', u'genus': None, u'class': u'Arachnid'}, u'uri': u'http://dbpedia.org/resource/Argiope_(spider)', u'label': u'Argiope', u'_id': ObjectId('5ea273532e3cf02a53f67895'), u'name': u'Argiope'}
