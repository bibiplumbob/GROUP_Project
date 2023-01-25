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

counting_set = []
for dict in royal_data:
    if "title" in dict:
        split_list = dict["title"].split('_')
        if "Prince" in split_list:
            print(dict["title"])
            counting_set.append(dict["title"])
        elif "Princess" in split_list:
            print(dict["title"])
            counting_set.append(dict["title"])
print(len(counting_set))