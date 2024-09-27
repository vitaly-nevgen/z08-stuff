def say_something(text):
    if text is not None:
        print('You have said: "{}"'.format(text))
    else:
        print('You have said nothing!')


say_something('Hello')
say_something(1)
say_something(0)
say_something(False)
say_something('')
say_something(None)