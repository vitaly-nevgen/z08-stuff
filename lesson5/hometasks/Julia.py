items = [6, 10, 5, 8, 9, 14, 5, 6]
result = []

max_value = 0

while len(items) > 0:
    for i, item in enumerate(items):
        if max_value < item:
            max_value = item
            max_value_index = i
    result.append(max_value)
    del items[max_value_index]
    
    max_value = 0
    max_value_index = None

print(result)

len = len(items)-1
for item in result:
    print(result[len])
    len = len - 1
