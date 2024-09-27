class First:
    def __init__(self):
        print('first')

class Second(First):
    def __init__(self):
        print('second')

class Third(First, Second):
    def __init__(self):
        print('third')



# Third --> Second --> First
# Third --> First