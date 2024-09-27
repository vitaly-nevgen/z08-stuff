"""
1. У нас есть библиотека, в библиотеке есть книги.
2. У каждой книги есть следующие параметры — автор, название, количество страниц.
3. Наша программа должна уметь следующее:
   3.1. Уметь добавить книгу.
   3.2. Вернуть информацию по названию книги.
"""


def show_book_info(book):
    print('{name} by {author} ({pages_count} pages)'.format(**book))

items = {}

welcome_text = (
    'Select action.\n'
    '1 — Add new book\n'
    '2 — Get info\n'
    '3 — Exit'
)

choice = None

while choice != 3:
    print(welcome_text)
    choice = int(input('Your choice: '))

    if choice == 1:
        # add new book choosen
        author = input('Type author name: ')
        name = input('Type book name: ')
        pages_count = input('Enter pages count: ')

        book = {
            'author': author, # Mark Pilgrim
            'name': name, # Drive into Python
            'pages_count': pages_count, # 320
        }

        print('Good! You have added following book:')
        show_book_info(book)

        items[name] = book

    elif choice == 2:
        # get info choosen
        name = input('Type search name: ')
        book = items[name]
        show_book_info(book)
        print('------')
    elif choice == 3:
        print('Ok, good bye')
    else:
        print('Sorry, invalid option')




# cars = {
# 	'lowcost': [{
# 		'name': 'Daewoo Matiz',
# 		'cost': '5000$'
# 	},{
# 		'name': 'Daewoo Matiz 2',
# 		'cost': '666$'
# 	}],
# 	'middle': ['VW Passat'],
# 	'premium': ['BMW 7']
# }


# print(cars['lowcost'][1]['cost'])



# cars_lowcost = ['a', 'b', 'c']
# cars_middle = ['d', 'e', 'f']
# cars_premium = ['x', 'y', 'z']



# class Book():
#    def __init__(self, x):
#        print(x)

# b = Book(5)

# array = [1, 2, 3]

# print('Before print')
# print(array.append(5))

# print('After print')
# print(array)


# utf8 


# hello = 'World' # utf8
# hello_2 = b'World'

# a = [1, 2, 2, 3, 3]
# b = set(a)

# print(b)



