# my_variable = 777

# def a():
# 	my_inner_variable = 666

# 	def b():
# 		print(my_inner_variable)
# 		print(my_variable)

# 	b()

# a()
# print(my_variable)

# var_from_outer_scope = 5

# def do_something():
# 	global var_from_outer_scope
# 	var_from_outer_scope += 1
# 	print(var_from_outer_scope)

# do_something()
# print('value is (out) = ', var_from_outer_scope)


def items_positional(cars, fruits):
    pass

def items_keywords(cars=None, fruits=None):
    if cars is not None:
        print('Your cars is', cars)

    if fruits is not None:
        print('Your fruits is', fruits)

# items_positional(['bmw', 'audi'], ['apple', 'banana'])

print('First case')
items_keywords(cars=['bmw', 'audi'], fruits=['apple', 'banana'])

print('----')
print('Second case')
items_keywords(fruits=['apple', 'banana'])

print('----')
print('Third case')
items_keywords(cars=['bmw', 'audi'])


# def process():
# 	a = 1
# 	b = 2
# 	c = 3

# 	def my_sum():
# 		a = 7
# 		b = 8
# 		c = 9
# 		return a + b + c

# 	print(my_sum())

# process()