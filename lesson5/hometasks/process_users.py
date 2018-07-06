import csv

filename = 'users.csv'
f = open(filename)

reader = csv.DictReader(f)

for item in reader:
    print( 'Hello, {first_name} {last_name}!'.format(**item))
