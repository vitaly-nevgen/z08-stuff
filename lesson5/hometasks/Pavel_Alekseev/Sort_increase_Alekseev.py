# 1. Переделать сортировку в порядке возрастания

items = [6, 10, 5, 8, 9, 14, 5, 6, 1, -1, 1, 0]

result = []
min_value = items[0]
min_value_index = 0

while len(items) > 0:
    for i, item in enumerate(items):
        if min_value > item:
            min_value = item
            min_value_index = i

    result.append(min_value)
    min_value = items[0]
    del items[min_value_index]

    min_value_index = 0

print('items', items)
print('result', result)