def say_before(fn):
    def wraps():
        print('It\'s said before')
        fn()

    return wraps

@say_before
def say_hello():
    print('Hello!')

@say_before
def say_bye():
    print('Bye!')

say_hello()
say_bye()

