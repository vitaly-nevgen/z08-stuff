import random

items = [random.randint(-10, 10) for i in range(10)]
print('Original items: ', items)


################################################################
# 1. Переделать сортировку в порядке возрастания

def selection_sort(items, type='ASC'):
    if type == 'ASC':
        items_copy = items.copy()
        result = []
        max_value = items_copy[0]
        max_value_index = 0

        while len(items_copy) > 1:
            for i, item in enumerate(items_copy):
                if max_value > item:
                    max_value = item
                    max_value_index = i
            result.append(max_value)
            del items_copy[max_value_index]

            max_value = items_copy[0]
            max_value_index = 0
        return result + items_copy
    elif type == 'DESC':
        return selection_sort(items)[::-1]
    else:
        return None


result = selection_sort(items)
if result == None:
    print('Type of selection sort is wrong. Please write \'ASC\' or \'DESC\' as type parameter')
else:
    print('Sorted items by selection sort: ', result)


################################################################
# 2. Реализовать сортировку вставками

def insertion_sort(items):
    items_copy = items.copy()
    for i in range(1, len(items_copy)):
        j = i - 1
        pivot_num = items_copy[i]
        while pivot_num < items_copy[j] and j >= 0:
            items_copy[j + 1] = items_copy[j]
            j -= 1
        items_copy[j + 1] = pivot_num
    return items_copy


print('Sorted items by insertion sort: ', insertion_sort(items))


################################################################
# 3. Гномья сортировка

def gnome_sort(items):
    items_copy = items.copy()
    for i in range(1, len(items_copy)):
        while i != 0:
            if items_copy[i] < items_copy[i - 1]:
                insertion = items_copy.pop(i)
                items_copy.insert(i - 1, insertion)
            i -= 1
    return items_copy


print('Sorted items by gnome sort: ', gnome_sort(items))


################################################################
# 4. Быстрая сортировка

def quick_sort(items):
    if len(items) > 1:
        pivot_num = items[-1]
        greater_seq = [item for item in items if item > pivot_num]
        less_seq = [item for item in items if item < pivot_num]
        same_seq = [item for item in items if item == pivot_num]
        return quick_sort(less_seq) + same_seq + quick_sort(greater_seq)
    else:
        return items


print('Sorted items by quick sort: ', quick_sort(items))


################################################################
# 5. Сортировка пузырьком:

def bubble_sort(items):
    items_copy = items.copy()
    length = len(items_copy)
    while length != 0:
        for i in range(1, length):
            if items_copy[i] < items_copy[i - 1]:
                insertion = items_copy[i]
                items_copy.pop(i)
                items_copy.insert(i - 1, insertion)
        length -= 1
    return items_copy


print('Sorted items by bubble sort: ', quick_sort(items))