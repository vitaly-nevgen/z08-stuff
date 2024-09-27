class Moon:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance


a = Moon()
a.some_attr = 5
b = Moon()
print(b.some_attr)

print(a)
print(b)

# class X:
#     some = 11
#
# x1 = X()
# X.some = 50
# x2 = X()
# x3 = X()
#
# print(x1.some)
# print(x2.some)
# print(x3.some)