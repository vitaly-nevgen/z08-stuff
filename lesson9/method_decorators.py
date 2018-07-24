class SomeClass():
    my_value = 88

    def __init__(self):
        self.value = 55

    def flower(self):
        pass

    @classmethod
    def something(cls):
        print(cls.my_value)
        print(cls.value)

    @staticmethod
    def hello():
        pass

# SomeClass.something()

sc = SomeClass()
sc.something()


#
# print(sc.my_value)
# print(SomeClass.my_value)
#
# print(sc.flower())
# print(SomeClass.flower())
