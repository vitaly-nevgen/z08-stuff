class Vehicle:
    name = None
    top_speed = None

    def __init__(self, name, top_speed):
        self.name = name
        self.top_speed = top_speed

    def calculate_lead_time(self, a, b):
        distance = abs(a - b)
        time = distance / self.top_speed
        return time


class WheeledVehicle(Vehicle):
    wheels_count = None

    def __init__(self, name, top_speed, wheels_count=None):
        if wheels_count:
            self.wheels_count = wheels_count

        super().__init__(name, top_speed)


class Helicopter(Vehicle):
    pass


class Car(WheeledVehicle):
    wheels_count = 4

class Bicycle(WheeledVehicle):
    wheels_count = 2


# MRO — Method Resolution Order
# Bicycle.calculate_lead_time()
# Bicycle --> WheeledVehicle --> Vehicle --> object

# Vehicle
# — name
# — top_speed

# WheeledVehicle
# — name
# — top_speed
# — wheels_count

a = 100
b = 500

bicycle = Bicycle('Red Bicycle', 20)
car = Car('Blue Audi', 250)
helicopter = Helicopter('Black Helicopter', 350)


print(bicycle.calculate_lead_time(a, b))
print(car.calculate_lead_time(a, b))
print(helicopter.calculate_lead_time(a, b))

print(Bicycle.__mro__)