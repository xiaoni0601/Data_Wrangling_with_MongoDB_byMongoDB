#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it,
clean it, come up with a data model, insert it into MongoDB and then run some
queries against your database. The set contains data about Arachnid class
animals.

Your task in this exercise is to parse the file, process only the fields that
are listed in the FIELDS dictionary as keys, and return a list of dictionaries
of cleaned values. 

The following things should be done:
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label'
  field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the
  same value as 'label'.
- if a value of a field is "NULL", convert it to None
- if there is a value in 'synonym', it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the
  cleanup is up to you, e.g. removing "*" prefixes etc. If there is a singular
  synonym, the value should still be formatted in a list.
- strip leading and ending whitespace from all fields, if there is any
- the output structure should be as follows:

[ { 'label': 'Argiope',
    'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
    'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
    'name': 'Argiope',
    'synonym': ["One", "Two"],
    'classification': {
                      'family': 'Orb-weaver spider',
                      'class': 'Arachnid',
                      'phylum': 'Arthropod',
                      'order': 'Spider',
                      'kingdom': 'Animal',
                      'genus': None
                      }
  },
  { 'label': ... , }, ...
]

  * Note that the value associated with the classification key is a dictionary
    with taxonomic labels.
"""
import codecs
import csv
import json
import pprint
import re

DATAFILE = 'arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}


def process_file(filename, fields):

    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for _ in range(3):
            reader.__next__()
        for line in reader:
                temp_data = {}
                
                if line["rdf-schema#label"] == 'NULL':
                    temp_data[fields['rdf-schema#label']] = None
                else :
                    temp_data[fields['rdf-schema#label']] = line["rdf-schema#label"].strip().split(' (')[0]
                    
                if line['URI'] == 'NULL':
                    temp_data[fields['URI']] = None
                else :
                    temp_data[fields['URI']] = line['URI'].strip()
                    
                if line['rdf-schema#comment'] == 'NULL':
                    temp_data[fields['rdf-schema#comment']] = None
                else :
                    temp_data[fields['rdf-schema#comment']] = line['rdf-schema#comment'].strip()
                    
                if line['name'] == 'NULL':
                    temp_data[fields['name']] = temp_data['label']
                else :
                    temp_data[fields['name']] = line['name'].strip()
                    
                if line['synonym'] == 'NULL':
                    temp_data[fields['synonym']] = None
                else :
                    temp_data[fields['synonym']] = parse_array(line['synonym'].strip())
                    
                    
                temp_class = {}
                
                if line['family_label'] == 'NULL':
                    temp_class[fields['family_label']] = None
                else :
                    temp_class[fields['family_label']] = line['family_label'].strip()
                    
                if line['class_label'] == 'NULL':
                    temp_class[fields['class_label']] = None
                else :
                    temp_class[fields['class_label']] = line['class_label'].strip()
                    
                if line['phylum_label'] == 'NULL':
                    temp_class[fields['phylum_label']] = None
                else :
                    temp_class[fields['phylum_label']] = line['phylum_label'].strip()
                    
                if line['order_label'] == 'NULL':
                    temp_class[fields['order_label']] = None
                else :
                    temp_class[fields['order_label']] = line['order_label'].strip()
                    
                    
                if line['kingdom_label'] == 'NULL':
                    temp_class[fields['kingdom_label']] = None
                else :
                    temp_class[fields['kingdom_label']] = line['kingdom_label'].strip() 
                    
                    
                if line['genus_label'] == 'NULL':
                    temp_class[fields['genus_label']] = None
                else :
                    temp_class[fields['genus_label']] = line['genus_label'].strip()     
                    
                
                temp_data['classification'] = temp_class
                
                data.append(temp_data)

            # YOUR CODE HERE
       
    return data


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]


def test():
    data = process_file(DATAFILE, FIELDS)
    print("Your first entry:")
    pprint.pprint(data[0])
    first_entry = {
        "synonym": None, 
        "name": "Argiope", 
        "classification": {
            "kingdom": "Animal", 
            "family": "Orb-weaver spider", 
            "order": "Spider", 
            "phylum": "Arthropod", 
            "genus": None, 
            "class": "Arachnid"
        }, 
        "uri": "http://dbpedia.org/resource/Argiope_(spider)", 
        "label": "Argiope", 
        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]

if __name__ == "__main__":
    test()

#OUTPUT
# Your first entry:
# {'classification': {'class': 'Arachnid',
#                     'family': 'Orb-weaver spider',
#                     'genus': None,
#                     'kingdom': 'Animal',
#                     'order': 'Spider',
#                     'phylum': 'Arthropod'},
#  'description': 'The genus Argiope includes rather large and spectacular '
#                 'spiders that often have a strikingly coloured abdomen. These '
#                 'spiders are distributed throughout the world. Most countries '
#                 'in tropical or temperate climates host one or more species '
#                 'that are similar in appearance. The etymology of the name is '
#                 'from a Greek name meaning silver-faced.',
#  'label': 'Argiope',
#  'name': 'Argiope',
#  'synonym': None,
#  'uri': 'http://dbpedia.org/resource/Argiope_(spider)'}