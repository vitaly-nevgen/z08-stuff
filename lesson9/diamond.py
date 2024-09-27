# explain about static & classmethods

class A(object):
    def my_method(self):
        print('Hello A!')


class B(A):
    def my_method(self):
        print('Hello B!')


class C(B):
    def my_method(self):
        pass


class D(B, C):
    pass

# D --> B --> A
# D --> C --> B --> A

d = D()
d.my_method()