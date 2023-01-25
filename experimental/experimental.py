royals =[{
    "places":["hello", "this", "croissant"],
    "status": "tired",
    "emotion": ["frustrated", "exhausted"],
    "attempt": "this_is_a_test"
},
{
    "places":["hello", "wow", "carbonara"],
    "status":"hungry",
    "emotion": ["annoyed", "cranky"],
    "attempt": "I_hate_life"
}]

#Pick last value of a list and add it to a new key
for dict in royals:
    if "status" in dict:
        if type(dict["status"]) is list:
            dict["the_word"] = dict["status"][-1]
        else:
            dict["the_word"] = dict["status"]
#Counting number of emotions into a new key 
    if "emotion" in dict:
        dict["num_of_emotes"] = len(dict["emotion"])
#Trying splitting and checking for frequency:
for dict in royals:
    if "attempt" in dict:
        split = dict["attempt"].split('_')
    #if "test" or "tests" in split:
        #print(dict["attempt"])

#trying dictwriter on this set 
#import csv
#names = ["status","emotion", "the_word", "num_of_emotes"]
#with open('experimental.csv', 'w', encoding = 'utf-8', newline= '') as f:
 #   writer= csv.DictWriter(f, fieldnames= names, extrasaction= 'ignore')
  #  writer.writeheader()
   # for dict in attempt_dict:
    #    writer.writerow(dict)

#Experimental -- comparing to another set to create a new set
countries = {"croissant", "carbonara", "coffee"}
manual_group = []
for dict in royals:
    if "places" in dict:
        # If only single place, i.e., string: convert to list
        if not type(dict["places"]) is list:
            dict["places"] = [dict["places"]]

        # Convert list of place names to set of placenames
        dict["places"] = set(dict["places"])

        # Find intersection between set of placenames and set of countries
        origin_countries = dict["places"] & countries

        # Check that intersection only contains single country
        if len(origin_countries) == 1:
            # Save single origin country back into dictionary
            origin_country = list(origin_countries)[0]
            dict['place'] = origin_country
        else:
            print(dict["places"], origin_countries)

        # for dict["words"] in dict:
        #     if dict["words"] in countries:
        #         dict["food_status"] = "my_fave"
        #     else:
        #         manual_group.append(dict)

print(royals)                

