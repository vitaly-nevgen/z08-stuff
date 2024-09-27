class Legs:
    def __init__(self):
        print('I have legs')
        super().__init__()


class Arms:
    def __init__(self):
        print('I have arms')
        super().__init__()


class Head:
    def __init__(self):
        print('I have head')
        super().__init__()


class Wings:
    def __init__(self):
        print('I have wings')
        super().__init__()


class Human(Legs, Arms, Head):
    pass


class Bird(Legs, Wings, Head):
    pass


h = Human()
print()
b = Bird()
