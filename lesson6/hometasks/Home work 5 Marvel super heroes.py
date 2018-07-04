import json
fielename = 'marvel_super_heroes.txt'
marvelheroes = open(fielename, mode='w', encoding='utf8')


heroes1 = {
    'name': 'wolverin',
    'team affiliations': 'x-men',
    'abilities': 'regenerative',
}


heroes2 = {
    'name': 'deadpool',
    'team affiliations': 'x-men',
    'abilities': 'regenerative',
}


heroes3 = {
    'name': 'beast',
    'team affiliations': 'x-men',
    'abilities': 'Genius-level intellect',
}


heroes4 = {
    'name': 'iron-man',
    'team affiliations': 'avengers',
    'abilities': ['Genius-level intellect', 'proficient scientist and engineer' ]
}

heroes = []
heroes.append(heroes1)
heroes.append(heroes2)
heroes.append(heroes3)
heroes.append(heroes4)



json.dump(heroes, marvelheroes)
marvelheroes.close()

###############################################################

marvelheroes = open(fielename, mode='r', encoding='utf8')
json_data = json.load(marvelheroes)

for user in json_data:
    print(user)
