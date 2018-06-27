import csv
import random


def get_coordinates_list(count):
    result = []
    for i in range(count):
        X = random.randint(0, 100)
        Y = random.randint(0, 100)
        Z = random.randint(0, 100)

        result.append((X, Y, Z))

    return result


def get_coordinates_generator(count):
    for i in range(count):
        X = random.randint(0, 100)
        Y = random.randint(0, 100)
        Z = random.randint(0, 100)

        yield (X, Y, Z)

for cords in get_coordinates_list(5):
    print(cords)

