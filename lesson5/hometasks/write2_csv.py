import random
import csv



def get_generate_coordinates(count):
    for i in range(count):
        x = random.randint(0,100)
        y = random.randint(0,100)
        z = random.randint(0,100)

        yield {
            'x cord': x,
            'y cord': y,
            'z cord': z,
        }


f = open('generated.csv', 'w')
fieldnames = ['x cord', 'y cord', 'z cord']
writer = csv.DictWriter(f, fieldnames=fieldnames)

for cords in get_generate_coordinates(100):
    writer.writerow(cords)