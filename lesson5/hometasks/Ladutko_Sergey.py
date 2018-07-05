items = [6, 10, 5, 8, 9, 14, 5, 6]
print('items:',items)
result =[]

min_value = 99999999999999999999999999999999999999
min_value_index = None

while len(items) > 0:
	for i, item in enumerate(items):
		if min_value > item:
			min_value = item
			min_value_index = i

	result.append(min_value)
	del items[min_value_index]	
	min_value = 99999999999999999999999999999999999999
	min_value_index = None

print('result', result)