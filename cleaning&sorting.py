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

print(len(royal_data))

#Checking if there's sufficient data with the helpful labels
death_year_counter = 0
birth_year_counter = 0
for dict in royal_data:
    if "ontology/deathYear" in dict:
        death_year_counter += 1
        if "ontology/birthYear" in dict:
            birth_year_counter += 1

#print(f"Data with death year is: {death_year_counter}")
#print(f"Data with birth year is: {birth_year_counter}")

#with open('cleaned_royalty.json', 'w') as f:
 #   json.dump(royal_data, f)

with open ('The_10k_royal_set.csv','w') as file:
    file.write('title,ontology/title,ontology/predecessor_label,ontology/successor_label,ontology/parent_label,ontology/deathPlace_label,ontology/birthPlace_label,ontology/spouse_label,ontology/birthYear,ontology/deathYear,ontology/birthDate,ontology/deathDate\n')
    for name in royal_data:
        file.write(f"{name['title']},{name['ontology/title']},{name['ontology/predecessor_label']},{name['ontology/successor_label']},{name['ontology/parent_label']},{name['ontology/deathPlace_label']},{name['ontology/birthPlace_label']},{name['ontology/birthYear']},{name['ontology/deathYear']},{name['ontology/birthDate']},{name['ontology/deathDate']}\n")

