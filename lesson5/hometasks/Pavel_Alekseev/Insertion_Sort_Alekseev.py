# 3. Реализовать сортировку вставками "Insertion sort"

items = [12, 10, 5, 8, 9, 14, 5, 6, 1, -1, 1, 0]
print(items)

for i, item in enumerate(items):
    x = items[i]
    j = i + 1
    if j >= len(items):
        break
    while items[j] < items[i] and i > -1:
        items[i] = items[j]
        items[j] = x
        #if i != 0:
        j = i
        i -= 1
        x = items[i]
    print(items)
print(items)
#----

# for i in range(1, len(items)):
#     x = items[i - 1]
#     while items[i] < items[i - 1] and i > 0:
#         items[i - 1] = items[i]
#         items[i] = x
#         i -= 1
#         x = items[i - 1]
#     print(items)
# print(items)
