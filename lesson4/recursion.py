call_count = 0
target_count = 100000

def a():
    print('Current call count', call_count)
    global call_count
    call_count += 1
    if call_count == target_count:
        raise Exception('Target count of {} reached'.format(target_count))
    else:
        a()

try:
    a()
except:
    pass