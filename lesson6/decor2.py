def say_loud(fn):
    def wraps():
        result = fn()
        return result.upper()

    return wraps

@say_loud
def say_hello():
    return 'Hello!'

def say_bye():
    return 'Bye!'

print(say_hello())
print(say_bye())

# ---------

"""
def page_handler():
    # ...
    pass

@check_auth
def secure_page_handler():
    # ...
    pass
"""