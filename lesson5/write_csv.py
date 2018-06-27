import csv
import random


def coordinates_generator(count):
    for i in range(count):
        X = random.randint(0, 100)
        Y = random.randint(0, 100)
        Z = random.randint(0, 100)
        yield {
            'X Cord': X,
            'Y Cord': Y,
            'Z Cord': Z,
        }


f = open('generated.csv', 'w')

fieldnames = ['X Cord', 'Y Cord', 'Z Cord']
writer = csv.DictWriter(f, fieldnames=fieldnames)

for cords in coordinates_generator(1):
    writer.writerow(cords)


