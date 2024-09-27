def drink(wine):
    return 'Drunk ' + wine


def collect(wine):
    return 'Collected ' + wine


def spill(wine):
    return 'Spilled ' + wine

wine = 'Starya Kelya'
wine = collect(spill(drink(wine)))

print(wine)
