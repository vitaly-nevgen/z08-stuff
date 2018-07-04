import json

dictionary = {'Python': '.py', 'C++': '.cpp', 'Java': '.java'}
json = json.dumps(dictionary)
f = open("dictionary.json")

#f.write(json)
#f.close()
dictionary = json.load(f)

with open("dictionary.json", "r") as fp:
    dictionary = json.load(f)

#open('dictionary.json')
#print({"wine"})

#w stands for writing permission for the opened file