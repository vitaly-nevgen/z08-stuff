
class Wheels:
    def __init__(self):
        print('Wheels added')
        super().__init__()


class Steering:
    def __init__(self):
        print('Steering added')
        super().__init__()


class Engine:
    engine_volume = None

    def __init__(self):
        # important action to configure engine
        self.engine_volume = 1998

        print('Engine added')
        super().__init__()

    def my_method(self):
        pass


class Car(Wheels, Steering, Engine):
    def __init__(self):
        print('I\'m car')
        print('Engine volume:', self.engine_volume)

        super().__init__()

        print('Engine volume:', self.engine_volume)


car = Car()
# print('------')
# bicycle = Bicycle()

