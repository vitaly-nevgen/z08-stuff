items = [6, 10, 5, 8, 9, 14, 5, 6, 28, 50, 32]
result = []
n = 1
while n < len(items):
    for i in range(len(items)-n):
        if items[i] > items[i+1]:
            items[i], items[i+1] = items[i+1], items[i]
    n += 1



max_value = 0
max_value_index = None

print("items:", items)
print('result', result)

