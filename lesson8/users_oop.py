from lesson8.users import users

class User():
    name = None
    gender = None
    age = None
    city = None

    def __init__(self, name, gender, age, city):
        self.name = name
        self.gender = gender
        self.age = age
        self.city = city

    def say_hello(self):
        print('My name is', self.name, 'i\'m', self.age, 'years old')

    def increase_age(self):
        self.age += 1
        print(self.name, 'now is', self.age)

    def __str__(self):
        return 'User ({})'.format(self.name)

    def __int__(self):
        return self.age

users_instances = []


def create_instances():
    for user in users:
        u = User(
            name=user['name'],
            gender=user['gender'],
            age=user['age'],
            city=user['city']
        )

        users_instances.append(u)

if __name__ == '__main__':
    create_instances()
    user = users_instances[0]
    # print(str(user))

    print('Hello ' + str(user) + ' World')
    print(int(user))

    # user.say_hello()
    # user.increase_age()
    # user.say_hello()
