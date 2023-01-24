attempt_dict =[{
    "words":["hello", "this", "croissant"],
    "status": "tired",
    "emotion": ["frustrated", "exhausted"]
},
{
    "words":["hello", "wow", "carbonara"],
    "status":"hungry",
    "emotion": ["annoyed", "cranky"]
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

print(attempt_dict)

#