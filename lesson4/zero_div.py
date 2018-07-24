a = 5
x = int(input('Type a number'))


try:
    print(not_existing_variable/x)
except ZeroDivisionError:
    print('Sorry, can\'t divide by zero')
except NameError:
    print('Name error happened')