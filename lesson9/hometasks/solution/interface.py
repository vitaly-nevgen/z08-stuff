class Figure:
    def get_area(self):
        raise NotImplementedError

    def get_description(self):
        raise NotImplementedError


class Circle(Figure):
    def get_area(self):
        return 5


a = Circle()
print(a.get_area())
print('Program is still running')