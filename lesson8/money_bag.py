class MoneyBag():
    _amount = None

    def __init__(self):
        self._amount = 1100

    def __float__(self):
        return self._amount / 100.0

    def __int__(self):
        return self._amount // 100

    @property
    def amount(self):
        return self.__float__()

    @amount.setter
    def amount(self, value):
        self._amount = value * 100

    def __str__(self):
        return 'MoneyBag with ${}'.format(self.__float__())

    def charge_addition_commission(self):
        print('We charged commission for addition with $1.00')
        self.amount -= 1

    def __add__(self, other):
        self.charge_addition_commission()
        return self.amount + other

    def __radd__(self, other):
        self.charge_addition_commission()
        return other + self.amount


mb1 = MoneyBag()
mb1.amount = 10

mb2 = MoneyBag()
mb2.amount = 5

print(mb1 + mb2)
print(mb1)
print(mb2)


# print(mb1 + 10)
# print(10 + mb1)


# print(int(mb))
# print(float(mb))
# print(mb)