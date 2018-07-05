# FP vs OOP
def dress_up(human):
    # modify human
    pass

def give_drink(human):
    # modify human
    pass

human = 'Vasya'

dress_up(human)
give_drink(human)

print(human) # dressed & drunk


class Human():
    def dress_up(self):
        pass

    def give_drink(self):
        pass


human = Human()
human.dress_up()
human.give_drink()

book = 'Harry Potter'
dress_up(book)