import csv

filename = 'coordinates.csv'
f = open(filename)

reader = csv.reader(f)

for item in reader:
    print('X={0}, Y={1}, Z={2}'.format(*item))


# def somefunc(a, b, c):
#     print('b is', b)
#
# somefunc(1, 2, 3)
# somefunc(*[4, 8, 9])


