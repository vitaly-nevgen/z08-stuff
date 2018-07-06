import csv

import random

def get_generate_list(count):
    result = []
    for i in range(count):
        x = random.randint(0,100)
        y = random.randint(0,100)
        z = random.randint(0,100)

        result.append((x, y, z))

    return result

def get_generate_coordinates(count):
    for i in range(count):
        x = random.randint(0,100)
        y = random.randint(0,100)
        z = random.randint(0,100)

    yield (x, y, z)
for cords in get_generate_list(5):
    print(cords)

#the difference between these 2 functions is that