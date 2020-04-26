#!/usr/bin/env python
"""
Use an aggregation query to answer the following question. 

Extrapolating from an earlier exercise in this lesson, find the average
regional city population for all countries in the cities collection. What we
are asking here is that you first calculate the average city population for each
region in a country and then calculate the average of all the regional averages
for a country.
  As a hint, _id fields in group stages need not be single values. They can
also be compound keys (documents composed of multiple fields). You will use the
same aggregation operator in more than one stage in writing this aggregation
query. I encourage you to write it one stage at a time and test after writing
each stage.

Please modify only the 'make_pipeline' function so that it creates and returns
an aggregation  pipeline that can be passed to the MongoDB aggregate function.
As in our examples in this lesson, the aggregation pipeline should be a list of
one or more dictionary objects. Please review the lesson examples if you are
unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you
want to run this code locally on your machine, you have to install MongoDB,
download and insert the dataset. For instructions related to MongoDB setup and
datasets please see Course Materials.

Please note that the dataset you are using here is a different version of the
cities collection provided in the course materials. If you attempt some of the
same queries that we look at in the problem set, your results may be different.
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = []

    unwind = {"$unwind": "$isPartOf"}
    pipeline.append(unwind)

    # first calculate the average city population for each region in a country 
    # and then calculate the average of all the regional averages for a country.

    group = {"$group": {"_id": {"country": "$country", 
                                "region": "$isPartOf"},
                        "avg": {"$avg": "$population"}}}
    pipeline.append(group)

    group = {"$group": {"_id": "$_id.country",
                        "avgRegionalPopulation": {"$avg": "$avg"}}}
    pipeline.append(group)

    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]

if __name__ == '__main__':
    # The following statements will be used to test your code by the grader.
    # Any modifications to the code past this point will not be reflected by
    # the Test Run.
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    if len(result) < 150:
        pprint.pprint(result)
    else:
        pprint.pprint(result[:100])
    key_pop = 0
    for country in result:
        if country["_id"] == 'Lithuania':
            assert country["_id"] == 'Lithuania'
            assert abs(country["avgRegionalPopulation"] - 14750.784447977203) < 1e-10
            key_pop = country["avgRegionalPopulation"]
    assert({'_id': 'Lithuania', 'avgRegionalPopulation': key_pop} in result)


# OUTPUT
# [{u'_id': u'Denmark', u'avgRegionalPopulation': 30570.0},
#  {u'_id': u'New Zealand', u'avgRegionalPopulation': 68901.0},
#  {u'_id': u'Sudan', u'avgRegionalPopulation': 363945.0},
#  {u'_id': u'East Timor', u'avgRegionalPopulation': 193563.0},
#  {u'_id': u'Senegal', u'avgRegionalPopulation': None},
#  {u'_id': u'Galmudug', u'avgRegionalPopulation': 545000.0},
#  {u'_id': u'Vanuatu', u'avgRegionalPopulation': 44040.0},
#  {u'_id': u'Guinea', u'avgRegionalPopulation': 95234.0},
#  {u'_id': u'Montenegro', u'avgRegionalPopulation': 156169.0},
#  {u'_id': u'Grenada', u'avgRegionalPopulation': 17367.0},
#  {u'_id': u'The_Democratic_Republic_Of_Congo',
#   u'avgRegionalPopulation': 9046000.0},
#  {u'_id': u'Fiji', u'avgRegionalPopulation': 52220.0},
#  {u'_id': u'Honduras', u'avgRegionalPopulation': 1126534.0},
#  {u'_id': u'Southeast Region Brazil', u'avgRegionalPopulation': 12883.0},
#  {u'_id': u'Iraq', u'avgRegionalPopulation': 174487.33333333334},
#  {u'_id': u'Cambodia', u'avgRegionalPopulation': 195898.0},
#  {u'_id': u'Botswana', u'avgRegionalPopulation': 56170.75},
#  {u'_id': u'Belize', u'avgRegionalPopulation': 41285.0},
#  {u'_id': u'Sweden', u'avgRegionalPopulation': 16616.0},
#  {u'_id': u'Paraguay', u'avgRegionalPopulation': 46473.125},
#  {u'_id': u'Papua New Guinea', u'avgRegionalPopulation': 307643.0},
#  {u'_id': u'Trinidad and Tobago', u'avgRegionalPopulation': 52360.0},
#  {u'_id': u'Macedonia', u'avgRegionalPopulation': 175194.0},
#  {u'_id': u'Romania', u'avgRegionalPopulation': 249408.0},
#  {u'_id': u'Cyprus', u'avgRegionalPopulation': 310355.0},
#  {u'_id': u'Haiti', u'avgRegionalPopulation': None},
#  {u'_id': u'Northeast Region Brazil', u'avgRegionalPopulation': 83558.25},
#  {u'_id': u'Belgium', u'avgRegionalPopulation': 29521.0},
#  {u'_id': u'Malawi', u'avgRegionalPopulation': None},
#  {u'_id': u'Saint Vincent and the Grenadines',
#   u'avgRegionalPopulation': 24518.0},
#  {u'_id': u'Georgia', u'avgRegionalPopulation': 8000.0},
#  {u'_id': u'Malta', u'avgRegionalPopulation': 4384.133333333333},
#  {u'_id': u'Niue', u'avgRegionalPopulation': 581.0},
#  {u'_id': u'Netherlands', u'avgRegionalPopulation': 77592.02266666667},
#  {u'_id': u'North Sumatra', u'avgRegionalPopulation': 152748.0},
#  {u'_id': u'Turkey', u'avgRegionalPopulation': 1945457.0},
#  {u'_id': u'Burma', u'avgRegionalPopulation': 308397.61904761905},
#  {u'_id': u'Latvia', u'avgRegionalPopulation': 27569.0},
#  {u'_id': u'Ghana', u'avgRegionalPopulation': 1185798.5},
#  {u'_id': u'Kuwait', u'avgRegionalPopulation': 115945.66666666667},
#  {u'_id': u'Nepal', u'avgRegionalPopulation': 50598.97019969278},
#  {u'_id': u'Georgia (country)', u'avgRegionalPopulation': 4800.0},
#  {u'_id': u'Iran', u'avgRegionalPopulation': 31174.275647889815},
#  {u'_id': u'Saudi Arabia', u'avgRegionalPopulation': 1826254.75},
#  {u'_id': u'Guatemala', u'avgRegionalPopulation': 346560.5},
#  {u'_id': u'Brazil', u'avgRegionalPopulation': 54914.12645502645},
#  {u'_id': u'Eritrea', u'avgRegionalPopulation': 78857.33333333333},
#  {u'_id': u'Mali', u'avgRegionalPopulation': 325112.0},
#  {u'_id': u'Bolivia', u'avgRegionalPopulation': 218946.875},
#  {u'_id': u'Togo', u'avgRegionalPopulation': 837437.0},
#  {u'_id': u'South Korea', u'avgRegionalPopulation': 367383.40037037036},
#  {u'_id': u'United States', u'avgRegionalPopulation': 18212.814783020633},
#  {u'_id': u'Republic of Macedonia', u'avgRegionalPopulation': 43395.0},
#  {u'_id': u'Tanzania', u'avgRegionalPopulation': 347210.5},
#  {u'_id': u'Thailand', u'avgRegionalPopulation': 390806.78571428574},
#  {u'_id': u'Kyrgyzstan', u'avgRegionalPopulation': 835800.0},
#  {u'_id': u'Philippines', u'avgRegionalPopulation': 294841.4283532705},
#  {u'_id': u'Cape Verde', u'avgRegionalPopulation': 50585.666666666664},
#  {u'_id': u'Slovenia', u'avgRegionalPopulation': 70727.64285714286},
#  {u'_id': u'Zambia', u'avgRegionalPopulation': 1103957.4285714286},
#  {u'_id': u'Tunisia', u'avgRegionalPopulation': 1138517.5},
#  {u'_id': u'Greece', u'avgRegionalPopulation': None},
#  {u'_id': u'Mauritius', u'avgRegionalPopulation': 137608.0},
#  {u'_id': u'Namibia', u'avgRegionalPopulation': 37933.958333333336},
#  {u'_id': u'Vietnam', u'avgRegionalPopulation': 260208.14814814818},
#  {u'_id': u'Republic of Ireland', u'avgRegionalPopulation': None},
#  {u'_id': u'Bulgaria', u'avgRegionalPopulation': 37341.0},
#  {u'_id': u'Lithuania', u'avgRegionalPopulation': 14750.784447977201},
#  {u'_id': u'El Salvador', u'avgRegionalPopulation': 125154.0},
#  {u'_id': u'Qatar', u'avgRegionalPopulation': 31547.0},
#  {u'_id': u'Portugal', u'avgRegionalPopulation': 121885.78431372548},
#  {u'_id': u'Ukraine', u'avgRegionalPopulation': 73994.05175865801},
#  {u'_id': u'Libya', u'avgRegionalPopulation': 180310.0},
#  {u'_id': u'Morocco', u'avgRegionalPopulation': 334771.76190476195},
#  {u'_id': u'Canada', u'avgRegionalPopulation': 123374.22370121692},
#  {u'_id': u'Zimbabwe', u'avgRegionalPopulation': 236817.625},
#  {u'_id': u'Liberia', u'avgRegionalPopulation': 12117.0},
#  {u'_id': u'Indonesia', u'avgRegionalPopulation': 447416.20084175083},
#  {u'_id': u'Jordan', u'avgRegionalPopulation': 93797.71666666666},
#  {u'_id': u'Chile', u'avgRegionalPopulation': 16103.314444444444},
#  {u'_id': u'United Arab Emirates', u'avgRegionalPopulation': 252772.0},
#  {u'_id': u'Yemen', u'avgRegionalPopulation': 64053.5},
#  {u'_id': u'Dominican Republic', u'avgRegionalPopulation': 820869.6666666666},
#  {u'_id': u'Mexico', u'avgRegionalPopulation': 234735.41910872312},
#  {u'_id': u'German Reich', u'avgRegionalPopulation': None},
#  {u'_id': u'Lebanon', u'avgRegionalPopulation': 29645.083333333332},
#  {u'_id': u'Czech Republic', u'avgRegionalPopulation': 182720.7142857143},
#  {u'_id': u'Azerbaijan', u'avgRegionalPopulation': 22696.98709677419},
#  {u'_id': u'Algeria', u'avgRegionalPopulation': 196969.7},
#  {u'_id': u'Madagascar', u'avgRegionalPopulation': 240172.6},
#  {u'_id': u'Pakistan', u'avgRegionalPopulation': 783512.2408810325},
#  {u'_id': u'Nigeria', u'avgRegionalPopulation': 635294.9708333333},
#  {u'_id': u'Argentina', u'avgRegionalPopulation': 75255.81502365487},
#  {u'_id': u'Ecuador', u'avgRegionalPopulation': 219074.18686868687},
#  {u'_id': u'Colombia', u'avgRegionalPopulation': 389760.31111111114},
#  {u'_id': u'Afghanistan', u'avgRegionalPopulation': 177409.9375},
#  {u'_id': u'Spain', u'avgRegionalPopulation': 69802.6516154918},
#  {u'_id': u'Malaysia', u'avgRegionalPopulation': 592408.6333333333},
#  {u'_id': u'Venezuela', u'avgRegionalPopulation': 533638.2941176471},
#  {u'_id': u'Iceland', u'avgRegionalPopulation': 58662.0},
#  {u'_id': u'Norway', u'avgRegionalPopulation': 8579.5},
#  {u'_id': u'Saint Lucia', u'avgRegionalPopulation': 61341.0},
#  {u'_id': u'Jamaica', u'avgRegionalPopulation': 937700.0},
#  {u'_id': u'Austria', u'avgRegionalPopulation': 24110.0},
#  {u'_id': u'China', u'avgRegionalPopulation': 1294543.23975458},
#  {u'_id': u'Panama', u'avgRegionalPopulation': 395576.0},
#  {u'_id': u'Hungary', u'avgRegionalPopulation': 157308.56666666668},
#  {u'_id': u'Peru', u'avgRegionalPopulation': 148784.33333333334},
#  {u'_id': None, u'avgRegionalPopulation': 11482305.530360173},
#  {u'_id': u'Angola', u'avgRegionalPopulation': 125904.66666666667},
#  {u'_id': u'Japan', u'avgRegionalPopulation': 579909.7013128701},
#  {u'_id': u'Ancient Egypt', u'avgRegionalPopulation': None},
#  {u'_id': u'Ivory Coast', u'avgRegionalPopulation': 164991.89444444442},
#  {u'_id': u'Somalia', u'avgRegionalPopulation': 297764.28571428574},
#  {u'_id': u'United Kingdom', u'avgRegionalPopulation': 1864957.8653846155},
#  {u'_id': u'Oman', u'avgRegionalPopulation': None},
#  {u'_id': u'Uruguay', u'avgRegionalPopulation': 95081.87714285715},
#  {u'_id': u'Poland', u'avgRegionalPopulation': 16676.166666666668},
#  {u'_id': u'Suriname', u'avgRegionalPopulation': None},
#  {u'_id': u'Barbados', u'avgRegionalPopulation': 96578.0},
#  {u'_id': u'Albania', u'avgRegionalPopulation': 55210.40909090909},
#  {u'_id': u'Laos', u'avgRegionalPopulation': 50000.0},
#  {u'_id': u'Kosovo', u'avgRegionalPopulation': 57586.75},
#  {u'_id': u'Estonia', u'avgRegionalPopulation': 104109.0},
#  {u'_id': u'India', u'avgRegionalPopulation': 201128.02415469187},
#  {u'_id': u'Taiwan', u'avgRegionalPopulation': 221659.86666666664},
#  {u'_id': u'Ethiopia', u'avgRegionalPopulation': 170932.0},
#  {u'_id': u'Cuba', u'avgRegionalPopulation': 1701228.0},
#  {u'_id': u'India national cricket team', u'avgRegionalPopulation': 1048240.0},
#  {u'_id': u'Benin', u'avgRegionalPopulation': 85848.47146464646},
#  {u'_id': u'S\xe3o Tom\xe9 and Pr\xedncipe',
#   u'avgRegionalPopulation': 56166.0},
#  {u'_id': u'Bosnia and Herzegovina', u'avgRegionalPopulation': 249496.6},
#  {u'_id': u'Kenya', u'avgRegionalPopulation': 1226727.4285714286},
#  {u'_id': u'Bangladesh', u'avgRegionalPopulation': 1193317.0925925926},
#  {u'_id': u'Egypt', u'avgRegionalPopulation': 682002.8125},
#  {u'_id': u'Costa Rica', u'avgRegionalPopulation': 48973.444444444445},
#  {u'_id': u'Uzbekistan', u'avgRegionalPopulation': 20404.875},
#  {u'_id': u'Croatia', u'avgRegionalPopulation': 39074.92156862745},
#  {u'_id': u'North Korea', u'avgRegionalPopulation': 542138.0454545454},
#  {u'_id': u'Turkmenistan', u'avgRegionalPopulation': None},
#  {u'_id': u'Mauritania', u'avgRegionalPopulation': 62021.666666666664},
#  {u'_id': u'Sri Lanka', u'avgRegionalPopulation': 116311.95138888889},
#  {u'_id': u'Kazakhstan', u'avgRegionalPopulation': 49971.2},
#  {u'_id': u'Moldova', u'avgRegionalPopulation': 20675.0},
#  {u'_id': u'Bexar County Texas', u'avgRegionalPopulation': 1300.0},
#  {u'_id': u'Syria', u'avgRegionalPopulation': 22004.51298701299},
#  {u'_id': u'Jubaland', u'avgRegionalPopulation': 183300.0},
#  {u'_id': u'Serbia', u'avgRegionalPopulation': 130687.55802469136}]