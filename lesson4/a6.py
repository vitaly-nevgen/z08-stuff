def a1():
    raise Exception('Some bad error')
    print('Finished')

def a2():
    a1()

def a3():
    a2()

def a4():
    a3()

def a5():
    a4()

def a6():
    a5()

a6()
