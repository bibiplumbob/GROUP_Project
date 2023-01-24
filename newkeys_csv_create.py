import json
with open("cleaned_royalty.json", encoding = 'utf-8') as f:
    royal_data = json.load(f)

#More cleaning up the data
for label in royal_data:
    if "ontology/parent_label" in label:
        del label["ontology/parent_label"]
    if "ontology/predecessor_label" in label:
        del label["ontology/predecessor_label"]
    if "ontology/successor_label" in label:
        del label["ontology/successor_label"]
    if "ontology/activeYearsStartYear" in label:
        del label["ontology/activeYearsStartYear"]
    if "ontology/activeYearsEndYear" in label:
        del label["ontology/activeYearsEndYear"]

#Picking and adding new keys 
for dict in royal_data:
    #death place new key
    if "ontology/deathPlace_label" in dict:
        if type(dict["ontology/deathPlace_label"]) is list:
            dict["deathPlace"] = dict["ontology/deathPlace_label"][-1]
        else:
            dict["deathPlace"] = dict["ontology/deathPlace_label"]
    #birth place new key
    if "ontology/birthPlace_label" in dict:
        if type(dict["ontology/birthPlace_label"]) is list:
            dict["birthPlace"] = dict["ontology/birthPlace_label"][-1]
        else:
            dict["birthPlace"] = dict["ontology/birthPlace_label"]
    #number of spouses new key
    if "ontology/spouse_label" in dict:
        if type(dict["ontology/spouse_label"]) is list:
            dict["num_spouses"] = len(dict["ontology/spouse_label"])
        else:
            dict["num_spouses"] = 1
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

with open('final_royalty.json', 'w', encoding= 'utf-8') as f:
    json.dump(birth_death_year, f)    

#PUT INTO A CSV FILE WITH DICTREADER
import csv
columns = ["title","ontology/title","deathPlace","birthPlace","num_spouses","ontology/birthYear","ontology/deathYear"]
with open('final_royal.csv', 'w', encoding = 'utf-8', newline= '') as f:
    writer = csv.DictWriter(f, fieldnames= columns, extrasaction='ignore')
    writer.writeheader()
    for dict in birth_death_year:
        writer.writerow(dict)
