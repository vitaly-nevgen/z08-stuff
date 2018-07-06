class Book(): # <-
    kind = 'paper' # <- it's attribute
    name = None
    pages_count = None

    def __init__(self, name, pages_count=None):
        self.name = name
        self.pages_count = pages_count

    def print_info(self):
        print('My name is "{}"'.format(self.name))
        print('I\'m from', self.kind)

        if self.pages_count:
            print('I have', self.pages_count, 'pages')
        else:
            print('I have no pages')

    def read(self):
        print('I was read')
        print('This is self = ', self)

    def what_kind(self):
        print(self.kind)

book1 = Book('Hello', pages_count=200)
# book1.pages_count = 200
book1.print_info()

book2 = Book('Harry Potter')
book2.print_info()





# class Human():
#     legs_count = 2
#
# vasya = Human()
# vasya.money = 100
# print(vasya.legs_count)
#
# petya = Human()
# petya.money = 200
# print(petya.legs_count)




# book = Book()
# book.some_attribute = '123'
# book.read()
# print(book.kind)
# print(book.some_attribute)
#
# print(Book.kind)
# print(Book.some_attribute)

# book.what_kind()

#print('This is book = ', book)
# print(str(book))