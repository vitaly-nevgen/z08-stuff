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
