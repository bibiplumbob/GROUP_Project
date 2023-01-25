attempt_dict =[{
    "words":["hello", "this", "croissant"],
    "status": "tired",
    "emotion": ["frustrated", "exhausted"],
    "attempt": "this_is_a_test"
},
{
    "words":["hello", "wow", "carbonara"],
    "status":"hungry",
    "emotion": ["annoyed", "cranky"],
    "attempt": "I_hate_life"
}]

#Pick last value of a list and add it to a new key
for dict in attempt_dict:
    if "words" in dict:
        if type(dict["status"]) is list:
            dict["the_word"] = dict["status"][-1]
        else:
            dict["the_word"] = dict["status"]
#Counting number of emotions into a new key 
    if "emotion" in dict:
        dict["num_of_emotes"] = len(dict["emotion"])
#Trying splitting and checking for frequency:
for dict in attempt_dict:
    if "attempt" in dict:
        split = dict["attempt"].split('_')
    if "test" or "tests" in split:
        print(dict["attempt"])

#trying dictwriter on this set 
#import csv
#names = ["status","emotion", "the_word", "num_of_emotes"]
#with open('experimental.csv', 'w', encoding = 'utf-8', newline= '') as f:
 #   writer= csv.DictWriter(f, fieldnames= names, extrasaction= 'ignore')
  #  writer.writeheader()
   # for dict in attempt_dict:
    #    writer.writerow(dict)