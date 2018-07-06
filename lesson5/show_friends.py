import json

f = open('friends.json')
friends = json.load(f)

print(friends[0]['first_name'])
