import json

dictionary = {
  "wine": [
    {"wine_name": "merlot",
      "grape_type": "red",
      "sweetness": "dry",
      "price": "100"
    },
    {"wine_name": "pinot_noir",
      "grape_type": "white",
      "sweetness": "sweet",
      "price": "150"
    },
    {"wine_name": "chardonnay",
      "grape_type": "white",
      "sweetness": "dry",
      "price": "200"

    },
    {
      "wine_name": " sauvignon_blanc",
      "grape_type": "red",
      "sweetness": "sweet",
      "price": "80"
    }
  ]
}
    json = json.dumps(dictionary)
f = open("dictionary.json")

#f.write(json)
#f.close()
dictionary = json.load(f)

with open("dictionary.json", "r") as fp:
    dictionary = json.load(f)

open('dictionary.json')
#print({"wine"})

#w stands for writing permission for the opened file