def func(a=None, b=None):
    print('a is', a)
    print('b is', b)

args = {
    'a': 111
}

func(**args)