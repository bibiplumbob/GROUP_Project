import json
with open("monarchs_file.json", encoding = 'utf-8') as f:
    royal_data = json.load(f)

#CLEANING UP DATA
for label in royal_data:
    if 'http://www.w3.org/2000/01/rdf-schema#label' in label:
        del label['http://www.w3.org/2000/01/rdf-schema#label']
    if 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type' in label:
        del label['http://www.w3.org/1999/02/22-rdf-syntax-ns#type']
    if 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label' in label:
        del label["http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label"]
    if 'http://www.w3.org/2000/01/rdf-schema#seeAlso' in label:
        del label['http://www.w3.org/2000/01/rdf-schema#seeAlso']
    if 'http://www.w3.org/2002/07/owl#differentFrom' in label:
        del label['http://www.w3.org/2002/07/owl#differentFrom']
    if 'ontology/parent' in label:
        del label['ontology/parent']
    if 'ontology/spouse_label' in label:
        del label['ontology/spouse']
    #want to put an else if need be
    if 'ontology/birthPlace' in label:
        del label['ontology/birthPlace']
    if 'ontology/deathPlace' in label:
        del label['ontology/deathPlace']
    if 'ontology/country' in label:
        del label['ontology/country']
    if 'ontology/successor' in label:
        del label['ontology/successor']
    if 'ontology/predecessor' in label:
        del label['ontology/predecessor']
    if 'ontology/restingPlace' in label:
        del label['ontology/restingPlace']
    if 'ontology/occupation' in label:
        del label['ontology/occupation']

#Creating a country set
with open('country_data.json') as f:
    country = json.load(f)

countries = set()
for dict in country:
    if 'Name' in dict:
        if dict['Name'] not in countries:
            countries.add(dict['Name'])
#Now to try and compare 
did_not_work = []
for dict in royal_data:
    if "ontology/birthPlace_label" in dict:
        # If only a single place, convert it to a list
        if type(dict["ontology/birthPlace_label"]) is not list:
            dict["ontology/birthPlace_label"] = [dict["ontology/birthPlace_label"]]
        
        # Convert list of place names to set of placenames (for set intersection later)
        dict["ontology/birthPlace_label"] = set(dict["ontology/birthPlace_label"])

        # Find the set intersection between countries and birthPlace
        origin_country = dict["ontology/birthPlace_label"] & countries

        #Check that the intersection is just one country
        if len(origin_country) == 1:
            #Save single country back into dictionary
            origin_country = list(origin_country)[0]
            dict["birthCountry"] = origin_country
        else:
            did_not_work.append(dict["ontology/birthPlace_label"])

#Filtering to data that has both birth year and death year 
birth_death_year = []
for dict in royal_data:
    if "ontology/birthYear" in dict:
        if "ontology/deathYear" in dict:
            birth_death_year.append(dict)

#Convert string to numbers for the year values
for dict in birth_death_year:
    if type(dict["ontology/birthYear"]) is str:
        dict["ontology/birthYear"] = int(dict["ontology/birthYear"])
    if type(dict["ontology/deathYear"]) is str:
        dict["ontology/deathYear"] = int(dict["ontology/deathYear"])

import csv
columns = ["title","ontology/title","deathPlace","birthPlace","num_spouses","ontology/birthYear","ontology/deathYear","birthCountry"]
with open('country_royals.csv', 'w', encoding = 'utf-8', newline= '') as f:
    writer = csv.DictWriter(f, fieldnames= columns, extrasaction='ignore')
    writer.writeheader()
    for dict in birth_death_year:
        writer.writerow(dict)
