# a = {
#     'name': 'Jack',
#     'gender': 'm',
#     'age': 20,
#     'city': 'Minsk'
# },
#
# a['name'] # Jack
# a['city'] # Minsk
#
# b = ['Jack', 'm', 20, 'Minsk']
#
# b[0] # Jack
# b[3] # Minsk

users = [
    {'name': 'Jack', 'gender': 'm', 'age': 20, 'city': 'Minsk'},
    {'name': 'Ann', 'gender': 'f', 'age': 36, 'city': 'Minsk'},
    {'name': 'Piotr', 'gender': 'm', 'age': 27, 'city': 'Minsk'},
    {'name': 'Masha', 'gender': 'f', 'age': 88, 'city': 'New York'},
    {'name': 'Andrew', 'gender': 'm', 'age': 42, 'city': 'Bryansk'},
]


def filter_city(users, city_name):
    for user in users:
        if user['city'] != city_name:
            users.remove(user)


def filter_max_age(users, max_age):
    fn = lambda x: x['age'] <= max_age
    return list(filter(fn, users))


if __name__ == '__main__':
    filter_city(users, 'Minsk')
    users = filter_max_age(users, 22)

    print(users)
